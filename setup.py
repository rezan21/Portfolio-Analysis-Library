from pathlib import Path

from setuptools import find_packages, setup

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

with open("requirements.txt", "r") as file:
    ALL_REQS = file.read().split("\n")
    ALL_REQS = [req for req in ALL_REQS if req]
    # to-do: separate dev requirements
    INSTALL_REQUIRES = ALL_REQS
    EXTRAS_REQUIRE = ALL_REQS


def get_src_modules():
    py_files = Path("./src/").glob("*.py")
    py_files = list(map(lambda file: file.stem, py_files))  # get file names
    py_files.remove("__init__")  # remove __init__.py
    return py_files


setup(
    name="portfolio-analysis-library",
    description="#WIP: Analysing Stock Returns & Constructing Portfolios with Python",
    version="0.0.3",
    author="Reza N",
    author_email="32329310+rezan21@users.noreply.github.com",
    url="https://github.com/rezan21/Portfolio-Analysis-Library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    # py_modules=["analysis", "log", "main", "pal", "params", "utils"],
    # package_dir={"": "src"},
    install_requires=INSTALL_REQUIRES,
    extras_require={"dev": EXTRAS_REQUIRE},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Office/Business :: Financial :: Investment",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
    ],
)
