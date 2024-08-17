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