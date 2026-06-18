# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise import PlaybookResponse, PaginatedPlaybookResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlaybooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.create(
            org_id="org_id",
            body="body",
            title="title",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.create(
            org_id="org_id",
            body="body",
            title="title",
            macro="macro",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DevinPlatform) -> None:
        response = client.organizations.playbooks.with_raw_response.create(
            org_id="org_id",
            body="body",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DevinPlatform) -> None:
        with client.organizations.playbooks.with_streaming_response.create(
            org_id="org_id",
            body="body",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.playbooks.with_raw_response.create(
                org_id="",
                body="body",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.retrieve(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.organizations.playbooks.with_raw_response.retrieve(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.organizations.playbooks.with_streaming_response.retrieve(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.playbooks.with_raw_response.retrieve(
                playbook_id="playbook-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playbook_id` but received ''"):
            client.organizations.playbooks.with_raw_response.retrieve(
                playbook_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
            macro="macro",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: DevinPlatform) -> None:
        response = client.organizations.playbooks.with_raw_response.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: DevinPlatform) -> None:
        with client.organizations.playbooks.with_streaming_response.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.playbooks.with_raw_response.update(
                playbook_id="playbook-abc123def456",
                org_id="",
                body="body",
                title="title",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playbook_id` but received ''"):
            client.organizations.playbooks.with_raw_response.update(
                playbook_id="",
                org_id="org_id",
                body="body",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.list(
            org_id="org_id",
        )
        assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.list(
            org_id="org_id",
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.organizations.playbooks.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = response.parse()
        assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.organizations.playbooks.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = response.parse()
            assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.playbooks.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DevinPlatform) -> None:
        playbook = client.organizations.playbooks.delete(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DevinPlatform) -> None:
        response = client.organizations.playbooks.with_raw_response.delete(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DevinPlatform) -> None:
        with client.organizations.playbooks.with_streaming_response.delete(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.playbooks.with_raw_response.delete(
                playbook_id="playbook-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playbook_id` but received ''"):
            client.organizations.playbooks.with_raw_response.delete(
                playbook_id="",
                org_id="org_id",
            )


class TestAsyncPlaybooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.create(
            org_id="org_id",
            body="body",
            title="title",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.create(
            org_id="org_id",
            body="body",
            title="title",
            macro="macro",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.playbooks.with_raw_response.create(
            org_id="org_id",
            body="body",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = await response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.playbooks.with_streaming_response.create(
            org_id="org_id",
            body="body",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = await response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.create(
                org_id="",
                body="body",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.retrieve(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.playbooks.with_raw_response.retrieve(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = await response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.playbooks.with_streaming_response.retrieve(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = await response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.retrieve(
                playbook_id="playbook-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playbook_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.retrieve(
                playbook_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
            macro="macro",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.playbooks.with_raw_response.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = await response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.playbooks.with_streaming_response.update(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
            body="body",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = await response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.update(
                playbook_id="playbook-abc123def456",
                org_id="",
                body="body",
                title="title",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playbook_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.update(
                playbook_id="",
                org_id="org_id",
                body="body",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.list(
            org_id="org_id",
        )
        assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.list(
            org_id="org_id",
            after="after",
            first=1,
        )
        assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.playbooks.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = await response.parse()
        assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.playbooks.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = await response.parse()
            assert_matches_type(PaginatedPlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevinPlatform) -> None:
        playbook = await async_client.organizations.playbooks.delete(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.playbooks.with_raw_response.delete(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playbook = await response.parse()
        assert_matches_type(PlaybookResponse, playbook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.playbooks.with_streaming_response.delete(
            playbook_id="playbook-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playbook = await response.parse()
            assert_matches_type(PlaybookResponse, playbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.delete(
                playbook_id="playbook-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playbook_id` but received ''"):
            await async_client.organizations.playbooks.with_raw_response.delete(
                playbook_id="",
                org_id="org_id",
            )
