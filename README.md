# dobby-pi

Raspberry Pi + Python control interface for dobby looms

## Getting Started

> **Technical Note:** Commands listed here are for a Windows environment with unix utilities installed
> via [Git for Windows](https://git-scm.com/download/win). Make sure that your VSCode integrated terminal is set up
> to work with these utilities. Use `ctrl + ,` to open VSCode settings, and click the `{}` icon to open the text editor.
> Add the following entries to your user settings:
> ```javascript
> "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
> "terminal.integrated.shellArgs.windows": ["-l"],
> ```

1. Install [Python 3](https://www.python.org/downloads/)
2. Install and update `pip`, `setuptools`, `pipenv`, and `wheel`:
    * `py -3 -m pip install -U pip setuptools pipenv wheel`
3. Source `setup.sh`: `source setup.sh`
4. Set up the pipenv: `py -3 -m pipenv install`
    * You should see output similar to the following:

    ```console
    $ py -3 -m pipenv install
    Creating a virtualenv for this project…
    Pipfile: ${workspaceRoot}\Pipfile
    Using %LOCALAPPDATA%/Programs/Python/Python36/python.exe (3.6.1) to create virtualenv…
    [   =] Creating virtual environment...Using base prefix '%LOCALAPPDATA%\\Programs\\Python\\Python36'
    New python executable in ${workspaceRoot}\.venv\Scripts\python.exe
    Installing setuptools, pip, wheel...
    done.
    Running virtualenv with interpreter C:/Users/broberto/AppData/Local/Programs/Python/Python36/python.exe

    Successfully created virtual environment!
    Virtualenv location: M:\Git\dobby-pi\.venv
    Installing dependencies from Pipfile.lock (1c7bc2)…
    ================================ 16/16 - 00:00:30
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    ```

4. Run the project using pipenv: `py -3 -m pipenv run main.py`

> **Troubleshooting:** If you run into issues getting your environment set up, check the following items:
> 1. Double check that `PIPENV_VENV_IN_PROJECT` is set: `echo $PIPENV_VENV_IN_PROJECT`
>    * If `PIPENV_VENV_IN_PROJECT` is not set, make sure to run `source setup.sh` before using any `pipenv` commands.
> 2. Enable `pylint`:
>     * Open Command Pallet (`Ctrl+Shift+P`)
>     * `> Python: Select Linter` → `pylint`
