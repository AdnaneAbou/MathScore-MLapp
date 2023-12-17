from setuptools import find_packages,setup
from typing import List


HYPHEN_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This Function return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements= [req.replace("\n"," ") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)


    return  requirements


setup(

name='end2end-ml',
version='0.0.1',
author='Adnane Aboutalib',
author_email='adnane.aboutalib@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)