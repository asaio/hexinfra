from typing import Optional, Dict, AnyStr, Any
from dataclasses import dataclass

@dataclass
class MetastoreConfig():
    """
    Represents Configurations Expected in a Metastore
    """
    encryption: dict = Optional[Dict[AnyStr, Any]]
