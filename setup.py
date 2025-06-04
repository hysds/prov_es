from setuptools import setup, find_packages

setup(
    name='prov_es',
    version='0.3.0',
    long_description='PROV-ES python library',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['prov>=2.0.0'],
    python_requires='>=3.12',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ],
)
