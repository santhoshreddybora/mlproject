from setuptools import find_packages,setup
from typing import List


def get_requirements(get_filepath:str)->List[str]:
    '''This function will return list of requirements'''
    requirements=[]
    with open(get_filepath) as e:
        requirements=e.readlines()#will read the data line by line 
        requirements=[req.replace("\n",'') for  req in requirements] #while reading \n will append at every end of line so it will remove that in list 
        if '-e .' in requirements:
            requirements.remove('-e .')# "-e ." is placed in requirements file because whenever requirements is being installed it will automatically trigger setup.py file and we don't need -e . to execute 
    return requirements        

setup(
    name='mlproject',
    version='0.0.1',
    author='santhosh',
    author_email='borasanthosh921@gmail.com',
    packages=find_packages(),# it will find __init__.py in folder and consider that as a package and build it accordingly 
    install_requires=get_requirements('requirements.txt')
)