# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import IPAccessListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPAccessList:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clear_access_list(self, client: DevinPlatform) -> None:
        ip_access_list = client.enterprise.ip_access_list.clear_access_list()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clear_access_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.ip_access_list.with_raw_response.clear_access_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_access_list = response.parse()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clear_access_list(self, client: DevinPlatform) -> None:
        with client.enterprise.ip_access_list.with_streaming_response.clear_access_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_access_list = response.parse()
            assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_access_list(self, client: DevinPlatform) -> None:
        ip_access_list = client.enterprise.ip_access_list.get_access_list()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_access_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.ip_access_list.with_raw_response.get_access_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_access_list = response.parse()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_access_list(self, client: DevinPlatform) -> None:
        with client.enterprise.ip_access_list.with_streaming_response.get_access_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_access_list = response.parse()
            assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_access_list(self, client: DevinPlatform) -> None:
        ip_access_list = client.enterprise.ip_access_list.replace_access_list(
            ip_ranges=["string"],
        )
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace_access_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.ip_access_list.with_raw_response.replace_access_list(
            ip_ranges=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_access_list = response.parse()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace_access_list(self, client: DevinPlatform) -> None:
        with client.enterprise.ip_access_list.with_streaming_response.replace_access_list(
            ip_ranges=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_access_list = response.parse()
            assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIPAccessList:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clear_access_list(self, async_client: AsyncDevinPlatform) -> None:
        ip_access_list = await async_client.enterprise.ip_access_list.clear_access_list()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clear_access_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.ip_access_list.with_raw_response.clear_access_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_access_list = await response.parse()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clear_access_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.ip_access_list.with_streaming_response.clear_access_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_access_list = await response.parse()
            assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_access_list(self, async_client: AsyncDevinPlatform) -> None:
        ip_access_list = await async_client.enterprise.ip_access_list.get_access_list()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_access_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.ip_access_list.with_raw_response.get_access_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_access_list = await response.parse()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_access_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.ip_access_list.with_streaming_response.get_access_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_access_list = await response.parse()
            assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_access_list(self, async_client: AsyncDevinPlatform) -> None:
        ip_access_list = await async_client.enterprise.ip_access_list.replace_access_list(
            ip_ranges=["string"],
        )
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace_access_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.ip_access_list.with_raw_response.replace_access_list(
            ip_ranges=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_access_list = await response.parse()
        assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace_access_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.ip_access_list.with_streaming_response.replace_access_list(
            ip_ranges=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_access_list = await response.parse()
            assert_matches_type(IPAccessListResponse, ip_access_list, path=["response"])

        assert cast(Any, response.is_closed) is True
