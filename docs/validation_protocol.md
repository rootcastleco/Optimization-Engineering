# Scientific validation protocol

## Experiment identity

- **Test function:** two-dimensional Rosenbrock objective, f(x₁,x₂) = (1−x₁)² + 100(x₂−x₁²)².
- **Initial point:** (−1.2,1.0) for every method.
- **Analytic reference:** minimizer (1,1), objective value 0.
- **Methods:** SciPy BFGS (finite-difference gradient), Powell and Nelder–Mead.
- **Budget:** at most 450 **objective function evaluations**, measured in one wrapper shared by all implementations.
- **Recorded environment:** Python with NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8.
- **Observation type:** deterministic smoke test on one analytic objective, not a benchmark suite or replicated research experiment.

## Measurements and instrumentation

For every objective evaluation, the driver records the evaluation index, minimum objective observed so far and associated incumbent decision vector. The driver cannot exceed the configured objective-call budget; even internal finite-difference calls by a solver are counted. Explicit exceptions prevent additional model evaluations after exhaustion.

The summary stores actual evaluations used, final incumbent, solver termination and budget status. Runtime is intentionally omitted from cross-algorithm ranking because a short single-run wall-clock comparison on an uncontrolled system could be misleading.

## Observed reference run

| Method | Evaluations | Best f | Recorded status |
|---|---:|---:|---|
| BFGS | 123 | 2.00559e-11 | solver_converged |
| Powell | 450 | 1.20802e-01 | solver_stopped (evaluation budget) |
| Nelder-Mead | 219 | 1.09909e-18 | solver_converged |

This record can vary across numerical library versions, stopping tolerances and floating-point environments. It is presented as an observed outcome, not as a portable performance guarantee. In particular, a 450-evaluation run cannot establish that Powell is generally inferior.

## Figure provenance

The README vector figures use sampled points from the exact incumbent traces in this experiment. They contain no fabricated observations. The convergence plot uses a floor of 1e-14 solely to enable a logarithmic display; solutions below this floor remain available in machine-readable results. Incumbents are held visually constant after early termination, not treated as additional evaluations.

The reproducible plotting script writes complete, non-downsampled curves as SVG, PNG at 350 dpi, and vector PDF. Uncertainty bands are intentionally absent because the experiment has no replicated trials.

## Acceptance gates

1. **Input integrity (PASS/FAIL):** all supplied values finite; objective evaluation deterministic for this case; dimensions correct.
2. **Budget integrity (PASS/FAIL):** no method exceeds configured objective-call budget.
3. **Incumbent monotonicity (PASS/FAIL):** best-observed objective never increases.
4. **Known-optimum sanity (PASS/FAIL):** the Rosenbrock global minimum at (1,1) evaluates numerically to zero.
5. **Gradient audit (PASS/FAIL):** central-difference directional derivative agrees with the analytic derivative inside a specified numerical tolerance at multiple nonstationary operating points.
6. **Industrial readiness (NOT VERIFIED):** instrument noise, actuator effects, safety constraints, dataset representativeness and deployment latency have not been tested here.

## Threat model and rollback

A malformed model, inadmissible sensor data, wrongly scaled constraints or a numerical overflow can yield apparently attractive but unsafe operating points. Deploy a separate validator that re-evaluates all hard constraints and policy limits. Fail closed on nonfinite values and unit mismatches. Use shadow mode, time-bounded execution and a versioned rollback path.

## Extension to a defensible comparative study

Evaluate several test problems spanning conditioning, smoothness, constraints and multimodality; run multiple seeds for stochastic methods; fix evaluation budgets and report objective distribution, feasibility violation, confidence interval methodology and computational cost. Predeclare success criteria before inspecting results.