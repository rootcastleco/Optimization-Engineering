#!/usr/bin/env python3
"""Independent central-difference gradient check on an analytic test function."""
import math
import numpy as np

from run_benchmarks import rosenbrock, analytic_gradient


def central_difference(fun, x, h=1e-5):
    point = np.asarray(x, dtype=float)
    grad = np.zeros_like(point)
    for j in range(point.size):
        delta = np.zeros_like(point)
        delta[j] = h
        grad[j] = (fun(point+delta)-fun(point-delta))/(2*h)
    return grad


def audit():
    points = ((-1.2, 1.0), (0.3, -0.2), (1.1, 1.2))
    for p in points:
        numeric = central_difference(rosenbrock, p)
        analytic = analytic_gradient(p)
        error = float(np.linalg.norm(numeric-analytic))
        relative = error/max(1.0, float(np.linalg.norm(analytic)))
        assert math.isfinite(relative) and relative < 1e-6, (p, relative)
        print("PASS x={} relative_gradient_error={:.4e}".format(p, relative))


if __name__ == "__main__":
    audit()
