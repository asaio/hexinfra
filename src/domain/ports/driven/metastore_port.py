from abc import ABC, abstractmethod
from typing import List, Dict, AnyStr, Any
from src.hexinfra.domain.entities.metastore_config import MetastoreConfig


class IMetastorePort(ABC):
    """
    Representation of a Metastore

    Keyword arguments:


    """

    @abstractmethod
    def list_databases(self) -> List[Dict[AnyStr, Any]]:
        """
        List All Databases in Metastore
        """
        raise NotImplementedError()

    @abstractmethod
    def get_database(self, database: str) -> Dict[AnyStr, Any]:
        """
        Get A single Database and its Metadata from Metastore
        """
        raise NotImplementedError()

    @abstractmethod
    def list_tables(self, database: str) -> List[Dict[AnyStr, Any]]:
        """
        List All Tables in a Database in Metastore
        """
        raise NotImplementedError()

    @abstractmethod
    def get_table(self, database: str, table: str) -> Dict[AnyStr, Any]:
        """
        Get a single Table and its Metadata from Metastore
        """
        raise NotImplementedError()

    @abstractmethod
    def list_partitions(self, database: str, table: str) -> Dict[AnyStr, Any]:
        """
        List All Partitions from a Table in a Database in Metastore
        """
        raise NotImplementedError()

    @abstractmethod
    def get_partition(
        self, database: str, table: str, partition: dict
    ) -> Dict[AnyStr, Any]:
        """
        Get a single Partition and its Metadata from Metastore
        """
        raise NotImplementedError()

    @abstractmethod
    def get_config(self) -> MetastoreConfig:
        """
        Get Metastore Configuration
        """
        raise NotImplementedError()

    @abstractmethod
    def update_config(self, config: Dict[AnyStr, Any]) -> Dict[AnyStr, Any]:
        """
        Creates or Updates Metastore Configuration
        """
        raise NotImplementedError()
