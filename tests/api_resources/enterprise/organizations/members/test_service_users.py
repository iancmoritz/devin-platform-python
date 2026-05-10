# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.members import ServiceUser, PaginatedServiceUser

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: DevinPlatform) -> None:
        service_user = client.enterprise.organizations.members.service_users.update(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
            role_id="role_id",
        )
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.members.service_users.with_raw_response.update(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_user = response.parse()
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.members.service_users.with_streaming_response.update(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_user = response.parse()
            assert_matches_type(ServiceUser, service_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.members.service_users.with_raw_response.update(
                service_user_id="service-user-abc123def456",
                org_id="",
                role_id="role_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.enterprise.organizations.members.service_users.with_raw_response.update(
                service_user_id="",
                org_id="org-abc123def456",
                role_id="role_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DevinPlatform) -> None:
        service_user = client.enterprise.organizations.members.service_users.delete(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.members.service_users.with_raw_response.delete(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_user = response.parse()
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.members.service_users.with_streaming_response.delete(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_user = response.parse()
            assert_matches_type(ServiceUser, service_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.members.service_users.with_raw_response.delete(
                service_user_id="service-user-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.enterprise.organizations.members.service_users.with_raw_response.delete(
                service_user_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_service_users(self, client: DevinPlatform) -> None:
        service_user = client.enterprise.organizations.members.service_users.retrieve_service_users(
            org_id="org-abc123def456",
        )
        assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_service_users_with_all_params(self, client: DevinPlatform) -> None:
        service_user = client.enterprise.organizations.members.service_users.retrieve_service_users(
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_service_users(self, client: DevinPlatform) -> None:
        response = client.enterprise.organizations.members.service_users.with_raw_response.retrieve_service_users(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_user = response.parse()
        assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_service_users(self, client: DevinPlatform) -> None:
        with client.enterprise.organizations.members.service_users.with_streaming_response.retrieve_service_users(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_user = response.parse()
            assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_service_users(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.organizations.members.service_users.with_raw_response.retrieve_service_users(
                org_id="",
            )


class TestAsyncServiceUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevinPlatform) -> None:
        service_user = await async_client.enterprise.organizations.members.service_users.update(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
            role_id="role_id",
        )
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.members.service_users.with_raw_response.update(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
            role_id="role_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_user = await response.parse()
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.members.service_users.with_streaming_response.update(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
            role_id="role_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_user = await response.parse()
            assert_matches_type(ServiceUser, service_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.members.service_users.with_raw_response.update(
                service_user_id="service-user-abc123def456",
                org_id="",
                role_id="role_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.enterprise.organizations.members.service_users.with_raw_response.update(
                service_user_id="",
                org_id="org-abc123def456",
                role_id="role_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevinPlatform) -> None:
        service_user = await async_client.enterprise.organizations.members.service_users.delete(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.organizations.members.service_users.with_raw_response.delete(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_user = await response.parse()
        assert_matches_type(ServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.organizations.members.service_users.with_streaming_response.delete(
            service_user_id="service-user-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_user = await response.parse()
            assert_matches_type(ServiceUser, service_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.members.service_users.with_raw_response.delete(
                service_user_id="service-user-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.enterprise.organizations.members.service_users.with_raw_response.delete(
                service_user_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_service_users(self, async_client: AsyncDevinPlatform) -> None:
        service_user = await async_client.enterprise.organizations.members.service_users.retrieve_service_users(
            org_id="org-abc123def456",
        )
        assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_service_users_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        service_user = await async_client.enterprise.organizations.members.service_users.retrieve_service_users(
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_service_users(self, async_client: AsyncDevinPlatform) -> None:
        response = (
            await async_client.enterprise.organizations.members.service_users.with_raw_response.retrieve_service_users(
                org_id="org-abc123def456",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_user = await response.parse()
        assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_service_users(self, async_client: AsyncDevinPlatform) -> None:
        async with (
            async_client.enterprise.organizations.members.service_users.with_streaming_response.retrieve_service_users(
                org_id="org-abc123def456",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_user = await response.parse()
            assert_matches_type(PaginatedServiceUser, service_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_service_users(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.organizations.members.service_users.with_raw_response.retrieve_service_users(
                org_id="",
            )
