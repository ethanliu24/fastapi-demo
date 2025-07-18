# fastapi-demo

## Installation

To contribute or run the app locally, clone the repo and step into it (i.e. `cd fastapi-demo`).

### Software Prerequisite
* [Python 3.9+](https://www.python.org/downloads/)
* [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) (latest version, if you have pip it's the best to upgrade it first)

### Installing dependencies
1. Create a Python virtual enviornment if one isn't present (see [FAQ](#faq)).
2. Start a Python virtual enviornment (see [FAQ](#faq)).
3. Run this line in the terminal: `pip install -r requirements.txt`.

## Running locally
1. Load the enviornment variables in `.env`.
2. Start a Python virtual enviornment. Do this for every terminal session running this project.
3. Optional: avoid Python creating `__pycache__` directories (see [FAQ](#faq)).
4. In the command line, enter `fastapi dev app/main.py`. This will keep the server running.
5. Navigate to `http://127.0.0.1:8000/`.
6. To close the server, type `Ctrl + C` in the terminal.

## FAQ
Everything in a code block with a "$" infront are meant to be run in a terminal*

1. Create a Python virtual enviornment:
> ```
> # this should create a .venv/ directory and shouldn't be commited into version control
> $ python -m venv .venv
> ```

2. Entering a Python enviornment (run in terminal):
* MacOS & Linux: `source .venv/bin/activate`
* Windoes Powershell: `.venv\Scripts\Activate.ps1`
* Windows Bash: `source .venv/Scripts/activate`

3. Exiting a Python enviornment (run in terminal):
* MacOS: `deactivate`

4. Checking if you are in the right virtual enviornment:
> ```
> # should return a path to the .venv/ directory in this project
> $ which python3
> ```

5. VS Code can't resolve package imports:

> This is because you downloaded dependencies in the `.venv/` folder rather than globaly. In VS Code, do the following:
* Do `Ctrl + Shift + P`
* Type in `Python: Select Interpreter`
* Select the current .venv enviornment

6. Python keeps generating `__pycache__/` directories, and I don't want it:
* Go to `.venv/bin/activate`
* Paste in `export PYTHONDONTWRITEBYTECODE=1` somewhere

7. Duplicate tool name sanity check
```
# something like this
from collections import Counter
tool_names = [tool.name for tool in TOOLS]
dupes = [name for name, count in Counter(tool_names).items() if count > 1]
assert not dupes, f"Duplicate tool names detected: {dupes}"
```
