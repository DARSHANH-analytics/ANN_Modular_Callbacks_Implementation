# ANN_Modular_Callbacks_Implementation

The below code in setup.py is needed to read subpackages in case we have packages inside the src packages

package_dir={"": "src"},
packages=setuptools.find_packages(where="src"),
python_requires=">=3.7",
install_requires=[
    "matplotlib",
    "numpy",
    "pandas",
    "seaborn",
    "tensorflow"
]

To make the src package available in the environment and be called like "import src" from other outside ANN_MODULAR_CALLBACKS_IMPLEMENTATION Exercise then we have to install locally in the environment
To install locally the src package use pip install -e .

if we install in the environment we can call the imports in training.py files starting with src i.e. i mean
instead of calling as 
--> from utils.common_utils import read_config 
we can call as 
--> from scr.utils.common_utils import read_config
