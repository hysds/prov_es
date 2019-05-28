from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name='prov_es',
    version='0.2.1',
    long_description='PROV-ES python library',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['prov==1.3.1', 'future>=0.17.1']
)
