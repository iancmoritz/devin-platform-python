# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.enterprise.members import idp_group_list_params, idp_group_assign_params, idp_group_update_params
from ....types.enterprise.members.idp_group import IdpGroup
from ....types.enterprise.members.paginated_idp_group import PaginatedIdpGroup

__all__ = ["IdpGroupsResource", "AsyncIdpGroupsResource"]


class IdpGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdpGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return IdpGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdpGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return IdpGroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        idp_group_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Get IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._get(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    def update(
        self,
        idp_group_name: str,
        *,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Update IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._patch(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            body=maybe_transform({"role_id": role_id}, idp_group_update_params.IdpGroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    def list(
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
    ) -> PaginatedIdpGroup:
        """
        List IDP Groups

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/members/idp-groups",
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
                    idp_group_list_params.IdpGroupListParams,
                ),
            ),
            cast_to=PaginatedIdpGroup,
        )

    def delete(
        self,
        idp_group_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Delete IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._delete(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    def assign(
        self,
        idp_group_name: str,
        *,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Assign IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._post(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            body=maybe_transform({"role_id": role_id}, idp_group_assign_params.IdpGroupAssignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )


class AsyncIdpGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdpGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdpGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdpGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncIdpGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        idp_group_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Get IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._get(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    async def update(
        self,
        idp_group_name: str,
        *,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Update IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._patch(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            body=await async_maybe_transform({"role_id": role_id}, idp_group_update_params.IdpGroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    async def list(
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
    ) -> PaginatedIdpGroup:
        """
        List IDP Groups

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/members/idp-groups",
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
                    idp_group_list_params.IdpGroupListParams,
                ),
            ),
            cast_to=PaginatedIdpGroup,
        )

    async def delete(
        self,
        idp_group_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Delete IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._delete(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    async def assign(
        self,
        idp_group_name: str,
        *,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Assign IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._post(
            path_template("/v3/enterprise/members/idp-groups/{idp_group_name}", idp_group_name=idp_group_name),
            body=await async_maybe_transform({"role_id": role_id}, idp_group_assign_params.IdpGroupAssignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )


class IdpGroupsResourceWithRawResponse:
    def __init__(self, idp_groups: IdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.retrieve = to_raw_response_wrapper(
            idp_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            idp_groups.update,
        )
        self.list = to_raw_response_wrapper(
            idp_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            idp_groups.delete,
        )
        self.assign = to_raw_response_wrapper(
            idp_groups.assign,
        )


class AsyncIdpGroupsResourceWithRawResponse:
    def __init__(self, idp_groups: AsyncIdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.retrieve = async_to_raw_response_wrapper(
            idp_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            idp_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            idp_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            idp_groups.delete,
        )
        self.assign = async_to_raw_response_wrapper(
            idp_groups.assign,
        )


class IdpGroupsResourceWithStreamingResponse:
    def __init__(self, idp_groups: IdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.retrieve = to_streamed_response_wrapper(
            idp_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            idp_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            idp_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            idp_groups.delete,
        )
        self.assign = to_streamed_response_wrapper(
            idp_groups.assign,
        )


class AsyncIdpGroupsResourceWithStreamingResponse:
    def __init__(self, idp_groups: AsyncIdpGroupsResource) -> None:
        self._idp_groups = idp_groups

        self.retrieve = async_to_streamed_response_wrapper(
            idp_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            idp_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            idp_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            idp_groups.delete,
        )
        self.assign = async_to_streamed_response_wrapper(
            idp_groups.assign,
        )
