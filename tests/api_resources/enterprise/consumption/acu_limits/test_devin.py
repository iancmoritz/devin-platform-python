# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.consumption.acu_limits import (
    DevinGetAcuLimitsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_acu_limits(self, client: DevinPlatform) -> None:
        devin = client.enterprise.consumption.acu_limits.devin.get_acu_limits()
        assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_acu_limits_with_all_params(self, client: DevinPlatform) -> None:
        devin = client.enterprise.consumption.acu_limits.devin.get_acu_limits(
            after="after",
            first=1,
        )
        assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_acu_limits(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.acu_limits.devin.with_raw_response.get_acu_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        devin = response.parse()
        assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_acu_limits(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.acu_limits.devin.with_streaming_response.get_acu_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            devin = response.parse()
            assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDevin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_acu_limits(self, async_client: AsyncDevinPlatform) -> None:
        devin = await async_client.enterprise.consumption.acu_limits.devin.get_acu_limits()
        assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_acu_limits_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        devin = await async_client.enterprise.consumption.acu_limits.devin.get_acu_limits(
            after="after",
            first=1,
        )
        assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_acu_limits(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.consumption.acu_limits.devin.with_raw_response.get_acu_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        devin = await response.parse()
        assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_acu_limits(self, async_client: AsyncDevinPlatform) -> None:
        async with (
            async_client.enterprise.consumption.acu_limits.devin.with_streaming_response.get_acu_limits()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            devin = await response.parse()
            assert_matches_type(DevinGetAcuLimitsResponse, devin, path=["response"])

        assert cast(Any, response.is_closed) is True
