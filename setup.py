from setuptools import setup, find_packages

VERSION = 0.2

setup(
    name='inner_service_api',
    version=VERSION,
    url='https://github.com/im-so-sorry/inner-service-module',
    author="Aidar Rakhimov",
    author_email="a.v.rakhimov@gmail.com",
    description="Common services for eos system",
    long_description=open('README.md').read(),
    license=open('LICENSE').read(),
    platforms=['linux', 'mac'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    test_suite="tests",
    install_requires=[
        'requests==2.23.0',
        'environs==7.4.0',
        'redis==4.4.4',
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Other/Nonlisted Topic',
        'Programming Language :: Python :: 3.7',
    ],
)