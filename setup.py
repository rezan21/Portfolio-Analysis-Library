from setuptools import find_packages, setup

with open("README.md", "r") as file:
    long_description = file.read()

# # to-do: separate dev requirements
setup(
    name="portfolio-analysis-library",
    description="#WIP: Analysing Stock Returns & Constructing Portfolios with Python",
    version="0.0.3",
    author="Reza N",
    author_email="32329310+rezan21@users.noreply.github.com",
    url="https://github.com/rezan21/Portfolio-Analysis-Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    # py_modules=["analysis", "log", "main", "pal", "params", "utils"],
    # package_dir={"": "src"},
    install_requires=["numpy", "pandas", "matplotlib", "seaborn", "tqdm"],
    extras_require={"dev": ["pytest"]},
    classifiers=[
        "Development Status :: 1 - Planning",
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
