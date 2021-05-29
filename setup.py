import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Carlos A Molina",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Read elpais.com entries without loging",
    include_package_data=True,
    install_requires=[
        "bs4",
        "pyyaml",
        "validators",
    ],
    long_description_content_type="text/markdown",
    long_description=long_description,
    name="elpais_reader",
    packages=setuptools.find_packages(),
    project_urls={
        "Documentation": "https://github.com/CarlosAMolina/elpais-reader",
        "Source": "https://github.com/CarlosAMolina/elpais-reader",
    },
    python_requires=">=3.6",
    version="0.0.1",
)
