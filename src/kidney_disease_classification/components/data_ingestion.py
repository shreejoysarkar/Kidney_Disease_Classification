import os
import sys
from src.kidney_disease_classification.exception import CustomException
from src.kidney_disease_classification.logger import logging
import pandas as pd
from src.kidney_disease_classification.utils import read_sql_data
from sklearn.model_selection import train_test_split


from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
