# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRedisDatabaseResult',
    'AwaitableGetRedisDatabaseResult',
    'get_redis_database',
    'get_redis_database_output',
]

@pulumi.output_type
class GetRedisDatabaseResult:
    """
    A collection of values returned by getRedisDatabase.
    """
    def __init__(__self__, consistent=None, creation_time=None, database_id=None, database_name=None, database_type=None, db_daily_bandwidth_limit=None, db_disk_threshold=None, db_max_clients=None, db_max_commands_per_second=None, db_max_entry_size=None, db_max_request_size=None, db_memory_threshold=None, endpoint=None, id=None, multizone=None, password=None, port=None, read_only_rest_token=None, region=None, rest_token=None, state=None, tls=None, user_email=None):
        if consistent and not isinstance(consistent, bool):
            raise TypeError("Expected argument 'consistent' to be a bool")
        if consistent is not None:
            warnings.warn("""Consistent option is deprecated.""", DeprecationWarning)
            pulumi.log.warn("""consistent is deprecated: Consistent option is deprecated.""")

        pulumi.set(__self__, "consistent", consistent)
        if creation_time and not isinstance(creation_time, int):
            raise TypeError("Expected argument 'creation_time' to be a int")
        pulumi.set(__self__, "creation_time", creation_time)
        if database_id and not isinstance(database_id, str):
            raise TypeError("Expected argument 'database_id' to be a str")
        pulumi.set(__self__, "database_id", database_id)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if db_daily_bandwidth_limit and not isinstance(db_daily_bandwidth_limit, int):
            raise TypeError("Expected argument 'db_daily_bandwidth_limit' to be a int")
        pulumi.set(__self__, "db_daily_bandwidth_limit", db_daily_bandwidth_limit)
        if db_disk_threshold and not isinstance(db_disk_threshold, int):
            raise TypeError("Expected argument 'db_disk_threshold' to be a int")
        pulumi.set(__self__, "db_disk_threshold", db_disk_threshold)
        if db_max_clients and not isinstance(db_max_clients, int):
            raise TypeError("Expected argument 'db_max_clients' to be a int")
        pulumi.set(__self__, "db_max_clients", db_max_clients)
        if db_max_commands_per_second and not isinstance(db_max_commands_per_second, int):
            raise TypeError("Expected argument 'db_max_commands_per_second' to be a int")
        pulumi.set(__self__, "db_max_commands_per_second", db_max_commands_per_second)
        if db_max_entry_size and not isinstance(db_max_entry_size, int):
            raise TypeError("Expected argument 'db_max_entry_size' to be a int")
        pulumi.set(__self__, "db_max_entry_size", db_max_entry_size)
        if db_max_request_size and not isinstance(db_max_request_size, int):
            raise TypeError("Expected argument 'db_max_request_size' to be a int")
        pulumi.set(__self__, "db_max_request_size", db_max_request_size)
        if db_memory_threshold and not isinstance(db_memory_threshold, int):
            raise TypeError("Expected argument 'db_memory_threshold' to be a int")
        pulumi.set(__self__, "db_memory_threshold", db_memory_threshold)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if multizone and not isinstance(multizone, bool):
            raise TypeError("Expected argument 'multizone' to be a bool")
        pulumi.set(__self__, "multizone", multizone)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if read_only_rest_token and not isinstance(read_only_rest_token, str):
            raise TypeError("Expected argument 'read_only_rest_token' to be a str")
        pulumi.set(__self__, "read_only_rest_token", read_only_rest_token)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if rest_token and not isinstance(rest_token, str):
            raise TypeError("Expected argument 'rest_token' to be a str")
        pulumi.set(__self__, "rest_token", rest_token)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tls and not isinstance(tls, bool):
            raise TypeError("Expected argument 'tls' to be a bool")
        pulumi.set(__self__, "tls", tls)
        if user_email and not isinstance(user_email, str):
            raise TypeError("Expected argument 'user_email' to be a str")
        pulumi.set(__self__, "user_email", user_email)

    @property
    @pulumi.getter
    def consistent(self) -> bool:
        return pulumi.get(self, "consistent")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> int:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> str:
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> str:
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter(name="dbDailyBandwidthLimit")
    def db_daily_bandwidth_limit(self) -> int:
        return pulumi.get(self, "db_daily_bandwidth_limit")

    @property
    @pulumi.getter(name="dbDiskThreshold")
    def db_disk_threshold(self) -> int:
        return pulumi.get(self, "db_disk_threshold")

    @property
    @pulumi.getter(name="dbMaxClients")
    def db_max_clients(self) -> int:
        return pulumi.get(self, "db_max_clients")

    @property
    @pulumi.getter(name="dbMaxCommandsPerSecond")
    def db_max_commands_per_second(self) -> int:
        return pulumi.get(self, "db_max_commands_per_second")

    @property
    @pulumi.getter(name="dbMaxEntrySize")
    def db_max_entry_size(self) -> int:
        return pulumi.get(self, "db_max_entry_size")

    @property
    @pulumi.getter(name="dbMaxRequestSize")
    def db_max_request_size(self) -> int:
        return pulumi.get(self, "db_max_request_size")

    @property
    @pulumi.getter(name="dbMemoryThreshold")
    def db_memory_threshold(self) -> int:
        return pulumi.get(self, "db_memory_threshold")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def multizone(self) -> bool:
        return pulumi.get(self, "multizone")

    @property
    @pulumi.getter
    def password(self) -> str:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="readOnlyRestToken")
    def read_only_rest_token(self) -> str:
        return pulumi.get(self, "read_only_rest_token")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="restToken")
    def rest_token(self) -> str:
        return pulumi.get(self, "rest_token")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tls(self) -> bool:
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> str:
        return pulumi.get(self, "user_email")


class AwaitableGetRedisDatabaseResult(GetRedisDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRedisDatabaseResult(
            consistent=self.consistent,
            creation_time=self.creation_time,
            database_id=self.database_id,
            database_name=self.database_name,
            database_type=self.database_type,
            db_daily_bandwidth_limit=self.db_daily_bandwidth_limit,
            db_disk_threshold=self.db_disk_threshold,
            db_max_clients=self.db_max_clients,
            db_max_commands_per_second=self.db_max_commands_per_second,
            db_max_entry_size=self.db_max_entry_size,
            db_max_request_size=self.db_max_request_size,
            db_memory_threshold=self.db_memory_threshold,
            endpoint=self.endpoint,
            id=self.id,
            multizone=self.multizone,
            password=self.password,
            port=self.port,
            read_only_rest_token=self.read_only_rest_token,
            region=self.region,
            rest_token=self.rest_token,
            state=self.state,
            tls=self.tls,
            user_email=self.user_email)


def get_redis_database(database_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRedisDatabaseResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    example_db_data = upstash.get_redis_database(database_id=resource["upstash_redis_database"]["exampleDB"]["database_id"])
    ```
    """
    __args__ = dict()
    __args__['databaseId'] = database_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('upstash:index/getRedisDatabase:getRedisDatabase', __args__, opts=opts, typ=GetRedisDatabaseResult).value

    return AwaitableGetRedisDatabaseResult(
        consistent=__ret__.consistent,
        creation_time=__ret__.creation_time,
        database_id=__ret__.database_id,
        database_name=__ret__.database_name,
        database_type=__ret__.database_type,
        db_daily_bandwidth_limit=__ret__.db_daily_bandwidth_limit,
        db_disk_threshold=__ret__.db_disk_threshold,
        db_max_clients=__ret__.db_max_clients,
        db_max_commands_per_second=__ret__.db_max_commands_per_second,
        db_max_entry_size=__ret__.db_max_entry_size,
        db_max_request_size=__ret__.db_max_request_size,
        db_memory_threshold=__ret__.db_memory_threshold,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        multizone=__ret__.multizone,
        password=__ret__.password,
        port=__ret__.port,
        read_only_rest_token=__ret__.read_only_rest_token,
        region=__ret__.region,
        rest_token=__ret__.rest_token,
        state=__ret__.state,
        tls=__ret__.tls,
        user_email=__ret__.user_email)


@_utilities.lift_output_func(get_redis_database)
def get_redis_database_output(database_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRedisDatabaseResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    example_db_data = upstash.get_redis_database(database_id=resource["upstash_redis_database"]["exampleDB"]["database_id"])
    ```
    """
    ...
