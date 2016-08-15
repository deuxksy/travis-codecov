from setuptools import setup, find_packages

setup(
    name='template_korean',
    version='0.0.1',
    package = find_packages(),
    install_requires=[
        'django',
        'korean',
    ]
)