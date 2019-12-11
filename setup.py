from setuptools import setup, find_packages

with open('financejson/__about__.py') as file:
    about = {}
    exec(file.read(), about)

with open('README.md') as file:
    readme = file.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    url=about['__url__'],
    author=about['__author__'],
    license=about['__license__'],
    packages=find_packages(),
    install_requires=['fastjsonschema', 'click', 'pandas'],
    test_requires=['pytest'],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'financejson': ['schema.json'], },
    entry_points={'console_scripts': ["financejson = financejson.cli:main"]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Financial'
    ],
)
