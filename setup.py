from setuptools import setup


setup(
    name='mstd_sentry',
    version='0.0.1',
    description='',
    long_description='',
    author='Romain Dorgueil',
    author_email='romain@makersquad.fr',
    license='Apache Software License',
    packages=['mstd.sentry'],
    install_requires=[
        "sentry-sdk ~= 1.5.2",
    ],
    zip_safe=False,
)
