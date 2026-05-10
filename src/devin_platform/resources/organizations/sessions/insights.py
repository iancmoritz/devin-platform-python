# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

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
from ....types.organizations.sessions import insight_list_params
from ....types.enterprise.sessions.session_insights import SessionInsights
from ....types.enterprise.sessions.session_insights_generate import SessionInsightsGenerate
from ....types.enterprise.sessions.paginated_session_insights_response import PaginatedSessionInsightsResponse

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

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
    ) -> SessionInsights:
        """
        Get detailed insights for a specific session, including message counts, session
        size classification, and AI-generated analysis.

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
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}/insights", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionInsights,
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
    ) -> PaginatedSessionInsightsResponse:
        """
        List sessions with detailed insights including message counts, session size
        classification, and AI-generated analysis.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/sessions/insights", org_id=org_id),
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
                    insight_list_params.InsightListParams,
                ),
            ),
            cast_to=PaginatedSessionInsightsResponse,
        )

    def generate(
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
    ) -> SessionInsightsGenerate:
        """
        Trigger on-demand generation of session insights.

        Returns `already_exists` if insights have already been generated. Otherwise
        kicks off generation in the background. Poll the GET insights endpoint to
        retrieve results once generation completes.

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
            path_template(
                "/v3/organizations/{org_id}/sessions/{devin_id}/insights/generate", org_id=org_id, devin_id=devin_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionInsightsGenerate,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

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
    ) -> SessionInsights:
        """
        Get detailed insights for a specific session, including message counts, session
        size classification, and AI-generated analysis.

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
            path_template("/v3/organizations/{org_id}/sessions/{devin_id}/insights", org_id=org_id, devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionInsights,
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
    ) -> PaginatedSessionInsightsResponse:
        """
        List sessions with detailed insights including message counts, session size
        classification, and AI-generated analysis.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/sessions/insights", org_id=org_id),
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
                    insight_list_params.InsightListParams,
                ),
            ),
            cast_to=PaginatedSessionInsightsResponse,
        )

    async def generate(
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
    ) -> SessionInsightsGenerate:
        """
        Trigger on-demand generation of session insights.

        Returns `already_exists` if insights have already been generated. Otherwise
        kicks off generation in the background. Poll the GET insights endpoint to
        retrieve results once generation completes.

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
            path_template(
                "/v3/organizations/{org_id}/sessions/{devin_id}/insights/generate", org_id=org_id, devin_id=devin_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionInsightsGenerate,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.retrieve = to_raw_response_wrapper(
            insights.retrieve,
        )
        self.list = to_raw_response_wrapper(
            insights.list,
        )
        self.generate = to_raw_response_wrapper(
            insights.generate,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.retrieve = async_to_raw_response_wrapper(
            insights.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            insights.list,
        )
        self.generate = async_to_raw_response_wrapper(
            insights.generate,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.retrieve = to_streamed_response_wrapper(
            insights.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            insights.list,
        )
        self.generate = to_streamed_response_wrapper(
            insights.generate,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.retrieve = async_to_streamed_response_wrapper(
            insights.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            insights.list,
        )
        self.generate = async_to_streamed_response_wrapper(
            insights.generate,
        )
