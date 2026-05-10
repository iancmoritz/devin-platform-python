# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import SessionResponse
from devin_platform.types.enterprise.sessions import PaginatedSessionMessage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        message = client.organizations.sessions.messages.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(PaginatedSessionMessage, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        message = client.organizations.sessions.messages.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedSessionMessage, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.messages.with_raw_response.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PaginatedSessionMessage, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.messages.with_streaming_response.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PaginatedSessionMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.messages.with_raw_response.list(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.messages.with_raw_response.list(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: DevinPlatform) -> None:
        message = client.organizations.sessions.messages.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
        )
        assert_matches_type(SessionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: DevinPlatform) -> None:
        message = client.organizations.sessions.messages.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
            message_as_user_id="message_as_user_id",
        )
        assert_matches_type(SessionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.messages.with_raw_response.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SessionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.messages.with_streaming_response.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SessionResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.messages.with_raw_response.send(
                devin_id="devin-abc123def456",
                org_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.messages.with_raw_response.send(
                devin_id="",
                org_id="org-abc123def456",
                message="message",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        message = await async_client.organizations.sessions.messages.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(PaginatedSessionMessage, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        message = await async_client.organizations.sessions.messages.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedSessionMessage, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.messages.with_raw_response.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PaginatedSessionMessage, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.messages.with_streaming_response.list(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PaginatedSessionMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.messages.with_raw_response.list(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.messages.with_raw_response.list(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncDevinPlatform) -> None:
        message = await async_client.organizations.sessions.messages.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
        )
        assert_matches_type(SessionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        message = await async_client.organizations.sessions.messages.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
            message_as_user_id="message_as_user_id",
        )
        assert_matches_type(SessionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.messages.with_raw_response.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(SessionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.messages.with_streaming_response.send(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(SessionResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.messages.with_raw_response.send(
                devin_id="devin-abc123def456",
                org_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.messages.with_raw_response.send(
                devin_id="",
                org_id="org-abc123def456",
                message="message",
            )
