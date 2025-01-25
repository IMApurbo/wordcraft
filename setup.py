from setuptools import setup, find_packages

setup(
    name="wordcraft",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "numpy",
        "pickle-mixin",
    ],
    description="A library for training language models with LSTM in TensorFlow.",
    author="AKM Korishee Apurbo",
    author_email="bandinvisible8@gmail.com",
    url="https://github.com/IMApurbo/wordcraft",
    license="MIT",
)
