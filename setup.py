# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)

import os
import sys
from setuptools import setup

import versioneer

rootpath = os.path.abspath(os.path.dirname(__file__))

if sys.version_info < (3, 5):
    error = """
    folium 0.9+ supports Python 3.5 and above.
    When using Python 2.7, please install folium 0.8.*.

    See folium `README.rst` file for more information:

    https://github.com/python-visualization/folium/blob/master/README.rst

    Python {py} detected.

    Try upgrading pip and retry.
    """.format(py='.'.join([str(v) for v in sys.version_info[:3]]))
    print(error, file=sys.stderr)
    sys.exit(1)


def read(*parts):
    return open(os.path.join(rootpath, *parts), 'r').read()


def walk_subpkg(name):
    data_files = []
    package_dir = 'folium'
    for parent, dirs, files in os.walk(os.path.join(package_dir, name)):
        # Remove package_dir from the path.
        sub_dir = os.sep.join(parent.split(os.sep)[1:])
        data_files.extend(os.path.join(sub_dir, f) for f in files)
    return data_files


package_data = {
    '': [
        '*.js',
        'plugins/*.js',
        'plugins/*.html',
        'plugins/*.css',
        'plugins/*.tpl',
        'templates/*.html',
        'templates/*.js',
        'templates/*.txt'
    ] + walk_subpkg('templates/tiles')
}

packages = [
    'folium',
    'folium.plugins'
]

# Dependencies.
with open('requirements.txt') as f:
    tests_require = f.readlines()
install_requires = [t.strip() for t in tests_require]

setup(
    name='folium',
    version=versioneer.get_version(),
    description='Make beautiful maps with Leaflet.js & Python',
    license="MIT",
    long_description=f'{read("README.rst")}',
    long_description_content_type="text/x-rst",
    author='Rob Story',
    author_email='wrobstory@gmail.com',
    url='https://github.com/python-visualization/folium',
    keywords='data visualization',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
    ],
    platforms="any",
    packages=packages,
    package_data=package_data,
    python_requires='>=3.5',
    extras_require={"testing": ["pytest"]},
    install_requires=install_requires,
    zip_safe=False,
    cmdclass=versioneer.get_cmdclass(),
)
