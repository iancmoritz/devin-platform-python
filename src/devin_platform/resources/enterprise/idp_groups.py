# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.enterprise import idp_group_list_idp_groups_params, idp_group_register_idp_groups_params
from ...types.enterprise.idp_group_response import IdpGroupResponse
from ...types.enterprise.idp_group_list_idp_groups_response import IdpGroupListIdpGroupsResponse
from ...types.enterprise.idp_group_register_idp_groups_response import IdpGroupRegisterIdpGroupsResponse

__all__ = ["IdpGroupsResource", "AsyncIdpGroupsResource"]


class IdpGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdpGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return IdpGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdpGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return IdpGroupsResourceWithStreamingResponse(self)

    def delete_idp_group(
        self,
        idp_group_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroupResponse:
        """
        Remove a registered IDP group from this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._delete(
            path_template("/v3/enterprise/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroupResponse,
        )

    def list_idp_groups(
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
    ) -> IdpGroupListIdpGroupsResponse:
        """
        List IDP groups registered with this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/idp-groups",
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
                    idp_group_list_idp_groups_params.IdpGroupListIdpGroupsParams,
                ),
            ),
            cast_to=IdpGroupListIdpGroupsResponse,
        )

    def register_idp_groups(
        self,
        *,
        idp_group_names: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroupRegisterIdpGroupsResponse:
        """Bulk create IDP groups for this enterprise.

        Existing groups are ignored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/enterprise/idp-groups",
            body=maybe_transform(
                {"idp_group_names": idp_group_names},
                idp_group_register_idp_groups_params.IdpGroupRegisterIdpGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroupRegisterIdpGroupsResponse,
        )


class AsyncIdpGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdpGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdpGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdpGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncIdpGroupsResourceWithStreamingResponse(self)

    async def delete_idp_group(
        self,
        idp_group_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroupResponse:
        """
        Remove a registered IDP group from this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._delete(
            path_template("/v3/enterprise/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroupResponse,
        )

    async def list_idp_groups(
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
    ) -> IdpGroupListIdpGroupsResponse:
        """
        List IDP groups registered with this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/idp-groups",
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
                    idp_group_list_idp_groups_params.IdpGroupListIdpGroupsParams,
                ),
            ),
            cast_to=IdpGroupListIdpGroupsResponse,
        )

    async def register_idp_groups(
        self,
        *,
        idp_group_names: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroupRegisterIdpGroupsResponse:
        """Bulk create IDP groups for this enterprise.

        Existing groups are ignored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/enterprise/idp-groups",
            body=await async_maybe_transform(
                {"idp_group_names": idp_group_names},
                idp_group_register_idp_groups_params.IdpGroupRegisterIdpGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroupRegisterIdpGroupsResponse,
        )


class IdpGroupsResourceWithRawResponse:
    def __init__(self, idp_groups: IdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.delete_idp_group = to_raw_response_wrapper(
            idp_groups.delete_idp_group,
        )
        self.list_idp_groups = to_raw_response_wrapper(
            idp_groups.list_idp_groups,
        )
        self.register_idp_groups = to_raw_response_wrapper(
            idp_groups.register_idp_groups,
        )


class AsyncIdpGroupsResourceWithRawResponse:
    def __init__(self, idp_groups: AsyncIdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.delete_idp_group = async_to_raw_response_wrapper(
            idp_groups.delete_idp_group,
        )
        self.list_idp_groups = async_to_raw_response_wrapper(
            idp_groups.list_idp_groups,
        )
        self.register_idp_groups = async_to_raw_response_wrapper(
            idp_groups.register_idp_groups,
        )


class IdpGroupsResourceWithStreamingResponse:
    def __init__(self, idp_groups: IdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.delete_idp_group = to_streamed_response_wrapper(
            idp_groups.delete_idp_group,
        )
        self.list_idp_groups = to_streamed_response_wrapper(
            idp_groups.list_idp_groups,
        )
        self.register_idp_groups = to_streamed_response_wrapper(
            idp_groups.register_idp_groups,
        )


class AsyncIdpGroupsResourceWithStreamingResponse:
    def __init__(self, idp_groups: AsyncIdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.delete_idp_group = async_to_streamed_response_wrapper(
            idp_groups.delete_idp_group,
        )
        self.list_idp_groups = async_to_streamed_response_wrapper(
            idp_groups.list_idp_groups,
        )
        self.register_idp_groups = async_to_streamed_response_wrapper(
            idp_groups.register_idp_groups,
        )
