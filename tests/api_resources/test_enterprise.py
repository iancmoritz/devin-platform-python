# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types import (
    PaginatedAuditLogResponse,
    EnterpriseListRolesResponse,
    EnterpriseGetQueueStatusResponse,
    EnterpriseListHypervisorsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnterprise:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_queue_status(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.get_queue_status()
        assert_matches_type(EnterpriseGetQueueStatusResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_queue_status(self, client: DevinPlatform) -> None:
        response = client.enterprise.with_raw_response.get_queue_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseGetQueueStatusResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_queue_status(self, client: DevinPlatform) -> None:
        with client.enterprise.with_streaming_response.get_queue_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseGetQueueStatusResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_audit_logs(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.list_audit_logs()
        assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_audit_logs_with_all_params(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.list_audit_logs(
            action="login",
            after="after",
            first=1,
            order="asc",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_audit_logs(self, client: DevinPlatform) -> None:
        response = client.enterprise.with_raw_response.list_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_audit_logs(self, client: DevinPlatform) -> None:
        with client.enterprise.with_streaming_response.list_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_hypervisors(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.list_hypervisors()
        assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_hypervisors_with_all_params(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.list_hypervisors(
            after="after",
            first=1,
            status="available",
        )
        assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_hypervisors(self, client: DevinPlatform) -> None:
        response = client.enterprise.with_raw_response.list_hypervisors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_hypervisors(self, client: DevinPlatform) -> None:
        with client.enterprise.with_streaming_response.list_hypervisors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_roles(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.list_roles()
        assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_roles_with_all_params(self, client: DevinPlatform) -> None:
        enterprise = client.enterprise.list_roles(
            after="after",
            first=1,
        )
        assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_roles(self, client: DevinPlatform) -> None:
        response = client.enterprise.with_raw_response.list_roles()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_roles(self, client: DevinPlatform) -> None:
        with client.enterprise.with_streaming_response.list_roles() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnterprise:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_queue_status(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.get_queue_status()
        assert_matches_type(EnterpriseGetQueueStatusResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_queue_status(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.with_raw_response.get_queue_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseGetQueueStatusResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_queue_status(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.with_streaming_response.get_queue_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseGetQueueStatusResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_audit_logs(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.list_audit_logs()
        assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_audit_logs_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.list_audit_logs(
            action="login",
            after="after",
            first=1,
            order="asc",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_audit_logs(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.with_raw_response.list_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_audit_logs(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.with_streaming_response.list_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(PaginatedAuditLogResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_hypervisors(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.list_hypervisors()
        assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_hypervisors_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.list_hypervisors(
            after="after",
            first=1,
            status="available",
        )
        assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_hypervisors(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.with_raw_response.list_hypervisors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_hypervisors(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.with_streaming_response.list_hypervisors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseListHypervisorsResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_roles(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.list_roles()
        assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_roles_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        enterprise = await async_client.enterprise.list_roles(
            after="after",
            first=1,
        )
        assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_roles(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.with_raw_response.list_roles()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_roles(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.with_streaming_response.list_roles() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseListRolesResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True
