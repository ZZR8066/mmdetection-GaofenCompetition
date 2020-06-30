from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class iSAIDDataset(CocoDataset):

    CLASSES = ('Small_Vehicle', 'Large_Vehicle', 'plane', 'storage_tank', 'ship', 'Swimming_pool', 'Harbor',         
                'tennis_court', 'Ground_Track_Field', 'Soccer_ball_field', 'baseball_diamond', 
                'Bridge', 'basketball_court', 'Roundabout', 'Helicopter')