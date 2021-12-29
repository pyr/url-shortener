import codecs
from os import path
from setuptools import setup, find_packages

with open("requirements.txt") as reqs:
    install_requires = [
        line for line in reqs.read().split("\n") if (line and not line.startswith("--"))
    ]


def read(*parts):
    return codecs.open(
        path.join(path.dirname(__file__), *parts), encoding="utf-8"
    ).read()


setup(
    name="url_shortener",
    version="0.5.20",
    description="Simple URL Shortener",
    long_description=read("README.rst"),
    url="https://github.com/pyr/url-shortener",
    author="Pierre-Yves Ritschard",
    author_email="pyr@spootnik.org",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    scripts=["bin/url-shortener"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
