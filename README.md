# ONT Output Specifications

This project is intended to contain parsable definitions of ONT software (specifically MinKNOW, Dorado, and EPI2ME) interchange formats.

## Public docs

The rendered documentation is [available here](https://nanoporetech.github.io/ont-output-specifications/latest/)

## Deploying new docs

Use [Mike](https://github.com/jimporter/mike) to deploy a new branch.

First ensure you are on the right branch (for example named ``release/25.03``) and the docs are correct.

Then build and deploy the docs to the ``gh-pages`` branch:

```
> mike deploy [version]
```

You can also update the ``latest`` alias if the branch you are deploying is the latest release:

```
> mike deploy [version] latest --update-aliases
```

These commands commit to the ``gh-pages`` on your local git repository. You can then push the ``gh-pages`` branch to the appropriate remote.

## Development

You can set up a local developer build of the documentation by first preparing a python local environment:

```bash
pip install -r ./requirements.txt
```

Then start the documentation in dev mode:

```bash
PYTHONPATH=./docs/mkdocs_extensions/ mkdocs serve
```
