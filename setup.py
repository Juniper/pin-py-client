{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
__author__ = "Sharanya Bhat"
__author_email__ = "sharanyab@juniper.net"
__licence__ = "Apache 2.0"

from setuptools import setup, find_packages

import versioneer


def requirements(filename='requirements.txt'):
    return open(filename.strip()).readlines()


with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = requirements()

setup(
    name='pinez',
    version=versioneer.get_version(),
    description='Healthbot Python Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    install_requires=install_requires,
    include_package_data=True,
    license=__licence__,
    keywords=['Juniper HealthBot Paragon Insights Automation'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Networking',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
