import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-gmap',
    version='0.1',
    packages=['simple_gmap'],
    include_package_data=True,
    license='BSD License',
    description='Simple Google Maps Integration For Django',
    long_description=README,
    url='https://github.com/six519/django-simple-gmap',
    author='Ferdinand Silva',
    author_email='ferdinandsilva@ferdinandsilva.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)