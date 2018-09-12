from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="csj_converter",
    version="0.0.1",
    author="Semooze",
    author_email="cloudtimewater@gmail.com",
    description="Utilities functions for deal with CSJ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Semooze/csj_converter",
    packages=['csj_converter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)