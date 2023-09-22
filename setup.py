from setuptools import setup, find_packages
from libmiyoushe import lib_version, lib_name, lib_desc

with open('./requirements.txt') as f:
    requires = list(map(lambda string: string.strip(), f.readlines()))

setup(
    name=lib_name,
    version=lib_version,
    description=lib_desc,
    author='Error063',
    author_email='admin@error063.work',
    license='GNU General Public License v3 (GPLv3)',
    keywords=['HoYoLab', '米游社', 'miyoushe'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
    python_requires='~=3.10',
    install_requires=requires
)
