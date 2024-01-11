from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    description='A brief description of my project',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
