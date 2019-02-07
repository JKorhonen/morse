import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="morse-jkorhonen",
    version="1.0.0",
    author="Jesse Korhonen",
    author_email="jesse.hermanni@gmail.com",
    description="Simple English to morse code and back converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkorhonen/morse-coder",
    packages=setuptools.find_packages(),
    install_requires=[
        'regex'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)