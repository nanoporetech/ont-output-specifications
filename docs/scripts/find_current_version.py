import subprocess


def get_current_release_name():
    try:
        # Run the git command to get the current branch name
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        branch_name = result.stdout.strip()

        if branch_name == "main":
            return "latest"

        # Remove the "release/" prefix if it exists
        return branch_name.removeprefix("release/")
    except subprocess.CalledProcessError as e:
        print(f"Error getting current branch: {e.stderr.strip()}")
        return None


if __name__ == "__main__":
    print(get_current_release_name())
