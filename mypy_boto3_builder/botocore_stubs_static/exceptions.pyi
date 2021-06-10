import sys
from typing import IO, Any, Dict, Iterable, Mapping

import requests
import urllib3

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class ClientErrorResponseError(TypedDict, total=False):
    Code: str
    Message: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int

class ClientErrorResponseTypeDef(TypedDict, total=False):
    Error: ClientErrorResponseError
    ResponseMetadata: ResponseMetadataTypeDef

class BotoCoreError(Exception):
    fmt: str
    def __init__(self, **kwargs: Any) -> None:
        self.kwargs: Mapping[str, Any]

class DataNotFoundErrorKwargs(TypedDict):
    data_path: str

class DataNotFoundError(BotoCoreError):
    def __init__(self, *, data_path: str = ..., **kwargs: Any) -> None:
        self.kwargs: DataNotFoundErrorKwargs

class UnknownServiceErrorKwargs(DataNotFoundErrorKwargs):
    service_name: str
    known_service_names: Iterable[str]

class UnknownServiceError(DataNotFoundError):
    def __init__(
        self, *, service_name: str = ..., known_service_names: Iterable[str] = ..., **kwargs: Any
    ) -> None:
        self.kwargs: UnknownServiceErrorKwargs

class ApiVersionNotFoundErrorKwargs(TypedDict):
    service_name: str
    api_version: str

class ApiVersionNotFoundError(BotoCoreError):
    def __init__(self, *, data_path: str = ..., api_version: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownServiceErrorKwargs

class HTTPClientErrorKwargs(TypedDict):
    error: Exception

class HTTPClientError(BotoCoreError):
    def __init__(self, request: Any = ..., response: Any = ..., **kwargs: Any) -> None:
        self.kwargs: HTTPClientErrorKwargs

class ConnectionErrorKwargs(TypedDict):
    error: Exception

class ConnectionError(BotoCoreError):
    def __init__(self, *, error: Exception = ..., **kwargs: Any) -> None:
        self.kwargs: ConnectionErrorKwargs

class InvalidIMDSEndpointErrorKwargs(TypedDict):
    endpoint: str

class InvalidIMDSEndpointError(BotoCoreError):
    def __init__(self, *, endpoint: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidIMDSEndpointErrorKwargs

class EndpointURLErrorKwargs(ConnectionErrorKwargs):
    endpoint_url: str

class EndpointConnectionError(ConnectionError):
    def __init__(self, *, endpoint_url: str = ..., **kwargs: Any) -> None:
        self.kwargs: EndpointURLErrorKwargs

class SSLErrorKwargs(TypedDict):
    endpoint_url: str
    error: Exception

class SSLError(ConnectionError, requests.exceptions.SSLError):
    def __init__(self, *, endpoint_url: str = ..., error: Exception = ..., **kwargs: Any) -> None:
        self.kwargs: SSLErrorKwargs

class ConnectionClosedError(HTTPClientError):
    def __init__(self, *, endpoint_url: str = ..., **kwargs: Any) -> None:
        self.kwargs: EndpointURLErrorKwargs

class ReadTimeoutError(
    HTTPClientError, requests.exceptions.ReadTimeout, urllib3.exceptions.ReadTimeoutError
):
    def __init__(self, *, endpoint_url: str = ..., **kwargs: Any) -> None:
        self.kwargs: EndpointURLErrorKwargs

class ConnectTimeoutError(ConnectionError, requests.exceptions.ConnectTimeout):
    def __init__(self, *, endpoint_url: str = ..., **kwargs: Any) -> None:
        self.kwargs: EndpointURLErrorKwargs

class ProxyConnectionErrorKwargs(ConnectionErrorKwargs):
    proxy_url: str

class ProxyConnectionError(ConnectionError, requests.exceptions.ProxyError):
    def __init__(self, *, proxy_url: str = ..., **kwargs: Any) -> None:
        self.kwargs: ProxyConnectionErrorKwargs

class NoCredentialsError(BotoCoreError): ...

class PartialCredentialsErrorKwargs(TypedDict):
    provider: str
    cred_var: str

class PartialCredentialsError(BotoCoreError):
    def __init__(self, *, provider: str = ..., cred_var: str = ..., **kwargs: Any) -> None:
        self.kwargs: PartialCredentialsErrorKwargs

class CredentialRetrievalErrorKwargs(TypedDict):
    provider: str

class CredentialRetrievalError(BotoCoreError):
    def __init__(self, *, provider: str = ..., **kwargs: Any) -> None:
        self.kwargs: CredentialRetrievalErrorKwargs

class UnknownSignatureVersionErrorKwargs(TypedDict):
    signature_version: str

class UnknownSignatureVersionError(BotoCoreError):
    def __init__(self, *, signature_version: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownSignatureVersionErrorKwargs

class ServiceNotInRegionErrorKwargs(TypedDict):
    service_name: str
    region_name: str

class ServiceNotInRegionError(BotoCoreError):
    def __init__(self, *, service_name: str = ..., region_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: ServiceNotInRegionErrorKwargs

class BaseEndpointResolverError(BotoCoreError): ...
class NoRegionError(BaseEndpointResolverError): ...

class UnknownEndpointErrorKwargs(TypedDict):
    service_name: str
    region_name: str

class UnknownEndpointError(BaseEndpointResolverError, ValueError):
    def __init__(self, *, service_name: str = ..., region_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownEndpointErrorKwargs

class UnknownFIPSEndpointErrorKwargs(TypedDict):
    service_name: str
    region_name: str

class UnknownFIPSEndpointError(BaseEndpointResolverError):
    def __init__(self, *, service_name: str = ..., region_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownFIPSEndpointErrorKwargs

class ProfileNotFoundKwargs(TypedDict):
    profile: str

class ProfileNotFound(BotoCoreError):
    def __init__(self, *, profile: str = ..., **kwargs: Any) -> None:
        self.kwargs: ProfileNotFoundKwargs

class ConfigParseErrorKwargs(TypedDict):
    path: str

class ConfigParseError(BotoCoreError):
    def __init__(self, *, path: str = ..., **kwargs: Any) -> None:
        self.kwargs: ConfigParseErrorKwargs

class ConfigNotFoundKwargs(TypedDict):
    path: str

class ConfigNotFound(BotoCoreError):
    def __init__(self, *, path: str = ..., **kwargs: Any) -> None:
        self.kwargs: ConfigNotFoundKwargs

class MissingParametersErrorKwargs(TypedDict):
    object: Any
    missing: Iterable[str]

class MissingParametersError(BotoCoreError):
    def __init__(self, *, object: Any = ..., missing: Iterable[str] = ..., **kwargs: Any) -> None:
        self.kwargs: MissingParametersErrorKwargs

class ValidationErrorKwargs(TypedDict):
    value: Any
    param: str
    type_name: str

class ValidationError(BotoCoreError):
    def __init__(
        self, *, value: Any = ..., param: str = ..., type_name: str = ..., **kwargs: Any
    ) -> None:
        self.kwargs: ValidationErrorKwargs

class ParamValidationErrorKwargs(TypedDict):
    report: str

class ParamValidationError(BotoCoreError):
    def __init__(self, *, report: str = ..., **kwargs: Any) -> None:
        self.kwargs: ParamValidationErrorKwargs

class UnknownKeyErrorKwargs(ValidationErrorKwargs):
    choices: Iterable[Any]

class UnknownKeyError(ValidationError):
    def __init__(
        self, *, value: Any = ..., param: str = ..., choices: Iterable[Any] = ..., **kwargs: Any
    ) -> None:
        self.kwargs: UnknownKeyErrorKwargs

class RangeErrorKwargs(ValidationErrorKwargs):
    min_value: Any
    max_value: Any

class RangeError(ValidationError):
    def __init__(
        self,
        *,
        value: Any = ...,
        param: str = ...,
        min_value: Any = ...,
        max_value: Any = ...,
        **kwargs: Any,
    ) -> None:
        self.kwargs: RangeErrorKwargs

class UnknownParameterErrorKwargs(ValidationErrorKwargs):
    name: str
    operation: str
    choices: Iterable[str]

class UnknownParameterError(ValidationError):
    def __init__(
        self, *, name: str = ..., operation: str = ..., choices: Iterable[str] = ..., **kwargs: Any
    ) -> None:
        self.kwargs: UnknownParameterErrorKwargs

class InvalidRegionErrorKwargs(ValidationErrorKwargs):
    region_name: str

class InvalidRegionError(ValidationError, ValueError):
    def __init__(self, *, region_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidRegionErrorKwargs

class AliasConflictParameterErrorKwargs(ValidationErrorKwargs):
    original: str
    alias: str
    operation: str

class AliasConflictParameterError(ValidationError):
    def __init__(
        self, *, original: str = ..., alias: str = ..., operation: str = ..., **kwargs: Any
    ) -> None:
        self.kwargs: AliasConflictParameterErrorKwargs

class UnknownServiceStyleKwargs(TypedDict):
    service_style: str

class UnknownServiceStyle(BotoCoreError):
    def __init__(self, *, service_style: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownServiceStyleKwargs

class PaginationErrorKwargs(TypedDict):
    message: str

class PaginationError(BotoCoreError):
    def __init__(self, *, message: str = ..., **kwargs: Any) -> None:
        self.kwargs: PaginationErrorKwargs

class OperationNotPageableErrorKwargs(TypedDict):
    operation_name: str

class OperationNotPageableError(BotoCoreError):
    def __init__(self, *, operation_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: OperationNotPageableErrorKwargs

class ChecksumErrorKwargs(TypedDict):
    checksum_type: str
    expected_checksum: str
    actual_checksum: str

class ChecksumError(BotoCoreError):
    def __init__(
        self,
        *,
        checksum_type: str = ...,
        expected_checksum: str = ...,
        actual_checksum: str = ...,
        **kwargs: Any,
    ) -> None:
        self.kwargs: ChecksumErrorKwargs

class UnseekableStreamErrorKwargs(TypedDict):
    stream_object: IO[Any]

class UnseekableStreamError(BotoCoreError):
    def __init__(self, *, stream_object: IO[Any] = ..., **kwargs: Any) -> None:
        self.kwargs: UnseekableStreamErrorKwargs

class WaiterError(BotoCoreError):
    def __init__(self, name: str, reason: str, last_response: ClientErrorResponseTypeDef) -> None:
        self.last_response: ClientErrorResponseTypeDef

class IncompleteReadErrorKwargs(TypedDict):
    actual_bytes: int
    expected_bytes: int

class IncompleteReadError(BotoCoreError):
    def __init__(
        self, *, actual_bytes: int = ..., expected_bytes: int = ..., **kwargs: Any
    ) -> None:
        self.kwargs: IncompleteReadErrorKwargs

class InvalidExpressionErrorKwargs(TypedDict):
    expression: str

class InvalidExpressionError(BotoCoreError):
    def __init__(self, *, expression: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidExpressionErrorKwargs

class UnknownCredentialErrorKwargs(TypedDict):
    name: str

class UnknownCredentialError(BotoCoreError):
    def __init__(self, *, name: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownCredentialErrorKwargs

class WaiterConfigErrorKwargs(TypedDict):
    error_msg: str

class WaiterConfigError(BotoCoreError):
    def __init__(self, *, error_msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: WaiterConfigErrorKwargs

class UnknownClientMethodErrorKwargs(TypedDict):
    method_name: str

class UnknownClientMethodError(BotoCoreError):
    def __init__(self, *, method_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnknownClientMethodErrorKwargs

class UnsupportedSignatureVersionErrorKwargs(TypedDict):
    signature_version: str

class UnsupportedSignatureVersionError(BotoCoreError):
    def __init__(self, *, signature_version: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedSignatureVersionErrorKwargs

class ClientError(Exception):
    MSG_TEMPLATE: str
    def __init__(self, error_response: ClientErrorResponseTypeDef, operation_name: str) -> None:
        self.response: ClientErrorResponseTypeDef
        self.operation_name: str

class EventStreamError(ClientError): ...
class UnsupportedTLSVersionWarning(Warning): ...
class ImminentRemovalWarning(Warning): ...

class InvalidDNSNameErrorKwargs(TypedDict):
    bucket_name: str

class InvalidDNSNameError(BotoCoreError):
    def __init__(self, *, bucket_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidDNSNameErrorKwargs

class InvalidS3AddressingStyleErrorKwargs(TypedDict):
    s3_addressing_style: str

class InvalidS3AddressingStyleError(BotoCoreError):
    def __init__(self, *, s3_addressing_style: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidS3AddressingStyleErrorKwargs

class UnsupportedS3ArnErrorKwargs(TypedDict):
    arn: str

class UnsupportedS3ArnError(BotoCoreError):
    def __init__(self, *, arn: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedS3ArnErrorKwargs

class UnsupportedS3ControlArnErrorKwargs(TypedDict):
    arn: str
    msg: str

class UnsupportedS3ControlArnError(BotoCoreError):
    def __init__(self, *, arn: str = ..., msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedS3ControlArnErrorKwargs

class InvalidHostLabelErrorKwargs(TypedDict):
    label: str

class InvalidHostLabelError(BotoCoreError):
    def __init__(self, *, label: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidHostLabelErrorKwargs

class UnsupportedOutpostResourceErrorKwargs(TypedDict):
    resource_name: str

class UnsupportedOutpostResourceError(BotoCoreError):
    def __init__(self, *, resource_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedOutpostResourceErrorKwargs

class UnsupportedS3ErrorKwargs(TypedDict):
    msg: str

class UnsupportedS3ConfigurationError(BotoCoreError):
    def __init__(self, *, msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedS3ErrorKwargs

class UnsupportedS3AccesspointConfigurationError(BotoCoreError):
    def __init__(self, *, msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedS3ErrorKwargs

class InvalidEndpointDiscoveryConfigurationErrorKwargs(TypedDict):
    config_value: str

class InvalidEndpointDiscoveryConfigurationError(BotoCoreError):
    def __init__(self, *, config_value: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidEndpointDiscoveryConfigurationErrorKwargs

class UnsupportedS3ControlConfigurationError(BotoCoreError):
    def __init__(self, *, msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: UnsupportedS3ErrorKwargs

class InvalidRetryConfigurationErrorKwargs(TypedDict):
    retry_config_option: str

class InvalidRetryConfigurationError(BotoCoreError):
    def __init__(self, *, retry_config_option: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidRetryConfigurationErrorKwargs

class InvalidMaxRetryAttemptsErrorKwargs(InvalidRetryConfigurationErrorKwargs):
    provided_max_attempts: int
    min_value: int

class InvalidMaxRetryAttemptsError(InvalidRetryConfigurationError):
    def __init__(
        self, *, provided_max_attempts: int = ..., min_value: int = ..., **kwargs: Any
    ) -> None:
        self.kwargs: InvalidMaxRetryAttemptsErrorKwargs

class InvalidRetryModeErrorKwargs(InvalidRetryConfigurationErrorKwargs):
    provided_retry_mode: str

class InvalidRetryModeError(InvalidRetryConfigurationError):
    def __init__(self, *, provided_retry_mode: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidRetryModeErrorKwargs

class InvalidS3UsEast1RegionalEndpointConfigErrorKwargs(TypedDict):
    s3_us_east_1_regional_endpoint_config: str

class InvalidS3UsEast1RegionalEndpointConfigError(BotoCoreError):
    def __init__(self, *, s3_us_east_1_regional_endpoint_config: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidS3UsEast1RegionalEndpointConfigErrorKwargs

class InvalidSTSRegionalEndpointsConfigErrorKwargs(TypedDict):
    sts_regional_endpoints_config: str

class InvalidSTSRegionalEndpointsConfigError(BotoCoreError):
    def __init__(self, *, sts_regional_endpoints_config: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidSTSRegionalEndpointsConfigErrorKwargs

class StubResponseErrorKwargs(TypedDict):
    operation_name: str

class StubResponseError(BotoCoreError):
    def __init__(self, *, operation_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: StubResponseErrorKwargs

class StubAssertionError(StubResponseError, AssertionError): ...
class UnStubbedResponseError(StubResponseError): ...

class InvalidConfigErrorKwargs(TypedDict):
    error_msg: str

class InvalidConfigError(BotoCoreError):
    def __init__(self, *, error_msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: InvalidConfigErrorKwargs

class InfiniteLoopConfigErrorKwargs(InvalidConfigErrorKwargs):
    source_profile: str
    visited_profiles: Iterable[str]

class InfiniteLoopConfigError(InvalidConfigError):
    def __init__(
        self, *, source_profile: str = ..., visited_profiles: Iterable[str] = ..., **kwargs: Any
    ) -> None:
        self.kwargs: InfiniteLoopConfigErrorKwargs

class RefreshWithMFAUnsupportedError(BotoCoreError): ...
class MD5UnavailableError(BotoCoreError): ...

class MetadataRetrievalErrorKwargs(TypedDict):
    error_msg: str

class MetadataRetrievalError(BotoCoreError):
    def __init__(self, *, error_msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: MetadataRetrievalErrorKwargs

class UndefinedModelAttributeError(Exception): ...

class MissingServiceIdErrorKwargs(TypedDict):
    service_name: str

class MissingServiceIdError(UndefinedModelAttributeError):
    def __init__(self, *, service_name: str = ..., **kwargs: Any) -> None:
        self.kwargs: MissingServiceIdErrorKwargs

class SSOError(BotoCoreError): ...

class SSOTokenLoadErrorKwargs(TypedDict):
    error_msg: str

class SSOTokenLoadError(SSOError):
    def __init__(self, *, error_msg: str = ..., **kwargs: Any) -> None:
        self.kwargs: SSOTokenLoadErrorKwargs

class UnauthorizedSSOTokenError(SSOError): ...
class CapacityNotAvailableError(BotoCoreError): ...
class InvalidProxiesConfigError(BotoCoreError): ...
