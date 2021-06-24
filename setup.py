from setuptools import find_packages
from setuptools import setup
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = '0.1.dev0'
shortdesc = 'Kivy extensions for 3D graphics'
longdesc = '\n\n'.join([read_file(name) for name in [
    'README.md',
    'CHANGES.md',
    'LICENSE.md'
]])


setup(
    name='kivy3',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Programming Language :: Python'
    ],
    author='Niko Skrypnik, kivy3 Contributors',
    author_email='nskrypnik@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'scipy',
        'kivy'
    ],
    extras_require=dict(
        stl=[
            'numpy-stl'
        ],
        urdf=[
            'lxml',
            'numpy-stl',
            'urdf_parser_py'
        ],
    ),
    dependency_links=[
        'https://github.com/ros/urdf_parser_py/archive/refs/tags/1.1.0.tar.gz#egg=urdf_parser_py-1.1.0'
    ]
)
