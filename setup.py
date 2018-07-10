import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="viptela_python",
    version="0.4.5",
    author="Eugene KY Wong",
    author_email="morphyme@gmail.com",
    description="This is the Cisco Viptela Python SDK",
    long_description="This is the Cisco Viptela Python SDK which allows direct execution or through another SDK such as an Ansible SDK",
    long_description_content_type="text/markdown",
    url="https://github.com/eugene-ky-wong/viptela-python",
    packages=setuptools.find_packages(),
    classifiers=(
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License v3 or later'
        ' (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    install_requires=[
        "requests",
    ],
    python_requires='~=2.7'
)

