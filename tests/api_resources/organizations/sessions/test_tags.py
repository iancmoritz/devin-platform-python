# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.enterprise.sessions import SessionTagsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        tag = client.organizations.sessions.tags.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.tags.with_raw_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.tags.with_streaming_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SessionTagsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.tags.with_raw_response.retrieve(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.tags.with_raw_response.retrieve(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_append(self, client: DevinPlatform) -> None:
        tag = client.organizations.sessions.tags.append(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_append(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.tags.with_raw_response.append(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_append(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.tags.with_streaming_response.append(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SessionTagsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_append(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.tags.with_raw_response.append(
                devin_id="devin-abc123def456",
                org_id="",
                tags=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.tags.with_raw_response.append(
                devin_id="",
                org_id="org-abc123def456",
                tags=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: DevinPlatform) -> None:
        tag = client.organizations.sessions.tags.replace(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: DevinPlatform) -> None:
        response = client.organizations.sessions.tags.with_raw_response.replace(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: DevinPlatform) -> None:
        with client.organizations.sessions.tags.with_streaming_response.replace(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SessionTagsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.sessions.tags.with_raw_response.replace(
                devin_id="devin-abc123def456",
                org_id="",
                tags=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            client.organizations.sessions.tags.with_raw_response.replace(
                devin_id="",
                org_id="org-abc123def456",
                tags=["string"],
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        tag = await async_client.organizations.sessions.tags.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.tags.with_raw_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.tags.with_streaming_response.retrieve(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(SessionTagsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.tags.with_raw_response.retrieve(
                devin_id="devin-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.tags.with_raw_response.retrieve(
                devin_id="",
                org_id="org-abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_append(self, async_client: AsyncDevinPlatform) -> None:
        tag = await async_client.organizations.sessions.tags.append(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_append(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.tags.with_raw_response.append(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_append(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.tags.with_streaming_response.append(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(SessionTagsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_append(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.tags.with_raw_response.append(
                devin_id="devin-abc123def456",
                org_id="",
                tags=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.tags.with_raw_response.append(
                devin_id="",
                org_id="org-abc123def456",
                tags=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncDevinPlatform) -> None:
        tag = await async_client.organizations.sessions.tags.replace(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.sessions.tags.with_raw_response.replace(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(SessionTagsResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.sessions.tags.with_streaming_response.replace(
            devin_id="devin-abc123def456",
            org_id="org-abc123def456",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(SessionTagsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.sessions.tags.with_raw_response.replace(
                devin_id="devin-abc123def456",
                org_id="",
                tags=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `devin_id` but received ''"):
            await async_client.organizations.sessions.tags.with_raw_response.replace(
                devin_id="",
                org_id="org-abc123def456",
                tags=["string"],
            )
