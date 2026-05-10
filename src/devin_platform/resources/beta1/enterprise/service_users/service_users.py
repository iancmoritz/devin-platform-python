# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ServiceUsersResource", "AsyncServiceUsersResource"]


class ServiceUsersResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> ServiceUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return ServiceUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return ServiceUsersResourceWithStreamingResponse(self)


class AsyncServiceUsersResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServiceUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncServiceUsersResourceWithStreamingResponse(self)


class ServiceUsersResourceWithRawResponse:
    def __init__(self, service_users: ServiceUsersResource) -> None:
        self._service_users = service_users

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._service_users.api_keys)


class AsyncServiceUsersResourceWithRawResponse:
    def __init__(self, service_users: AsyncServiceUsersResource) -> None:
        self._service_users = service_users

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._service_users.api_keys)


class ServiceUsersResourceWithStreamingResponse:
    def __init__(self, service_users: ServiceUsersResource) -> None:
        self._service_users = service_users

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._service_users.api_keys)


class AsyncServiceUsersResourceWithStreamingResponse:
    def __init__(self, service_users: AsyncServiceUsersResource) -> None:
        self._service_users = service_users

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._service_users.api_keys)
