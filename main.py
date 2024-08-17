from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage02_prepare_basemodel import PrepareBaseModelPipeline

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
if __name__ =="__main__":
    try:
        logger.info(f">>>>stage:{STAGE_NAME} started<<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>stage:{STAGE_NAME} completed<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e