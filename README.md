# ONT Output Specifications

This project is intended to contain parsable definitions of ONT software (specifically MinKNOW, Dorado, and EPI2ME) interchange formats.

# Deploying new docs

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
