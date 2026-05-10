# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.organizations.git_providers import (
    GitPermission,
    PermissionListResponse,
    PermissionCreateResponse,
    PermissionDeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DevinPlatform) -> None:
        permission = client.enterprise.organizations.git_providers.permissions.create(
            org_id="org-abc123def456",
            permissions=[{"git_connection_id": "git_connection_id"}],
        )
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.git_providers.permissions.with_raw_response.create(
            org_id="org-abc123def456",
            permissions=[{"git_connection_id": "git_connection_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.git_providers.permissions.with_streaming_response.create(
            org_id="org-abc123def456",
            permissions=[{"git_connection_id": "git_connection_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionCreateResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.git_providers.permissions.with_raw_response.create(
                org_id="",
                permissions=[{"git_connection_id": "git_connection_id"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        permission = client.enterprise.organizations.git_providers.permissions.list(
            org_id="org-abc123def456",
        )
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        permission = client.enterprise.organizations.git_providers.permissions.list(
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.git_providers.permissions.with_raw_response.list(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.git_providers.permissions.with_streaming_response.list(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionListResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.git_providers.permissions.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DevinPlatform) -> None:
        permission = client.enterprise.organizations.git_providers.permissions.delete(
            git_permission_id="git-permission-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(GitPermission, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.git_providers.permissions.with_raw_response.delete(
            git_permission_id="git-permission-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(GitPermission, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.git_providers.permissions.with_streaming_response.delete(
            git_permission_id="git-permission-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(GitPermission, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.git_providers.permissions.with_raw_response.delete(
                git_permission_id="git-permission-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `git_permission_id` but received ''"):
            client.enterprise.organizations.git_providers.permissions.with_raw_response.delete(
                git_permission_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: DevinPlatform) -> None:
        permission = client.enterprise.organizations.git_providers.permissions.delete_all(
            "org-abc123def456",
        )
        assert_matches_type(PermissionDeleteAllResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.git_providers.permissions.with_raw_response.delete_all(
            "org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionDeleteAllResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.git_providers.permissions.with_streaming_response.delete_all(
            "org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionDeleteAllResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.git_providers.permissions.with_raw_response.delete_all(
                "",
            )


class TestAsyncPermissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevinPlatform) -> None:
        permission = await async_client.enterprise.organizations.git_providers.permissions.create(
            org_id="org-abc123def456",
            permissions=[{"git_connection_id": "git_connection_id"}],
        )
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.create(
            org_id="org-abc123def456",
            permissions=[{"git_connection_id": "git_connection_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.git_providers.permissions.with_streaming_response.create(
            org_id="org-abc123def456",
            permissions=[{"git_connection_id": "git_connection_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionCreateResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.create(
                org_id="",
                permissions=[{"git_connection_id": "git_connection_id"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        permission = await async_client.enterprise.organizations.git_providers.permissions.list(
            org_id="org-abc123def456",
        )
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        permission = await async_client.enterprise.organizations.git_providers.permissions.list(
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.list(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.git_providers.permissions.with_streaming_response.list(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionListResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevinPlatform) -> None:
        permission = await async_client.enterprise.organizations.git_providers.permissions.delete(
            git_permission_id="git-permission-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(GitPermission, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.delete(
            git_permission_id="git-permission-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(GitPermission, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.git_providers.permissions.with_streaming_response.delete(
            git_permission_id="git-permission-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(GitPermission, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.delete(
                git_permission_id="git-permission-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `git_permission_id` but received ''"):
            await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.delete(
                git_permission_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncDevinPlatform) -> None:
        permission = await async_client.enterprise.organizations.git_providers.permissions.delete_all(
            "org-abc123def456",
        )
        assert_matches_type(PermissionDeleteAllResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.delete_all(
            "org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionDeleteAllResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.git_providers.permissions.with_streaming_response.delete_all(
            "org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionDeleteAllResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.git_providers.permissions.with_raw_response.delete_all(
                "",
            )
