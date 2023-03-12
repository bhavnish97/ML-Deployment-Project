import os
import sys

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)


from exception import CustomException
from logger import logging
import data_transformation

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact',"train.csv")
    test_data_path: str = os.path.join('artifact',"test.csv")
    raw_data_path: str = os.path.join('artifact',"raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered in data ingesion step")

        try:
            df = pd.read_csv('notebooks/StudentsPerformance.csv')
            logging.info("dataset exported now in dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("train_test_split initialted")

            train_set, test_set = train_test_split(df,test_size=0.2, random_state=48)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data completed now")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
