from setuptools import setup

import elifearticle

with open('README.rst') as fp:
    readme = fp.read()

setup(name='elifearticle',
    version=elifearticle.__version__,
    description='eLife article object.',
    long_description=readme,
    packages=['elifearticle'],
    license = 'MIT',
    install_requires=[
        "elifetools"
    ],
    url='https://github.com/elifesciences/elife-article',
    maintainer='eLife Sciences Publications Ltd.',
    maintainer_email='py@elifesciences.org',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        ]
    )
