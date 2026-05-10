# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .idp_groups import (
    IdpGroupsResource,
    AsyncIdpGroupsResource,
    IdpGroupsResourceWithRawResponse,
    AsyncIdpGroupsResourceWithRawResponse,
    IdpGroupsResourceWithStreamingResponse,
    AsyncIdpGroupsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .service_users import (
    ServiceUsersResource,
    AsyncServiceUsersResource,
    ServiceUsersResourceWithRawResponse,
    AsyncServiceUsersResourceWithRawResponse,
    ServiceUsersResourceWithStreamingResponse,
    AsyncServiceUsersResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.enterprise import member_list_idp_group_users_params
from ....types.enterprise.paginated_idp_group_user import PaginatedIdpGroupUser

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def idp_groups(self) -> IdpGroupsResource:
        return IdpGroupsResource(self._client)

    @cached_property
    def service_users(self) -> ServiceUsersResource:
        return ServiceUsersResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def list_idp_group_users(
        self,
        *,
        after: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedIdpGroupUser:
        """
        List users whose enterprise membership is derived from IDP group assignments.

        Args:
          email: Filter by exact email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/members/idp-users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "email": email,
                        "first": first,
                    },
                    member_list_idp_group_users_params.MemberListIdpGroupUsersParams,
                ),
            ),
            cast_to=PaginatedIdpGroupUser,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def idp_groups(self) -> AsyncIdpGroupsResource:
        return AsyncIdpGroupsResource(self._client)

    @cached_property
    def service_users(self) -> AsyncServiceUsersResource:
        return AsyncServiceUsersResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list_idp_group_users(
        self,
        *,
        after: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedIdpGroupUser:
        """
        List users whose enterprise membership is derived from IDP group assignments.

        Args:
          email: Filter by exact email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/members/idp-users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "email": email,
                        "first": first,
                    },
                    member_list_idp_group_users_params.MemberListIdpGroupUsersParams,
                ),
            ),
            cast_to=PaginatedIdpGroupUser,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list_idp_group_users = to_raw_response_wrapper(
            members.list_idp_group_users,
        )

    @cached_property
    def idp_groups(self) -> IdpGroupsResourceWithRawResponse:
        return IdpGroupsResourceWithRawResponse(self._members.idp_groups)

    @cached_property
    def service_users(self) -> ServiceUsersResourceWithRawResponse:
        return ServiceUsersResourceWithRawResponse(self._members.service_users)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._members.users)


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list_idp_group_users = async_to_raw_response_wrapper(
            members.list_idp_group_users,
        )

    @cached_property
    def idp_groups(self) -> AsyncIdpGroupsResourceWithRawResponse:
        return AsyncIdpGroupsResourceWithRawResponse(self._members.idp_groups)

    @cached_property
    def service_users(self) -> AsyncServiceUsersResourceWithRawResponse:
        return AsyncServiceUsersResourceWithRawResponse(self._members.service_users)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._members.users)


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list_idp_group_users = to_streamed_response_wrapper(
            members.list_idp_group_users,
        )

    @cached_property
    def idp_groups(self) -> IdpGroupsResourceWithStreamingResponse:
        return IdpGroupsResourceWithStreamingResponse(self._members.idp_groups)

    @cached_property
    def service_users(self) -> ServiceUsersResourceWithStreamingResponse:
        return ServiceUsersResourceWithStreamingResponse(self._members.service_users)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._members.users)


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list_idp_group_users = async_to_streamed_response_wrapper(
            members.list_idp_group_users,
        )

    @cached_property
    def idp_groups(self) -> AsyncIdpGroupsResourceWithStreamingResponse:
        return AsyncIdpGroupsResourceWithStreamingResponse(self._members.idp_groups)

    @cached_property
    def service_users(self) -> AsyncServiceUsersResourceWithStreamingResponse:
        return AsyncServiceUsersResourceWithStreamingResponse(self._members.service_users)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._members.users)
