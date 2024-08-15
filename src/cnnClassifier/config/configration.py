import os
from cnnClassifier.constants import *
from src.cnnClassifier.utils.comman import read_yaml, create_path
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
            self,
            config_file_path =CONFIG_FILE_PATH,
            parms_file_path = PARMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.parms = read_yaml(parms_file_path)
        create_path([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        os.makedirs(config.root_dir,exist_ok = True)
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url= config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            )
        return data_ingestion_config