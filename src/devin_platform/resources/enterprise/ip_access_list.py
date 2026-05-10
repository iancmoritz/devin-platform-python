# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.enterprise import ip_access_list_replace_access_list_params
from ...types.enterprise.ip_access_list_response import IPAccessListResponse

__all__ = ["IPAccessListResource", "AsyncIPAccessListResource"]


class IPAccessListResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPAccessListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return IPAccessListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPAccessListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return IPAccessListResourceWithStreamingResponse(self)

    def clear_access_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPAccessListResponse:
        """Clear IP Access List"""
        return self._delete(
            "/v3/enterprise/ip-access-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPAccessListResponse,
        )

    def get_access_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPAccessListResponse:
        """Get IP Access List"""
        return self._get(
            "/v3/enterprise/ip-access-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPAccessListResponse,
        )

    def replace_access_list(
        self,
        *,
        ip_ranges: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPAccessListResponse:
        """
        Replace IP Access List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v3/enterprise/ip-access-list",
            body=maybe_transform(
                {"ip_ranges": ip_ranges}, ip_access_list_replace_access_list_params.IPAccessListReplaceAccessListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPAccessListResponse,
        )


class AsyncIPAccessListResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPAccessListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPAccessListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPAccessListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncIPAccessListResourceWithStreamingResponse(self)

    async def clear_access_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPAccessListResponse:
        """Clear IP Access List"""
        return await self._delete(
            "/v3/enterprise/ip-access-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPAccessListResponse,
        )

    async def get_access_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPAccessListResponse:
        """Get IP Access List"""
        return await self._get(
            "/v3/enterprise/ip-access-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPAccessListResponse,
        )

    async def replace_access_list(
        self,
        *,
        ip_ranges: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPAccessListResponse:
        """
        Replace IP Access List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v3/enterprise/ip-access-list",
            body=await async_maybe_transform(
                {"ip_ranges": ip_ranges}, ip_access_list_replace_access_list_params.IPAccessListReplaceAccessListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPAccessListResponse,
        )


class IPAccessListResourceWithRawResponse:
    def __init__(self, ip_access_list: IPAccessListResource) -> None:
        self._ip_access_list = ip_access_list

        self.clear_access_list = to_raw_response_wrapper(
            ip_access_list.clear_access_list,
        )
        self.get_access_list = to_raw_response_wrapper(
            ip_access_list.get_access_list,
        )
        self.replace_access_list = to_raw_response_wrapper(
            ip_access_list.replace_access_list,
        )


class AsyncIPAccessListResourceWithRawResponse:
    def __init__(self, ip_access_list: AsyncIPAccessListResource) -> None:
        self._ip_access_list = ip_access_list

        self.clear_access_list = async_to_raw_response_wrapper(
            ip_access_list.clear_access_list,
        )
        self.get_access_list = async_to_raw_response_wrapper(
            ip_access_list.get_access_list,
        )
        self.replace_access_list = async_to_raw_response_wrapper(
            ip_access_list.replace_access_list,
        )


class IPAccessListResourceWithStreamingResponse:
    def __init__(self, ip_access_list: IPAccessListResource) -> None:
        self._ip_access_list = ip_access_list

        self.clear_access_list = to_streamed_response_wrapper(
            ip_access_list.clear_access_list,
        )
        self.get_access_list = to_streamed_response_wrapper(
            ip_access_list.get_access_list,
        )
        self.replace_access_list = to_streamed_response_wrapper(
            ip_access_list.replace_access_list,
        )


class AsyncIPAccessListResourceWithStreamingResponse:
    def __init__(self, ip_access_list: AsyncIPAccessListResource) -> None:
        self._ip_access_list = ip_access_list

        self.clear_access_list = async_to_streamed_response_wrapper(
            ip_access_list.clear_access_list,
        )
        self.get_access_list = async_to_streamed_response_wrapper(
            ip_access_list.get_access_list,
        )
        self.replace_access_list = async_to_streamed_response_wrapper(
            ip_access_list.replace_access_list,
        )
