# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.enterprise.consumption.acu_limits import devin_get_acu_limits_params
from ......types.enterprise.consumption.acu_limits.devin_get_acu_limits_response import DevinGetAcuLimitsResponse

__all__ = ["DevinResource", "AsyncDevinResource"]


class DevinResource(SyncAPIResource):
    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return DevinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return DevinResourceWithStreamingResponse(self)

    def get_acu_limits(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DevinGetAcuLimitsResponse:
        """
        Get all org-level Devin ACU limits for this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/consumption/acu-limits/devin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    devin_get_acu_limits_params.DevinGetAcuLimitsParams,
                ),
            ),
            cast_to=DevinGetAcuLimitsResponse,
        )


class AsyncDevinResource(AsyncAPIResource):
    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncDevinResourceWithStreamingResponse(self)

    async def get_acu_limits(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DevinGetAcuLimitsResponse:
        """
        Get all org-level Devin ACU limits for this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/consumption/acu-limits/devin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    devin_get_acu_limits_params.DevinGetAcuLimitsParams,
                ),
            ),
            cast_to=DevinGetAcuLimitsResponse,
        )


class DevinResourceWithRawResponse:
    def __init__(self, devin: DevinResource) -> None:
        self._devin = devin

        self.get_acu_limits = to_raw_response_wrapper(
            devin.get_acu_limits,
        )

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._devin.organizations)


class AsyncDevinResourceWithRawResponse:
    def __init__(self, devin: AsyncDevinResource) -> None:
        self._devin = devin

        self.get_acu_limits = async_to_raw_response_wrapper(
            devin.get_acu_limits,
        )

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._devin.organizations)


class DevinResourceWithStreamingResponse:
    def __init__(self, devin: DevinResource) -> None:
        self._devin = devin

        self.get_acu_limits = to_streamed_response_wrapper(
            devin.get_acu_limits,
        )

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._devin.organizations)


class AsyncDevinResourceWithStreamingResponse:
    def __init__(self, devin: AsyncDevinResource) -> None:
        self._devin = devin

        self.get_acu_limits = async_to_streamed_response_wrapper(
            devin.get_acu_limits,
        )

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._devin.organizations)
