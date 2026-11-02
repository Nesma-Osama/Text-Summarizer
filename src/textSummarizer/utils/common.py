import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from textSummarizer.logging import logger
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """Reads a yaml file and returns the content

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        e: empty file
        ValueError: if ymal is empty file

    Returns:
       ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file:{path_to_yaml} is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
            
@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB

    Args:
        path (Path): path of file

    Returns:
        str: size in KB
    """
    size_in_kb=(os.path.getsize(path))/1024
    return f"~{size_in_kb:.2f} KB"
