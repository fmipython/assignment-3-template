set dotenv-load

init:
    @pip install -r requirements.txt >/dev/null 2>&1

generate-requirements:
    @pip freeze > requirements.txt

confirm_setup:
    if [ "$(which direnv)" == "" ]; then
    echo "direnv is not installed"
    fi

test: init
    #!/usr/bin/env sh
    if [ "$GITHUB_TOKEN" == "" ]; then
        echo "❗❗❗ Your GitHub Personal Access Token is not set. Some tests might fail"
        echo "Visit https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"
        echo "And then run:"
        echo "just set-gh-token"
    fi
    python -m pytest -s --token ${GITHUB_TOKEN:-"GH PAC is not set"}

coverage: init
    @python -m coverage report --omit="*/test*"

coverage-html: init
    @python -m coverage html --omit="*/test*"

lint: init
    @python -m pylint src --disable=E0401

prospector: init
    @python -m prospector

set-gh-token:
    #!/usr/bin/env sh
    echo "Enter your GH Personal Access Token:"
    read token
    echo "export GITHUB_TOKEN=$token" > .env

pull-template:
    #!/usr/bin/env sh
    git remote add template https://github.com/fmipython/assignment-3-template 2>/dev/null
    git fetch --all

    if git diff --exit-code &>/dev/null && git diff --staged --exit-code &>/dev/null; then
        echo "Creating a commit with all current changes as backup"
        git add --all
        git commit -m "Checkpoint before merging template"
    fi

    if git merge template/main --allow-unrelated-histories -m 'Merge template' &>/dev/null; then
        echo "Merge conflicts occurred, resolving coflicts"
        git checkout src* --ours &>/dev/null
        git checkout tests* --theirs &>/dev/null
        git checkout justfile --theirs &>/dev/null
        git add --all
        git merge --continue &>/dev/null
    fi

    echo "Merge with template completed"
