from base64 import encodebytes as encodebytes
from collections import MutableMapping as MutableMapping
from collections import OrderedDict as OrderedDict
from email.utils import formatdate as formatdate
from http.client import HTTPResponse as HTTPResponse
from itertools import zip_longest as zip_longest
from typing import Any, Iterable, Mapping, Optional, Tuple, TypeVar
from urllib.parse import parse_qs as parse_qs
from urllib.parse import parse_qsl as parse_qsl
from urllib.parse import quote as quote
from urllib.parse import unquote as unquote
from urllib.parse import unquote_plus
from urllib.parse import urlencode as urlencode
from urllib.parse import urljoin as urljoin
from urllib.parse import urlparse as urlparse
from urllib.parse import urlsplit as urlsplit
from urllib.parse import urlunsplit as urlunsplit
from xml.etree import ElementTree as ETree

from botocore.exceptions import MD5UnavailableError as MD5UnavailableError
from six.moves import http_client

_R = TypeVar("_R")

class HTTPHeaders(http_client.HTTPMessage):
    @classmethod
    def from_dict(cls: _R, d: Mapping[str, Any]) -> _R: ...
    @classmethod
    def from_pairs(cls: _R, pairs: Iterable[Tuple[str, Any]]) -> _R: ...

file_type: Any
unquote_str = unquote_plus

def set_socket_timeout(http_response: Any, timeout: Any) -> None: ...
def accepts_kwargs(func: Any) -> Any: ...
def ensure_unicode(s: Any, encoding: Optional[Any] = ..., errors: Optional[Any] = ...) -> Any: ...
def ensure_bytes(s: Any, encoding: str = ..., errors: str = ...) -> Any: ...

XMLParseError = ETree.ParseError

def filter_ssl_warnings() -> None: ...
def copy_kwargs(kwargs: Any) -> Any: ...
def total_seconds(delta: Any) -> Any: ...

MD5_AVAILABLE: bool

def get_md5(*args: Any, **kwargs: Any) -> Any: ...
def compat_shell_split(s: Any, platform: Optional[Any] = ...) -> Any: ...
def get_tzinfo_options() -> Any: ...
