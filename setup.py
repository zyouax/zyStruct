from setuptools import setup, find_packages

setup(
    name="zystruct",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "zystruct=main:main"
        ],
    },
)
