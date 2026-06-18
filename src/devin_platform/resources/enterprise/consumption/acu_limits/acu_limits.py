# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .devin.devin import (
    DevinResource,
    AsyncDevinResource,
    DevinResourceWithRawResponse,
    AsyncDevinResourceWithRawResponse,
    DevinResourceWithStreamingResponse,
    AsyncDevinResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AcuLimitsResource", "AsyncAcuLimitsResource"]


class AcuLimitsResource(SyncAPIResource):
    @cached_property
    def devin(self) -> DevinResource:
        return DevinResource(self._client)

    @cached_property
    def with_raw_response(self) -> AcuLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AcuLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AcuLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AcuLimitsResourceWithStreamingResponse(self)


class AsyncAcuLimitsResource(AsyncAPIResource):
    @cached_property
    def devin(self) -> AsyncDevinResource:
        return AsyncDevinResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAcuLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAcuLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAcuLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncAcuLimitsResourceWithStreamingResponse(self)


class AcuLimitsResourceWithRawResponse:
    def __init__(self, acu_limits: AcuLimitsResource) -> None:
        self._acu_limits = acu_limits

    @cached_property
    def devin(self) -> DevinResourceWithRawResponse:
        return DevinResourceWithRawResponse(self._acu_limits.devin)


class AsyncAcuLimitsResourceWithRawResponse:
    def __init__(self, acu_limits: AsyncAcuLimitsResource) -> None:
        self._acu_limits = acu_limits

    @cached_property
    def devin(self) -> AsyncDevinResourceWithRawResponse:
        return AsyncDevinResourceWithRawResponse(self._acu_limits.devin)


class AcuLimitsResourceWithStreamingResponse:
    def __init__(self, acu_limits: AcuLimitsResource) -> None:
        self._acu_limits = acu_limits

    @cached_property
    def devin(self) -> DevinResourceWithStreamingResponse:
        return DevinResourceWithStreamingResponse(self._acu_limits.devin)


class AsyncAcuLimitsResourceWithStreamingResponse:
    def __init__(self, acu_limits: AsyncAcuLimitsResource) -> None:
        self._acu_limits = acu_limits

    @cached_property
    def devin(self) -> AsyncDevinResourceWithStreamingResponse:
        return AsyncDevinResourceWithStreamingResponse(self._acu_limits.devin)
