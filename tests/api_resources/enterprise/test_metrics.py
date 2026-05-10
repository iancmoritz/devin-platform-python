# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import (
    PrMetrics,
    UsageMetrics,
    SearchMetrics,
    SessionMetrics,
    ActiveUserMetrics,
    MetricGetDailyActiveUsersResponse,
    MetricGetWeeklyActiveUsersResponse,
    MetricGetMonthlyActiveUsersResponse,
    MetricGetSessionMetricsByCategoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_active_users(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(ActiveUserMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_active_users_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(ActiveUserMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_active_users(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(ActiveUserMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_active_users(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(ActiveUserMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_active_users(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_daily_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_active_users_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_daily_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_active_users(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_daily_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_active_users(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_daily_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_monthly_active_users(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_monthly_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_monthly_active_users_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_monthly_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_monthly_active_users(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_monthly_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_monthly_active_users(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_monthly_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pr_metrics(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_pr_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(PrMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pr_metrics_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_pr_metrics(
            time_after=0,
            time_before=0,
            org_ids=["string"],
            playbook_id="playbook_id",
            service_user_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(PrMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_pr_metrics(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_pr_metrics(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(PrMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_pr_metrics(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_pr_metrics(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(PrMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_search_metrics(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_search_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(SearchMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_search_metrics_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_search_metrics(
            time_after=0,
            time_before=0,
            org_ids=["string"],
        )
        assert_matches_type(SearchMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_search_metrics(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_search_metrics(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(SearchMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_search_metrics(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_search_metrics(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(SearchMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_session_metrics(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_session_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(SessionMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_session_metrics_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_session_metrics(
            time_after=0,
            time_before=0,
            org_ids=["string"],
            playbook_id="playbook_id",
            service_user_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(SessionMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_session_metrics(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_session_metrics(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(SessionMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_session_metrics(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_session_metrics(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(SessionMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_session_metrics_by_category(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_session_metrics_by_category_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_session_metrics_by_category(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_session_metrics_by_category(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_usage_metrics(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_usage_metrics()
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_usage_metrics_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_usage_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_usage_metrics(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_usage_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_usage_metrics(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_usage_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(UsageMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_weekly_active_users(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_weekly_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_weekly_active_users_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.metrics.get_weekly_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_weekly_active_users(self, client: DevinPlatform) -> None:
        response = client.enterprise.metrics.with_raw_response.get_weekly_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_weekly_active_users(self, client: DevinPlatform) -> None:
        with client.enterprise.metrics.with_streaming_response.get_weekly_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_active_users(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(ActiveUserMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_active_users_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(ActiveUserMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_active_users(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(ActiveUserMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_active_users(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(ActiveUserMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_active_users(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_daily_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_active_users_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_daily_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_active_users(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_daily_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_active_users(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_daily_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricGetDailyActiveUsersResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_monthly_active_users(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_monthly_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_monthly_active_users_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_monthly_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_monthly_active_users(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_monthly_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_monthly_active_users(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_monthly_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricGetMonthlyActiveUsersResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pr_metrics(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_pr_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(PrMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pr_metrics_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_pr_metrics(
            time_after=0,
            time_before=0,
            org_ids=["string"],
            playbook_id="playbook_id",
            service_user_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(PrMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_pr_metrics(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_pr_metrics(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(PrMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_pr_metrics(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_pr_metrics(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(PrMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_search_metrics(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_search_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(SearchMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_search_metrics_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_search_metrics(
            time_after=0,
            time_before=0,
            org_ids=["string"],
        )
        assert_matches_type(SearchMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_search_metrics(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_search_metrics(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(SearchMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_search_metrics(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_search_metrics(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(SearchMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_session_metrics(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_session_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(SessionMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_session_metrics_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_session_metrics(
            time_after=0,
            time_before=0,
            org_ids=["string"],
            playbook_id="playbook_id",
            service_user_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(SessionMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_session_metrics(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_session_metrics(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(SessionMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_session_metrics(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_session_metrics(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(SessionMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_session_metrics_by_category(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_session_metrics_by_category_with_all_params(
        self, async_client: AsyncDevinPlatform
    ) -> None:
        metric = await async_client.enterprise.metrics.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_session_metrics_by_category(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_session_metrics_by_category(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_session_metrics_by_category(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricGetSessionMetricsByCategoryResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_usage_metrics(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_usage_metrics()
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_usage_metrics_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_usage_metrics(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_usage_metrics(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_usage_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_usage_metrics(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_usage_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(UsageMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_weekly_active_users(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_weekly_active_users(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_weekly_active_users_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.metrics.get_weekly_active_users(
            time_after=0,
            time_before=0,
            min_searches=0,
            min_sessions=0,
            org_ids=["string"],
        )
        assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_weekly_active_users(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.metrics.with_raw_response.get_weekly_active_users(
            time_after=0,
            time_before=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_weekly_active_users(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.metrics.with_streaming_response.get_weekly_active_users(
            time_after=0,
            time_before=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricGetWeeklyActiveUsersResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
