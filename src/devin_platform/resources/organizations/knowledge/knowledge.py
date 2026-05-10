# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .notes import (
    NotesResource,
    AsyncNotesResource,
    NotesResourceWithRawResponse,
    AsyncNotesResourceWithRawResponse,
    NotesResourceWithStreamingResponse,
    AsyncNotesResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.enterprise.folder_tree import FolderTree

__all__ = ["KnowledgeResource", "AsyncKnowledgeResource"]


class KnowledgeResource(SyncAPIResource):
    @cached_property
    def notes(self) -> NotesResource:
        return NotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> KnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return KnowledgeResourceWithStreamingResponse(self)

    def get_folders(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderTree:
        """
        Return the full folder tree with per-folder note counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/knowledge/folders", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderTree,
        )


class AsyncKnowledgeResource(AsyncAPIResource):
    @cached_property
    def notes(self) -> AsyncNotesResource:
        return AsyncNotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncKnowledgeResourceWithStreamingResponse(self)

    async def get_folders(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderTree:
        """
        Return the full folder tree with per-folder note counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/knowledge/folders", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderTree,
        )


class KnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.get_folders = to_raw_response_wrapper(
            knowledge.get_folders,
        )

    @cached_property
    def notes(self) -> NotesResourceWithRawResponse:
        return NotesResourceWithRawResponse(self._knowledge.notes)


class AsyncKnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.get_folders = async_to_raw_response_wrapper(
            knowledge.get_folders,
        )

    @cached_property
    def notes(self) -> AsyncNotesResourceWithRawResponse:
        return AsyncNotesResourceWithRawResponse(self._knowledge.notes)


class KnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.get_folders = to_streamed_response_wrapper(
            knowledge.get_folders,
        )

    @cached_property
    def notes(self) -> NotesResourceWithStreamingResponse:
        return NotesResourceWithStreamingResponse(self._knowledge.notes)


class AsyncKnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.get_folders = async_to_streamed_response_wrapper(
            knowledge.get_folders,
        )

    @cached_property
    def notes(self) -> AsyncNotesResourceWithStreamingResponse:
        return AsyncNotesResourceWithStreamingResponse(self._knowledge.notes)
