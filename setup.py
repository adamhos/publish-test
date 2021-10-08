import os
import setuptools
import re

with open('publish-test-25/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
                        f.read(), flags=re.MULTILINE).group(1)

setuptools.setup(name='publish-test-25',
    version=version,
    description='Description of a package',
    long_description='A package',
    author='nobody',
    author_email='nobody@example.com',
    license='Apache 2.0',
    packages=setuptools.find_packages(),
    keywords=[],
    classifiers=[],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6"
)
