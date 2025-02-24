from setuptools import setup, find_packages

setup(
    name='weather',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'geocoder',
    ],
    entry_points={
        'console_scripts': [
            'weather=weather_cli:cli',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)