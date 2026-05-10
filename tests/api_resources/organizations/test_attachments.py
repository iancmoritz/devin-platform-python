# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform.types.organizations import AttachmentUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download(self, client: DevinPlatform) -> None:
        attachment = client.organizations.attachments.download(
            name="name",
            org_id="org_id",
            uuid="uuid",
        )
        assert_matches_type(object, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: DevinPlatform) -> None:
        response = client.organizations.attachments.with_raw_response.download(
            name="name",
            org_id="org_id",
            uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(object, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: DevinPlatform) -> None:
        with client.organizations.attachments.with_streaming_response.download(
            name="name",
            org_id="org_id",
            uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(object, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.attachments.with_raw_response.download(
                name="name",
                org_id="",
                uuid="uuid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.organizations.attachments.with_raw_response.download(
                name="name",
                org_id="org_id",
                uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.organizations.attachments.with_raw_response.download(
                name="",
                org_id="org_id",
                uuid="uuid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: DevinPlatform) -> None:
        attachment = client.organizations.attachments.upload(
            org_id="org_id",
            file=b"Example data",
        )
        assert_matches_type(AttachmentUploadResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: DevinPlatform) -> None:
        response = client.organizations.attachments.with_raw_response.upload(
            org_id="org_id",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentUploadResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: DevinPlatform) -> None:
        with client.organizations.attachments.with_streaming_response.upload(
            org_id="org_id",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentUploadResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.attachments.with_raw_response.upload(
                org_id="",
                file=b"Example data",
            )


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncDevinPlatform) -> None:
        attachment = await async_client.organizations.attachments.download(
            name="name",
            org_id="org_id",
            uuid="uuid",
        )
        assert_matches_type(object, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.attachments.with_raw_response.download(
            name="name",
            org_id="org_id",
            uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(object, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.attachments.with_streaming_response.download(
            name="name",
            org_id="org_id",
            uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(object, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.attachments.with_raw_response.download(
                name="name",
                org_id="",
                uuid="uuid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.organizations.attachments.with_raw_response.download(
                name="name",
                org_id="org_id",
                uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.organizations.attachments.with_raw_response.download(
                name="",
                org_id="org_id",
                uuid="uuid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncDevinPlatform) -> None:
        attachment = await async_client.organizations.attachments.upload(
            org_id="org_id",
            file=b"Example data",
        )
        assert_matches_type(AttachmentUploadResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.attachments.with_raw_response.upload(
            org_id="org_id",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentUploadResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.attachments.with_streaming_response.upload(
            org_id="org_id",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentUploadResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.attachments.with_raw_response.upload(
                org_id="",
                file=b"Example data",
            )
