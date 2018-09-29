from distutils.core import setup

setup(
    name="PyGObject-stubs",
    url="https://github.com/pygobject/pygobject-stubs",
    author="Christoph Reiter",
    author_email="reiter.christoph@gmai.com",
    version="0.0.1",
    package_data={
        "gi-stubs": ["__init__.pyi"]},
    packages=["gi-stubs"],
    install_requires=["PyGObject"],
)
