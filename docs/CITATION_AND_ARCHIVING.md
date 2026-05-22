# Citation and Archiving

OMNIA-MINIMAL includes citation and archiving metadata.

---

## Citation file

The citation file is:

    CITATION.cff

GitHub can use this file to generate a citation panel.

---

## Zenodo metadata

The Zenodo metadata file is:

    .zenodo.json

This helps prepare the repository for archival publication.

---

## DOI

No DOI should be written manually before Zenodo generates it.

If Zenodo archives the GitHub release, it will generate a DOI.

After the DOI exists, update:

    CITATION.cff
    README.md
    RELEASE_NOTES.md

---

## Recommended citation text

Until a DOI exists, cite the repository as:

    Brighindi, Massimiliano. OMNIA-MINIMAL: Structural Stability Beyond Surface Correctness. GitHub repository, v0.6.0. https://github.com/Tuttotorna/OMNIA-MINIMAL

After Zenodo generates a DOI, cite the archived release.

---

## Boundary

Citation does not turn the repository into universal proof.

It only makes the minimal demonstration identifiable, reproducible, and referenceable.

The claim remains:

    correctness is not structural stability

The boundary remains:

    measurement != inference != decision
