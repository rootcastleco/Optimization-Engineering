#!/usr/bin/env python3
"""Scientific Figure Making workflow: documented, source-derived Matplotlib plots.

Reproducible exports: SVG (editable text), PDF (vector), PNG (350 dpi).
Every plotted value derives from benchmark trace JSON; no fabricated error bars.
"""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

COLORS = {"BFGS": "#0E3D8A", "Powell": "#228B55", "Nelder-Mead": "#4A4A4A"}
STYLES = {"BFGS": "-", "Powell": "--", "Nelder-Mead": ":"}


def configure():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
        "axes.titlesize": 12, "axes.linewidth": 1.1, "legend.frameon": False,
        "svg.fonttype": "none", "savefig.bbox": "tight",
        "savefig.pad_inches": 0.13})


def save(fig, dest, name):
    for extension in ("svg", "pdf", "png"):
        fig.savefig(dest / (name + "." + extension), dpi=350,
                    facecolor="white")
    plt.close(fig)


def plot_convergence(report, destination):
    fig, ax = plt.subplots(figsize=(8.5, 4.3))
    for run in report["methods"]:
        history = run["trace"]
        x = [t["evaluation"] for t in history]
        y = [max(float(t["best_f"]), 1e-14) for t in history]
        if x[-1] < run["evaluation_budget"]:
            x.append(run["evaluation_budget"])
            y.append(y[-1])
        ax.step(x, y, where="post", color=COLORS[run["method"]],
                linestyle=STYLES[run["method"]], linewidth=2.2,
                label="{} ({} evaluations)".format(run["method"], run["n_evaluations"]))
    ax.set_yscale("log")
    ax.set_xlim(0, report["methods"][0]["evaluation_budget"])
    ax.set_ylim(1e-14, 1e4)
    ax.set_xlabel("Objective-function evaluations (count)")
    ax.set_ylabel("Best observed objective value, f(x)")
    ax.set_title("Rosenbrock minimization: evaluation-normalized convergence")
    ax.grid(which="major", color="#E2E6E9", linewidth=0.7)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper right")
    fig.tight_layout()
    save(fig, destination, "rosenbrock_convergence")


def plot_trajectories(report, destination):
    x = np.linspace(-1.8, 1.7, 280)
    y = np.linspace(-0.6, 2.2, 250)
    xx, yy = np.meshgrid(x, y)
    zz = (1-xx)**2+100*(yy-xx*xx)**2
    fig, ax = plt.subplots(figsize=(7.4, 5.5))
    lines = ax.contour(xx, yy, zz, levels=[0.1,1,5,20,100,500,2000],
                       colors="#C8CED5", linewidths=0.9)
    ax.clabel(lines, fontsize=7, fmt="%g")
    for run in report["methods"]:
        pts = np.asarray([t["best_x"] for t in run["trace"]], dtype=float)
        if len(pts) < 2:
            continue
        changed = np.r_[True, np.any(np.diff(pts, axis=0) != 0, axis=1)]
        pts = pts[changed]
        ax.plot(pts[:,0], pts[:,1], color=COLORS[run["method"]],
                linestyle=STYLES[run["method"]], linewidth=1.7,
                label=run["method"])
        ax.scatter([pts[-1,0]], [pts[-1,1]], color=COLORS[run["method"]], s=25)
    ax.scatter([-1.2], [1], marker="s", facecolors="white",
               edgecolors="black", s=65, label="Initial point", zorder=8)
    ax.scatter([1], [1], marker="*", color="black", s=110,
               label="Analytical minimizer", zorder=8)
    ax.set(xlim=(-1.8, 1.7), ylim=(-0.6, 2.2), xlabel="x1",
           ylabel="x2", title="Rosenbrock landscape: best-incumbent trajectories")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="#F0F2F3", linewidth=0.5)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    save(fig, destination, "rosenbrock_trajectories")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path,
                   default=Path("artifacts/rosenbrock_traces.json"))
    p.add_argument("--output", type=Path, default=Path("assets/figures"))
    a = p.parse_args()
    report = json.loads(a.input.read_text(encoding="utf-8"))
    if len(report["methods"]) != 3:
        raise ValueError("Expected three benchmark methods")
    for run in report["methods"]:
        history = run["trace"]
        if not history or not all(np.isfinite(t["best_f"]) for t in history):
            raise ValueError("No valid objective trace")
    a.output.mkdir(parents=True, exist_ok=True)
    configure()
    plot_convergence(report, a.output)
    plot_trajectories(report, a.output)


if __name__ == "__main__":
    main()
