from setuptools import setup, find_packages

long_desc = '''
This package contains the ``jsx`` Sphinx extension.

Adds a directive named ``jsx`` which supports injecting JSX code into page.
'''

requires = [
    'Sphinx>=1.2',
    'PyReact>=0.3.1'
]

setup(
    name='sphinxcontrib-jsx',
    version='0.1.0',
    url='https://github.com/prometheusresearch/sphinxcontrib-jsx',
    license='BSD',
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
