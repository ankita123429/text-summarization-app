import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="Textsummarizationapp"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "research/trial.ipynb"
]
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename =os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for this {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
            logging.info(f"{filename} is already exist")
       


