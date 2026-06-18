# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.enterprise import org_group_limit_update_org_group_config_params
from ...types.enterprise.org_groups_config import OrgGroupsConfig

__all__ = ["OrgGroupLimitsResource", "AsyncOrgGroupLimitsResource"]


class OrgGroupLimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgGroupLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return OrgGroupLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgGroupLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return OrgGroupLimitsResourceWithStreamingResponse(self)

    def get_org_group_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgGroupsConfig:
        """Get the current organization groups configuration."""
        return self._get(
            "/v3/enterprise/org-group-limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgGroupsConfig,
        )

    def update_org_group_config(
        self,
        *,
        groups: Dict[str, org_group_limit_update_org_group_config_params.Groups],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgGroupsConfig:
        """
        Update the organization groups configuration.

        This endpoint replaces the entire org groups configuration with the provided
        config.

        - Groups not in the request will be deleted
        - Groups in the request will be created or updated to match the config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v3/enterprise/org-group-limits",
            body=maybe_transform(
                {"groups": groups},
                org_group_limit_update_org_group_config_params.OrgGroupLimitUpdateOrgGroupConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgGroupsConfig,
        )


class AsyncOrgGroupLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgGroupLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgGroupLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgGroupLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncOrgGroupLimitsResourceWithStreamingResponse(self)

    async def get_org_group_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgGroupsConfig:
        """Get the current organization groups configuration."""
        return await self._get(
            "/v3/enterprise/org-group-limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgGroupsConfig,
        )

    async def update_org_group_config(
        self,
        *,
        groups: Dict[str, org_group_limit_update_org_group_config_params.Groups],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgGroupsConfig:
        """
        Update the organization groups configuration.

        This endpoint replaces the entire org groups configuration with the provided
        config.

        - Groups not in the request will be deleted
        - Groups in the request will be created or updated to match the config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v3/enterprise/org-group-limits",
            body=await async_maybe_transform(
                {"groups": groups},
                org_group_limit_update_org_group_config_params.OrgGroupLimitUpdateOrgGroupConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgGroupsConfig,
        )


class OrgGroupLimitsResourceWithRawResponse:
    def __init__(self, org_group_limits: OrgGroupLimitsResource) -> None:
        self._org_group_limits = org_group_limits

        self.get_org_group_config = to_raw_response_wrapper(
            org_group_limits.get_org_group_config,
        )
        self.update_org_group_config = to_raw_response_wrapper(
            org_group_limits.update_org_group_config,
        )


class AsyncOrgGroupLimitsResourceWithRawResponse:
    def __init__(self, org_group_limits: AsyncOrgGroupLimitsResource) -> None:
        self._org_group_limits = org_group_limits

        self.get_org_group_config = async_to_raw_response_wrapper(
            org_group_limits.get_org_group_config,
        )
        self.update_org_group_config = async_to_raw_response_wrapper(
            org_group_limits.update_org_group_config,
        )


class OrgGroupLimitsResourceWithStreamingResponse:
    def __init__(self, org_group_limits: OrgGroupLimitsResource) -> None:
        self._org_group_limits = org_group_limits

        self.get_org_group_config = to_streamed_response_wrapper(
            org_group_limits.get_org_group_config,
        )
        self.update_org_group_config = to_streamed_response_wrapper(
            org_group_limits.update_org_group_config,
        )


class AsyncOrgGroupLimitsResourceWithStreamingResponse:
    def __init__(self, org_group_limits: AsyncOrgGroupLimitsResource) -> None:
        self._org_group_limits = org_group_limits

        self.get_org_group_config = async_to_streamed_response_wrapper(
            org_group_limits.get_org_group_config,
        )
        self.update_org_group_config = async_to_streamed_response_wrapper(
            org_group_limits.update_org_group_config,
        )
