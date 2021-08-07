from setuptools import setup, find_packages
import codecs
import os

from supabase_client import __version__

here = os.path.abspath(os.path.dirname(__file__))

VERSION = __version__
DESCRIPTION = 'A supabase client for Python'

# Setting up
setup(
    name="supabase_client",
    version=VERSION,
    author="Kenneth Gabriel",
    author_email="kennethgabriel78@gmail.com",
    description=DESCRIPTION,
    long_description="",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "aiohttp >= 3.7.4",
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
    },
    keywords=['python', 'supabase', 'request', 'aiohttp', 'client'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)