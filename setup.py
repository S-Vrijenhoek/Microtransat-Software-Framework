from distutils.core import setup

setup(name='Microtransat Software Framework',
      version='0.1',
      description='Microtransat Software Framework',
      author='Hogeschool Rotterdam',
      url='https://www.hogeschoolrotterdam.nl/',
      packages=['poseidon', 'poseidon.computation', 'poseidon.core', 'poseidon.exception',
                'poseidon.module', 'poseidon.module_factory'],
      install_requires=['flake8', 'ruamel.yaml'],)
