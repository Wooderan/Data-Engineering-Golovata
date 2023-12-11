from setuptools import find_packages, setup

setup(
    name="lesson02",
    version="0.1.0",
    packages=find_packages(include=["ht_template\job1", "ht_template\job1.*", "ht_template\job2", "ht_template\job2.*"]),
)