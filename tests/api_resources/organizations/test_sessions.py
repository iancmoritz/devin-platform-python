# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import SessionResponse, PaginatedSessionResponse
from devin_platform.types.organizations import (
    SessionListAttachmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.create(
            org_id="org-abc123def456",
            prompt="prompt",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.create(
            org_id="org-abc123def456",
            prompt="prompt",
            devin_id="devin_id",
            attachment_urls=["https://example.com"],
            bypass_approval=True,
            child_playbook_id="child_playbook_id",
            create_as_user_id="create_as_user_id",
            knowledge_ids=["string"],
            max_acu_limit=0,
            platform="platform",
            playbook_id="playbook_id",
            repos=["string"],
            secret_ids=["string"],
            session_links=["string"],
            session_secrets=[
                {
                    "key": "x",
                    "value": "value",
                    "sensitive": True,
                }
            ],
            structured_output_required=True,
            structured_output_schema={"foo": "bar"},
            tags=["string"],
            title="title",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.with_raw_response.create(
            org_id="org-abc123def456",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.with_streaming_response.create(
            org_id="org-abc123def456",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.with_raw_response.create(
                org_id="",
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.with_raw_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.with_streaming_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.with_raw_response.retrieve(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.with_raw_response.retrieve(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.list(
            org_id="org-abc123def456",
            qs={},
        )
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.list(
            org_id="org-abc123def456",
            qs={
                "after": "after",
                "category": "bug_fixing",
                "created_after": 0,
                "created_before": 0,
                "first": 1,
                "is_archived": True,
                "origins": ["webapp"],
                "playbook_id": "playbook_id",
                "repo_names": ["string"],
                "schedule_id": "schedule_id",
                "service_user_ids": ["string"],
                "session_ids": ["string"],
                "tags": ["string"],
                "updated_after": 0,
                "updated_before": 0,
                "user_ids": ["string"],
            },
            devin_id="devin_id",
        )
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.with_raw_response.list(
            org_id="org-abc123def456",
            qs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.with_streaming_response.list(
            org_id="org-abc123def456",
            qs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(PaginatedSessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.with_raw_response.list(
                org_id="",
                qs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.archive(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.with_raw_response.archive(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.with_streaming_response.archive(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.with_raw_response.archive(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.with_raw_response.archive(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.list_attachments(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionListAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attachments(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.with_raw_response.list_attachments(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attachments(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.with_streaming_response.list_attachments(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListAttachmentsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attachments(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.with_raw_response.list_attachments(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.with_raw_response.list_attachments(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_terminate(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_terminate_with_all_params(self, client: DevinPlatform) -> None:
        session = client.organizations.sessions.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            archive=True,
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.with_raw_response.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.with_streaming_response.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.with_raw_response.terminate(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.with_raw_response.terminate(
                devin_id="",
                org_id="org-abc123def456",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.create(
            org_id="org-abc123def456",
            prompt="prompt",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.create(
            org_id="org-abc123def456",
            prompt="prompt",
            devin_id="devin_id",
            attachment_urls=["https://example.com"],
            bypass_approval=True,
            child_playbook_id="child_playbook_id",
            create_as_user_id="create_as_user_id",
            knowledge_ids=["string"],
            max_acu_limit=0,
            platform="platform",
            playbook_id="playbook_id",
            repos=["string"],
            secret_ids=["string"],
            session_links=["string"],
            session_secrets=[
                {
                    "key": "x",
                    "value": "value",
                    "sensitive": True,
                }
            ],
            structured_output_required=True,
            structured_output_schema={"foo": "bar"},
            tags=["string"],
            title="title",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.with_raw_response.create(
            org_id="org-abc123def456",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.with_streaming_response.create(
            org_id="org-abc123def456",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.create(
                org_id="",
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.with_raw_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.with_streaming_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.retrieve(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.retrieve(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.list(
            org_id="org-abc123def456",
            qs={},
        )
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.list(
            org_id="org-abc123def456",
            qs={
                "after": "after",
                "category": "bug_fixing",
                "created_after": 0,
                "created_before": 0,
                "first": 1,
                "is_archived": True,
                "origins": ["webapp"],
                "playbook_id": "playbook_id",
                "repo_names": ["string"],
                "schedule_id": "schedule_id",
                "service_user_ids": ["string"],
                "session_ids": ["string"],
                "tags": ["string"],
                "updated_after": 0,
                "updated_before": 0,
                "user_ids": ["string"],
            },
            devin_id="devin_id",
        )
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.with_raw_response.list(
            org_id="org-abc123def456",
            qs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(PaginatedSessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.with_streaming_response.list(
            org_id="org-abc123def456",
            qs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(PaginatedSessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.list(
                org_id="",
                qs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.archive(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.with_raw_response.archive(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.with_streaming_response.archive(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.archive(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.archive(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.list_attachments(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionListAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attachments(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.with_raw_response.list_attachments(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListAttachmentsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attachments(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.with_streaming_response.list_attachments(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListAttachmentsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attachments(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.list_attachments(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.list_attachments(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_terminate_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        session = await async_client.organizations.sessions.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            archive=True,
        )
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.with_raw_response.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.with_streaming_response.terminate(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.terminate(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.with_raw_response.terminate(
                devin_id="",
                org_id="org-abc123def456",
            )
