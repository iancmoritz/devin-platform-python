# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.knowledge import (
    KnowledgeNote,
    PaginatedKnowledgeNoteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.create(
            body="body",
            name="name",
            trigger="trigger",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.create(
            body="body",
            name="name",
            trigger="trigger",
            pinned_repo="pinned_repo",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DevinPlatform) -> None:
        response = client.enterprise.knowledge.notes.with_raw_response.create(
            body="body",
            name="name",
            trigger="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DevinPlatform) -> None:
        with client.enterprise.knowledge.notes.with_streaming_response.create(
            body="body",
            name="name",
            trigger="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.retrieve(
            "note-abc123def456",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.enterprise.knowledge.notes.with_raw_response.retrieve(
            "note-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.enterprise.knowledge.notes.with_streaming_response.retrieve(
            "note-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            client.enterprise.knowledge.notes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
            pinned_repo="pinned_repo",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: DevinPlatform) -> None:
        response = client.enterprise.knowledge.notes.with_raw_response.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: DevinPlatform) -> None:
        with client.enterprise.knowledge.notes.with_streaming_response.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            client.enterprise.knowledge.notes.with_raw_response.update(
                note_id="",
                body="body",
                name="name",
                trigger="trigger",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.list()
        assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.list(
            access_type="org",
            after="after",
            first=1,
            folder_path="folder_path",
            pinned_repo="pinned_repo",
            search="search",
        )
        assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.enterprise.knowledge.notes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.enterprise.knowledge.notes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DevinPlatform) -> None:
        note = client.enterprise.knowledge.notes.delete(
            "note-abc123def456",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DevinPlatform) -> None:
        response = client.enterprise.knowledge.notes.with_raw_response.delete(
            "note-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DevinPlatform) -> None:
        with client.enterprise.knowledge.notes.with_streaming_response.delete(
            "note-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            client.enterprise.knowledge.notes.with_raw_response.delete(
                "",
            )


class TestAsyncNotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.create(
            body="body",
            name="name",
            trigger="trigger",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.create(
            body="body",
            name="name",
            trigger="trigger",
            pinned_repo="pinned_repo",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.knowledge.notes.with_raw_response.create(
            body="body",
            name="name",
            trigger="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.knowledge.notes.with_streaming_response.create(
            body="body",
            name="name",
            trigger="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.retrieve(
            "note-abc123def456",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.knowledge.notes.with_raw_response.retrieve(
            "note-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.knowledge.notes.with_streaming_response.retrieve(
            "note-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            await async_client.enterprise.knowledge.notes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
            pinned_repo="pinned_repo",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.knowledge.notes.with_raw_response.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.knowledge.notes.with_streaming_response.update(
            note_id="note-abc123def456",
            body="body",
            name="name",
            trigger="trigger",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            await async_client.enterprise.knowledge.notes.with_raw_response.update(
                note_id="",
                body="body",
                name="name",
                trigger="trigger",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.list()
        assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.list(
            access_type="org",
            after="after",
            first=1,
            folder_path="folder_path",
            pinned_repo="pinned_repo",
            search="search",
        )
        assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.knowledge.notes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.knowledge.notes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(PaginatedKnowledgeNoteResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevinPlatform) -> None:
        note = await async_client.enterprise.knowledge.notes.delete(
            "note-abc123def456",
        )
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.enterprise.knowledge.notes.with_raw_response.delete(
            "note-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(KnowledgeNote, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.enterprise.knowledge.notes.with_streaming_response.delete(
            "note-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(KnowledgeNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            await async_client.enterprise.knowledge.notes.with_raw_response.delete(
                "",
            )
