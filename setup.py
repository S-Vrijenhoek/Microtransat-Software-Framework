from distutils.core import setup

setup(name='Microtransat Software Framework',
      version='0.1.1',
      description='Microtransat Software Framework',
      author='Hogeschool Rotterdam',
      url='https://www.hogeschoolrotterdam.nl/',
      packages=['poseidon'],
      package_dir={'poseidon': 'poseidon'},
      package_data={'poseidon': ['poseidon/settings.yaml']},
      install_requires=['flake8', 'ruamel.yaml'],)
