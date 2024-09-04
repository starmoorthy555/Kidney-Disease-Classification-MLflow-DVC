from src.cnnClassifier.components.model_training import Training
from src.cnnClassifier.config.configration import ConfigurationManager

class Model_Training_Pipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generater()
        training.train()