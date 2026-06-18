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
from .....types.enterprise.members.service_user import ServiceUser
from .....types.enterprise.organizations.members import (
    service_user_update_params,
    service_user_retrieve_service_users_params,
)
from .....types.enterprise.members.paginated_service_user import PaginatedServiceUser

__all__ = ["ServiceUsersResource", "AsyncServiceUsersResource"]


class ServiceUsersResource(SyncAPIResource):
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

    def update(
        self,
        service_user_id: str,
        *,
        org_id: str,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceUser:
        """
        Assign organization role to service user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return self._post(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/service-users/{service_user_id}",
                org_id=org_id,
                service_user_id=service_user_id,
            ),
            body=maybe_transform({"role_id": role_id}, service_user_update_params.ServiceUserUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceUser,
        )

    def delete(
        self,
        service_user_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceUser:
        """
        Remove service user from the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return self._delete(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/service-users/{service_user_id}",
                org_id=org_id,
                service_user_id=service_user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceUser,
        )

    def retrieve_service_users(
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
    ) -> PaginatedServiceUser:
        """
        List service users in the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/enterprise/organizations/{org_id}/members/service-users", org_id=org_id),
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
                    service_user_retrieve_service_users_params.ServiceUserRetrieveServiceUsersParams,
                ),
            ),
            cast_to=PaginatedServiceUser,
        )


class AsyncServiceUsersResource(AsyncAPIResource):
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

    async def update(
        self,
        service_user_id: str,
        *,
        org_id: str,
        role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceUser:
        """
        Assign organization role to service user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return await self._post(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/service-users/{service_user_id}",
                org_id=org_id,
                service_user_id=service_user_id,
            ),
            body=await async_maybe_transform({"role_id": role_id}, service_user_update_params.ServiceUserUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceUser,
        )

    async def delete(
        self,
        service_user_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceUser:
        """
        Remove service user from the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return await self._delete(
            path_template(
                "/v3/enterprise/organizations/{org_id}/members/service-users/{service_user_id}",
                org_id=org_id,
                service_user_id=service_user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceUser,
        )

    async def retrieve_service_users(
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
    ) -> PaginatedServiceUser:
        """
        List service users in the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/enterprise/organizations/{org_id}/members/service-users", org_id=org_id),
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
                    service_user_retrieve_service_users_params.ServiceUserRetrieveServiceUsersParams,
                ),
            ),
            cast_to=PaginatedServiceUser,
        )


class ServiceUsersResourceWithRawResponse:
    def __init__(self, service_users: ServiceUsersResource) -> None:
        self._service_users = service_users

        self.update = to_raw_response_wrapper(
            service_users.update,
        )
        self.delete = to_raw_response_wrapper(
            service_users.delete,
        )
        self.retrieve_service_users = to_raw_response_wrapper(
            service_users.retrieve_service_users,
        )


class AsyncServiceUsersResourceWithRawResponse:
    def __init__(self, service_users: AsyncServiceUsersResource) -> None:
        self._service_users = service_users

        self.update = async_to_raw_response_wrapper(
            service_users.update,
        )
        self.delete = async_to_raw_response_wrapper(
            service_users.delete,
        )
        self.retrieve_service_users = async_to_raw_response_wrapper(
            service_users.retrieve_service_users,
        )


class ServiceUsersResourceWithStreamingResponse:
    def __init__(self, service_users: ServiceUsersResource) -> None:
        self._service_users = service_users

        self.update = to_streamed_response_wrapper(
            service_users.update,
        )
        self.delete = to_streamed_response_wrapper(
            service_users.delete,
        )
        self.retrieve_service_users = to_streamed_response_wrapper(
            service_users.retrieve_service_users,
        )


class AsyncServiceUsersResourceWithStreamingResponse:
    def __init__(self, service_users: AsyncServiceUsersResource) -> None:
        self._service_users = service_users

        self.update = async_to_streamed_response_wrapper(
            service_users.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_users.delete,
        )
        self.retrieve_service_users = async_to_streamed_response_wrapper(
            service_users.retrieve_service_users,
        )
