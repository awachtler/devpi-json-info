from setuptools import setup
from devpi_json_info import __version__ as package_version

setup(
    name="devpi-json-info",
    license="MIT",
    version=package_version,
    entry_points={
        'devpi_server': [
            "devpi-json-info = devpi_json_info.devpi_json_info"]},
    install_requires=['devpi-server'],
    packages=['devpi_json_info'])
