"""Reproducible numerical smoke tests; not production or field validation."""
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
from run_benchmarks import rosenbrock, analytic_gradient, run_method
from audit_gradient import central_difference


class NumericalTests(unittest.TestCase):
    def test_known_minimizer(self):
        self.assertAlmostEqual(rosenbrock([1.,1.]),0.)
        self.assertGreater(rosenbrock([-1.2,1.0]),0.)

    def test_gradient(self):
        for p in ([-1.2,1.0],[0.3,-0.2],[1.1,1.2]):
            g = analytic_gradient(p)
            fd = central_difference(rosenbrock, p)
            self.assertLess(np.linalg.norm(g-fd)/max(1,np.linalg.norm(g)),1e-6)

    def test_evaluation_budget(self):
        for method in ("BFGS","Powell","Nelder-Mead"):
            r=run_method(method, budget=80)
            self.assertGreaterEqual(r["n_evaluations"],1)
            self.assertLessEqual(r["n_evaluations"],80)
            self.assertEqual(r["n_evaluations"],len(r["trace"]))
            self.assertTrue(math.isfinite(r["best_f"]))
            b=[t["best_f"] for t in r["trace"]]
            self.assertTrue(all(b[i+1]<=b[i] for i in range(len(b)-1)))

    def test_invalid_configuration(self):
        with self.assertRaises(ValueError):
            run_method("BFGS", budget=1)
        with self.assertRaises(ValueError):
            run_method("unknown", budget=5)


if __name__=="__main__":
    unittest.main()
