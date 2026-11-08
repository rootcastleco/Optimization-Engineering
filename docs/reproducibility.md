# Reproduction and responsible integration

## Reproducing the reference experiment

Install from `requirements.txt`, run `python -m unittest discover -s tests -v`, then execute the benchmark and plotting commands in the root README. The driver writes `artifacts/rosenbrock_traces.json` and `artifacts/rosenbrock_summary.csv` on each invocation. These are traceable experimental outputs, not dataset training evidence.

## Reusing the solver adapter pattern

An external numerical method belongs behind a versioned adapter interface. It should accept an immutable model version, a typed decision vector, resource limits and a reproducible seed. It must return a candidate solution, execution diagnostics and a complete evaluation trace.

An independent validator checks input finiteness, units, bound constraints, hard interlocks and any domain-specific performance thresholds. A candidate cannot be applied to a machine solely because its objective decreased. Keep new algorithms in shadow mode until independent test evidence and the authorized operational gate are complete.

## Comparing two implementations

Use an unmodified input fixture, fixed call budget, consistent physical units and the same post-processor. Report objective values, residuals, infeasibility rates, termination counts and resource usage. Use separate test cases that target pathological curvature, nonconvexity, severe noise, nonidentifiability and failure-to-converge scenarios.

## Known limitations

The included experiment contains one analytic objective, three off-the-shelf local methods and a single starting point. It does not estimate a method's generalization performance, nor can it test GNSS hardware, rotor dynamics, embedded timing or external production APIs.