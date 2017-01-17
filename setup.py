# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-simplegetapi',
    version='0.0.1',
    author=u'Joshua Tauberer',
    author_email=u'jt@occams.info',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/govtrack/django-simplegetapi',
    license='CC0 (copyright waived)',
    description='The world needs an even simpler Django app for making a read-only API.',
    long_description=open("README.md").read(),
    keywords="simple django rest api",
    install_requires=["lxml"],
)
