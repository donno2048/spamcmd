from setuptools import setup
from itertools import product
console_scripts = []
for i in range(1, 4):
    for j in product([chr(k) for k in range(97, 123)], repeat=i): console_scripts += ["".join(j) + "=random:seed"]
setup(
    name='spamcmd',
    version='1.0.0',
    description='Delete every three letters command in the cmd using brute-force',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/spamcmd',
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': console_scripts }
)