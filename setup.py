# Copyright 2011 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import setuptools
import sys


requirements = ["httplib2",
                "argparse",
                "lprettytable"]
if sys.version_info < (2, 6):
    requirements.append("simplejson")


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setuptools.setup(
    name="python-lnovaclient",
    version="2.6.8",
    author="Rackspace, Modified by Kevin Carter, and based on work by Jacob Kaplan-Moss",
    author_email="kevin@bkintegration.com",
    description="Client library for Rackspace Legacy Nova API.",
    long_description=read_file("README.rst"),
    license="Apache License, Version 2.0",
    url="https://github.com/openstack/python-lnovaclient",
    packages=["lnovaclient", "lnovaclient.v1_0", "lnovaclient.v1_1"],
    install_requires=requirements,
    tests_require=["nose", "mock"],
    test_suite="nose.collector",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    entry_points={
        "console_scripts": ["lnova = lnovaclient.shell:main"]
    }
)
