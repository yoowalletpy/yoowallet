# Установка
Существует два способа установки:

- [Через PyPI](#pypi)
- [Из исходного кода](#_2)

!!! tip inline end "Виртуальное окружение Python"

	Установка и работа должна проводиться
	в виртуальном окружении:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

## :simple-pypi: Через PyPI
Вы просто можете установить SDK через PyPI:
```bash
# Базовый
pip install yoowallet

# С поддержкой синхронного API
pip install yoowallet[sync]

# С пакетами для рзработки
pip install yoowallet[dev]
```

## :fontawesome-brands-square-git: Из исходного кода
Также установка SDK возможна из исходного кода:
```bash
git clone <repo>
cd yoowallet
pip install .
```

Теперь самое время [создать приложение](authorization.md) :simple-authy:
