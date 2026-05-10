# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.beta1.organizations import RepositoryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepositories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        repository = client.beta1.organizations.repositories.list(
            org_id="org-abc123def456",
        )
        assert_matches_type(RepositoryListResponse, repository, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        repository = client.beta1.organizations.repositories.list(
            org_id="org-abc123def456",
            after="after",
            exclude_repo_paths=["string"],
            filter_name="filter_name",
            first=1,
            load_indexing_status=True,
            only_repo_paths=["string"],
        )
        assert_matches_type(RepositoryListResponse, repository, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.with_raw_response.list(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repository = response.parse()
        assert_matches_type(RepositoryListResponse, repository, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.with_streaming_response.list(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repository = response.parse()
            assert_matches_type(RepositoryListResponse, repository, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.with_raw_response.list(
                org_id="",
            )


class TestAsyncRepositories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        repository = await async_client.beta1.organizations.repositories.list(
            org_id="org-abc123def456",
        )
        assert_matches_type(RepositoryListResponse, repository, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        repository = await async_client.beta1.organizations.repositories.list(
            org_id="org-abc123def456",
            after="after",
            exclude_repo_paths=["string"],
            filter_name="filter_name",
            first=1,
            load_indexing_status=True,
            only_repo_paths=["string"],
        )
        assert_matches_type(RepositoryListResponse, repository, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.with_raw_response.list(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repository = await response.parse()
        assert_matches_type(RepositoryListResponse, repository, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.with_streaming_response.list(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repository = await response.parse()
            assert_matches_type(RepositoryListResponse, repository, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.with_raw_response.list(
                org_id="",
            )
