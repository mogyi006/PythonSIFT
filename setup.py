import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysift", # Replace with your username

    version="1.0.0",

    author="<authorname>",

    author_email="<authorname@templatepackage.com>",

    description="SIFT implementetion in Python",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/rmislam/PythonSIFT",

    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
)
