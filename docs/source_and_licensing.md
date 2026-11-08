# References, provenance and license boundaries

## Primary reference

Kochenderfer, Mykel J., and Tim A. Wheeler. **Algorithms for Optimization**, second edition. MIT Press, 2026. Publisher: https://mitpress.mit.edu/9780262047012/algorithms-for-optimization/ (verify catalog URL before using as an archival identifier). Prefer the verified title, author names, edition, publisher and year when citing.

The user-supplied reference PDF contains **633 PDF pages**, 24 methodological chapters, and three technical appendices. It carries a **CC BY-NC-ND 4.0 International** notice. In the authors' preface, the Julia algorithm listings are explicitly described as illustrative rather than production-quality.

## What this repository does and does not reproduce

- The README, technical notes, prompts and agent workflows are newly written descriptions of engineering procedures and original application examples.
- No source textbook PDF, source figure, table image or substantial passage is included.
- Mathematical methods and scientific concepts are attributed as background; this is not a translation or altered edition of the book.
- Citation of a source does not confer its copyright license on separately authored work, and the repository's MIT license does not grant permissions in the book.
- The scientific figures are separately generated from numerical experiments; they are not reproduced from the source textbook.

## Scientific figure-making workflow

Scientific plotting conventions were informed by the installed **Scientific Figure Making** skill, which credits Chen Liu's figures4papers project. The code in this repository is independently authored using Matplotlib; the third-party skill's helper module, graphic assets, and reference text have not been copied. If third-party artifacts are later incorporated, their separate licensing obligations must be reviewed before commercial use.

## Academic integrity and claims

This repository has not been peer reviewed or independently certified for industrial deployment. Benchmark figures reflect one controlled test configuration. The mathematical verification, operating limits and safety case of any actual Rootcastle system remain separate obligations.

## Provenance

Reference PDF SHA-256 (as calculated for the source uploaded in the preparation workflow): `874e643064b827597a7fd872144df91ebc68092fb68121f828b7f71a18799bd4`. This checksum is supplied for source-version identification; the PDF itself is not distributed.

## Associated research publication (separate deposited work)

Batuhan Ayrıbaş (2026), *Optimization Engineering: A Traceable Research-Software Workflow for Reproducible Numerical Optimization*, Zenodo version 1, https://doi.org/10.5281/zenodo.24046577.

The Zenodo deposit describes the paper as CC BY 4.0 and offers the research PDF separately from the GitHub source distribution. The original repository MIT license applies to the independently authored software and documentation in this repository, not automatically to the Zenodo paper or to the third-party optimization textbook. Zenodo currently classifies this record's resource type as "Standard"; it must not be represented as a peer-reviewed journal article without independent evidence. The paper itself is linked rather than mirrored in this GitHub source tree.
