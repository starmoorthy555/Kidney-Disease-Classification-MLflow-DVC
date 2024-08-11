import os
from pathlib import Path
import logging

# Logging string(Insted of printing them we just logg it)
logging.basicConfig(level=logging.INFO,format="[%(asctime)s]:%(message)s:")

project_name = "cnnClassifier"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trail.ipynb",
    "templets/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,folder_name = os.path.split(filepath)

    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating_directory; {file_dir} for the file:{folder_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w')as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"file name allready exist")        
        
