# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import (
    IdpGroupResponse,
    IdpGroupListIdpGroupsResponse,
    IdpGroupRegisterIdpGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdpGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_idp_group(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.idp_groups.delete_idp_group(
            "idp_group_name",
        )
        assert_matches_type(IdpGroupResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_idp_group(self, client: DevinPlatform) -> None:
        response = client.enterprise.idp_groups.with_raw_response.delete_idp_group(
            "idp_group_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroupResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_idp_group(self, client: DevinPlatform) -> None:
        with client.enterprise.idp_groups.with_streaming_response.delete_idp_group(
            "idp_group_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroupResponse, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_idp_group(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            client.enterprise.idp_groups.with_raw_response.delete_idp_group(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_idp_groups(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.idp_groups.list_idp_groups()
        assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_idp_groups_with_all_params(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.idp_groups.list_idp_groups(
            after="after",
            first=1,
        )
        assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_idp_groups(self, client: DevinPlatform) -> None:
        response = client.enterprise.idp_groups.with_raw_response.list_idp_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_idp_groups(self, client: DevinPlatform) -> None:
        with client.enterprise.idp_groups.with_streaming_response.list_idp_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register_idp_groups(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.idp_groups.register_idp_groups(
            idp_group_names=["string"],
        )
        assert_matches_type(IdpGroupRegisterIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_register_idp_groups(self, client: DevinPlatform) -> None:
        response = client.enterprise.idp_groups.with_raw_response.register_idp_groups(
            idp_group_names=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroupRegisterIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_register_idp_groups(self, client: DevinPlatform) -> None:
        with client.enterprise.idp_groups.with_streaming_response.register_idp_groups(
            idp_group_names=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroupRegisterIdpGroupsResponse, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIdpGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_idp_group(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.idp_groups.delete_idp_group(
            "idp_group_name",
        )
        assert_matches_type(IdpGroupResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_idp_group(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.idp_groups.with_raw_response.delete_idp_group(
            "idp_group_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroupResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_idp_group(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.idp_groups.with_streaming_response.delete_idp_group(
            "idp_group_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroupResponse, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_idp_group(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            await async_client.enterprise.idp_groups.with_raw_response.delete_idp_group(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_idp_groups(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.idp_groups.list_idp_groups()
        assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_idp_groups_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.idp_groups.list_idp_groups(
            after="after",
            first=1,
        )
        assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_idp_groups(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.idp_groups.with_raw_response.list_idp_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_idp_groups(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.idp_groups.with_streaming_response.list_idp_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroupListIdpGroupsResponse, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register_idp_groups(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.idp_groups.register_idp_groups(
            idp_group_names=["string"],
        )
        assert_matches_type(IdpGroupRegisterIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_register_idp_groups(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.idp_groups.with_raw_response.register_idp_groups(
            idp_group_names=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroupRegisterIdpGroupsResponse, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_register_idp_groups(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.idp_groups.with_streaming_response.register_idp_groups(
            idp_group_names=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroupRegisterIdpGroupsResponse, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True
