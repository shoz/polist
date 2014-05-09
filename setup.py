from setuptools import setup

def readme():
    with open("README.rst") as f:
        return f.read()

setup(
    name='polist',
    version='0.0.2',
    description='polist, partially ordered list',
    long_description=readme(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        ],
    keywords='data structure list topological sort',
    author='Shoji Ihara',
    author_email='shoji.ihara@gmail.com',
    url='https://github.com/shoz/polist',
    packages=['polist'],
    license='MIT'
)
