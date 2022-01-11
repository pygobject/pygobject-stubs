from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="PyGObject-stubs",
    description="Typing stubs for PyGobject",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/pygobject/pygobject-stubs",
    author="Christoph Reiter",
    author_email="reiter.christoph@gmail.com",
    version="0.0.4",
    package_data={"gi-stubs": ["*.pyi", "*/*.pyi"]},
    packages=["gi-stubs"],
    install_requires=["PyGObject"],
)
