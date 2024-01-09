from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    description='A brief description of my project',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.23.5',
        'pandas>=1.5.4',
        'requests~=2.28.1',
        'matplotlib>=3.6.2',
        'sklearn'
    ]
)
