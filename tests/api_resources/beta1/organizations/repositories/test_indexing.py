# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.beta1.organizations.repositories import (
    RepoIndexingStatus,
    RepositoryIndexing,
    IndexingListResponse,
    IndexingBulkIndexResponse,
    IndexingBulkRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.list(
            org_id="org-abc123def456",
        )
        assert_matches_type(IndexingListResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.list(
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(IndexingListResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.list(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(IndexingListResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.list(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(IndexingListResponse, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_index(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.bulk_index(
            org_id="org-abc123def456",
            repositories=[{"repository_path": "repository_path"}],
        )
        assert_matches_type(IndexingBulkIndexResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_index(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.bulk_index(
            org_id="org-abc123def456",
            repositories=[{"repository_path": "repository_path"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(IndexingBulkIndexResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_index(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.bulk_index(
            org_id="org-abc123def456",
            repositories=[{"repository_path": "repository_path"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(IndexingBulkIndexResponse, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_bulk_index(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.bulk_index(
                org_id="",
                repositories=[{"repository_path": "repository_path"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_remove(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.bulk_remove(
            org_id="org-abc123def456",
            repository_paths=["string"],
        )
        assert_matches_type(IndexingBulkRemoveResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_remove(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.bulk_remove(
            org_id="org-abc123def456",
            repository_paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(IndexingBulkRemoveResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_remove(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.bulk_remove(
            org_id="org-abc123def456",
            repository_paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(IndexingBulkRemoveResponse, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_bulk_remove(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.bulk_remove(
                org_id="",
                repository_paths=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.get_status(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )
        assert_matches_type(RepoIndexingStatus, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.get_status(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(RepoIndexingStatus, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.get_status(
            repository_path="repository_path",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(RepoIndexingStatus, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.get_status(
                repository_path="repository_path",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.get_status(
                repository_path="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_index(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_index_with_all_params(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
            branch_names=["string"],
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_index(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_index(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(RepositoryIndexing, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_index(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.index(
                repository_path="repository_path",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.index(
                repository_path="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.remove(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.remove(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.remove(
            repository_path="repository_path",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(RepositoryIndexing, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.remove(
                repository_path="repository_path",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.remove(
                repository_path="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_branch(self, client: DevinPlatform) -> None:
        indexing = client.beta1.organizations.repositories.indexing.remove_branch(
            branch_name="branch_name",
            org_id="org-abc123def456",
            repository_path="repository_path",
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_branch(self, client: DevinPlatform) -> None:
        response = client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
            branch_name="branch_name",
            org_id="org-abc123def456",
            repository_path="repository_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = response.parse()
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_branch(self, client: DevinPlatform) -> None:
        with client.beta1.organizations.repositories.indexing.with_streaming_response.remove_branch(
            branch_name="branch_name",
            org_id="org-abc123def456",
            repository_path="repository_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = response.parse()
            assert_matches_type(RepositoryIndexing, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_branch(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
                branch_name="branch_name",
                org_id="",
                repository_path="repository_path",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
                branch_name="branch_name",
                org_id="org-abc123def456",
                repository_path="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_name` but received ''"):
            client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
                branch_name="",
                org_id="org-abc123def456",
                repository_path="repository_path",
            )


class TestAsyncIndexing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.list(
            org_id="org-abc123def456",
        )
        assert_matches_type(IndexingListResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.list(
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(IndexingListResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.list(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(IndexingListResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.list(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(IndexingListResponse, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_index(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.bulk_index(
            org_id="org-abc123def456",
            repositories=[{"repository_path": "repository_path"}],
        )
        assert_matches_type(IndexingBulkIndexResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_index(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.bulk_index(
            org_id="org-abc123def456",
            repositories=[{"repository_path": "repository_path"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(IndexingBulkIndexResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_index(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.bulk_index(
            org_id="org-abc123def456",
            repositories=[{"repository_path": "repository_path"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(IndexingBulkIndexResponse, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_bulk_index(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.bulk_index(
                org_id="",
                repositories=[{"repository_path": "repository_path"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_remove(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.bulk_remove(
            org_id="org-abc123def456",
            repository_paths=["string"],
        )
        assert_matches_type(IndexingBulkRemoveResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_remove(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.bulk_remove(
            org_id="org-abc123def456",
            repository_paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(IndexingBulkRemoveResponse, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_remove(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.bulk_remove(
            org_id="org-abc123def456",
            repository_paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(IndexingBulkRemoveResponse, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_bulk_remove(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.bulk_remove(
                org_id="",
                repository_paths=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.get_status(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )
        assert_matches_type(RepoIndexingStatus, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.get_status(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(RepoIndexingStatus, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.get_status(
            repository_path="repository_path",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(RepoIndexingStatus, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.get_status(
                repository_path="repository_path",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.get_status(
                repository_path="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_index(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_index_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
            branch_names=["string"],
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_index(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_index(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.index(
            repository_path="repository_path",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(RepositoryIndexing, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_index(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.index(
                repository_path="repository_path",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.index(
                repository_path="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.remove(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove(
            repository_path="repository_path",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.remove(
            repository_path="repository_path",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(RepositoryIndexing, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove(
                repository_path="repository_path",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove(
                repository_path="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_branch(self, async_client: AsyncDevinPlatform) -> None:
        indexing = await async_client.beta1.organizations.repositories.indexing.remove_branch(
            branch_name="branch_name",
            org_id="org-abc123def456",
            repository_path="repository_path",
        )
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_branch(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
            branch_name="branch_name",
            org_id="org-abc123def456",
            repository_path="repository_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing = await response.parse()
        assert_matches_type(RepositoryIndexing, indexing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_branch(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.organizations.repositories.indexing.with_streaming_response.remove_branch(
            branch_name="branch_name",
            org_id="org-abc123def456",
            repository_path="repository_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing = await response.parse()
            assert_matches_type(RepositoryIndexing, indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_branch(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
                branch_name="branch_name",
                org_id="",
                repository_path="repository_path",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_path` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
                branch_name="branch_name",
                org_id="org-abc123def456",
                repository_path="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_name` but received ''"):
            await async_client.beta1.organizations.repositories.indexing.with_raw_response.remove_branch(
                branch_name="",
                org_id="org-abc123def456",
                repository_path="repository_path",
            )
