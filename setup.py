from setuptools import setup

setup(
    name='weather',
    version='0.1',
    py_modules=['weather'],
    install_requires=[
        'Click',
        'requests',
        'geocoder',
    ],
    entry_points={
        'console_scripts': [
            'weather=weather:cli',
        ],
    },
)