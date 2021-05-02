# Literals for boto3 KinesisVideo module

> [Index](../index.md) > [KinesisVideo](./index.md) > Literals

Auto-generated documentation for [KinesisVideo](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo)
type annotations stubs module [mypy_boto3_kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/).

- [Literals for boto3 KinesisVideo module](#literals-for-boto3-kinesisvideo-module)
  - [APIName](#apiname)
  - [ChannelProtocol](#channelprotocol)
  - [ChannelRole](#channelrole)
  - [ChannelType](#channeltype)
  - [ComparisonOperator](#comparisonoperator)
  - [ListSignalingChannelsPaginatorName](#listsignalingchannelspaginatorname)
  - [ListStreamsPaginatorName](#liststreamspaginatorname)
  - [Status](#status)
  - [UpdateDataRetentionOperation](#updatedataretentionoperation)

## APIName

```python
from mypy_boto3_kinesisvideo.literals import APIName
```

Values:

- `GET_CLIP`
- `GET_DASH_STREAMING_SESSION_URL`
- `GET_HLS_STREAMING_SESSION_URL`
- `GET_MEDIA`
- `GET_MEDIA_FOR_FRAGMENT_LIST`
- `LIST_FRAGMENTS`
- `PUT_MEDIA`

## ChannelProtocol

```python
from mypy_boto3_kinesisvideo.literals import ChannelProtocol
```

Values:

- `HTTPS`
- `WSS`

## ChannelRole

```python
from mypy_boto3_kinesisvideo.literals import ChannelRole
```

Values:

- `MASTER`
- `VIEWER`

## ChannelType

```python
from mypy_boto3_kinesisvideo.literals import ChannelType
```

Values:

- `SINGLE_MASTER`

## ComparisonOperator

```python
from mypy_boto3_kinesisvideo.literals import ComparisonOperator
```

Values:

- `BEGINS_WITH`

## ListSignalingChannelsPaginatorName

```python
from mypy_boto3_kinesisvideo.literals import ListSignalingChannelsPaginatorName
```

Values:

- `list_signaling_channels`

## ListStreamsPaginatorName

```python
from mypy_boto3_kinesisvideo.literals import ListStreamsPaginatorName
```

Values:

- `list_streams`

## Status

```python
from mypy_boto3_kinesisvideo.literals import Status
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `UPDATING`

## UpdateDataRetentionOperation

```python
from mypy_boto3_kinesisvideo.literals import UpdateDataRetentionOperation
```

Values:

- `DECREASE_DATA_RETENTION`
- `INCREASE_DATA_RETENTION`
