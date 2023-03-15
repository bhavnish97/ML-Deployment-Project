import os
import sys

import numpy as np
import pandas as pd
import dill

parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        
    except Exception as e:
        raise CustomException