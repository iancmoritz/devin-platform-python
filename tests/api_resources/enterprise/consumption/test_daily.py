# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.consumption import (
    Consumption,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDaily:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_consumption(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_daily_consumption()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_consumption_with_all_params(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_daily_consumption(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_consumption(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.daily.with_raw_response.get_daily_consumption()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_consumption(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.daily.with_streaming_response.get_daily_consumption() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_org_daily_consumption(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_org_daily_consumption(
            org_id="org-abc123def456",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_org_daily_consumption_with_all_params(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_org_daily_consumption(
            org_id="org-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_org_daily_consumption(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.daily.with_raw_response.get_org_daily_consumption(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_org_daily_consumption(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.daily.with_streaming_response.get_org_daily_consumption(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_org_daily_consumption(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.consumption.daily.with_raw_response.get_org_daily_consumption(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_service_user_daily_consumption(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_service_user_daily_consumption_with_all_params(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_service_user_daily_consumption(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.daily.with_raw_response.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_service_user_daily_consumption(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.daily.with_streaming_response.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_service_user_daily_consumption(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.enterprise.consumption.daily.with_raw_response.get_service_user_daily_consumption(
                service_user_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_session_daily_consumption(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_session_daily_consumption(
            session_id="devin-abc123def456",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_session_daily_consumption_with_all_params(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_session_daily_consumption(
            session_id="devin-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_session_daily_consumption(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.daily.with_raw_response.get_session_daily_consumption(
            session_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_session_daily_consumption(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.daily.with_streaming_response.get_session_daily_consumption(
            session_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_session_daily_consumption(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.enterprise.consumption.daily.with_raw_response.get_session_daily_consumption(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_user_daily_consumption(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_user_daily_consumption(
            user_id="user_id",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_user_daily_consumption_with_all_params(self, client: DevinPlatform) -> None:
        daily = client.enterprise.consumption.daily.get_user_daily_consumption(
            user_id="user_id",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_user_daily_consumption(self, client: DevinPlatform) -> None:
        response = client.enterprise.consumption.daily.with_raw_response.get_user_daily_consumption(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_user_daily_consumption(self, client: DevinPlatform) -> None:
        with client.enterprise.consumption.daily.with_streaming_response.get_user_daily_consumption(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_user_daily_consumption(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.enterprise.consumption.daily.with_raw_response.get_user_daily_consumption(
                user_id="",
            )


class TestAsyncDaily:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_daily_consumption()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_consumption_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_daily_consumption(
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.consumption.daily.with_raw_response.get_daily_consumption()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = await response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        async with (
            async_client.enterprise.consumption.daily.with_streaming_response.get_daily_consumption()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = await response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_org_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_org_daily_consumption(
            org_id="org-abc123def456",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_org_daily_consumption_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_org_daily_consumption(
            org_id="org-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_org_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.consumption.daily.with_raw_response.get_org_daily_consumption(
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = await response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_org_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.consumption.daily.with_streaming_response.get_org_daily_consumption(
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = await response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_org_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.consumption.daily.with_raw_response.get_org_daily_consumption(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_service_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_service_user_daily_consumption_with_all_params(
        self, async_client: AsyncDevinPlatform
    ) -> None:
        daily = await async_client.enterprise.consumption.daily.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_service_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.consumption.daily.with_raw_response.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = await response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_service_user_daily_consumption(
        self, async_client: AsyncDevinPlatform
    ) -> None:
        async with async_client.enterprise.consumption.daily.with_streaming_response.get_service_user_daily_consumption(
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = await response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_service_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.enterprise.consumption.daily.with_raw_response.get_service_user_daily_consumption(
                service_user_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_session_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_session_daily_consumption(
            session_id="devin-abc123def456",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_session_daily_consumption_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_session_daily_consumption(
            session_id="devin-abc123def456",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_session_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.consumption.daily.with_raw_response.get_session_daily_consumption(
            session_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = await response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_session_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.consumption.daily.with_streaming_response.get_session_daily_consumption(
            session_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = await response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_session_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.enterprise.consumption.daily.with_raw_response.get_session_daily_consumption(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_user_daily_consumption(
            user_id="user_id",
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_user_daily_consumption_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        daily = await async_client.enterprise.consumption.daily.get_user_daily_consumption(
            user_id="user_id",
            time_after=0,
            time_before=0,
        )
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.consumption.daily.with_raw_response.get_user_daily_consumption(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily = await response.parse()
        assert_matches_type(Consumption, daily, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.consumption.daily.with_streaming_response.get_user_daily_consumption(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily = await response.parse()
            assert_matches_type(Consumption, daily, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_user_daily_consumption(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.enterprise.consumption.daily.with_raw_response.get_user_daily_consumption(
                user_id="",
            )
