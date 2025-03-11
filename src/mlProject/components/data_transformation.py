import os
from src.mlProject import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlProject.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

        ## Note: You can add different data transformation techniques such as scaler, PCA and all
        ## You can also perform all kinds of EDA in ML cycle here before passing this data to the model

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test [0.75, 0.25]
        train, test = train_test_split(data, test_size=0.25)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted  data into training and test")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape) 