# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import atexit

long_description="""<a href="https://qiskit.org/aqua" rel=nofollow>Qiskit Chemistry</a> 
 is a set of quantum computing algorithms, 
 tools and APIs for experimenting with real-world chemistry applications on near-term quantum devices.""" 

requirements = [
    "qiskit-aqua>=0.4.0",
    "numpy>=1.13",
    "h5py",
    "psutil>=5",
    "jsonschema>=2.6,<2.7",
    "pyobjc-core; sys_platform == 'darwin'",
    "pyobjc-framework-Cocoa; sys_platform == 'darwin'"
]


def _post_install():
    from qiskit_aqua_cmd import Preferences
    preferences = Preferences()
    preferences.remove_package('qiskit_aqua_chemistry.aqua_extensions')
    preferences.add_package('qiskit_chemistry.aqua_extensions')
    preferences.save()


class CustomInstallCommand(install):
    def run(self):
        atexit.register(_post_install)
        install.run(self)


class CustomDevelopCommand(develop):
    def run(self):
        atexit.register(_post_install)
        develop.run(self)


class CustomEggInfoCommand(egg_info):
    def run(self):
        atexit.register(_post_install)
        egg_info.run(self)


setuptools.setup(
    name='qiskit-chemistry',
    version="0.4.1",  # this should match __init__.__version__
    description='Qiskit Chemistry: Experiment with chemistry applications on a quantum machine',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Qiskit/qiskit-chemistry',
    author='Qiskit Chemistry Development Team',
    author_email='qiskit@us.ibm.com',
    license='Apache-2.0',
    classifiers=(
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering"
    ),
    keywords='qiskit sdk quantum chemistry',
    packages=setuptools.find_packages(exclude=['test*']),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand
    },
    entry_points = {
        'console_scripts': [
                'qiskit_chemistry_cmd=qiskit_chemistry_cmd.command_line:main'
        ],
        'gui_scripts': [
                'qiskit_chemistry_ui=qiskit_chemistry_ui.command_line:main'
        ]
    }
)