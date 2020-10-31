# Microtransat Software Framework

## Getting started

### Prerequisites

* Python >= 3.8
* pip
* PlantUML (optional)

### Installation

#### Windows
1. Clone the repository.
```bash
git clone git@github.com:S-Vrijenhoek/Microtransat-Software-Framework.git
``` 
2. Create a new virtual environment.
```bash
python -m venv env
``` 
3. Activate the virtual environment.
```bash
.\env\Scripts\activate
``` 
4. Install the specified packages that are needed to run this project.
```bash
pip install -r requirements.txt
``` 

### Contributing
Make sure to pull the latest changes and to follow the steps specified below before contributing. 
1. Lint with flake8
```bash
flake8 --count --show-source --statistics src
flake8 --count --show-source --statistics tests
``` 
2. Test with unittest
```bash
python -m unittest discover
``` 
If no errors occured while running these commands it is safe to push.
