# dobby-pi
Raspberry Pi + Python control interface for dobby looms

## Getting Started

1. Install [Python 3](https://www.python.org/downloads/)
2. Install and update `pip`, `setuptools`, `pipenv`, and `wheel`:
    * `py -3 -m pip install -U pip setuptools pipenv wheel`
3. Set up the pipenv: `py -3 -m pipenv install`
    * You should see output similar to the following:

```
$ py -3 -m pipenv install
Adding kivy.deps.glew to Pipfile's [packages]…
Creating a virtualenv for this project…
Pipfile: ~\dobby-pi\Pipfile
[=== ] Creating virtual environment...
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: ~\.virtualenvs\dobby-pi-<stuff>

Installing docutils…
Installation Succeeded
Installing pygments…
Installation Succeeded
Installing pypiwin32…
Installation Succeeded
Installing kivy.deps.sdl2…
Installation Succeeded
Installing kivy.deps.glew…
Installation Succeeded
```

4. Run the project using pipenv: `py -3 -m pipenv run main.py`