# Overview

Meddra toolkit to handle ontology files

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

[![Unix Build Status](https://img.shields.io/travis/com/posos-tech/meddra-toolkit.svg?label=unix)](https://travis-ci.com/posos-tech/meddra-toolkit)
[![Windows Build Status](https://img.shields.io/appveyor/ci/posos-tech/meddra-toolkit.svg?label=windows)](https://ci.appveyor.com/project/posos-tech/meddra-toolkit)
[![Coverage Status](https://img.shields.io/coveralls/posos-tech/meddra-toolkit.svg)](https://coveralls.io/r/posos-tech/meddra-toolkit)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/posos-tech/meddra-toolkit.svg)](https://scrutinizer-ci.com/g/posos-tech/meddra-toolkit)
[![PyPI Version](https://img.shields.io/pypi/v/meddra-toolkit.svg)](https://pypi.org/project/meddra-toolkit)
[![PyPI License](https://img.shields.io/pypi/l/meddra-toolkit.svg)](https://pypi.org/project/meddra-toolkit)

# Setup

## Requirements

* Python 3.9+

## Installation

Install it directly into an activated virtual environment:

```text
$ pip install meddra-toolkit
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add meddra-toolkit
```

# Usage

After installation, the package can imported.
Then load a Meddra Version and explore it:

```python
from meddra_toolkit import meddra
base = meddra.MeddraData(meddra.VERSION_24_0_FR)
base.load()
result = base.find("covid", regex=True)
# `result` is an array of `MeddraConcept`
```

