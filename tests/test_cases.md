# QA Test Cases: Unicode to Plain Text

This document outlines the formal "Golden Test Cases" designed to avoid regressions in our Unicode conversion engine (`src/mapping_engine.py`).

## Verifiable Strategy
Success for a conversion is defined entirely by the alteration of the input characters' **Code Point**. 
For example, converting a Mathematical Alphanumeric Bold 'P' (`U+1D40F`) must result precisely in the standard Latin Capital Letter 'P' (`U+0050`). No visual similarities are accepted as successful tests unless the exact hex code corresponds.

## Golden Test Cases

| Test ID | Input (Unicode Stylized) | Input Hex | Expected Output (Plain Text ASCII) | Expected Output Hex | Verification Method |
|---------|--------------------------|-----------|----------------------------------|---------------------|---------------------|
| TC-01 | **Bold**: `𝐀` | `U+1D400` | `A` | `U+0041` | `U+1D400` -> `U+0041` |
| TC-02 | **Italic**: `𝐵` | `U+1D435` | `B` | `U+0042` | `U+1D435` -> `U+0042` |
| TC-03 | **Script**: `𝒞` | `U+1D49E` | `C` | `U+0043` | `U+1D49E` -> `U+0043` |
| TC-04 | **Fraktur**: `𝔇` | `U+1D507` | `D` | `U+0044` | `U+1D507` -> `U+0044` |
| TC-05 | **Monospace**: `𝙴` | `U+1D674` | `E` | `U+0045` | `U+1D674` -> `U+0045` |
| TC-06 | **Double-struck**: `𝔽` | `U+1D53D` | `F` | `U+0046` | `U+1D53D` -> `U+0046` |
| TC-07 | **Fallback (NFKD)**: `é` | `U+00E9` | `e` (Base char) | `U+0065` | `U+00E9` -> `U+0065` followed by `U+0301` |

*These cases must be asserted securely before any major release.*
