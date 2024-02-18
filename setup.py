"""Setups up the D4RL module."""
from setuptools import setup

def get_description():
    """Gets the description from the readme."""
    with open("README.md") as fh:
        long_description = ""
        header_count = 0
        for line in fh:
            if line.startswith("##"):
                header_count += 1
            if header_count < 2:
                long_description += line
            else:
                break
    return header_count, long_description


def get_version():
    """Gets the d4rl version."""
    path = "d4rl/__init__.py"
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("__version__"):
            return line.strip().split()[-1].strip().strip('"')
    raise RuntimeError("bad version data in __init__.py")


version = get_version()
header_count, long_description = get_description()

setup(
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
