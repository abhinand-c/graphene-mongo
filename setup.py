from setuptools import find_packages, setup

setup(
    name="graphene-mongo",
    version="0.3.1",
    description="Graphene Mongoengine integration",
    long_description=open("README.rst").read(),
    url="https://github.com/graphql-python/graphene-mongo",
    author="Abaw Chen",
    author_email="abaw.chen@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="api graphql protocol rest relay graphene mongo mongoengine",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "graphene==3.0b7",
        "promise==2.3",
        "mongoengine>=0.23.0",
        "singledispatch>=3.4.0.3",
        "iso8601>=0.1.12",
        'futures; python_version < "3.0"'
    ],
    python_requires=">=3.6",
    zip_safe=True,
    tests_require=["pytest>=3.3.2", "mongomock", "mock"],
)
