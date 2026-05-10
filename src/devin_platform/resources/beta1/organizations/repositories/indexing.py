# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

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
from .....types.beta1.organizations.repositories import (
    indexing_list_params,
    indexing_index_params,
    indexing_bulk_index_params,
    indexing_bulk_remove_params,
)
from .....types.beta1.organizations.repositories.repository_indexing import RepositoryIndexing
from .....types.beta1.organizations.repositories.repo_indexing_status import RepoIndexingStatus
from .....types.beta1.organizations.repositories.indexing_list_response import IndexingListResponse
from .....types.beta1.organizations.repositories.indexing_bulk_index_response import IndexingBulkIndexResponse
from .....types.beta1.organizations.repositories.indexing_bulk_remove_response import IndexingBulkRemoveResponse

__all__ = ["IndexingResource", "AsyncIndexingResource"]


class IndexingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndexingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return IndexingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return IndexingResourceWithStreamingResponse(self)

    def list(
        self,
        org_id: str,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingListResponse:
        """
        List indexed repositories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3beta1/organizations/{org_id}/repositories/indexing", org_id=org_id),
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
                    indexing_list_params.IndexingListParams,
                ),
            ),
            cast_to=IndexingListResponse,
        )

    def bulk_index(
        self,
        org_id: str,
        *,
        repositories: Iterable[indexing_bulk_index_params.Repository],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingBulkIndexResponse:
        """
        Idempotently enables indexing for a batch of repositories and triggers indexing
        jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._put(
            path_template("/v3beta1/organizations/{org_id}/repositories/indexing", org_id=org_id),
            body=maybe_transform({"repositories": repositories}, indexing_bulk_index_params.IndexingBulkIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingBulkIndexResponse,
        )

    def bulk_remove(
        self,
        org_id: str,
        *,
        repository_paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingBulkRemoveResponse:
        """
        Disables indexing and clears configured branches for a batch of repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._delete(
            path_template("/v3beta1/organizations/{org_id}/repositories/indexing", org_id=org_id),
            body=maybe_transform(
                {"repository_paths": repository_paths}, indexing_bulk_remove_params.IndexingBulkRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingBulkRemoveResponse,
        )

    def get_status(
        self,
        repository_path: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepoIndexingStatus:
        """
        Get indexing status for a repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        return self._get(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing",
                org_id=org_id,
                repository_path=repository_path,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoIndexingStatus,
        )

    def index(
        self,
        repository_path: str,
        *,
        org_id: str,
        branch_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryIndexing:
        """
        Idempotently enables indexing for a single repository and triggers indexing
        jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        return self._put(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing",
                org_id=org_id,
                repository_path=repository_path,
            ),
            body=maybe_transform({"branch_names": branch_names}, indexing_index_params.IndexingIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryIndexing,
        )

    def remove(
        self,
        repository_path: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryIndexing:
        """
        Disables indexing and clears configured branches for a single repository.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        return self._delete(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing",
                org_id=org_id,
                repository_path=repository_path,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryIndexing,
        )

    def remove_branch(
        self,
        branch_name: str,
        *,
        org_id: str,
        repository_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryIndexing:
        """
        Remove a branch from indexing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        if not branch_name:
            raise ValueError(f"Expected a non-empty value for `branch_name` but received {branch_name!r}")
        return self._delete(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing/branches/{branch_name}",
                org_id=org_id,
                repository_path=repository_path,
                branch_name=branch_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryIndexing,
        )


class AsyncIndexingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndexingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncIndexingResourceWithStreamingResponse(self)

    async def list(
        self,
        org_id: str,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingListResponse:
        """
        List indexed repositories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3beta1/organizations/{org_id}/repositories/indexing", org_id=org_id),
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
                    indexing_list_params.IndexingListParams,
                ),
            ),
            cast_to=IndexingListResponse,
        )

    async def bulk_index(
        self,
        org_id: str,
        *,
        repositories: Iterable[indexing_bulk_index_params.Repository],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingBulkIndexResponse:
        """
        Idempotently enables indexing for a batch of repositories and triggers indexing
        jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._put(
            path_template("/v3beta1/organizations/{org_id}/repositories/indexing", org_id=org_id),
            body=await async_maybe_transform(
                {"repositories": repositories}, indexing_bulk_index_params.IndexingBulkIndexParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingBulkIndexResponse,
        )

    async def bulk_remove(
        self,
        org_id: str,
        *,
        repository_paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingBulkRemoveResponse:
        """
        Disables indexing and clears configured branches for a batch of repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._delete(
            path_template("/v3beta1/organizations/{org_id}/repositories/indexing", org_id=org_id),
            body=await async_maybe_transform(
                {"repository_paths": repository_paths}, indexing_bulk_remove_params.IndexingBulkRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingBulkRemoveResponse,
        )

    async def get_status(
        self,
        repository_path: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepoIndexingStatus:
        """
        Get indexing status for a repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        return await self._get(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing",
                org_id=org_id,
                repository_path=repository_path,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoIndexingStatus,
        )

    async def index(
        self,
        repository_path: str,
        *,
        org_id: str,
        branch_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryIndexing:
        """
        Idempotently enables indexing for a single repository and triggers indexing
        jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        return await self._put(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing",
                org_id=org_id,
                repository_path=repository_path,
            ),
            body=await async_maybe_transform({"branch_names": branch_names}, indexing_index_params.IndexingIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryIndexing,
        )

    async def remove(
        self,
        repository_path: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryIndexing:
        """
        Disables indexing and clears configured branches for a single repository.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        return await self._delete(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing",
                org_id=org_id,
                repository_path=repository_path,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryIndexing,
        )

    async def remove_branch(
        self,
        branch_name: str,
        *,
        org_id: str,
        repository_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryIndexing:
        """
        Remove a branch from indexing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not repository_path:
            raise ValueError(f"Expected a non-empty value for `repository_path` but received {repository_path!r}")
        if not branch_name:
            raise ValueError(f"Expected a non-empty value for `branch_name` but received {branch_name!r}")
        return await self._delete(
            path_template(
                "/v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing/branches/{branch_name}",
                org_id=org_id,
                repository_path=repository_path,
                branch_name=branch_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryIndexing,
        )


class IndexingResourceWithRawResponse:
    def __init__(self, indexing: IndexingResource) -> None:
        self._indexing = indexing

        self.list = to_raw_response_wrapper(
            indexing.list,
        )
        self.bulk_index = to_raw_response_wrapper(
            indexing.bulk_index,
        )
        self.bulk_remove = to_raw_response_wrapper(
            indexing.bulk_remove,
        )
        self.get_status = to_raw_response_wrapper(
            indexing.get_status,
        )
        self.index = to_raw_response_wrapper(
            indexing.index,
        )
        self.remove = to_raw_response_wrapper(
            indexing.remove,
        )
        self.remove_branch = to_raw_response_wrapper(
            indexing.remove_branch,
        )


class AsyncIndexingResourceWithRawResponse:
    def __init__(self, indexing: AsyncIndexingResource) -> None:
        self._indexing = indexing

        self.list = async_to_raw_response_wrapper(
            indexing.list,
        )
        self.bulk_index = async_to_raw_response_wrapper(
            indexing.bulk_index,
        )
        self.bulk_remove = async_to_raw_response_wrapper(
            indexing.bulk_remove,
        )
        self.get_status = async_to_raw_response_wrapper(
            indexing.get_status,
        )
        self.index = async_to_raw_response_wrapper(
            indexing.index,
        )
        self.remove = async_to_raw_response_wrapper(
            indexing.remove,
        )
        self.remove_branch = async_to_raw_response_wrapper(
            indexing.remove_branch,
        )


class IndexingResourceWithStreamingResponse:
    def __init__(self, indexing: IndexingResource) -> None:
        self._indexing = indexing

        self.list = to_streamed_response_wrapper(
            indexing.list,
        )
        self.bulk_index = to_streamed_response_wrapper(
            indexing.bulk_index,
        )
        self.bulk_remove = to_streamed_response_wrapper(
            indexing.bulk_remove,
        )
        self.get_status = to_streamed_response_wrapper(
            indexing.get_status,
        )
        self.index = to_streamed_response_wrapper(
            indexing.index,
        )
        self.remove = to_streamed_response_wrapper(
            indexing.remove,
        )
        self.remove_branch = to_streamed_response_wrapper(
            indexing.remove_branch,
        )


class AsyncIndexingResourceWithStreamingResponse:
    def __init__(self, indexing: AsyncIndexingResource) -> None:
        self._indexing = indexing

        self.list = async_to_streamed_response_wrapper(
            indexing.list,
        )
        self.bulk_index = async_to_streamed_response_wrapper(
            indexing.bulk_index,
        )
        self.bulk_remove = async_to_streamed_response_wrapper(
            indexing.bulk_remove,
        )
        self.get_status = async_to_streamed_response_wrapper(
            indexing.get_status,
        )
        self.index = async_to_streamed_response_wrapper(
            indexing.index,
        )
        self.remove = async_to_streamed_response_wrapper(
            indexing.remove,
        )
        self.remove_branch = async_to_streamed_response_wrapper(
            indexing.remove_branch,
        )
