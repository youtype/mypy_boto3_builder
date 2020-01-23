from pathlib import Path

from setuptools import setup, find_packages

from mypy_boto3_builder.version import __version__ as version


ROOT_PATH = Path(__file__).absolute().parent
README_PATH = ROOT_PATH / "README.md"
REQUIREMENTS_PATH = ROOT_PATH / "requirements.txt"


LONG_DESCRIPTION = README_PATH.read_text()
INSTALL_REQUIRES = REQUIREMENTS_PATH.read_text().split("\n")


setup(
    name="mypy-boto3-builder",
    version=version,
    packages=find_packages(),
    url="https://github.com/vemel/mypy_boto3_builder",
    license="MIT License",
    package_data={
        "mypy_boto3_builder": [
            "templates/*/*.jinja2",
            "templates/*/*/*.jinja2",
            "templates/*/*/*/*.jinja2",
            "boto3_stubs_static/*.pyi",
            "boto3_stubs_static/*/*.pyi",
            "boto3_stubs_static/*/*.py",
        ]
    },
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Builder for boto3-stubs.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    keywords="boto3 type-annotations mypy boto3-stubs",
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://mypy-boto3-builder.readthedocs.io/en/latest/",
        "Source": "https://github.com/vemel/mypy_boto3_builder",
        "Tracker": "https://github.com/vemel/mypy_boto3_builder/issues",
    },
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["mypy_boto3_builder = mypy_boto3_builder.main:main"]
    },
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
)
