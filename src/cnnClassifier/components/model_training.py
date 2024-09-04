import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from pathlib import Path
from cnnClassifier.entity.config_entity import TrainingConfiq

class Training:
    def __init__(self,config:TrainingConfiq):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generater(self):
        datagenerater_kwargs = dict(rescale = 1./255,validation_split = 0.20)
        dataflow_kwargs= dict(target_size = self.config.parms_image_size[:-1],batch_size = self.config.parms_batch_size,interpolation = 'bilinear')
        valid_datagenerater = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerater_kwargs)

        self.valid_generator = valid_datagenerater.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )
        if self.config.parms_is_augumentaion:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerater_kwargs
            )
        else:
            train_datagenerator = valid_datagenerater

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.parms_epoch,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )