from datetime import datetime
from sensor.constants import training_pipeline
from sensor.constants.training_pipeline import *
from sensor.exception import SensorException
import os,sys
class TrainingPipelineConfig:
    def __init__(self,timestamp = datetime.now()):
        try:
            timestamp = timestamp.strftime('%m_%d_%Y-%H_%M_%S')
            self.pipeline_name:str = training_pipeline.PIPELINE_NAME 
            self.artifact_dir_path = os.path.join(training_pipeline.ARTIFACT_DIR,timestamp)
            self.timestamp = timestamp
        except Exception as e:
            raise SensorException(e,sys)
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_ingestion_dir = os.path.join(
                training_pipeline_config.artifact_dir_path,training_pipeline.DATA_INGESTION_DIR_NAME
            )
            self.feature_store_file_path = os.path.join(
                self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
                training_pipeline.FILE_NAME
            )
            self.training_file_path = os.path.join(
                self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,
                training_pipeline.TRAIN_FILE_NAME
                )
            self.testing_file_path = os.path.join(
                self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,
                training_pipeline.TEST_FILE_NAME
            )
            self.train_test_split_ratio:float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
            self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME 
        except Exception as e:
            raise SensorException(e,sys)

class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir_path,training_pipeline.DATA_VALIDATION_DIR_NAME)
            
            self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
            
            self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
            
            self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
            
            self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
            
            self.invalid_train_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
            
            self.invalid_test_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
            
            self.drift_report_file_path:str = os.path.join(
                self.data_validation_dir,
                training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
                training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
            )
        except Exception as e:
            raise SensorException(e,sys)

class DataTransformationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_transformation_dir:str = os.path.join(
            training_pipeline_config.artifact_dir_path,training_pipeline.DATA_TRANSFORMATION_DIR_NAME
            )
            self.transformed_train_file_path:str = os.path.join(
                self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                training_pipeline.TRAIN_FILE_NAME.replace('csv','npy')
            )
            self.transformed_test_file_path:str = os.path.join(
                self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                training_pipeline.TEST_FILE_NAME.replace('csv','npy')
            )
            self.transformed_object_file_path = os.path.join(self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME)

        except Exception as e:
            raise SensorException(e,sys)

class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.model_trainer_dir:str = os.path.join(training_pipeline_config.artifact_dir_path,
            training_pipeline.MODEL_TRAINER_DIR_NAME)
            
            self.trained_model_file_path = os.path.join(self.model_trainer_dir,
            training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,training_pipeline.MODEL_TRAINER_TRAINED_MODEL_FILE_NAME)

            self.expected_accuracy:float = training_pipeline.MODEL_TRAINER_EXPECTED_SCORE

            self.overfitting_underfitting_threshold:float = training_pipeline.MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD
        except Exception as e:
            raise SensorException(e,sys)

class ModelEvaluationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.model_evaluation_dir:str = os.path.join(
                training_pipeline_config.artifact_dir_path,training_pipeline.MODEL_EVALUATION_DIR_NAME
            )
            self.report_file_path = os.path.join(
                self.model_evaluation_dir,training_pipeline.MODEL_EVALUATION_REPORT_NAME
            )
            self.change_threshold = training_pipeline.MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
        except Exception as e:
            raise SensorException(e,sys)

class ModelPusherConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.model_pusher_dir:str = os.path.join(
                training_pipeline_config.artifact_dir_path,training_pipeline.MODEL_PUSHER_DIR_NAME
            )
            self.model_file_path = os.path.join(self.model_pusher_dir,training_pipeline.MODEL_FILE_NAME)
            timestamp = round(datetime.now().timestamp())
            self.saved_model_path = os.path.join(
                training_pipeline.SAVED_MODEL_DIR,
                f"{timestamp}",
                training_pipeline.MODEL_FILE_NAME
            )
        except Exception as e:
            raise SensorException(e,sys)
