from setuptools import setup
import sys


# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()
number_of_arguments = len(sys.argv)
version_parameter = sys.argv[-1]
version = version_parameter.split("=")[1]
sys.argv = sys.argv[0:number_of_arguments-1]

setup(
    name="pyversioninc",
    description='Collection of classes and functions used for the versioning',
    version=version,
    packages=['version_tools'],
    # Define the author of the repository.
    author='Brice Fotzo',
    # Define the Author's email, so people know who to reach out to.
    author_email='brice.fotzo@hotmail.com',
    # I have a long description but that will just be my README
    # file, note the variable up above where I read the file.
    long_description=long_description,
    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",
    # Here is the URL where you can find the code, in this case on GitHub.
    url='https://github.com/BriceFotzo/py_version_tools',
    # Here are the keywords of my library.
    keywords='python packages, version, python versions, versioning',
)
