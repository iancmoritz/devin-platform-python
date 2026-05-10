# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.enterprise.organizations.tags import default_create_params
from .....types.enterprise.organizations.tags.default_tag import DefaultTag

__all__ = ["DefaultResource", "AsyncDefaultResource"]


class DefaultResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return DefaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return DefaultResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        tag: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DefaultTag:
        """Set the default tag for an organization.

        The tag must exist in the allowed tags
        list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._put(
            path_template("/v3/enterprise/organizations/{org_id}/tags/default", org_id=org_id),
            body=maybe_transform({"tag": tag}, default_create_params.DefaultCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultTag,
        )

    def list(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DefaultTag:
        """
        Get the current default tag for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/enterprise/organizations/{org_id}/tags/default", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultTag,
        )

    def delete_all(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DefaultTag:
        """
        Clear the default tag for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._delete(
            path_template("/v3/enterprise/organizations/{org_id}/tags/default", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultTag,
        )


class AsyncDefaultResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncDefaultResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        tag: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DefaultTag:
        """Set the default tag for an organization.

        The tag must exist in the allowed tags
        list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._put(
            path_template("/v3/enterprise/organizations/{org_id}/tags/default", org_id=org_id),
            body=await async_maybe_transform({"tag": tag}, default_create_params.DefaultCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultTag,
        )

    async def list(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DefaultTag:
        """
        Get the current default tag for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/enterprise/organizations/{org_id}/tags/default", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultTag,
        )

    async def delete_all(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DefaultTag:
        """
        Clear the default tag for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._delete(
            path_template("/v3/enterprise/organizations/{org_id}/tags/default", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultTag,
        )


class DefaultResourceWithRawResponse:
    def __init__(self, default: DefaultResource) -> None:
        self._default = default

        self.create = to_raw_response_wrapper(
            default.create,
        )
        self.list = to_raw_response_wrapper(
            default.list,
        )
        self.delete_all = to_raw_response_wrapper(
            default.delete_all,
        )


class AsyncDefaultResourceWithRawResponse:
    def __init__(self, default: AsyncDefaultResource) -> None:
        self._default = default

        self.create = async_to_raw_response_wrapper(
            default.create,
        )
        self.list = async_to_raw_response_wrapper(
            default.list,
        )
        self.delete_all = async_to_raw_response_wrapper(
            default.delete_all,
        )


class DefaultResourceWithStreamingResponse:
    def __init__(self, default: DefaultResource) -> None:
        self._default = default

        self.create = to_streamed_response_wrapper(
            default.create,
        )
        self.list = to_streamed_response_wrapper(
            default.list,
        )
        self.delete_all = to_streamed_response_wrapper(
            default.delete_all,
        )


class AsyncDefaultResourceWithStreamingResponse:
    def __init__(self, default: AsyncDefaultResource) -> None:
        self._default = default

        self.create = async_to_streamed_response_wrapper(
            default.create,
        )
        self.list = async_to_streamed_response_wrapper(
            default.list,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            default.delete_all,
        )
