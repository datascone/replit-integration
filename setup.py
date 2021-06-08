from setuptools import setup, find_packages

setup(
    name="montools",
    version="0.1.0",
    description="ML Mondays Tools",
    long_description="",
    long_description_content_type="text/markdown",
    author="datascone",
    packages=find_packages(where="src"),
    package_dir={
        "": "src"
    },
    include_package_data=True,
    #scripts=[
    #    "bin/fintools"
    #],
    python_requires=">3.5, <4"
)