#!/bin/bash
#
# This script deploys the current branch to the local `gh-pages` branch.
#
# The user can follow up by pushing the gh-pages branch to github or gitlab.
#
# Usage:
#   ./tools/deploy_pages.sh
#
# Prerequisites:
#   - `mike` must be installed and available in the PATH.


# Check `mike` is installed and available in PATH
if ! command -v mike &> /dev/null; then
    echo "Error: 'mike' is not installed or not in PATH" >&2
    exit 1
fi

# Ensure mike has everything it needs to run:
export PYTHONPATH=./docs/mkdocs_extensions/

# Get the current branch name
branch=$(git rev-parse --abbrev-ref HEAD)

# Strip the 'release/' prefix if present
branch=${branch#release/}

# Check if branch is `main` if so, set it to `latest`
if [[ "$branch" == "main" ]]; then
    branch="latest"

# Check if branch doesn't start with `release/`, abort if so.
elif [[ ! "$branch" =~ ^release/ ]]; then
    echo "Error: The current branch is not a release branch." >&2
    exit 1
fi

echo "Deploying: ${branch}"

mike deploy "${branch}"
