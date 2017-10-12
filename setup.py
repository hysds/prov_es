from setuptools import setup, find_packages

setup(
    name='prov_es',
    version='0.1.1',
    long_description='PROV-ES python library',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['prov==1.3.1']
)
