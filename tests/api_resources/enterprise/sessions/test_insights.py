# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.sessions import (
    SessionInsights,
    SessionInsightsGenerate,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        insight = client.enterprise.sessions.insights.list(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionInsights, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        insight = client.enterprise.sessions.insights.list(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionInsights, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.sessions.insights.with_raw_response.list(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(SessionInsights, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.enterprise.sessions.insights.with_streaming_response.list(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(SessionInsights, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.enterprise.sessions.insights.with_raw_response.list(
                devin_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: DevinPlatform) -> None:
        insight = client.enterprise.sessions.insights.generate(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: DevinPlatform) -> None:
        insight = client.enterprise.sessions.insights.generate(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: DevinPlatform) -> None:
        response = client.enterprise.sessions.insights.with_raw_response.generate(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: DevinPlatform) -> None:
        with client.enterprise.sessions.insights.with_streaming_response.generate(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.enterprise.sessions.insights.with_raw_response.generate(
                devin_id="",
            )


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        insight = await async_client.enterprise.sessions.insights.list(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionInsights, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        insight = await async_client.enterprise.sessions.insights.list(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionInsights, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.sessions.insights.with_raw_response.list(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(SessionInsights, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.sessions.insights.with_streaming_response.list(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(SessionInsights, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.enterprise.sessions.insights.with_raw_response.list(
                devin_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncDevinPlatform) -> None:
        insight = await async_client.enterprise.sessions.insights.generate(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        insight = await async_client.enterprise.sessions.insights.generate(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.sessions.insights.with_raw_response.generate(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.sessions.insights.with_streaming_response.generate(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(SessionInsightsGenerate, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.enterprise.sessions.insights.with_raw_response.generate(
                devin_id="",
            )
