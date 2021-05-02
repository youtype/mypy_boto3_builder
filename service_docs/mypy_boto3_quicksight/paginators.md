# Paginators for boto3 QuickSight module

> [Index](../index.md) > [QuickSight](./index.md) > Paginators

Auto-generated documentation for [QuickSight](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight)
type annotations stubs module [mypy_boto3_quicksight](https://pypi.org/project/mypy-boto3-quicksight/).

- [Paginators for boto3 QuickSight module](#paginators-for-boto3-quicksight-module)
  - [ListAnalysesPaginator](#listanalysespaginator)
  - [ListDashboardVersionsPaginator](#listdashboardversionspaginator)
  - [ListDashboardsPaginator](#listdashboardspaginator)
  - [ListDataSetsPaginator](#listdatasetspaginator)
  - [ListDataSourcesPaginator](#listdatasourcespaginator)
  - [ListIngestionsPaginator](#listingestionspaginator)
  - [ListNamespacesPaginator](#listnamespacespaginator)
  - [ListTemplateAliasesPaginator](#listtemplatealiasespaginator)
  - [ListTemplateVersionsPaginator](#listtemplateversionspaginator)
  - [ListTemplatesPaginator](#listtemplatespaginator)
  - [ListThemeVersionsPaginator](#listthemeversionspaginator)
  - [ListThemesPaginator](#listthemespaginator)
  - [SearchAnalysesPaginator](#searchanalysespaginator)
  - [SearchDashboardsPaginator](#searchdashboardspaginator)

## ListAnalysesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_analyses")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListAnalysesPaginator

def get_list_analyses_paginator() -> ListAnalysesPaginator:
    return boto3.client("quicksight").get_paginator("list_analyses")
```

[Paginator.ListAnalyses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)

```python
class ListAnalysesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalysesResponseTypeDef]:
        pass
```
## ListDashboardVersionsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_dashboard_versions")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListDashboardVersionsPaginator

def get_list_dashboard_versions_paginator() -> ListDashboardVersionsPaginator:
    return boto3.client("quicksight").get_paginator("list_dashboard_versions")
```

[Paginator.ListDashboardVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)

```python
class ListDashboardVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        DashboardId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardVersionsResponseTypeDef]:
        pass
```
## ListDashboardsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_dashboards")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListDashboardsPaginator

def get_list_dashboards_paginator() -> ListDashboardsPaginator:
    return boto3.client("quicksight").get_paginator("list_dashboards")
```

[Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)

```python
class ListDashboardsPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsResponseTypeDef]:
        pass
```
## ListDataSetsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_data_sets")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListDataSetsPaginator

def get_list_data_sets_paginator() -> ListDataSetsPaginator:
    return boto3.client("quicksight").get_paginator("list_data_sets")
```

[Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)

```python
class ListDataSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSetsResponseTypeDef]:
        pass
```
## ListDataSourcesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_data_sources")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListDataSourcesPaginator

def get_list_data_sources_paginator() -> ListDataSourcesPaginator:
    return boto3.client("quicksight").get_paginator("list_data_sources")
```

[Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)

```python
class ListDataSourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        pass
```
## ListIngestionsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_ingestions")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListIngestionsPaginator

def get_list_ingestions_paginator() -> ListIngestionsPaginator:
    return boto3.client("quicksight").get_paginator("list_ingestions")
```

[Paginator.ListIngestions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)

```python
class ListIngestionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DataSetId: str,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionsResponseTypeDef]:
        pass
```
## ListNamespacesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_namespaces")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListNamespacesPaginator

def get_list_namespaces_paginator() -> ListNamespacesPaginator:
    return boto3.client("quicksight").get_paginator("list_namespaces")
```

[Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)

```python
class ListNamespacesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        pass
```
## ListTemplateAliasesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_template_aliases")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListTemplateAliasesPaginator

def get_list_template_aliases_paginator() -> ListTemplateAliasesPaginator:
    return boto3.client("quicksight").get_paginator("list_template_aliases")
```

[Paginator.ListTemplateAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)

```python
class ListTemplateAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        TemplateId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateAliasesResponseTypeDef]:
        pass
```
## ListTemplateVersionsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_template_versions")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListTemplateVersionsPaginator

def get_list_template_versions_paginator() -> ListTemplateVersionsPaginator:
    return boto3.client("quicksight").get_paginator("list_template_versions")
```

[Paginator.ListTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)

```python
class ListTemplateVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        TemplateId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateVersionsResponseTypeDef]:
        pass
```
## ListTemplatesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_templates")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListTemplatesPaginator

def get_list_templates_paginator() -> ListTemplatesPaginator:
    return boto3.client("quicksight").get_paginator("list_templates")
```

[Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)

```python
class ListTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        pass
```
## ListThemeVersionsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_theme_versions")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListThemeVersionsPaginator

def get_list_theme_versions_paginator() -> ListThemeVersionsPaginator:
    return boto3.client("quicksight").get_paginator("list_theme_versions")
```

[Paginator.ListThemeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)

```python
class ListThemeVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        ThemeId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemeVersionsResponseTypeDef]:
        pass
```
## ListThemesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("list_themes")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import ListThemesPaginator

def get_list_themes_paginator() -> ListThemesPaginator:
    return boto3.client("quicksight").get_paginator("list_themes")
```

[Paginator.ListThemes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)

```python
class ListThemesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        Type: ThemeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemesResponseTypeDef]:
        pass
```
## SearchAnalysesPaginator

Type annotations for `boto3.client("quicksight").get_paginator("search_analyses")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import SearchAnalysesPaginator

def get_search_analyses_paginator() -> SearchAnalysesPaginator:
    return boto3.client("quicksight").get_paginator("search_analyses")
```

[Paginator.SearchAnalyses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)

```python
class SearchAnalysesPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        Filters: List[AnalysisSearchFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchAnalysesResponseTypeDef]:
        pass
```
## SearchDashboardsPaginator

Type annotations for `boto3.client("quicksight").get_paginator("search_dashboards")`.

Can be used directly:

```python
from mypy_boto3_quicksight.paginators import SearchDashboardsPaginator

def get_search_dashboards_paginator() -> SearchDashboardsPaginator:
    return boto3.client("quicksight").get_paginator("search_dashboards")
```

[Paginator.SearchDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)

```python
class SearchDashboardsPaginator(Boto3Paginator):
    def paginate(
        self,
        AwsAccountId: str,
        Filters: List[DashboardSearchFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDashboardsResponseTypeDef]:
        pass
```