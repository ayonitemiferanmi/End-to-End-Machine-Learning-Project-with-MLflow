from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_training import ModelTraining
from src.mlProject import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_training_config = ModelTraining(config=model_training_config)
        model_training_config.train_model()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=====x")
    except Exception as e:
        logger.exception(e)
        raise e