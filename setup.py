from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in plant_equipment/__init__.py
from plant_equipment import __version__ as version

setup(
	name="plant_equipment",
	version=version,
	description="Plant and Equipment",
	author="Chandru",
	author_email="plant@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
