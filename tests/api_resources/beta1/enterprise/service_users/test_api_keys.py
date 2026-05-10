# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.beta1.enterprise.service_users import (
    APIKey,
    APIKeyWithToken,
    APIKeyListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.create(
            service_user_id="service-user-abc123def456",
            name="x",
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.create(
            service_user_id="service-user-abc123def456",
            name="x",
            expires_at=0,
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DevinPlatform) -> None:
        response = client.beta1.enterprise.service_users.api_keys.with_raw_response.create(
            service_user_id="service-user-abc123def456",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DevinPlatform) -> None:
        with client.beta1.enterprise.service_users.api_keys.with_streaming_response.create(
            service_user_id="service-user-abc123def456",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyWithToken, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.beta1.enterprise.service_users.api_keys.with_raw_response.create(
                service_user_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.list(
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.list(
            service_user_id="service-user-abc123def456",
            status="active",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.beta1.enterprise.service_users.api_keys.with_raw_response.list(
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.beta1.enterprise.service_users.api_keys.with_streaming_response.list(
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.beta1.enterprise.service_users.api_keys.with_raw_response.list(
                service_user_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.revoke(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: DevinPlatform) -> None:
        response = client.beta1.enterprise.service_users.api_keys.with_raw_response.revoke(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: DevinPlatform) -> None:
        with client.beta1.enterprise.service_users.api_keys.with_streaming_response.revoke(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.beta1.enterprise.service_users.api_keys.with_raw_response.revoke(
                api_key_id="api_key_id",
                service_user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            client.beta1.enterprise.service_users.api_keys.with_raw_response.revoke(
                api_key_id="",
                service_user_id="service-user-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_with_all_params(self, client: DevinPlatform) -> None:
        api_key = client.beta1.enterprise.service_users.api_keys.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
            new_key_expires_at=0,
            revoke_current=True,
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate(self, client: DevinPlatform) -> None:
        response = client.beta1.enterprise.service_users.api_keys.with_raw_response.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate(self, client: DevinPlatform) -> None:
        with client.beta1.enterprise.service_users.api_keys.with_streaming_response.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyWithToken, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            client.beta1.enterprise.service_users.api_keys.with_raw_response.rotate(
                api_key_id="api_key_id",
                service_user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            client.beta1.enterprise.service_users.api_keys.with_raw_response.rotate(
                api_key_id="",
                service_user_id="service-user-abc123def456",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.create(
            service_user_id="service-user-abc123def456",
            name="x",
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.create(
            service_user_id="service-user-abc123def456",
            name="x",
            expires_at=0,
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.create(
            service_user_id="service-user-abc123def456",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.enterprise.service_users.api_keys.with_streaming_response.create(
            service_user_id="service-user-abc123def456",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyWithToken, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.create(
                service_user_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.list(
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.list(
            service_user_id="service-user-abc123def456",
            status="active",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.list(
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.enterprise.service_users.api_keys.with_streaming_response.list(
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.list(
                service_user_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.revoke(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.revoke(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.enterprise.service_users.api_keys.with_streaming_response.revoke(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.revoke(
                api_key_id="api_key_id",
                service_user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.revoke(
                api_key_id="",
                service_user_id="service-user-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        api_key = await async_client.beta1.enterprise.service_users.api_keys.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
            new_key_expires_at=0,
            revoke_current=True,
        )
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyWithToken, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.beta1.enterprise.service_users.api_keys.with_streaming_response.rotate(
            api_key_id="api_key_id",
            service_user_id="service-user-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyWithToken, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_user_id` but received ''"):
            await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.rotate(
                api_key_id="api_key_id",
                service_user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            await async_client.beta1.enterprise.service_users.api_keys.with_raw_response.rotate(
                api_key_id="",
                service_user_id="service-user-abc123def456",
            )
