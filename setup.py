from setuptools import setup, find_packages

setup(name='Microtransat Software Framework',
      version='0.4',
      description='Microtransat Software Framework',
      author='Hogeschool Rotterdam',
      url='https://www.hogeschoolrotterdam.nl/',
      packages=find_packages(exclude=['.github', 'docs', 'tests']),
      package_data={'poseidon': ['example_settings.yaml']},
      include_package_data=True,
      install_requires=['ruamel.yaml'],)
