# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import FolderTree

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders(self, client: DevinPlatform) -> None:
        knowledge = client.enterprise.knowledge.list_folders()
        assert_matches_type(FolderTree, knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_folders(self, client: DevinPlatform) -> None:
        response = client.enterprise.knowledge.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(FolderTree, knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_folders(self, client: DevinPlatform) -> None:
        with client.enterprise.knowledge.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(FolderTree, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders(self, async_client: AsyncDevinPlatform) -> None:
        knowledge = await async_client.enterprise.knowledge.list_folders()
        assert_matches_type(FolderTree, knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_folders(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.knowledge.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(FolderTree, knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_folders(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.knowledge.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(FolderTree, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True
