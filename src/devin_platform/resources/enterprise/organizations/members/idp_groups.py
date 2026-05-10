# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.enterprise.members.idp_group import IdpGroup
from .....types.enterprise.organizations.members import idp_group_update_params, idp_group_retrieve_idp_groups_params
from .....types.enterprise.members.paginated_idp_group import PaginatedIdpGroup

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

    def retrieve(
        self,
        idp_group_name: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Get Organization IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._get(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}",
                org_id=org_id,
                idp_group_name=idp_group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    def update(
        self,
        idp_group_name: str,
        *,
        org_id: str,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Assign Organization IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._post(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}",
                org_id=org_id,
                idp_group_name=idp_group_name,
            ),
            body=maybe_transform({"role_id": role_id}, idp_group_update_params.IdpGroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    def delete(
        self,
        idp_group_name: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Remove idp_group from the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return self._delete(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}",
                org_id=org_id,
                idp_group_name=idp_group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    def retrieve_idp_groups(
        self,
        org_id: str,
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
        List Organization IDP Groups

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/enterprise/organizations/{org_id}/members/idp-groups", org_id=org_id),
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
                    idp_group_retrieve_idp_groups_params.IdpGroupRetrieveIdpGroupsParams,
                ),
            ),
            cast_to=PaginatedIdpGroup,
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

    async def retrieve(
        self,
        idp_group_name: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Get Organization IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._get(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}",
                org_id=org_id,
                idp_group_name=idp_group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    async def update(
        self,
        idp_group_name: str,
        *,
        org_id: str,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Assign Organization IDP Group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._post(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}",
                org_id=org_id,
                idp_group_name=idp_group_name,
            ),
            body=await async_maybe_transform({"role_id": role_id}, idp_group_update_params.IdpGroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    async def delete(
        self,
        idp_group_name: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdpGroup:
        """
        Remove idp_group from the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not idp_group_name:
            raise ValueError(f"Expected a non-empty value for `idp_group_name` but received {idp_group_name!r}")
        return await self._delete(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}",
                org_id=org_id,
                idp_group_name=idp_group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdpGroup,
        )

    async def retrieve_idp_groups(
        self,
        org_id: str,
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
        List Organization IDP Groups

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/enterprise/organizations/{org_id}/members/idp-groups", org_id=org_id),
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
                    idp_group_retrieve_idp_groups_params.IdpGroupRetrieveIdpGroupsParams,
                ),
            ),
            cast_to=PaginatedIdpGroup,
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
        self.delete = to_raw_response_wrapper(
            idp_groups.delete,
        )
        self.retrieve_idp_groups = to_raw_response_wrapper(
            idp_groups.retrieve_idp_groups,
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
        self.delete = async_to_raw_response_wrapper(
            idp_groups.delete,
        )
        self.retrieve_idp_groups = async_to_raw_response_wrapper(
            idp_groups.retrieve_idp_groups,
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
        self.delete = to_streamed_response_wrapper(
            idp_groups.delete,
        )
        self.retrieve_idp_groups = to_streamed_response_wrapper(
            idp_groups.retrieve_idp_groups,
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
        self.delete = async_to_streamed_response_wrapper(
            idp_groups.delete,
        )
        self.retrieve_idp_groups = async_to_streamed_response_wrapper(
            idp_groups.retrieve_idp_groups,
        )
