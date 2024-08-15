import os
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from cnnClassifier import logger
import json
import joblib
from typing import any
import base64

@ensure_annotations
def read_yaml(path_of_yaml:Path) -> ConfigBox:
    """ read yaml file and returns
    
    Args:
        path to yaml file
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfiqBox: ConfiqBox type
    """
    try:
        with open(path_of_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path of yaml} load sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_path(list_of_paths:list,verbose=True):
      """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in list_of paths:
        os.makedirs(path,exist_ok=True)
        if verbose:
             logger.info(f"Directorys:{path} sucessfully")


@ensure_annotations
def save_json(path:Path,data:dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(Path,'w') as file:
         json.dump(data,file,indent=4)
    logger.info(f"Json_file save at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as file:
         content = json.load(file)
    
    logger.info(f"json file load sucessfully from{path}")
    return ConfigBox(content)
     
          
@ensure_annotations
def save_bin(data: Any,path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binnary file save at:{path}")

@ensure_annotations
def load_bin(path:Path) ->str:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file load from:{path}")

@ensure_annotations
def get_siz(path:Path)->str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring,filename):
     imagedata = base64.b64decode(imgstring)
     with open(filename , 'wb')as file:
          file.write(imagedata)
          file.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())








     




















