from setuptools import setup, find_packages

long_desc = '''
This package contains the jsx_directive Sphinx extension.

jsx_directive adds a directive named ``jsx`` which supports injecting JSX code
into page
'''

requires = [
    'Sphinx>=1.0',
    'PyReact>=0.3.0'
]

setup(
    name='sphinxcontrib-jsx',
    version='',
    license='AGPLv3',
    author='Prometheus Research, LLC',
    description='Sphinx JSX directive extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
