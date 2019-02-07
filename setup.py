import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="morse_jkorhonen",
    version="1.0.0",
    author="Jesse Korhonen",
    author_email="jesse.hermanni@gmail.com",
    license="MIT",
    description="Convert English to Morse code and back",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkorhonen/morse-coder",
    packages=[
        'morse'
    ],
    scripts=[
        'bin/morse-cli'
    ],
    install_requires=[
        'regex'  # For better regex handling
    ],
    setup_requires=[
        'pytest_runner'
    ],
    tests_require=[
        'pytest'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
