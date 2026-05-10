# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.organizations import session_list_params, session_create_params, session_terminate_params
from ....types.enterprise.session_response import SessionResponse
from ....types.enterprise.paginated_session_response import PaginatedSessionResponse
from ....types.organizations.session_list_attachments_response import SessionListAttachmentsResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        prompt: str,
        advanced_mode: Optional[Literal["analyze", "create", "improve", "batch", "manage"]] | Omit = omit,
        attachment_urls: Optional[SequenceNotStr[str]] | Omit = omit,
        bypass_approval: Optional[bool] | Omit = omit,
        child_playbook_id: Optional[str] | Omit = omit,
        create_as_user_id: Optional[str] | Omit = omit,
        knowledge_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        max_acu_limit: Optional[int] | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        repos: Optional[SequenceNotStr[str]] | Omit = omit,
        secret_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        session_links: Optional[SequenceNotStr[str]] | Omit = omit,
        session_secrets: Optional[Iterable[session_create_params.SessionSecret]] | Omit = omit,
        structured_output_schema: Optional[Dict[str, object]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Create a new session

        Args:
          structured_output_schema: JSON Schema (Draft 7) for validating structured output. Max 64KB. Must be
              self-contained (no external $ref).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/v3/organizations/{org_id}/sessions", org_id=org_id),
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "advanced_mode": advanced_mode,
                    "attachment_urls": attachment_urls,
                    "bypass_approval": bypass_approval,
                    "child_playbook_id": child_playbook_id,
                    "create_as_user_id": create_as_user_id,
                    "knowledge_ids": knowledge_ids,
                    "max_acu_limit": max_acu_limit,
                    "playbook_id": playbook_id,
                    "repos": repos,
                    "secret_ids": secret_ids,
                    "session_links": session_links,
                    "session_secrets": session_secrets,
                    "structured_output_schema": structured_output_schema,
                    "tags": tags,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionResponse,
        )

    def retrieve(
        self,
        devin_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Get details of a specific session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionResponse,
        )

    def list(
        self,
        org_id: str,
        *,
        after: Optional[str] | Omit = omit,
        created_after: Optional[int] | Omit = omit,
        created_before: Optional[int] | Omit = omit,
        first: int | Omit = omit,
        origins: Optional[
            List[Literal["webapp", "slack", "teams", "api", "linear", "jira", "scheduled", "cli", "other"]]
        ]
        | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        schedule_id: Optional[str] | Omit = omit,
        service_user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        session_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        updated_after: Optional[int] | Omit = omit,
        updated_before: Optional[int] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedSessionResponse:
        """
        List sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/sessions", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "origins": origins,
                        "playbook_id": playbook_id,
                        "schedule_id": schedule_id,
                        "service_user_ids": service_user_ids,
                        "session_ids": session_ids,
                        "tags": tags,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "user_ids": user_ids,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=PaginatedSessionResponse,
        )

    def archive(
        self,
        devin_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Archive session and put it to sleep if currently running

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return self._post(
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}/archive", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionResponse,
        )

    def list_attachments(
        self,
        devin_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListAttachmentsResponse:
        """
        List all attachments for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return self._get(
            path_template(
                "/v3/organizations/{org_id}/sessions/{devin_id}/attachments", org_id=org_id, devin_id=devin_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionListAttachmentsResponse,
        )

    def terminate(
        self,
        devin_id: str,
        *,
        org_id: str,
        archive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Terminate session

        Args:
          archive: Whether to archive the devin session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return self._delete(
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archive": archive}, session_terminate_params.SessionTerminateParams),
            ),
            cast_to=SessionResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        prompt: str,
        advanced_mode: Optional[Literal["analyze", "create", "improve", "batch", "manage"]] | Omit = omit,
        attachment_urls: Optional[SequenceNotStr[str]] | Omit = omit,
        bypass_approval: Optional[bool] | Omit = omit,
        child_playbook_id: Optional[str] | Omit = omit,
        create_as_user_id: Optional[str] | Omit = omit,
        knowledge_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        max_acu_limit: Optional[int] | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        repos: Optional[SequenceNotStr[str]] | Omit = omit,
        secret_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        session_links: Optional[SequenceNotStr[str]] | Omit = omit,
        session_secrets: Optional[Iterable[session_create_params.SessionSecret]] | Omit = omit,
        structured_output_schema: Optional[Dict[str, object]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Create a new session

        Args:
          structured_output_schema: JSON Schema (Draft 7) for validating structured output. Max 64KB. Must be
              self-contained (no external $ref).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/v3/organizations/{org_id}/sessions", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "advanced_mode": advanced_mode,
                    "attachment_urls": attachment_urls,
                    "bypass_approval": bypass_approval,
                    "child_playbook_id": child_playbook_id,
                    "create_as_user_id": create_as_user_id,
                    "knowledge_ids": knowledge_ids,
                    "max_acu_limit": max_acu_limit,
                    "playbook_id": playbook_id,
                    "repos": repos,
                    "secret_ids": secret_ids,
                    "session_links": session_links,
                    "session_secrets": session_secrets,
                    "structured_output_schema": structured_output_schema,
                    "tags": tags,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionResponse,
        )

    async def retrieve(
        self,
        devin_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Get details of a specific session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionResponse,
        )

    async def list(
        self,
        org_id: str,
        *,
        after: Optional[str] | Omit = omit,
        created_after: Optional[int] | Omit = omit,
        created_before: Optional[int] | Omit = omit,
        first: int | Omit = omit,
        origins: Optional[
            List[Literal["webapp", "slack", "teams", "api", "linear", "jira", "scheduled", "cli", "other"]]
        ]
        | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        schedule_id: Optional[str] | Omit = omit,
        service_user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        session_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        updated_after: Optional[int] | Omit = omit,
        updated_before: Optional[int] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedSessionResponse:
        """
        List sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/sessions", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "origins": origins,
                        "playbook_id": playbook_id,
                        "schedule_id": schedule_id,
                        "service_user_ids": service_user_ids,
                        "session_ids": session_ids,
                        "tags": tags,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "user_ids": user_ids,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=PaginatedSessionResponse,
        )

    async def archive(
        self,
        devin_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Archive session and put it to sleep if currently running

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return await self._post(
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}/archive", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionResponse,
        )

    async def list_attachments(
        self,
        devin_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListAttachmentsResponse:
        """
        List all attachments for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return await self._get(
            path_template(
                "/v3/organizations/{org_id}/sessions/{devin_id}/attachments", org_id=org_id, devin_id=devin_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionListAttachmentsResponse,
        )

    async def terminate(
        self,
        devin_id: str,
        *,
        org_id: str,
        archive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionResponse:
        """
        Terminate session

        Args:
          archive: Whether to archive the devin session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return await self._delete(
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archive": archive}, session_terminate_params.SessionTerminateParams
                ),
            ),
            cast_to=SessionResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.archive = to_raw_response_wrapper(
            sessions.archive,
        )
        self.list_attachments = to_raw_response_wrapper(
            sessions.list_attachments,
        )
        self.terminate = to_raw_response_wrapper(
            sessions.terminate,
        )

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._sessions.insights)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._sessions.messages)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._sessions.tags)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.archive = async_to_raw_response_wrapper(
            sessions.archive,
        )
        self.list_attachments = async_to_raw_response_wrapper(
            sessions.list_attachments,
        )
        self.terminate = async_to_raw_response_wrapper(
            sessions.terminate,
        )

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._sessions.insights)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._sessions.messages)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._sessions.tags)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.archive = to_streamed_response_wrapper(
            sessions.archive,
        )
        self.list_attachments = to_streamed_response_wrapper(
            sessions.list_attachments,
        )
        self.terminate = to_streamed_response_wrapper(
            sessions.terminate,
        )

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._sessions.insights)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._sessions.messages)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._sessions.tags)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            sessions.archive,
        )
        self.list_attachments = async_to_streamed_response_wrapper(
            sessions.list_attachments,
        )
        self.terminate = async_to_streamed_response_wrapper(
            sessions.terminate,
        )

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._sessions.insights)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._sessions.messages)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._sessions.tags)
