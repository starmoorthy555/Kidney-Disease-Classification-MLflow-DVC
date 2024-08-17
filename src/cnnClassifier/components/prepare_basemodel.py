import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import PrepareModelConfiq

class PrepareBaseModel:
    def __init__(self,config = PrepareModelConfiq):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.parms_image_size,
            include_top=self.config.parms_include_top,
            weights= self.config.parms_weights
        )
        self.save_model(path=self.config.base_model_path,model=self.model)

    #@staticmethod
    def prepare_full_model(self,model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
            for layers in model.layers:
                model.trained=False
        elif (freeze_all is not None) and (freeze_till>0):
            for layer in model.layers[:-freeze_till]:
                model.trained=False
        
        flatten_in = tf.keras.layers.Flatten()(model.output)
        
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
            )
        
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
            )
        
        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.parms_classes,  # corrected from params_classes to parms_classes
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.parms_learning_rate
        )
        self.save_model(path=self.config.base_model_updated_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

