# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .daily import (
    DailyResource,
    AsyncDailyResource,
    DailyResourceWithRawResponse,
    AsyncDailyResourceWithRawResponse,
    DailyResourceWithStreamingResponse,
    AsyncDailyResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.enterprise import consumption_list_consumption_cycles_params
from .acu_limits.acu_limits import (
    AcuLimitsResource,
    AsyncAcuLimitsResource,
    AcuLimitsResourceWithRawResponse,
    AsyncAcuLimitsResourceWithRawResponse,
    AcuLimitsResourceWithStreamingResponse,
    AsyncAcuLimitsResourceWithStreamingResponse,
)
from ....types.enterprise.consumption_list_consumption_cycles_response import ConsumptionListConsumptionCyclesResponse

__all__ = ["ConsumptionResource", "AsyncConsumptionResource"]


class ConsumptionResource(SyncAPIResource):
    @cached_property
    def acu_limits(self) -> AcuLimitsResource:
        return AcuLimitsResource(self._client)

    @cached_property
    def daily(self) -> DailyResource:
        return DailyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConsumptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return ConsumptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return ConsumptionResourceWithStreamingResponse(self)

    def list_consumption_cycles(
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
    ) -> ConsumptionListConsumptionCyclesResponse:
        """
        List Consumption Cycles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/consumption/cycles",
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
                    consumption_list_consumption_cycles_params.ConsumptionListConsumptionCyclesParams,
                ),
            ),
            cast_to=ConsumptionListConsumptionCyclesResponse,
        )


class AsyncConsumptionResource(AsyncAPIResource):
    @cached_property
    def acu_limits(self) -> AsyncAcuLimitsResource:
        return AsyncAcuLimitsResource(self._client)

    @cached_property
    def daily(self) -> AsyncDailyResource:
        return AsyncDailyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConsumptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsumptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncConsumptionResourceWithStreamingResponse(self)

    async def list_consumption_cycles(
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
    ) -> ConsumptionListConsumptionCyclesResponse:
        """
        List Consumption Cycles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/consumption/cycles",
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
                    consumption_list_consumption_cycles_params.ConsumptionListConsumptionCyclesParams,
                ),
            ),
            cast_to=ConsumptionListConsumptionCyclesResponse,
        )


class ConsumptionResourceWithRawResponse:
    def __init__(self, consumption: ConsumptionResource) -> None:
        self._consumption = consumption

        self.list_consumption_cycles = to_raw_response_wrapper(
            consumption.list_consumption_cycles,
        )

    @cached_property
    def acu_limits(self) -> AcuLimitsResourceWithRawResponse:
        return AcuLimitsResourceWithRawResponse(self._consumption.acu_limits)

    @cached_property
    def daily(self) -> DailyResourceWithRawResponse:
        return DailyResourceWithRawResponse(self._consumption.daily)


class AsyncConsumptionResourceWithRawResponse:
    def __init__(self, consumption: AsyncConsumptionResource) -> None:
        self._consumption = consumption

        self.list_consumption_cycles = async_to_raw_response_wrapper(
            consumption.list_consumption_cycles,
        )

    @cached_property
    def acu_limits(self) -> AsyncAcuLimitsResourceWithRawResponse:
        return AsyncAcuLimitsResourceWithRawResponse(self._consumption.acu_limits)

    @cached_property
    def daily(self) -> AsyncDailyResourceWithRawResponse:
        return AsyncDailyResourceWithRawResponse(self._consumption.daily)


class ConsumptionResourceWithStreamingResponse:
    def __init__(self, consumption: ConsumptionResource) -> None:
        self._consumption = consumption

        self.list_consumption_cycles = to_streamed_response_wrapper(
            consumption.list_consumption_cycles,
        )

    @cached_property
    def acu_limits(self) -> AcuLimitsResourceWithStreamingResponse:
        return AcuLimitsResourceWithStreamingResponse(self._consumption.acu_limits)

    @cached_property
    def daily(self) -> DailyResourceWithStreamingResponse:
        return DailyResourceWithStreamingResponse(self._consumption.daily)


class AsyncConsumptionResourceWithStreamingResponse:
    def __init__(self, consumption: AsyncConsumptionResource) -> None:
        self._consumption = consumption

        self.list_consumption_cycles = async_to_streamed_response_wrapper(
            consumption.list_consumption_cycles,
        )

    @cached_property
    def acu_limits(self) -> AsyncAcuLimitsResourceWithStreamingResponse:
        return AsyncAcuLimitsResourceWithStreamingResponse(self._consumption.acu_limits)

    @cached_property
    def daily(self) -> AsyncDailyResourceWithStreamingResponse:
        return AsyncDailyResourceWithStreamingResponse(self._consumption.daily)
