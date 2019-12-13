from distutils.core import setup

with open("README.rst", "r") as fh:
	long_description = fh.read()
	
setup(
	name = 'fraudster',
	packages = ['fraudster'],
	version = '1.3beta',
	description = 'fraudster is a service which lets you use and integrate disposable emails for free.',
	author = 'TheSpeedX',
	author_email = 'ggspeedx29@gmail.com',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url = 'https://github.com/TheSpeedX/fraudster',
	download_url = 'https://github.com/TheSpeedX/fraudster/archive/v1.3beta.tar.gz',
	keywords = ['fraud','fraudster','anonmail', 'fakemail', 'tempmail', 'mailapi','disposable','secure','temporary'],
	data_files=[('', ['LICENSE'])],
    install_requires=['requests'],
	include_package_data=True,
	classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Operating System :: OS Independent',
	'Environment :: Console',
	],
)
