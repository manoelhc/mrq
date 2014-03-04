from setuptools import setup, find_packages
import os
from pip.req import parse_requirements


def get_requirements():
    # found at http://stackoverflow.com/questions/14399534/how-can-i-reference-requirements-txt-for-the-install-requires-kwarg-in-setuptool
    # reqs is a list of requirement
    # e.g. ['django==1.5.1', 'mezzanine==1.4.6']
    reqs = []
    for filename in ["requirements", "requirements-dashboard"]:
        # parse_requirements() returns generator of pip.req.InstallRequirement objects
        install_reqs = parse_requirements(filename)
        reqs += [str(ir.req) for ir in install_reqs]
    return reqs


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'mrq/version.py')) as f:
        locals = {}
        exec(f.read(), locals)
        return locals['VERSION']
    raise RuntimeError('No version info found.')

setup(
    name="mrq",
    packages=find_packages(exclude=['tests']),
    version=get_version(),
    description="Mongo Redis Queue",
    author="Pricing Assistant",
    license='MIT',
    author_email="contact@pricingassistant.com",
    url="http://github.com/pricingassistant/mrq",
    # download_url="http://chardet.feedparser.org/download/python3-chardet-1.0.1.tgz",
    keywords=["worker", "task", "distributed", "queue", "asynchronous"],
    platforms='any',
    entry_points={
        'console_scripts': [
            'mrq-worker = mrq.bin.mrq_worker:main',
            'mrq-run = mrq.bin.mrq_run:main',
            'mrq-dashboard = mrq.dashboard.app:main'
        ]
    },
    zip_safe=False,
    install_requires=get_requirements(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    long_description=open("README.md").read()
)
