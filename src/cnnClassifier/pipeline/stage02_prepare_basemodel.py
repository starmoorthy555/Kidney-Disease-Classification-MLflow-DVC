from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.prepare_basemodel import PrepareBaseModel
from src.cnnClassifier import logger


STAGE_NAME="Prepare base model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



