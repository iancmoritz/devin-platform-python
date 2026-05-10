# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devin_platform import DevinPlatform, AsyncDevinPlatform

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_acu_limit(self, client: DevinPlatform) -> None:
        organization = client.enterprise.consumption.acu_limits.devin.organizations.delete_acu_limit(
            "org-abc123def456",
        )
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_acu_limit(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.delete_acu_limit(
            "org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_acu_limit(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.acu_limits.devin.organizations.with_streaming_response.delete_acu_limit(
            "org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_acu_limit(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.delete_acu_limit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_acu_limit(self, client: DevinPlatform) -> None:
        organization = client.enterprise.consumption.acu_limits.devin.organizations.set_acu_limit(
            org_id="org-abc123def456",
            cycle_acu_limit=0,
        )
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_acu_limit(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.set_acu_limit(
            org_id="org-abc123def456",
            cycle_acu_limit=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_acu_limit(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.acu_limits.devin.organizations.with_streaming_response.set_acu_limit(
            org_id="org-abc123def456",
            cycle_acu_limit=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_acu_limit(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.set_acu_limit(
                org_id="",
                cycle_acu_limit=0,
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        organization = await async_client.enterprise.consumption.acu_limits.devin.organizations.delete_acu_limit(
            "org-abc123def456",
        )
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        response = (
            await async_client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.delete_acu_limit(
                "org-abc123def456",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        async with (
            async_client.enterprise.consumption.acu_limits.devin.organizations.with_streaming_response.delete_acu_limit(
                "org-abc123def456",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.delete_acu_limit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        organization = await async_client.enterprise.consumption.acu_limits.devin.organizations.set_acu_limit(
            org_id="org-abc123def456",
            cycle_acu_limit=0,
        )
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        response = (
            await async_client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.set_acu_limit(
                org_id="org-abc123def456",
                cycle_acu_limit=0,
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        async with (
            async_client.enterprise.consumption.acu_limits.devin.organizations.with_streaming_response.set_acu_limit(
                org_id="org-abc123def456",
                cycle_acu_limit=0,
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_acu_limit(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.consumption.acu_limits.devin.organizations.with_raw_response.set_acu_limit(
                org_id="",
                cycle_acu_limit=0,
            )
