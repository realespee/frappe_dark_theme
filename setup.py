from setuptools import setup, find_packages


with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ni_dark_theme/__init__.py
from ni_dark_theme import __version__ as version


setup(
	name='ni_dark_theme',
	version=version,
	description='Custom Theme for Frappe',
	author='Randy Lowery',
	author_email='lowerymayorga@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
