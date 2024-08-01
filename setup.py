from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='yoowallet',
    version='0.1.0',
    author='Shkvaldev',
    description='Simple async/sync python SDK for YooMoney',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.8',
    packages=find_packages(),
    project_urls={
        'Documentation': 'https://yoowalletpy.github.io',
        'Source Code': 'https://github.com/yoowalletpy/yoowallet'
    },
    install_requires=[
        'aiohttp'
    ],
    extras_require={
        'sync': [
            'requests'  
        ],
        'dev': [
            'setuptools',
            'mkdocs',
            'mkdocstrings[python]',
            'mkdocs-material'
        ],
    }
)

