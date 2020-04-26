import setuptools


setuptools.setup(
	name="stackoverflow",
	version="1.0.0",
	descriptions="Python Wrapper for Stack Exchange API",
	author="Rafaela S. Sacconi",
    author_email="rafaelassacconi@gmail.com",
    url="https://github.com/rafaelassacconi/stackoverflow",
	packages=setuptools.find_packages(),
	install_requires=[
		"requests==2.23.0",
	],
    python_requires=">=3.6",
	include_package_data=True,
	zip_safe=False
)
