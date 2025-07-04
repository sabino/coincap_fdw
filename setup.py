from setuptools import setup

setup(
    name='coincap_fdw',
    version='0.0.1',
    author='sabino',
    author_email='sabino@secret.fyi',
    url='https://github.com/sabino/coincap_fdw',
    license='WTFPL',
    packages=['coincap_fdw'],
    install_requires=[
        'requests==2.25.1',
        'hy==0.20.0'
    ],
    package_data={'coincap_fdw': ['*.py', '*.hy']},
    package_dir={'coincap_fdw': 'coincap_fdw'}
)


