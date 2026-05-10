# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Query, Headers, NotGiven, FileTypes, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organizations import attachment_upload_params
from ...types.organizations.attachment_upload_response import AttachmentUploadResponse

__all__ = ["AttachmentsResource", "AsyncAttachmentsResource"]


class AttachmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AttachmentsResourceWithStreamingResponse(self)

    def download(
        self,
        name: str,
        *,
        org_id: str,
        uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Download a file attachment.

        Returns a redirect to a presigned URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/attachments/{uuid}/{name}", org_id=org_id, uuid=uuid, name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def upload(
        self,
        org_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentUploadResponse:
        """
        Upload a file attachment that can be used in Devin sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v3/organizations/{org_id}/attachments", org_id=org_id),
            body=maybe_transform(body, attachment_upload_params.AttachmentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentUploadResponse,
        )


class AsyncAttachmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncAttachmentsResourceWithStreamingResponse(self)

    async def download(
        self,
        name: str,
        *,
        org_id: str,
        uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Download a file attachment.

        Returns a redirect to a presigned URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/attachments/{uuid}/{name}", org_id=org_id, uuid=uuid, name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def upload(
        self,
        org_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentUploadResponse:
        """
        Upload a file attachment that can be used in Devin sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v3/organizations/{org_id}/attachments", org_id=org_id),
            body=await async_maybe_transform(body, attachment_upload_params.AttachmentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentUploadResponse,
        )


class AttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.download = to_raw_response_wrapper(
            attachments.download,
        )
        self.upload = to_raw_response_wrapper(
            attachments.upload,
        )


class AsyncAttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.download = async_to_raw_response_wrapper(
            attachments.download,
        )
        self.upload = async_to_raw_response_wrapper(
            attachments.upload,
        )


class AttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.download = to_streamed_response_wrapper(
            attachments.download,
        )
        self.upload = to_streamed_response_wrapper(
            attachments.upload,
        )


class AsyncAttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.download = async_to_streamed_response_wrapper(
            attachments.download,
        )
        self.upload = async_to_streamed_response_wrapper(
            attachments.upload,
        )
