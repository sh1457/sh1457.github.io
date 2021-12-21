import setuptools


setuptools.setup(
    name='dobby',
    version='0.1.0',
    description='Custom scripts to build zola+tailwind site',
    long_description='Custom scripts to build zola+tailwind site',
    long_description_content_type='text/markdown',
    author='Sujith Sudarshan',
    author_email='sh1457@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/sh1457/sh1457.github.io',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    entry_points={
        'console_scripts': ["pmake=dobby.__main__:pmake",
                            "tests=dobby.__main__:tests"],
    },
    install_requires=['click'],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
