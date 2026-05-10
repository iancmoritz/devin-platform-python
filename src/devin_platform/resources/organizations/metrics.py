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
from ...types.organizations import (
    metric_get_pr_metrics_params,
    metric_get_active_users_params,
    metric_get_usage_metrics_params,
    metric_get_search_metrics_params,
    metric_get_session_metrics_params,
    metric_get_daily_active_users_params,
    metric_get_weekly_active_users_params,
    metric_get_monthly_active_users_params,
)
from ...types.enterprise.pr_metrics import PrMetrics
from ...types.enterprise.usage_metrics import UsageMetrics
from ...types.enterprise.search_metrics import SearchMetrics
from ...types.enterprise.session_metrics import SessionMetrics
from ...types.enterprise.active_user_metrics import ActiveUserMetrics
from ...types.organizations.metric_get_daily_active_users_response import MetricGetDailyActiveUsersResponse
from ...types.organizations.metric_get_weekly_active_users_response import MetricGetWeeklyActiveUsersResponse
from ...types.organizations.metric_get_monthly_active_users_response import MetricGetMonthlyActiveUsersResponse

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def get_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActiveUserMetrics:
        """
        Get unique active users for a custom date range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/active-users", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_active_users_params.MetricGetActiveUsersParams,
                ),
            ),
            cast_to=ActiveUserMetrics,
        )

    def get_daily_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetDailyActiveUsersResponse:
        """
        Get daily active users for each day in the specified time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/dau", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_daily_active_users_params.MetricGetDailyActiveUsersParams,
                ),
            ),
            cast_to=MetricGetDailyActiveUsersResponse,
        )

    def get_monthly_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetMonthlyActiveUsersResponse:
        """
        Get monthly active users for each month in the specified time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/mau", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_monthly_active_users_params.MetricGetMonthlyActiveUsersParams,
                ),
            ),
            cast_to=MetricGetMonthlyActiveUsersResponse,
        )

    def get_pr_metrics(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        playbook_id: Optional[str] | Omit = omit,
        service_user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrMetrics:
        """
        Get aggregated PR metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/prs", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "playbook_id": playbook_id,
                        "service_user_ids": service_user_ids,
                        "user_ids": user_ids,
                    },
                    metric_get_pr_metrics_params.MetricGetPrMetricsParams,
                ),
            ),
            cast_to=PrMetrics,
        )

    def get_search_metrics(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchMetrics:
        """
        Get aggregated search metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/searches", org_id=org_id),
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
                    metric_get_search_metrics_params.MetricGetSearchMetricsParams,
                ),
            ),
            cast_to=SearchMetrics,
        )

    def get_session_metrics(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        playbook_id: Optional[str] | Omit = omit,
        service_user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionMetrics:
        """
        Get aggregated session metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/sessions", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "playbook_id": playbook_id,
                        "service_user_ids": service_user_ids,
                        "user_ids": user_ids,
                    },
                    metric_get_session_metrics_params.MetricGetSessionMetricsParams,
                ),
            ),
            cast_to=SessionMetrics,
        )

    def get_usage_metrics(
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
    ) -> UsageMetrics:
        """
        Get aggregated usage metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/usage", org_id=org_id),
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
                    metric_get_usage_metrics_params.MetricGetUsageMetricsParams,
                ),
            ),
            cast_to=UsageMetrics,
        )

    def get_weekly_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetWeeklyActiveUsersResponse:
        """
        Get weekly active users for each week in the specified time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/metrics/wau", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_weekly_active_users_params.MetricGetWeeklyActiveUsersParams,
                ),
            ),
            cast_to=MetricGetWeeklyActiveUsersResponse,
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def get_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActiveUserMetrics:
        """
        Get unique active users for a custom date range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/active-users", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_active_users_params.MetricGetActiveUsersParams,
                ),
            ),
            cast_to=ActiveUserMetrics,
        )

    async def get_daily_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetDailyActiveUsersResponse:
        """
        Get daily active users for each day in the specified time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/dau", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_daily_active_users_params.MetricGetDailyActiveUsersParams,
                ),
            ),
            cast_to=MetricGetDailyActiveUsersResponse,
        )

    async def get_monthly_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetMonthlyActiveUsersResponse:
        """
        Get monthly active users for each month in the specified time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/mau", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_monthly_active_users_params.MetricGetMonthlyActiveUsersParams,
                ),
            ),
            cast_to=MetricGetMonthlyActiveUsersResponse,
        )

    async def get_pr_metrics(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        playbook_id: Optional[str] | Omit = omit,
        service_user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrMetrics:
        """
        Get aggregated PR metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/prs", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "playbook_id": playbook_id,
                        "service_user_ids": service_user_ids,
                        "user_ids": user_ids,
                    },
                    metric_get_pr_metrics_params.MetricGetPrMetricsParams,
                ),
            ),
            cast_to=PrMetrics,
        )

    async def get_search_metrics(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchMetrics:
        """
        Get aggregated search metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/searches", org_id=org_id),
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
                    metric_get_search_metrics_params.MetricGetSearchMetricsParams,
                ),
            ),
            cast_to=SearchMetrics,
        )

    async def get_session_metrics(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        playbook_id: Optional[str] | Omit = omit,
        service_user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionMetrics:
        """
        Get aggregated session metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/sessions", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "playbook_id": playbook_id,
                        "service_user_ids": service_user_ids,
                        "user_ids": user_ids,
                    },
                    metric_get_session_metrics_params.MetricGetSessionMetricsParams,
                ),
            ),
            cast_to=SessionMetrics,
        )

    async def get_usage_metrics(
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
    ) -> UsageMetrics:
        """
        Get aggregated usage metrics for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/usage", org_id=org_id),
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
                    metric_get_usage_metrics_params.MetricGetUsageMetricsParams,
                ),
            ),
            cast_to=UsageMetrics,
        )

    async def get_weekly_active_users(
        self,
        org_id: str,
        *,
        time_after: int,
        time_before: int,
        min_searches: int | Omit = omit,
        min_sessions: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricGetWeeklyActiveUsersResponse:
        """
        Get weekly active users for each week in the specified time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/metrics/wau", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_after": time_after,
                        "time_before": time_before,
                        "min_searches": min_searches,
                        "min_sessions": min_sessions,
                    },
                    metric_get_weekly_active_users_params.MetricGetWeeklyActiveUsersParams,
                ),
            ),
            cast_to=MetricGetWeeklyActiveUsersResponse,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.get_active_users = to_raw_response_wrapper(
            metrics.get_active_users,
        )
        self.get_daily_active_users = to_raw_response_wrapper(
            metrics.get_daily_active_users,
        )
        self.get_monthly_active_users = to_raw_response_wrapper(
            metrics.get_monthly_active_users,
        )
        self.get_pr_metrics = to_raw_response_wrapper(
            metrics.get_pr_metrics,
        )
        self.get_search_metrics = to_raw_response_wrapper(
            metrics.get_search_metrics,
        )
        self.get_session_metrics = to_raw_response_wrapper(
            metrics.get_session_metrics,
        )
        self.get_usage_metrics = to_raw_response_wrapper(
            metrics.get_usage_metrics,
        )
        self.get_weekly_active_users = to_raw_response_wrapper(
            metrics.get_weekly_active_users,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.get_active_users = async_to_raw_response_wrapper(
            metrics.get_active_users,
        )
        self.get_daily_active_users = async_to_raw_response_wrapper(
            metrics.get_daily_active_users,
        )
        self.get_monthly_active_users = async_to_raw_response_wrapper(
            metrics.get_monthly_active_users,
        )
        self.get_pr_metrics = async_to_raw_response_wrapper(
            metrics.get_pr_metrics,
        )
        self.get_search_metrics = async_to_raw_response_wrapper(
            metrics.get_search_metrics,
        )
        self.get_session_metrics = async_to_raw_response_wrapper(
            metrics.get_session_metrics,
        )
        self.get_usage_metrics = async_to_raw_response_wrapper(
            metrics.get_usage_metrics,
        )
        self.get_weekly_active_users = async_to_raw_response_wrapper(
            metrics.get_weekly_active_users,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.get_active_users = to_streamed_response_wrapper(
            metrics.get_active_users,
        )
        self.get_daily_active_users = to_streamed_response_wrapper(
            metrics.get_daily_active_users,
        )
        self.get_monthly_active_users = to_streamed_response_wrapper(
            metrics.get_monthly_active_users,
        )
        self.get_pr_metrics = to_streamed_response_wrapper(
            metrics.get_pr_metrics,
        )
        self.get_search_metrics = to_streamed_response_wrapper(
            metrics.get_search_metrics,
        )
        self.get_session_metrics = to_streamed_response_wrapper(
            metrics.get_session_metrics,
        )
        self.get_usage_metrics = to_streamed_response_wrapper(
            metrics.get_usage_metrics,
        )
        self.get_weekly_active_users = to_streamed_response_wrapper(
            metrics.get_weekly_active_users,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.get_active_users = async_to_streamed_response_wrapper(
            metrics.get_active_users,
        )
        self.get_daily_active_users = async_to_streamed_response_wrapper(
            metrics.get_daily_active_users,
        )
        self.get_monthly_active_users = async_to_streamed_response_wrapper(
            metrics.get_monthly_active_users,
        )
        self.get_pr_metrics = async_to_streamed_response_wrapper(
            metrics.get_pr_metrics,
        )
        self.get_search_metrics = async_to_streamed_response_wrapper(
            metrics.get_search_metrics,
        )
        self.get_session_metrics = async_to_streamed_response_wrapper(
            metrics.get_session_metrics,
        )
        self.get_usage_metrics = async_to_streamed_response_wrapper(
            metrics.get_usage_metrics,
        )
        self.get_weekly_active_users = async_to_streamed_response_wrapper(
            metrics.get_weekly_active_users,
        )
