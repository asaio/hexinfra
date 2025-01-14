from typing import Optional, Dict
import boto3
from src.hexinfra.domain.ports.driven.metastore_port import IMetastorePort
from src.hexinfra.domain.entities.metastore_config import MetastoreConfig


class GlueMetastore(IMetastorePort):
    def __init__(
        self,
        account_id: str,
        credentials: Optional[Dict] = None,
        profile: Optional[str] = None,
        region: Optional[str] = None,
    ):
        if not region:
            region = boto3.session.Session().region_name
        if profile:
            self.client = boto3.session.Session(
                profile_name=profile, region_name=region
            ).client("glue")
        if credentials:
            self.client = boto3.session.Session(**credentials).client("glue")
        self.account_id = account_id

    def get_config(self) -> MetastoreConfig:
        """
        Get Metastore Configuration
        """
        configs = MetastoreConfig(
            encryption=self.client.get_data_catalog_encryption_settings(
                CatalogId=self.account_id
            )
        )
        return configs
