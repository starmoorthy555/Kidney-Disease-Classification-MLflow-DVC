from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class PrepareModelConfiq:
    root_dir: Path
    base_model_path: Path
    base_model_updated_path: Path
    parms_image_size: list
    parms_learning_rate: float
    parms_include_top: bool
    parms_weights: str
    parms_classes: int

@dataclass(frozen=True)
class TrainingConfiq:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    parms_epoch: int
    parms_batch_size: int
    parms_is_augumentaion: bool
    parms_image_size: list