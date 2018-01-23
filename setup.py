'''Setup for Chevir'''
from distutils.core import setup

setup(
    # Application name:
    name="Chevir",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Zafer Gurel",
    author_email="zafergurel@gmail.com",

    # Packages
    packages=[],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/Chevir_v010/",
    license="LICENSE",
    description="a simple video converter",
    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pexpect>=4.3.1",
        "pika>=0.11.2",
        "PyYAML>=3.12"
    ],
)
