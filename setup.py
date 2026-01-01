from io import open
from os import environ

from setuptools import setup


def read(filename):
    """Read file contents with error handling."""
    try:
        with open(filename, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def requirements():
    """Read requirements from requirements.txt or return default dependencies."""
    try:
        with open("requirements.txt", "r") as req:
            return [r.strip() for r in req.read().split("\n") if r.strip() and not r.startswith("#")]
    except FileNotFoundError:
        # Fallback to hardcoded dependencies if requirements.txt is not available
        return [
            "pydantic>=2.0.0",
            "httpx>=0.27.0",
            "ujson>=5.4.0",
            "appdirs>=1.4.4",
        ]


setup(
    name="tochechka",
    version=environ.get("TAG_VERSION", "0.0.0").replace("v", ""),
    packages=[
        "tochka_api",
        "tochka_api.exceptions",
        "tochka_api.models",
        "tochka_api.models.responses",
        "tochka_api.modules",
    ],
    url="https://github.com/Ramedon1/tochechka",
    license="Mozilla Public License 2.0",
    author="Ramedon1",
    description="Simple Tochka Bank Open API client",
    install_requires=requirements(),
    project_urls={
        "Source code ORIGINAL": "https://github.com/WhiteApfel/tochka-api",
    },
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="tochka openapi api bank",
)
