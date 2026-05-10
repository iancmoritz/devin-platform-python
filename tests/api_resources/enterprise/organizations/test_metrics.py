# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import UsageMetrics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_usage(self, client: DevinPlatform) -> None:
        metric = client.enterprise.organizations.metrics.retrieve_usage(
            org_id="org-abc123def456",
        )
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_usage_with_all_params(self, client: DevinPlatform) -> None:
        metric = client.enterprise.organizations.metrics.retrieve_usage(
            org_id="org-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_usage(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.metrics.with_raw_response.retrieve_usage(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_usage(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.metrics.with_streaming_response.retrieve_usage(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(UsageMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_usage(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.metrics.with_raw_response.retrieve_usage(
                org_id="",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_usage(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.organizations.metrics.retrieve_usage(
            org_id="org-abc123def456",
        )
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_usage_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        metric = await async_client.enterprise.organizations.metrics.retrieve_usage(
            org_id="org-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_usage(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.metrics.with_raw_response.retrieve_usage(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(UsageMetrics, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_usage(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.metrics.with_streaming_response.retrieve_usage(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(UsageMetrics, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_usage(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.metrics.with_raw_response.retrieve_usage(
                org_id="",
            )
