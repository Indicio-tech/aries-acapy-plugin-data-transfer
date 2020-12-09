"""acapy-plugin-data-transfer"""

from setuptools import setup, find_packages


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == '__main__':
    with open('README.md', 'r') as fh:
        LONG_DESCRIPTION = fh.read()

    setup(
        name='aries-acapy-plugin-data-transfer',
        version='0.1.0',
        author='Daniel Bluhm <daniel@indicio.tech>',
        description='Aries Cloud Agent - Python Plugin for Data Transfer protocol',
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        url='https://github.com/Indicio-tech/aries-acapy-plugin-data-transfer',
        license='Apache 2.0',
        packages=find_packages(),
        install_requires=parse_requirements('requirements.txt'),
        python_requires='>=3.6',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent'
        ]
    )
