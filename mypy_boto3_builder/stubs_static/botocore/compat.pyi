from base64 import encodebytes as encodebytes
from collections import OrderedDict as OrderedDict
from email.utils import formatdate as formatdate
from http.client import HTTPMessage
from http.client import HTTPResponse as HTTPResponse
from itertools import zip_longest as zip_longest
from re import Pattern
from typing import Any, Dict, Iterable, Mapping, Optional, Tuple, Type, TypeVar
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

_R = TypeVar("_R")

class HTTPHeaders(HTTPMessage):
    @classmethod
    def from_dict(cls: Type[_R], d: Mapping[str, Any]) -> _R: ...
    @classmethod
    def from_pairs(cls: Type[_R], pairs: Iterable[Tuple[str, Any]]) -> _R: ...

file_type: Any
unquote_str = unquote_plus

def set_socket_timeout(http_response: Any, timeout: Any) -> None: ...
def accepts_kwargs(func: Any) -> Any: ...
def ensure_unicode(s: Any, encoding: Optional[Any] = ..., errors: Optional[Any] = ...) -> Any: ...
def ensure_bytes(s: Any, encoding: str = ..., errors: str = ...) -> Any: ...

XMLParseError = ETree.ParseError

def filter_ssl_warnings() -> None: ...
def _from_dict(cls: Type[_R], d: Dict[str, Any]) -> _R: ...

from_dict = classmethod(_from_dict)

def _from_pairs(cls: Type[_R], d: Dict[str, Any]) -> _R: ...

from_pairs = classmethod(_from_pairs)

def copy_kwargs(kwargs: Any) -> Any: ...
def total_seconds(delta: Any) -> Any: ...

MD5_AVAILABLE: bool

def get_md5(*args: Any, **kwargs: Any) -> Any: ...
def compat_shell_split(s: Any, platform: Optional[Any] = ...) -> Any: ...
def get_tzinfo_options() -> Any: ...

HAS_CRT: bool
IPV4_PAT: str
HEX_PAT: str
LS32_PAT: str
UNRESERVED_PAT: str
IPV6_PAT: str
ZONE_ID_PAT: str
IPV6_ADDRZ_PAT: str
IPV6_ADDRZ_RE: Pattern[str]
UNSAFE_URL_CHARS: frozenset[str]
HAS_GZIP: bool
