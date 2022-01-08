from setuptools import setup

setup(
    name="PyGObject-stubs",
    url="https://github.com/pygobject/pygobject-stubs",
    author="Christoph Reiter",
    author_email="reiter.christoph@gmail.com",
    version="0.0.3",
    package_data={"gi-stubs": ["*.pyi", "*/*.pyi"]},
    packages=["gi-stubs"],
    install_requires=["PyGObject"],
)
