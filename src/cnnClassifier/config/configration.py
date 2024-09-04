import os
from cnnClassifier.constants import *
from src.cnnClassifier.utils.comman import read_yaml, create_path
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                    PrepareModelConfiq,
                                                    TrainingConfiq)

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
    
    def get_prepare_base_model_config(self):
        config = self.config.prepare_base_model
        create_path([config.root_dir])
        prepare_base_model_config = PrepareModelConfiq(
            root_dir = Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            base_model_updated_path=Path(config.base_model_updated_path),
            parms_image_size=self.parms.IMAGE_SIZE,
            parms_learning_rate=self.parms.LEARNING_RATE,
            parms_include_top=self.parms.INCLUDE_TOP,
            parms_weights=self.parms.WEIGHTS,
            parms_classes=self.parms.CLASSES
        )       
        return prepare_base_model_config
    
    def get_training_config(self):
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        parms = self.parms
        trainig_data = os.path.join(self.config.data_ingestion.unzip_dir,'Kidney-CT-Scan')

        create_path([Path(training.root_dir)])

        training_confiq=TrainingConfiq(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.training_model_path),
            updated_base_model_path = Path(prepare_base_model.base_model_updated_path),
            training_data = trainig_data,
            parms_epoch = parms.EPOCHS,
            parms_batch_size = parms.BATCH_SIZE,
            parms_is_augumentaion = parms.AUGUMENTATION,
            parms_image_size = parms.IMAGE_SIZE
            )
        return training_confiq