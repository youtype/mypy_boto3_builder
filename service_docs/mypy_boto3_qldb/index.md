# Type annotations for boto3 QLDB module

> [Index](../index.md) > QLDB

Auto-generated documentation for [QLDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB)
type annotations stubs module [mypy_boto3_qldb](https://pypi.org/project/mypy-boto3-qldb/).

```bash
pip install mypy-boto3-qldb
```

- [Type annotations for boto3 QLDB module](#type-annotations-for-boto3-qldb-module)
  - [QLDBClient](#qldbclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## QLDBClient

Type annotations for  `boto3.client("qldb")` as [QLDBClient](./client.md)

Can be used directly:

```python
from mypy_boto3_qldb.client import QLDBClient
```


QLDBClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_journal_kinesis_stream](./client.md#cancel-journal-kinesis-stream)
- [create_ledger](./client.md#create-ledger)
- [delete_ledger](./client.md#delete-ledger)
- [describe_journal_kinesis_stream](./client.md#describe-journal-kinesis-stream)
- [describe_journal_s3_export](./client.md#describe-journal-s3-export)
- [describe_ledger](./client.md#describe-ledger)
- [export_journal_to_s3](./client.md#export-journal-to-s3)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_block](./client.md#get-block)
- [get_digest](./client.md#get-digest)
- [get_revision](./client.md#get-revision)
- [list_journal_kinesis_streams_for_ledger](./client.md#list-journal-kinesis-streams-for-ledger)
- [list_journal_s3_exports](./client.md#list-journal-s3-exports)
- [list_journal_s3_exports_for_ledger](./client.md#list-journal-s3-exports-for-ledger)
- [list_ledgers](./client.md#list-ledgers)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [stream_journal_to_kinesis](./client.md#stream-journal-to-kinesis)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_ledger](./client.md#update-ledger)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourcePreconditionNotMetException](./client.md#resourcepreconditionnotmetexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_qldb.literals import ErrorCause, ...
```

- [ErrorCause](./literals.md#errorcause)
- [ExportStatus](./literals.md#exportstatus)
- [LedgerState](./literals.md#ledgerstate)
- [PermissionsMode](./literals.md#permissionsmode)
- [S3ObjectEncryptionType](./literals.md#s3objectencryptiontype)
- [StreamStatus](./literals.md#streamstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_qldb.type_defs import JournalKinesisStreamDescriptionTypeDef, ...
```

- [JournalKinesisStreamDescriptionTypeDef](./type_defs.md#journalkinesisstreamdescriptiontypedef)
- [JournalS3ExportDescriptionTypeDef](./type_defs.md#journals3exportdescriptiontypedef)
- [KinesisConfigurationTypeDef](./type_defs.md#kinesisconfigurationtypedef)
- [LedgerSummaryTypeDef](./type_defs.md#ledgersummarytypedef)
- [S3EncryptionConfigurationTypeDef](./type_defs.md#s3encryptionconfigurationtypedef)
- [S3ExportConfigurationTypeDef](./type_defs.md#s3exportconfigurationtypedef)
- [ValueHolderTypeDef](./type_defs.md#valueholdertypedef)
- [CancelJournalKinesisStreamResponseTypeDef](./type_defs.md#canceljournalkinesisstreamresponsetypedef)
- [CreateLedgerResponseTypeDef](./type_defs.md#createledgerresponsetypedef)
- [DescribeJournalKinesisStreamResponseTypeDef](./type_defs.md#describejournalkinesisstreamresponsetypedef)
- [DescribeJournalS3ExportResponseTypeDef](./type_defs.md#describejournals3exportresponsetypedef)
- [DescribeLedgerResponseTypeDef](./type_defs.md#describeledgerresponsetypedef)
- [ExportJournalToS3ResponseTypeDef](./type_defs.md#exportjournaltos3responsetypedef)
- [GetBlockResponseTypeDef](./type_defs.md#getblockresponsetypedef)
- [GetDigestResponseTypeDef](./type_defs.md#getdigestresponsetypedef)
- [GetRevisionResponseTypeDef](./type_defs.md#getrevisionresponsetypedef)
- [ListJournalKinesisStreamsForLedgerResponseTypeDef](./type_defs.md#listjournalkinesisstreamsforledgerresponsetypedef)
- [ListJournalS3ExportsForLedgerResponseTypeDef](./type_defs.md#listjournals3exportsforledgerresponsetypedef)
- [ListJournalS3ExportsResponseTypeDef](./type_defs.md#listjournals3exportsresponsetypedef)
- [ListLedgersResponseTypeDef](./type_defs.md#listledgersresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [StreamJournalToKinesisResponseTypeDef](./type_defs.md#streamjournaltokinesisresponsetypedef)
- [UpdateLedgerResponseTypeDef](./type_defs.md#updateledgerresponsetypedef)
