# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .enterprise.enterprise import (
    EnterpriseResource,
    AsyncEnterpriseResource,
    EnterpriseResourceWithRawResponse,
    AsyncEnterpriseResourceWithRawResponse,
    EnterpriseResourceWithStreamingResponse,
    AsyncEnterpriseResourceWithStreamingResponse,
)
from .organizations.organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)

__all__ = ["Beta1Resource", "AsyncBeta1Resource"]


class Beta1Resource(SyncAPIResource):
    @cached_property
    def enterprise(self) -> EnterpriseResource:
        return EnterpriseResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> Beta1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return Beta1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Beta1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return Beta1ResourceWithStreamingResponse(self)


class AsyncBeta1Resource(AsyncAPIResource):
    @cached_property
    def enterprise(self) -> AsyncEnterpriseResource:
        return AsyncEnterpriseResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBeta1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBeta1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBeta1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncBeta1ResourceWithStreamingResponse(self)


class Beta1ResourceWithRawResponse:
    def __init__(self, beta1: Beta1Resource) -> None:
        self._beta1 = beta1

    @cached_property
    def enterprise(self) -> EnterpriseResourceWithRawResponse:
        return EnterpriseResourceWithRawResponse(self._beta1.enterprise)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._beta1.organizations)


class AsyncBeta1ResourceWithRawResponse:
    def __init__(self, beta1: AsyncBeta1Resource) -> None:
        self._beta1 = beta1

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResourceWithRawResponse:
        return AsyncEnterpriseResourceWithRawResponse(self._beta1.enterprise)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._beta1.organizations)


class Beta1ResourceWithStreamingResponse:
    def __init__(self, beta1: Beta1Resource) -> None:
        self._beta1 = beta1

    @cached_property
    def enterprise(self) -> EnterpriseResourceWithStreamingResponse:
        return EnterpriseResourceWithStreamingResponse(self._beta1.enterprise)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._beta1.organizations)


class AsyncBeta1ResourceWithStreamingResponse:
    def __init__(self, beta1: AsyncBeta1Resource) -> None:
        self._beta1 = beta1

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResourceWithStreamingResponse:
        return AsyncEnterpriseResourceWithStreamingResponse(self._beta1.enterprise)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._beta1.organizations)
