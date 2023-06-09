from dataclasses import dataclass
from typing import List, Tuple, Optional

from dataclasses_json import dataclass_json

from coco_loader.bases import Annotation, Category, Dataset


@dataclass_json
@dataclass
class ObjectDetectionAnnotation(Annotation):
    id: int
    image_id: int
    category_id: int
    segmentation: List[List[float]]
    area: float
    bbox: Tuple[float, float, float, float]
    iscrowd: int


@dataclass_json
@dataclass
class ObjectDetectionCategory(Category):
    id: int
    name: str
    supercategory: str


@dataclass_json
@dataclass
class ObjectDetectionDataset(Dataset):
    categories: Optional[List[ObjectDetectionCategory]] = None
    annotations: Optional[List[ObjectDetectionAnnotation]] = None
