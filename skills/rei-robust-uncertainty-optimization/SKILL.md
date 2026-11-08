---
name: rei-robust-uncertainty-optimization
description: "Set-based uncertainty, chance constraints, Monte Carlo, Taylor approximations and polynomial chaos. Use for engineering work involving set-based uncertainty, chance constraints, monte carlo, taylor approximations and polynomial chaos, especially Rootcastle machinery, IoT telemetry, numerical models, calibration, experimental design, and optimization QA. Require reproducible evidence and safety-gated rollout."
---

# Robust Optimization and Uncertainty Propagation

## Engineering objective

Set-based uncertainty, chance constraints, Monte Carlo, Taylor approximations and polynomial chaos. Distinguish measurement error, aleatoric variability and epistemic uncertainty and test tail failures.

## Required evidence and input contract

Ask for or identify the objective, baseline data, decision variables, parameter units, numerical bounds, equality and inequality constraints, noise or model uncertainty, evaluation cost and operational safety envelope. Treat any missing critical datum as **NOT VERIFIED**, not as permission to invent it.

## Procedure

1. **Formulate:** Write a typed problem statement with objective, feasible domain, real units and explicit assumptions; distinguish hard operational restrictions from soft penalties.
2. **Select:** Diagnose smoothness, derivative quality, convexity, variable type, data reliability and compute budget. Select an appropriate baseline and at most two candidate algorithm families with a justification tied to the observed structure.
3. **Implement in isolation:** Keep the solver behind an adapter boundary. Provide deterministic configuration, immutable model version, evaluation quota, random seed when relevant, and explicit termination reasons.
4. **Validate:** Re-evaluate all hard constraints with an independent validator; detect NaN/Inf, ill conditioning, inconsistent units and numerical nonconvergence. Distinguish measurement error, aleatoric variability and epistemic uncertainty and test tail failures.
5. **Compare:** Use matched objective-evaluation or measured-resource budgets. For stochastic procedures report multiple seeds, dispersion, failure frequency and worst feasible results.
6. **Integrate:** Begin in read-only shadow mode. Require a separate authorization and machine interlocks before any physical actuation; preserve a reversible rollback route and record every decision.
7. **Report:** State objective value, residuals, feasibility, stop criteria, algorithm assumptions, evidence limits, regression status, and three next actions.

## Guardrails

- Never call a stationary point a globally optimal solution without a valid applicable argument or certificate.
- Never claim a synthetic test establishes embedded, industrial or field readiness.
- Never replace a safety interlock with a software objective penalty.
- If a tolerance is not supplied or derived from a validated specification, label it **provisional**.
- Avoid modifying any Rootcastle production core; prefer versioned integration APIs, feature flags, canaries and rollback.

## Primary source and reading

Kochenderfer, M. J., and Wheeler, T. A. (2026). *Algorithms for Optimization*, 2nd ed. MIT Press. **Relevant chapter(s): 20–21**. See [chapter map](../../docs/chapter_map.md) and [source/rights note](../../docs/source_and_licensing.md). This workflow is independently written, not an extract or altered edition of the book.

## Output template

**Model and data provenance → algorithm-selection reasoning → numerical output → independent constraint and gradient checks → risk controls → acceptance status (PASS / FAIL / NOT VERIFIED) → rollback → next three actions.**
