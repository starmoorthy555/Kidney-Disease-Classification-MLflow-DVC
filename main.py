from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage02_prepare_basemodel import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.stage03_model_training import Model_Training_Pipeline
from src.cnnClassifier.pipeline.stage04_model_evaluation import EvaluationPipeline


STAGE_NAME =  "Data Ingestion Stage"
try:
    logger.info(f">>>>stage:{STAGE_NAME} started<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>stage:{STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME =  "Preparebase model"


try:
    logger.info(f">>>>stage:{STAGE_NAME} started<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>stage:{STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
        


STAGE_NAME = "Model_Training"
try:
    logger.info(f">>>>stage:{STAGE_NAME} started<<<<<<")
    obj = Model_Training_Pipeline()
    obj.main()
    logger.info(f">>>>>stage:{STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model_Evaluation"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
        