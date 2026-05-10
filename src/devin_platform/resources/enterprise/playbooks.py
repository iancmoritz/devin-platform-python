# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.enterprise import playbook_list_params, playbook_create_params, playbook_update_params
from ...types.enterprise.playbook_response import PlaybookResponse
from ...types.enterprise.paginated_playbook_response import PaginatedPlaybookResponse

__all__ = ["PlaybooksResource", "AsyncPlaybooksResource"]


class PlaybooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlaybooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return PlaybooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaybooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return PlaybooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: str,
        title: str,
        macro: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """Create an enterprise-level playbook

        Args:
          macro: Playbook macro identifier.

        Must start with '!' followed by one or more letters,
              digits, underscores, or hyphens. Example: '!my_macro' or '!my-macro'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/enterprise/playbooks",
            body=maybe_transform(
                {
                    "body": body,
                    "title": title,
                    "macro": macro,
                },
                playbook_create_params.PlaybookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )

    def retrieve(
        self,
        playbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """
        Get a specific playbook by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playbook_id:
            raise ValueError(f"Expected a non-empty value for `playbook_id` but received {playbook_id!r}")
        return self._get(
            path_template("/v3/enterprise/playbooks/{playbook_id}", playbook_id=playbook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )

    def update(
        self,
        playbook_id: str,
        *,
        body: str,
        title: str,
        macro: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """Update a playbook

        Args:
          macro: Playbook macro identifier.

        Must start with '!' followed by one or more letters,
              digits, underscores, or hyphens. Example: '!my_macro' or '!my-macro'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playbook_id:
            raise ValueError(f"Expected a non-empty value for `playbook_id` but received {playbook_id!r}")
        return self._put(
            path_template("/v3/enterprise/playbooks/{playbook_id}", playbook_id=playbook_id),
            body=maybe_transform(
                {
                    "body": body,
                    "title": title,
                    "macro": macro,
                },
                playbook_update_params.PlaybookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedPlaybookResponse:
        """
        List all playbooks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/playbooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    playbook_list_params.PlaybookListParams,
                ),
            ),
            cast_to=PaginatedPlaybookResponse,
        )

    def delete(
        self,
        playbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """
        Delete a playbook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playbook_id:
            raise ValueError(f"Expected a non-empty value for `playbook_id` but received {playbook_id!r}")
        return self._delete(
            path_template("/v3/enterprise/playbooks/{playbook_id}", playbook_id=playbook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )


class AsyncPlaybooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlaybooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaybooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaybooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncPlaybooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: str,
        title: str,
        macro: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """Create an enterprise-level playbook

        Args:
          macro: Playbook macro identifier.

        Must start with '!' followed by one or more letters,
              digits, underscores, or hyphens. Example: '!my_macro' or '!my-macro'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/enterprise/playbooks",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "title": title,
                    "macro": macro,
                },
                playbook_create_params.PlaybookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )

    async def retrieve(
        self,
        playbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """
        Get a specific playbook by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playbook_id:
            raise ValueError(f"Expected a non-empty value for `playbook_id` but received {playbook_id!r}")
        return await self._get(
            path_template("/v3/enterprise/playbooks/{playbook_id}", playbook_id=playbook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )

    async def update(
        self,
        playbook_id: str,
        *,
        body: str,
        title: str,
        macro: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """Update a playbook

        Args:
          macro: Playbook macro identifier.

        Must start with '!' followed by one or more letters,
              digits, underscores, or hyphens. Example: '!my_macro' or '!my-macro'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playbook_id:
            raise ValueError(f"Expected a non-empty value for `playbook_id` but received {playbook_id!r}")
        return await self._put(
            path_template("/v3/enterprise/playbooks/{playbook_id}", playbook_id=playbook_id),
            body=await async_maybe_transform(
                {
                    "body": body,
                    "title": title,
                    "macro": macro,
                },
                playbook_update_params.PlaybookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )

    async def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedPlaybookResponse:
        """
        List all playbooks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/playbooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    playbook_list_params.PlaybookListParams,
                ),
            ),
            cast_to=PaginatedPlaybookResponse,
        )

    async def delete(
        self,
        playbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaybookResponse:
        """
        Delete a playbook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playbook_id:
            raise ValueError(f"Expected a non-empty value for `playbook_id` but received {playbook_id!r}")
        return await self._delete(
            path_template("/v3/enterprise/playbooks/{playbook_id}", playbook_id=playbook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaybookResponse,
        )


class PlaybooksResourceWithRawResponse:
    def __init__(self, playbooks: PlaybooksResource) -> None:
        self._playbooks = playbooks

        self.create = to_raw_response_wrapper(
            playbooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            playbooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            playbooks.update,
        )
        self.list = to_raw_response_wrapper(
            playbooks.list,
        )
        self.delete = to_raw_response_wrapper(
            playbooks.delete,
        )


class AsyncPlaybooksResourceWithRawResponse:
    def __init__(self, playbooks: AsyncPlaybooksResource) -> None:
        self._playbooks = playbooks

        self.create = async_to_raw_response_wrapper(
            playbooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            playbooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            playbooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            playbooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            playbooks.delete,
        )


class PlaybooksResourceWithStreamingResponse:
    def __init__(self, playbooks: PlaybooksResource) -> None:
        self._playbooks = playbooks

        self.create = to_streamed_response_wrapper(
            playbooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            playbooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            playbooks.update,
        )
        self.list = to_streamed_response_wrapper(
            playbooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            playbooks.delete,
        )


class AsyncPlaybooksResourceWithStreamingResponse:
    def __init__(self, playbooks: AsyncPlaybooksResource) -> None:
        self._playbooks = playbooks

        self.create = async_to_streamed_response_wrapper(
            playbooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            playbooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            playbooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            playbooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            playbooks.delete,
        )
