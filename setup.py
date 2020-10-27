import io
from pathlib import Path
from setuptools import setup, find_packages, find_namespace_packages

req_file: Path = Path(__file__).parent /  "requirements.txt"

requirements = req_file.read_text().splitlines()

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

setup(
    name="my_dashboard",
    subpackages=find_namespace_packages(".", include=("my_dashboard.*",)),
    version="0.1.0",
    url="https://github.com/seanbreckenridge/my_dashboard",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description=("""dashboard for HPI"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=["my_dashboard"]),
    test_suite="tests",
    install_requires=requirements,
    python_requires=">=3.7",
    extras_require={
        "testing": [
            "pytest",
            "mypy",
        ],
    }
)
