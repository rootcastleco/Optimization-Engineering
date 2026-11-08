# Method selection: a scientific decision protocol

The selection matrix below is a **diagnostic aid**, not a universal ranking. Its recommendations are conditional on the validity of the problem structure and the available evidence.

| Problem characteristics | Candidate families | Diagnostic checks | Limits on claims |
|---|---|---|---|
| Smooth, differentiable, high-dimensional | gradient descent, momentum, L-BFGS | gradient check, scaling, step acceptance | local stationarity does not imply global optimum |
| Smooth nonlinear least squares | Gauss–Newton, Levenberg–Marquardt | Jacobian rank, residual model, identifiability | estimated covariance depends on modeling assumptions |
| Discontinuous or gradient-unavailable | Nelder–Mead, pattern search, mesh-adaptive direct search | evaluation budget, restart stability | heuristic incumbent; no generic global guarantee |
| Multimodal black-box search | differential evolution, CMA-ES, simulated annealing | seeds, population diversity, per-evaluation cost | stochastic dispersion matters |
| Linear objective and affine constraints | linear programming | primal/dual residuals, infeasibility checks | certificate only when solver assumptions and residual tolerances hold |
| Convex quadratic objective with affine constraints | quadratic programming | PSD validation, KKT, duality | numerical certificate depends on precision and formulation |
| Verified disciplined convex model | DCP-compatible solver | curvature rules, canonicalization, feasibility | original formulation must satisfy modeled assumptions |
| Mixed discrete or integer parameters | MILP, branch-and-bound, dynamic programming | integrality gap, bounds, combinatorial size | a heuristic rounding step may violate constraints |
| Expensive simulation/experimental function | DOE, surrogate, Gaussian process, Bayesian optimization | calibration, held-out residuals, acquisition budget | GP uncertainty conditional on prior/kernel/data |
| Multiple competing objectives | weighted/epsilon constraints, Pareto sampling | dominance, feasibility, normalization, stakeholder preference | no single design is intrinsically 'best' without preferences |
| Uncertain measurements or environment | robust or chance-constrained optimization | sensitivity, dependence, scenario coverage, uncertainty model | chance constraint validity needs calibrated distributions |
| Coupled hardware/software disciplines | multidisciplinary design optimization | subsystem consistency, interface tolerances, convergence stability | subsystems optimized separately may be globally poor |

## Selection sequence

1. Establish whether the problem is continuous, mixed-integer, stochastic, constrained, multiobjective or multidisciplinary.
2. Determine if derivatives are available and *correct*. Compare analytic/automatic derivatives with an independent numerical check on representative points.
3. Test convexity or exploitable structure only where justified. Distinguish a proof of convexity from a visual appearance of convexity.
4. Compare a small baseline set (typically one simple baseline plus no more than two candidates) at fixed resources.
5. Retain the simplest method meeting predeclared feasibility, performance, robustness and operational acceptance criteria.

For source routing, use the [24-chapter map](chapter_map.md) and the corresponding skill reference cards.