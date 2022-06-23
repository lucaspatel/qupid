# Much of this page is taken from the gemelli setup file
import ast
import re
from setuptools import find_packages, setup

# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("qupid/__init__.py", 'rb') as f:
    hit = _version_re.search(f.read().decode("utf-8")).group(1)
    version = str(ast.literal_eval(hit))

with open("README.md") as f:
    long_description = f.read()

classes = """
    Development Status :: 3 - Alpha
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split("\n") if s]

description = "Case-control matching for microbiome data."

standalone = ["qupid=qupid.cli.cli:qupid"]
q2_cmds = ["q2-qupid=qupid.q2.plugin_setup:plugin"]

setup(
    name="qupid",
    author="Gibraan Rahman",
    author_email="grahman@eng.ucsd.edu",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    license="BSD-3-Clause",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "biom-format",
        "pandas>=1.0.0",
        "scikit-bio",
        "networkx",
        "joblib",
        "scipy"
    ],
    classifiers=classifiers,
    include_package_data=True,
    extras_require={"dev": ["pytest", "pytest-cov", "flake8"]},
    package_data={"qupid": ["tests/asd.tsv"]},
    entry_points={"console_scripts": standalone,
                  "qiime2.plugins": q2_cmds}
)
