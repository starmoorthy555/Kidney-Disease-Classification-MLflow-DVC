import setuptools

with open("README.md",'r',encoding='utf-8') as file:
    long_discription = file.read()

__version__="0.0.0"

REPO_NAME = "Kidney-Disease-Classification-MLflow-DVC"
AUTHOR_NAME = 'starmoorthy55'
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = 'starmoorthy555@gmailcom'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small pakage for cnn app',
    long_description=long_discription,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
    )