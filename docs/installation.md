# Installation
There are two ways of installation:

- [via PyPI](#via-pypi)
- [from source](#from-source)

!!! tip inline end "Python virtual environment"

	Installation and usage must be performed
	in virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

## :simple-pypi: Via PyPI
You can simply install SDK via PyPI:
```bash
# Basic
pip install yoowallet

# With synchronous API support
pip install yoowallet[sync]

# With packages for developing
pip install yoowallet[dev]
```

## :fontawesome-brands-square-git: From source
Getting SDK from source is also an option:
```bash
git clone <repo>
cd yoowallet
pip install .
```

Now it's time to [create an application](authorization.md) :simple-authy:
