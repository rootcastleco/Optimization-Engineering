#!/usr/bin/env python3
"""Reproduce the deterministic Rosenbrock reference comparison.

No claim of algorithm superiority, industrial certification or statistical significance.
"""
import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize


class BudgetReached(Exception):
    """Stop before exceeding the shared objective-evaluation budget."""


def rosenbrock(x):
    x = np.asarray(x, dtype=float)
    a, b = float(x[0]), float(x[1])
    return (1 - a) ** 2 + 100 * (b - a * a) ** 2


def analytic_gradient(x):
    a, b = map(float, x)
    return np.array([-2 * (1 - a) - 400 * a * (b - a*a),
                     200 * (b - a*a)], dtype=float)


def run_method(method, budget=450, initial=(-1.2, 1.0)):
    if budget < 4:
        raise ValueError("Budget must be >= 4")
    if method not in ("BFGS", "Powell", "Nelder-Mead"):
        raise ValueError("Unknown method")
    incumbent = math.inf
    incumbent_x = list(initial)
    trace = []

    def objective(x):
        nonlocal incumbent, incumbent_x
        if len(trace) >= budget:
            raise BudgetReached
        value = rosenbrock(x)
        if value < incumbent:
            incumbent, incumbent_x = value, [float(t) for t in x]
        trace.append({"evaluation": len(trace)+1, "best_f": float(incumbent),
                      "best_x": incumbent_x.copy()})
        return float(value)

    opts = {"maxiter": 500}
    if method == "BFGS":
        opts.update(gtol=1e-8)
    elif method == "Powell":
        opts.update(maxfev=budget, xtol=1e-8, ftol=1e-9)
    else:
        opts.update(maxfev=budget, xatol=1e-8, fatol=1e-10)
    try:
        result = minimize(objective, np.asarray(initial, dtype=float),
                          method=method, options=opts)
        status = "solver_converged" if result.success else "solver_stopped"
        message = str(result.message)
    except BudgetReached:
        status, message = "evaluation_budget_exhausted", "Budget reached"
    return {"method": method, "evaluation_budget": budget, "n_evaluations": len(trace),
            "best_f": float(incumbent), "best_x": incumbent_x,
            "status": status, "message": message, "trace": trace}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=int, default=450)
    parser.add_argument("--out-dir", type=Path, default=Path("artifacts"))
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    runs = [run_method(method, args.budget) for method in
            ("BFGS", "Powell", "Nelder-Mead")]
    report = {"objective": "two-dimensional Rosenbrock",
              "formula": "(1-x1)^2 + 100*(x2-x1^2)^2",
              "initial": [-1.2, 1.0], "analytic_minimizer": [1.0, 1.0],
              "comparison": "same cap on objective evaluations, not equal CPU time",
              "limitations": "one deterministic problem, one initial point",
              "methods": runs}
    (args.out_dir/"rosenbrock_traces.json").write_text(
        json.dumps(report, indent=2)+"\n", encoding="utf-8")
    with (args.out_dir/"rosenbrock_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        fieldnames = ("method", "evaluation_budget", "n_evaluations",
                      "best_f", "best_x", "status")
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for run in runs:
            writer.writerow({k:run[k] for k in fieldnames})
    for run in runs:
        print("{method:12s} nfev={n_evaluations:3d} "
              "f={best_f:.8e} {status}".format(**run))


if __name__ == "__main__":
    main()
