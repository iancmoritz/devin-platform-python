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
from ....types.enterprise.consumption import (
    daily_get_daily_consumption_params,
    daily_get_org_daily_consumption_params,
    daily_get_user_daily_consumption_params,
    daily_get_session_daily_consumption_params,
    daily_get_service_user_daily_consumption_params,
)
from ....types.enterprise.consumption.consumption import Consumption

__all__ = ["DailyResource", "AsyncDailyResource"]


class DailyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DailyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return DailyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DailyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return DailyResourceWithStreamingResponse(self)

    def get_daily_consumption(
        self,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for the entire enterprise.

        Returns total ACUs and consumption broken down by date.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/consumption/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_daily_consumption_params.DailyGetDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    def get_org_daily_consumption(
        self,
        org_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific organization.

        Returns total ACUs and consumption broken down by date for the org.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/enterprise/consumption/daily/organizations/{org_id}", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_org_daily_consumption_params.DailyGetOrgDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    def get_service_user_daily_consumption(
        self,
        service_user_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific service user.

        Returns total ACUs and consumption broken down by date for sessions created by
        the given service user.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return self._get(
            path_template(
                "/v3/enterprise/consumption/daily/service-users/{service_user_id}", service_user_id=service_user_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_service_user_daily_consumption_params.DailyGetServiceUserDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    def get_session_daily_consumption(
        self,
        session_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific session.

        Returns total ACUs and consumption broken down by date for the session.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/v3/enterprise/consumption/daily/sessions/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_session_daily_consumption_params.DailyGetSessionDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    def get_user_daily_consumption(
        self,
        user_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific user.

        Returns total ACUs and consumption broken down by date for the user.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v3/enterprise/consumption/daily/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_user_daily_consumption_params.DailyGetUserDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )


class AsyncDailyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDailyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDailyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDailyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncDailyResourceWithStreamingResponse(self)

    async def get_daily_consumption(
        self,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for the entire enterprise.

        Returns total ACUs and consumption broken down by date.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/consumption/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_daily_consumption_params.DailyGetDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    async def get_org_daily_consumption(
        self,
        org_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific organization.

        Returns total ACUs and consumption broken down by date for the org.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/enterprise/consumption/daily/organizations/{org_id}", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_org_daily_consumption_params.DailyGetOrgDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    async def get_service_user_daily_consumption(
        self,
        service_user_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific service user.

        Returns total ACUs and consumption broken down by date for sessions created by
        the given service user.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return await self._get(
            path_template(
                "/v3/enterprise/consumption/daily/service-users/{service_user_id}", service_user_id=service_user_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_service_user_daily_consumption_params.DailyGetServiceUserDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    async def get_session_daily_consumption(
        self,
        session_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific session.

        Returns total ACUs and consumption broken down by date for the session.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/v3/enterprise/consumption/daily/sessions/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_session_daily_consumption_params.DailyGetSessionDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )

    async def get_user_daily_consumption(
        self,
        user_id: str,
        *,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Consumption:
        """
        Get daily ACU consumption for a specific user.

        Returns total ACUs and consumption broken down by date for the user.

        **Timezone behavior**: Billing cycles use midnight PST (Pacific Standard Time)
        as the day boundary, which corresponds to 08:00:00 UTC. To match the consumption
        data shown in the Devin dashboard, pass Unix timestamps that align with this
        timezone offset (e.g., 1733385600 for December 5, 2025 at midnight PST).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v3/enterprise/consumption/daily/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    daily_get_user_daily_consumption_params.DailyGetUserDailyConsumptionParams,
                ),
            ),
            cast_to=Consumption,
        )


class DailyResourceWithRawResponse:
    def __init__(self, daily: DailyResource) -> None:
        self._daily = daily

        self.get_daily_consumption = to_raw_response_wrapper(
            daily.get_daily_consumption,
        )
        self.get_org_daily_consumption = to_raw_response_wrapper(
            daily.get_org_daily_consumption,
        )
        self.get_service_user_daily_consumption = to_raw_response_wrapper(
            daily.get_service_user_daily_consumption,
        )
        self.get_session_daily_consumption = to_raw_response_wrapper(
            daily.get_session_daily_consumption,
        )
        self.get_user_daily_consumption = to_raw_response_wrapper(
            daily.get_user_daily_consumption,
        )


class AsyncDailyResourceWithRawResponse:
    def __init__(self, daily: AsyncDailyResource) -> None:
        self._daily = daily

        self.get_daily_consumption = async_to_raw_response_wrapper(
            daily.get_daily_consumption,
        )
        self.get_org_daily_consumption = async_to_raw_response_wrapper(
            daily.get_org_daily_consumption,
        )
        self.get_service_user_daily_consumption = async_to_raw_response_wrapper(
            daily.get_service_user_daily_consumption,
        )
        self.get_session_daily_consumption = async_to_raw_response_wrapper(
            daily.get_session_daily_consumption,
        )
        self.get_user_daily_consumption = async_to_raw_response_wrapper(
            daily.get_user_daily_consumption,
        )


class DailyResourceWithStreamingResponse:
    def __init__(self, daily: DailyResource) -> None:
        self._daily = daily

        self.get_daily_consumption = to_streamed_response_wrapper(
            daily.get_daily_consumption,
        )
        self.get_org_daily_consumption = to_streamed_response_wrapper(
            daily.get_org_daily_consumption,
        )
        self.get_service_user_daily_consumption = to_streamed_response_wrapper(
            daily.get_service_user_daily_consumption,
        )
        self.get_session_daily_consumption = to_streamed_response_wrapper(
            daily.get_session_daily_consumption,
        )
        self.get_user_daily_consumption = to_streamed_response_wrapper(
            daily.get_user_daily_consumption,
        )


class AsyncDailyResourceWithStreamingResponse:
    def __init__(self, daily: AsyncDailyResource) -> None:
        self._daily = daily

        self.get_daily_consumption = async_to_streamed_response_wrapper(
            daily.get_daily_consumption,
        )
        self.get_org_daily_consumption = async_to_streamed_response_wrapper(
            daily.get_org_daily_consumption,
        )
        self.get_service_user_daily_consumption = async_to_streamed_response_wrapper(
            daily.get_service_user_daily_consumption,
        )
        self.get_session_daily_consumption = async_to_streamed_response_wrapper(
            daily.get_session_daily_consumption,
        )
        self.get_user_daily_consumption = async_to_streamed_response_wrapper(
            daily.get_user_daily_consumption,
        )
