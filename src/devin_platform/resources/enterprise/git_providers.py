# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.enterprise import git_provider_list_connections_params
from ...types.enterprise.git_provider_list_connections_response import GitProviderListConnectionsResponse

__all__ = ["GitProvidersResource", "AsyncGitProvidersResource"]


class GitProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return GitProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return GitProvidersResourceWithStreamingResponse(self)

    def list_connections(
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
    ) -> GitProviderListConnectionsResponse:
        """
        List Git Connections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/git-providers/connections",
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
                    git_provider_list_connections_params.GitProviderListConnectionsParams,
                ),
            ),
            cast_to=GitProviderListConnectionsResponse,
        )


class AsyncGitProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncGitProvidersResourceWithStreamingResponse(self)

    async def list_connections(
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
    ) -> GitProviderListConnectionsResponse:
        """
        List Git Connections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/git-providers/connections",
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
                    git_provider_list_connections_params.GitProviderListConnectionsParams,
                ),
            ),
            cast_to=GitProviderListConnectionsResponse,
        )


class GitProvidersResourceWithRawResponse:
    def __init__(self, git_providers: GitProvidersResource) -> None:
        self._git_providers = git_providers

        self.list_connections = to_raw_response_wrapper(
            git_providers.list_connections,
        )


class AsyncGitProvidersResourceWithRawResponse:
    def __init__(self, git_providers: AsyncGitProvidersResource) -> None:
        self._git_providers = git_providers

        self.list_connections = async_to_raw_response_wrapper(
            git_providers.list_connections,
        )


class GitProvidersResourceWithStreamingResponse:
    def __init__(self, git_providers: GitProvidersResource) -> None:
        self._git_providers = git_providers

        self.list_connections = to_streamed_response_wrapper(
            git_providers.list_connections,
        )


class AsyncGitProvidersResourceWithStreamingResponse:
    def __init__(self, git_providers: AsyncGitProvidersResource) -> None:
        self._git_providers = git_providers

        self.list_connections = async_to_streamed_response_wrapper(
            git_providers.list_connections,
        )
