from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="pal",
    description="#WIP: Analysing Stock Returns & Constructing Portfolios with Python",
    version="0.0.1",
    author="Reza N",
    author_email="32329310+rezan21@users.noreply.github.com",
    url="https://github.com/rezan21/Portfolio-Analysis-Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["pal"],
    package_dir={"": "src"},
    install_requires=["numpy", "pandas", "matplotlib", "seaborn", "tqdm"],
    extras_require={"dev": ["pytest", "pytest-cov", "pytest-mock", "pytest-xdist"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
