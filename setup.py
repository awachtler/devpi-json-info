from setuptools import setup
from devpi_json_info import __version__ as package_version

with open("README.md") as f:
    long_description = f.read()

setup(
    name="devpi-json-info",
    license="MIT",
    version=package_version,
    author_email="axel@uracoli.de",
    description="devpi-server plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awachtler/devpi-json-info",
    entry_points={
        "devpi_server": ["devpi-json-info = devpi_json_info.devpi_json_info"]
    },
    install_requires=["devpi-server"],
    packages=["devpi_json_info"],
)
