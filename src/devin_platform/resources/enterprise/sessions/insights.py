# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.enterprise.sessions import insight_list_params, insight_generate_params
from ....types.enterprise.sessions.session_insights import SessionInsights
from ....types.enterprise.sessions.session_insights_generate import SessionInsightsGenerate

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

    def list(
        self,
        devin_id: str,
        *,
        org_id: Optional[str] | Omit = omit,
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
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return self._get(
            path_template("/v3/enterprise/sessions/{devin_id}/insights", devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"org_id": org_id}, insight_list_params.InsightListParams),
            ),
            cast_to=SessionInsights,
        )

    def generate(
        self,
        devin_id: str,
        *,
        org_id: Optional[str] | Omit = omit,
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
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return self._post(
            path_template("/v3/enterprise/sessions/{devin_id}/insights/generate", devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"org_id": org_id}, insight_generate_params.InsightGenerateParams),
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

    async def list(
        self,
        devin_id: str,
        *,
        org_id: Optional[str] | Omit = omit,
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
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return await self._get(
            path_template("/v3/enterprise/sessions/{devin_id}/insights", devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"org_id": org_id}, insight_list_params.InsightListParams),
            ),
            cast_to=SessionInsights,
        )

    async def generate(
        self,
        devin_id: str,
        *,
        org_id: Optional[str] | Omit = omit,
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
        if not devin_id:
            raise ValueError(f"Expected a non-empty value for `devin_id` but received {devin_id!r}")
        return await self._post(
            path_template("/v3/enterprise/sessions/{devin_id}/insights/generate", devin_id=devin_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"org_id": org_id}, insight_generate_params.InsightGenerateParams),
            ),
            cast_to=SessionInsightsGenerate,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.list = to_raw_response_wrapper(
            insights.list,
        )
        self.generate = to_raw_response_wrapper(
            insights.generate,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.list = async_to_raw_response_wrapper(
            insights.list,
        )
        self.generate = async_to_raw_response_wrapper(
            insights.generate,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.list = to_streamed_response_wrapper(
            insights.list,
        )
        self.generate = to_streamed_response_wrapper(
            insights.generate,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.list = async_to_streamed_response_wrapper(
            insights.list,
        )
        self.generate = async_to_streamed_response_wrapper(
            insights.generate,
        )
