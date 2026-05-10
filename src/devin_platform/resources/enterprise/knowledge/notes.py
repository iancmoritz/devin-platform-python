# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.enterprise.knowledge import note_list_params, note_create_params, note_update_params
from ....types.enterprise.knowledge.knowledge_note import KnowledgeNote
from ....types.enterprise.knowledge.paginated_knowledge_note_response import PaginatedKnowledgeNoteResponse

__all__ = ["NotesResource", "AsyncNotesResource"]


class NotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return NotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return NotesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: str,
        name: str,
        trigger: str,
        pinned_repo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Create an enterprise-level note

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/enterprise/knowledge/notes",
            body=maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "trigger": trigger,
                    "pinned_repo": pinned_repo,
                },
                note_create_params.NoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )

    def retrieve(
        self,
        note_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Get a note by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not note_id:
            raise ValueError(f"Expected a non-empty value for `note_id` but received {note_id!r}")
        return self._get(
            path_template("/v3/enterprise/knowledge/notes/{note_id}", note_id=note_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )

    def update(
        self,
        note_id: str,
        *,
        body: str,
        name: str,
        trigger: str,
        pinned_repo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Update a note

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not note_id:
            raise ValueError(f"Expected a non-empty value for `note_id` but received {note_id!r}")
        return self._put(
            path_template("/v3/enterprise/knowledge/notes/{note_id}", note_id=note_id),
            body=maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "trigger": trigger,
                    "pinned_repo": pinned_repo,
                },
                note_update_params.NoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )

    def list(
        self,
        *,
        access_type: Optional[Literal["org", "enterprise"]] | Omit = omit,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        pinned_repo: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedKnowledgeNoteResponse:
        """
        List all notes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/knowledge/notes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "access_type": access_type,
                        "after": after,
                        "first": first,
                        "folder_path": folder_path,
                        "pinned_repo": pinned_repo,
                        "search": search,
                    },
                    note_list_params.NoteListParams,
                ),
            ),
            cast_to=PaginatedKnowledgeNoteResponse,
        )

    def delete(
        self,
        note_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Delete a note

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not note_id:
            raise ValueError(f"Expected a non-empty value for `note_id` but received {note_id!r}")
        return self._delete(
            path_template("/v3/enterprise/knowledge/notes/{note_id}", note_id=note_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )


class AsyncNotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncNotesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: str,
        name: str,
        trigger: str,
        pinned_repo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Create an enterprise-level note

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/enterprise/knowledge/notes",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "trigger": trigger,
                    "pinned_repo": pinned_repo,
                },
                note_create_params.NoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )

    async def retrieve(
        self,
        note_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Get a note by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not note_id:
            raise ValueError(f"Expected a non-empty value for `note_id` but received {note_id!r}")
        return await self._get(
            path_template("/v3/enterprise/knowledge/notes/{note_id}", note_id=note_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )

    async def update(
        self,
        note_id: str,
        *,
        body: str,
        name: str,
        trigger: str,
        pinned_repo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Update a note

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not note_id:
            raise ValueError(f"Expected a non-empty value for `note_id` but received {note_id!r}")
        return await self._put(
            path_template("/v3/enterprise/knowledge/notes/{note_id}", note_id=note_id),
            body=await async_maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "trigger": trigger,
                    "pinned_repo": pinned_repo,
                },
                note_update_params.NoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )

    async def list(
        self,
        *,
        access_type: Optional[Literal["org", "enterprise"]] | Omit = omit,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        pinned_repo: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedKnowledgeNoteResponse:
        """
        List all notes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/knowledge/notes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "access_type": access_type,
                        "after": after,
                        "first": first,
                        "folder_path": folder_path,
                        "pinned_repo": pinned_repo,
                        "search": search,
                    },
                    note_list_params.NoteListParams,
                ),
            ),
            cast_to=PaginatedKnowledgeNoteResponse,
        )

    async def delete(
        self,
        note_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeNote:
        """
        Delete a note

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not note_id:
            raise ValueError(f"Expected a non-empty value for `note_id` but received {note_id!r}")
        return await self._delete(
            path_template("/v3/enterprise/knowledge/notes/{note_id}", note_id=note_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeNote,
        )


class NotesResourceWithRawResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.create = to_raw_response_wrapper(
            notes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            notes.update,
        )
        self.list = to_raw_response_wrapper(
            notes.list,
        )
        self.delete = to_raw_response_wrapper(
            notes.delete,
        )


class AsyncNotesResourceWithRawResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.create = async_to_raw_response_wrapper(
            notes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            notes.update,
        )
        self.list = async_to_raw_response_wrapper(
            notes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notes.delete,
        )


class NotesResourceWithStreamingResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.create = to_streamed_response_wrapper(
            notes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            notes.update,
        )
        self.list = to_streamed_response_wrapper(
            notes.list,
        )
        self.delete = to_streamed_response_wrapper(
            notes.delete,
        )


class AsyncNotesResourceWithStreamingResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.create = async_to_streamed_response_wrapper(
            notes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            notes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            notes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notes.delete,
        )
