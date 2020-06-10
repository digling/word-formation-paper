from setuptools import setup, find_packages

setup(
    name='worforpy',
    description='Python code for testing and annotating word family relations in multi- and mono-lingual word lists',
    author='Johann-Mattis List and Nathanael Schweikhard',
    url='https://github.com/lingpy/morphopy',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    version='0.1.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['lingpy', 'segments'],
    extras_require={
        'dev': [
            'tox',
            'flake8',
            'wheel',
            'twine',
        ],
    },
    entry_points={
        'console_scripts': ['worforpy=worforpy.__main__:main'],
    },
)
