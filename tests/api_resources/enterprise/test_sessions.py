# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import (
    SessionResponse,
    PaginatedSessionResponse,
    SessionRetrieveAttachmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        session = client.enterprise.sessions.retrieve(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: DevinPlatform) -> None:
        session = client.enterprise.sessions.retrieve(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.enterprise.sessions.with_raw_response.retrieve(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.enterprise.sessions.with_streaming_response.retrieve(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.enterprise.sessions.with_raw_response.retrieve(
                devin_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        session = client.enterprise.sessions.list()
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        session = client.enterprise.sessions.list(
            after="after",
            created_after=0,
            created_before=0,
            first=1,
            org_ids=["string"],
            origins=["webapp"],
            playbook_id="playbook_id",
            schedule_id="schedule_id",
            service_user_ids=["string"],
            session_ids=["string"],
            tags=["string"],
            updated_after=0,
            updated_before=0,
            user_ids=["string"],
        )
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.enterprise.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(PaginatedSessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_attachments(self, client: DevinPlatform) -> None:
        session = client.enterprise.sessions.retrieve_attachments(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_attachments_with_all_params(self, client: DevinPlatform) -> None:
        session = client.enterprise.sessions.retrieve_attachments(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_attachments(self, client: DevinPlatform) -> None:
        response = client.enterprise.sessions.with_raw_response.retrieve_attachments(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_attachments(self, client: DevinPlatform) -> None:
        with client.enterprise.sessions.with_streaming_response.retrieve_attachments(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_attachments(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.enterprise.sessions.with_raw_response.retrieve_attachments(
                devin_id="",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.enterprise.sessions.retrieve(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.enterprise.sessions.retrieve(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.sessions.with_raw_response.retrieve(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.sessions.with_streaming_response.retrieve(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.enterprise.sessions.with_raw_response.retrieve(
                devin_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.enterprise.sessions.list()
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.enterprise.sessions.list(
            after="after",
            created_after=0,
            created_before=0,
            first=1,
            org_ids=["string"],
            origins=["webapp"],
            playbook_id="playbook_id",
            schedule_id="schedule_id",
            service_user_ids=["string"],
            session_ids=["string"],
            tags=["string"],
            updated_after=0,
            updated_before=0,
            user_ids=["string"],
        )
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(PaginatedSessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_attachments(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.enterprise.sessions.retrieve_attachments(
            devin_id="devin-abc123def456",
        )
        assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_attachments_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.enterprise.sessions.retrieve_attachments(
            devin_id="devin-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_attachments(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.sessions.with_raw_response.retrieve_attachments(
            devin_id="devin-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_attachments(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.sessions.with_streaming_response.retrieve_attachments(
            devin_id="devin-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveAttachmentsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_attachments(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.enterprise.sessions.with_raw_response.retrieve_attachments(
                devin_id="",
            )
