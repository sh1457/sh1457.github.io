import setuptools


setuptools.setup(
    name='pmake',
    version='0.1.0',
    description='Custom scripts to build zola+tailwind site',
    long_description='Custom scripts to build zola+tailwind site',
    long_description_content_type='text/markdown',
    author='Sujith Sudarshan',
    author_email='sh1457@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/sh1457/sh1457.github.io',
    package_dir={'': 'src'},
    py_modules=['pmake'],
    entry_points={
        'console_scripts': ["make=pmake:make"],
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
