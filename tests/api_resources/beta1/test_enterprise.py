# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.beta1 import PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnterprise:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_guardrail_violations(self, client: DevinPlatform) -> None:
        enterprise = client.beta1.enterprise.list_guardrail_violations()
        assert_matches_type(PaginatedResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_guardrail_violations_with_all_params(self, client: DevinPlatform) -> None:
        enterprise = client.beta1.enterprise.list_guardrail_violations(
            after="after",
            first=1,
            guardrail_id="guardrail_id",
            order="asc",
            session_id="session_id",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(PaginatedResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_guardrail_violations(self, client: DevinPlatform) -> None:
        response = client.beta1.enterprise.with_raw_response.list_guardrail_violations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(PaginatedResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_guardrail_violations(self, client: DevinPlatform) -> None:
        with client.beta1.enterprise.with_streaming_response.list_guardrail_violations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(PaginatedResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnterprise:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_guardrail_violations(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.beta1.enterprise.list_guardrail_violations()
        assert_matches_type(PaginatedResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_guardrail_violations_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.beta1.enterprise.list_guardrail_violations(
            after="after",
            first=1,
            guardrail_id="guardrail_id",
            order="asc",
            session_id="session_id",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(PaginatedResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_guardrail_violations(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.enterprise.with_raw_response.list_guardrail_violations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(PaginatedResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_guardrail_violations(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.enterprise.with_streaming_response.list_guardrail_violations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(PaginatedResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True
