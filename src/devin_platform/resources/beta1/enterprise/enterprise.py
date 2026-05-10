# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ....types.beta1 import enterprise_list_guardrail_violations_params
from ...._base_client import make_request_options
from .service_users.service_users import (
    ServiceUsersResource,
    AsyncServiceUsersResource,
    ServiceUsersResourceWithRawResponse,
    AsyncServiceUsersResourceWithRawResponse,
    ServiceUsersResourceWithStreamingResponse,
    AsyncServiceUsersResourceWithStreamingResponse,
)
from ....types.beta1.paginated_response import PaginatedResponse

__all__ = ["EnterpriseResource", "AsyncEnterpriseResource"]


class EnterpriseResource(SyncAPIResource):
    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def service_users(self) -> ServiceUsersResource:
        return ServiceUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnterpriseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return EnterpriseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnterpriseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return EnterpriseResourceWithStreamingResponse(self)

    def list_guardrail_violations(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        guardrail_id: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedResponse:
        """
        List guardrail violations across the enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3beta1/enterprise/guardrail-violations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                        "guardrail_id": guardrail_id,
                        "order": order,
                        "session_id": session_id,
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    enterprise_list_guardrail_violations_params.EnterpriseListGuardrailViolationsParams,
                ),
            ),
            cast_to=PaginatedResponse,
        )


class AsyncEnterpriseResource(AsyncAPIResource):
    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def service_users(self) -> AsyncServiceUsersResource:
        return AsyncServiceUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnterpriseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnterpriseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnterpriseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncEnterpriseResourceWithStreamingResponse(self)

    async def list_guardrail_violations(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        guardrail_id: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedResponse:
        """
        List guardrail violations across the enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3beta1/enterprise/guardrail-violations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "first": first,
                        "guardrail_id": guardrail_id,
                        "order": order,
                        "session_id": session_id,
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    enterprise_list_guardrail_violations_params.EnterpriseListGuardrailViolationsParams,
                ),
            ),
            cast_to=PaginatedResponse,
        )


class EnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

        self.list_guardrail_violations = to_raw_response_wrapper(
            enterprise.list_guardrail_violations,
        )

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._enterprise.organizations)

    @cached_property
    def service_users(self) -> ServiceUsersResourceWithRawResponse:
        return ServiceUsersResourceWithRawResponse(self._enterprise.service_users)


class AsyncEnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

        self.list_guardrail_violations = async_to_raw_response_wrapper(
            enterprise.list_guardrail_violations,
        )

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._enterprise.organizations)

    @cached_property
    def service_users(self) -> AsyncServiceUsersResourceWithRawResponse:
        return AsyncServiceUsersResourceWithRawResponse(self._enterprise.service_users)


class EnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

        self.list_guardrail_violations = to_streamed_response_wrapper(
            enterprise.list_guardrail_violations,
        )

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._enterprise.organizations)

    @cached_property
    def service_users(self) -> ServiceUsersResourceWithStreamingResponse:
        return ServiceUsersResourceWithStreamingResponse(self._enterprise.service_users)


class AsyncEnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

        self.list_guardrail_violations = async_to_streamed_response_wrapper(
            enterprise.list_guardrail_violations,
        )

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._enterprise.organizations)

    @cached_property
    def service_users(self) -> AsyncServiceUsersResourceWithStreamingResponse:
        return AsyncServiceUsersResourceWithStreamingResponse(self._enterprise.service_users)
