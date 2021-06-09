from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="robot-mongodb-library",
    version="0.0.5",
    author="tarathep",
    author_email="bokie.tarathep@gmail.com",
    description="robotframework extension lib for test mongodb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tarathep/robot-mongodb-library",
    license="MIT",
    packages=find_packages(),
    package_dir={'robotMongoDBLibrary': 'RobotMongoDBLibrary'},
    install_requires=[
        'pymongo'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)