import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py4logistic_regression",
    version="0.0.4",
    author="Mgs. M. Luthfi Ramadhan",
    author_email="luthfir96@gmail.com",
    description="Logistic Regression Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luthfi118/py4logistic_regression",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy'
      ],
    python_requires='>=3.7'
)
