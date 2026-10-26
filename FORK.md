# About this fork

This is a fork of **[Kaggle/learntools](https://github.com/Kaggle/learntools)**, the checking code of the Kaggle Learn courses, made and maintained by Kaggle. All credit for learntools goes to Kaggle and its contributors. It is licensed under the Apache License 2.0 (see [LICENSE](LICENSE)), and so is this fork.

The fork is used by the course *Cultural Data Analysis* at the University of Amsterdam, whose notebooks check exercises with learntools. It exists so that the course has a stable copy that installs with current versions of pip and uv.

## What is different from the original

Forked from Kaggle/learntools at commit [`e9ba66d`](https://github.com/Kaggle/learntools/commit/e9ba66dc) (28 September 2026). Only the packaging is changed; the learntools code itself is not.

- `setup.py` reads the version number from `learntools/__init__.py` as text instead of importing the package. Since pip 25.3, pip (like uv) always builds packages in an isolated environment. There, `import learntools` fails because pandas is missing, so `pip install git+https://github.com/Kaggle/learntools.git` stops with `ModuleNotFoundError: No module named 'pandas'`. The workaround with the original is `pip install --no-build-isolation git+https://github.com/Kaggle/learntools.git`.
- `pyproject.toml` added, declaring setuptools as the build system.
- This file, and a pointer to it at the top of `README.md`.

## Install

```
pip install git+https://github.com/goto4711/learntools.git
```

learntools needs pandas, numpy and the other usual libraries at runtime; they are not installed with it (as in the original). Google Colab has them already.

## Keeping up with the original

Changes from Kaggle/learntools can be pulled in with "Sync fork" on GitHub. If Kaggle fixes the install problem, this fork is no longer needed and the course will go back to the original.
