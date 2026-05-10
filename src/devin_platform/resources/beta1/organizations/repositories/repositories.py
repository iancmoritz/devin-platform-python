# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .indexing import (
    IndexingResource,
    AsyncIndexingResource,
    IndexingResourceWithRawResponse,
    AsyncIndexingResourceWithRawResponse,
    IndexingResourceWithStreamingResponse,
    AsyncIndexingResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.beta1.organizations import repository_list_params
from .....types.beta1.organizations.repository_list_response import RepositoryListResponse

__all__ = ["RepositoriesResource", "AsyncRepositoriesResource"]


class RepositoriesResource(SyncAPIResource):
    @cached_property
    def indexing(self) -> IndexingResource:
        return IndexingResource(self._client)

    @cached_property
    def with_raw_response(self) -> RepositoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return RepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RepositoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return RepositoriesResourceWithStreamingResponse(self)

    def list(
        self,
        org_id: str,
        *,
        after: Optional[str] | Omit = omit,
        exclude_repo_paths: Optional[SequenceNotStr[str]] | Omit = omit,
        filter_name: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        load_indexing_status: bool | Omit = omit,
        only_repo_paths: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryListResponse:
        """
        List repositories available to an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3beta1/organizations/{org_id}/repositories", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "exclude_repo_paths": exclude_repo_paths,
                        "filter_name": filter_name,
                        "first": first,
                        "load_indexing_status": load_indexing_status,
                        "only_repo_paths": only_repo_paths,
                    },
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )


class AsyncRepositoriesResource(AsyncAPIResource):
    @cached_property
    def indexing(self) -> AsyncIndexingResource:
        return AsyncIndexingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRepositoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncRepositoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        org_id: str,
        *,
        after: Optional[str] | Omit = omit,
        exclude_repo_paths: Optional[SequenceNotStr[str]] | Omit = omit,
        filter_name: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        load_indexing_status: bool | Omit = omit,
        only_repo_paths: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryListResponse:
        """
        List repositories available to an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3beta1/organizations/{org_id}/repositories", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "exclude_repo_paths": exclude_repo_paths,
                        "filter_name": filter_name,
                        "first": first,
                        "load_indexing_status": load_indexing_status,
                        "only_repo_paths": only_repo_paths,
                    },
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )


class RepositoriesResourceWithRawResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_raw_response_wrapper(
            repositories.list,
        )

    @cached_property
    def indexing(self) -> IndexingResourceWithRawResponse:
        return IndexingResourceWithRawResponse(self._repositories.indexing)


class AsyncRepositoriesResourceWithRawResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_raw_response_wrapper(
            repositories.list,
        )

    @cached_property
    def indexing(self) -> AsyncIndexingResourceWithRawResponse:
        return AsyncIndexingResourceWithRawResponse(self._repositories.indexing)


class RepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_streamed_response_wrapper(
            repositories.list,
        )

    @cached_property
    def indexing(self) -> IndexingResourceWithStreamingResponse:
        return IndexingResourceWithStreamingResponse(self._repositories.indexing)


class AsyncRepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_streamed_response_wrapper(
            repositories.list,
        )

    @cached_property
    def indexing(self) -> AsyncIndexingResourceWithStreamingResponse:
        return AsyncIndexingResourceWithStreamingResponse(self._repositories.indexing)
