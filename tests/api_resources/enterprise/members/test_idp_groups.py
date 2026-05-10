# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.members import (
    IdpGroup,
    PaginatedIdpGroup,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdpGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.members.idp_groups.retrieve(
            "idp_group_name",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.enterprise.members.idp_groups.with_raw_response.retrieve(
            "idp_group_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.enterprise.members.idp_groups.with_streaming_response.retrieve(
            "idp_group_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            client.enterprise.members.idp_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.members.idp_groups.update(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: DevinPlatform) -> None:
        response = client.enterprise.members.idp_groups.with_raw_response.update(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: DevinPlatform) -> None:
        with client.enterprise.members.idp_groups.with_streaming_response.update(
            idp_group_name="idp_group_name",
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            client.enterprise.members.idp_groups.with_raw_response.update(
                idp_group_name="",
                role_id="role_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.members.idp_groups.list()
        assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.members.idp_groups.list(
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.members.idp_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.enterprise.members.idp_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.members.idp_groups.delete(
            "idp_group_name",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DevinPlatform) -> None:
        response = client.enterprise.members.idp_groups.with_raw_response.delete(
            "idp_group_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DevinPlatform) -> None:
        with client.enterprise.members.idp_groups.with_streaming_response.delete(
            "idp_group_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            client.enterprise.members.idp_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign(self, client: DevinPlatform) -> None:
        idp_group = client.enterprise.members.idp_groups.assign(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: DevinPlatform) -> None:
        response = client.enterprise.members.idp_groups.with_raw_response.assign(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: DevinPlatform) -> None:
        with client.enterprise.members.idp_groups.with_streaming_response.assign(
            idp_group_name="idp_group_name",
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_assign(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            client.enterprise.members.idp_groups.with_raw_response.assign(
                idp_group_name="",
                role_id="role_id",
            )


class TestAsyncIdpGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.members.idp_groups.retrieve(
            "idp_group_name",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.members.idp_groups.with_raw_response.retrieve(
            "idp_group_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.members.idp_groups.with_streaming_response.retrieve(
            "idp_group_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            await async_client.enterprise.members.idp_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.members.idp_groups.update(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.members.idp_groups.with_raw_response.update(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.members.idp_groups.with_streaming_response.update(
            idp_group_name="idp_group_name",
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            await async_client.enterprise.members.idp_groups.with_raw_response.update(
                idp_group_name="",
                role_id="role_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.members.idp_groups.list()
        assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.members.idp_groups.list(
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.members.idp_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.members.idp_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(PaginatedIdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.members.idp_groups.delete(
            "idp_group_name",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.members.idp_groups.with_raw_response.delete(
            "idp_group_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.members.idp_groups.with_streaming_response.delete(
            "idp_group_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            await async_client.enterprise.members.idp_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncDevinPlatform) -> None:
        idp_group = await async_client.enterprise.members.idp_groups.assign(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.members.idp_groups.with_raw_response.assign(
            idp_group_name="idp_group_name",
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_group = await response.parse()
        assert_matches_type(IdpGroup, idp_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.members.idp_groups.with_streaming_response.assign(
            idp_group_name="idp_group_name",
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_group = await response.parse()
            assert_matches_type(IdpGroup, idp_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_assign(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `idp_group_name` but received ''"):
            await async_client.enterprise.members.idp_groups.with_raw_response.assign(
                idp_group_name="",
                role_id="role_id",
            )
