# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import OrgGroupsConfig

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgGroupLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_org_group_config(self, client: DevinPlatform) -> None:
        org_group_limit = client.enterprise.org_group_limits.get_org_group_config()
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_org_group_config(self, client: DevinPlatform) -> None:
        response = client.enterprise.org_group_limits.with_raw_response.get_org_group_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org_group_limit = response.parse()
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_org_group_config(self, client: DevinPlatform) -> None:
        with client.enterprise.org_group_limits.with_streaming_response.get_org_group_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org_group_limit = response.parse()
            assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_org_group_config(self, client: DevinPlatform) -> None:
        org_group_limit = client.enterprise.org_group_limits.update_org_group_config(
            groups={"foo": {"org_ids": ["string"]}},
        )
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_org_group_config(self, client: DevinPlatform) -> None:
        response = client.enterprise.org_group_limits.with_raw_response.update_org_group_config(
            groups={"foo": {"org_ids": ["string"]}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org_group_limit = response.parse()
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_org_group_config(self, client: DevinPlatform) -> None:
        with client.enterprise.org_group_limits.with_streaming_response.update_org_group_config(
            groups={"foo": {"org_ids": ["string"]}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org_group_limit = response.parse()
            assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrgGroupLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_org_group_config(self, async_client: AsyncDevinPlatform) -> None:
        org_group_limit = await async_client.enterprise.org_group_limits.get_org_group_config()
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_org_group_config(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.org_group_limits.with_raw_response.get_org_group_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org_group_limit = await response.parse()
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_org_group_config(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.org_group_limits.with_streaming_response.get_org_group_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org_group_limit = await response.parse()
            assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_org_group_config(self, async_client: AsyncDevinPlatform) -> None:
        org_group_limit = await async_client.enterprise.org_group_limits.update_org_group_config(
            groups={"foo": {"org_ids": ["string"]}},
        )
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_org_group_config(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.org_group_limits.with_raw_response.update_org_group_config(
            groups={"foo": {"org_ids": ["string"]}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org_group_limit = await response.parse()
        assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_org_group_config(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.org_group_limits.with_streaming_response.update_org_group_config(
            groups={"foo": {"org_ids": ["string"]}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org_group_limit = await response.parse()
            assert_matches_type(OrgGroupsConfig, org_group_limit, path=["response"])

        assert cast(Any, response.is_closed) is True
