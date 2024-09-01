from botocore.configprovider import ConfigValueStore, SmartDefaultsConfigStoreFactory

class AioSmartDefaultsConfigStoreFactory(SmartDefaultsConfigStoreFactory):
    async def merge_smart_defaults(  # type: ignore [override]
        self,
        config_store: ConfigValueStore,
        mode: str,
        region_name: str,
    ) -> None: ...
    async def resolve_auto_mode(self, region_name: str) -> str: ...  # type: ignore [override]
