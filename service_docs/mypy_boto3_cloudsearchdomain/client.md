# CloudSearchDomainClient for boto3 CloudSearchDomain module

> [Index](../index.md) > [CloudSearchDomain](./index.md) > CloudSearchDomainClient

Auto-generated documentation for [CloudSearchDomain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain)
type annotations stubs module [mypy_boto3_cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain/).

- [CloudSearchDomainClient for boto3 CloudSearchDomain module](#cloudsearchdomainclient-for-boto3-cloudsearchdomain-module)
  - [CloudSearchDomainClient](#cloudsearchdomainclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [search](#search)
    - [suggest](#suggest)
    - [upload_documents](#upload_documents)

## CloudSearchDomainClient

Type annotations for `boto3.client("cloudsearchdomain")`

Can be used directly:

```python
from mypy_boto3_cloudsearchdomain.client import CloudSearchDomainClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudsearchdomain.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DocumentServiceException`
- `Exceptions.SearchException`


## Methods


### can_paginate

Type annotations for `boto3.client("cloudsearchdomain").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudsearchdomain").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### search

Type annotations for `boto3.client("cloudsearchdomain").search` method.

[Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)

```python
def search(
    self,
    query: str,
    cursor: str = None,
    expr: str = None,
    facet: str = None,
    filterQuery: str = None,
    highlight: str = None,
    partial: bool = None,
    queryOptions: str = None,
    queryParser: QueryParser = None,
    returnFields: str = None,
    size: int = None,
    sort: str = None,
    start: int = None,
    stats: str = None
) -> SearchResponseTypeDef:
    pass
```

### suggest

Type annotations for `boto3.client("cloudsearchdomain").suggest` method.

[Client.suggest documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)

```python
def suggest(
    self,
    query: str,
    suggester: str,
    size: int = None
) -> SuggestResponseTypeDef:
    pass
```

### upload_documents

Type annotations for `boto3.client("cloudsearchdomain").upload_documents` method.

[Client.upload_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)

```python
def upload_documents(
    self,
    documents: Union[bytes, IO[bytes]],
    contentType: ContentType
) -> UploadDocumentsResponseTypeDef:
    pass
```