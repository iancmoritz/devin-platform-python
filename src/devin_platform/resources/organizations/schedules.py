# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.organizations import schedule_list_params, schedule_create_params, schedule_update_params
from ...types.organizations.schedule import Schedule
from ...types.organizations.schedule_list_response import ScheduleListResponse

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return SchedulesResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        name: str,
        prompt: str,
        agent: Literal["devin", "data_analyst", "advanced"] | Omit = omit,
        bypass_approval: bool | Omit = omit,
        create_as_user_id: Optional[str] | Omit = omit,
        frequency: Optional[str] | Omit = omit,
        interval_count: int | Omit = omit,
        notify_on: Literal["always", "failure", "never"] | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        schedule_type: Literal["recurring", "one_time"] | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        slack_channel_id: Optional[str] | Omit = omit,
        slack_team_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_devin_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Create a new scheduled session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/v3/organizations/{org_id}/schedules", org_id=org_id),
            body=maybe_transform(
                {
                    "name": name,
                    "prompt": prompt,
                    "agent": agent,
                    "bypass_approval": bypass_approval,
                    "create_as_user_id": create_as_user_id,
                    "frequency": frequency,
                    "interval_count": interval_count,
                    "notify_on": notify_on,
                    "playbook_id": playbook_id,
                    "schedule_type": schedule_type,
                    "scheduled_at": scheduled_at,
                    "slack_channel_id": slack_channel_id,
                    "slack_team_id": slack_team_id,
                    "tags": tags,
                    "target_devin_id": target_devin_id,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )

    def retrieve(
        self,
        schedule_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Get a specific schedule by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/schedules/{schedule_id}", org_id=org_id, schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )

    def update(
        self,
        schedule_id: str,
        *,
        org_id: str,
        agent: Optional[Literal["devin", "data_analyst", "advanced"]] | Omit = omit,
        bypass_approval: Optional[bool] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        frequency: Optional[str] | Omit = omit,
        interval_count: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        notify_on: Optional[Literal["always", "failure", "never"]] | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        run_as_user_id: Optional[str] | Omit = omit,
        schedule_type: Optional[Literal["recurring", "one_time"]] | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        slack_channel_id: Optional[str] | Omit = omit,
        slack_team_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_devin_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Update an existing schedule.

        Args:
          run_as_user_id: Set the user ID that this schedule will run as. Requires ImpersonateOrgSessions
              permission. Setting to null reverts to the default bot user. Omitting the field
              leaves the current identity unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._patch(
            path_template("/v3/organizations/{org_id}/schedules/{schedule_id}", org_id=org_id, schedule_id=schedule_id),
            body=maybe_transform(
                {
                    "agent": agent,
                    "bypass_approval": bypass_approval,
                    "enabled": enabled,
                    "frequency": frequency,
                    "interval_count": interval_count,
                    "name": name,
                    "notify_on": notify_on,
                    "playbook_id": playbook_id,
                    "prompt": prompt,
                    "run_as_user_id": run_as_user_id,
                    "schedule_type": schedule_type,
                    "scheduled_at": scheduled_at,
                    "slack_channel_id": slack_channel_id,
                    "slack_team_id": slack_team_id,
                    "tags": tags,
                    "target_devin_id": target_devin_id,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )

    def list(
        self,
        org_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        List all schedules for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v3/organizations/{org_id}/schedules", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    def delete(
        self,
        schedule_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Soft delete a schedule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._delete(
            path_template("/v3/organizations/{org_id}/schedules/{schedule_id}", org_id=org_id, schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )


class AsyncSchedulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncSchedulesResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        name: str,
        prompt: str,
        agent: Literal["devin", "data_analyst", "advanced"] | Omit = omit,
        bypass_approval: bool | Omit = omit,
        create_as_user_id: Optional[str] | Omit = omit,
        frequency: Optional[str] | Omit = omit,
        interval_count: int | Omit = omit,
        notify_on: Literal["always", "failure", "never"] | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        schedule_type: Literal["recurring", "one_time"] | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        slack_channel_id: Optional[str] | Omit = omit,
        slack_team_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_devin_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Create a new scheduled session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/v3/organizations/{org_id}/schedules", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "prompt": prompt,
                    "agent": agent,
                    "bypass_approval": bypass_approval,
                    "create_as_user_id": create_as_user_id,
                    "frequency": frequency,
                    "interval_count": interval_count,
                    "notify_on": notify_on,
                    "playbook_id": playbook_id,
                    "schedule_type": schedule_type,
                    "scheduled_at": scheduled_at,
                    "slack_channel_id": slack_channel_id,
                    "slack_team_id": slack_team_id,
                    "tags": tags,
                    "target_devin_id": target_devin_id,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )

    async def retrieve(
        self,
        schedule_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Get a specific schedule by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/schedules/{schedule_id}", org_id=org_id, schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )

    async def update(
        self,
        schedule_id: str,
        *,
        org_id: str,
        agent: Optional[Literal["devin", "data_analyst", "advanced"]] | Omit = omit,
        bypass_approval: Optional[bool] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        frequency: Optional[str] | Omit = omit,
        interval_count: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        notify_on: Optional[Literal["always", "failure", "never"]] | Omit = omit,
        playbook_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        run_as_user_id: Optional[str] | Omit = omit,
        schedule_type: Optional[Literal["recurring", "one_time"]] | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        slack_channel_id: Optional[str] | Omit = omit,
        slack_team_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_devin_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Update an existing schedule.

        Args:
          run_as_user_id: Set the user ID that this schedule will run as. Requires ImpersonateOrgSessions
              permission. Setting to null reverts to the default bot user. Omitting the field
              leaves the current identity unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._patch(
            path_template("/v3/organizations/{org_id}/schedules/{schedule_id}", org_id=org_id, schedule_id=schedule_id),
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "bypass_approval": bypass_approval,
                    "enabled": enabled,
                    "frequency": frequency,
                    "interval_count": interval_count,
                    "name": name,
                    "notify_on": notify_on,
                    "playbook_id": playbook_id,
                    "prompt": prompt,
                    "run_as_user_id": run_as_user_id,
                    "schedule_type": schedule_type,
                    "scheduled_at": scheduled_at,
                    "slack_channel_id": slack_channel_id,
                    "slack_team_id": slack_team_id,
                    "tags": tags,
                    "target_devin_id": target_devin_id,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )

    async def list(
        self,
        org_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        List all schedules for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v3/organizations/{org_id}/schedules", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    async def delete(
        self,
        schedule_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Schedule:
        """
        Soft delete a schedule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._delete(
            path_template("/v3/organizations/{org_id}/schedules/{schedule_id}", org_id=org_id, schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Schedule,
        )


class SchedulesResourceWithRawResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.create = to_raw_response_wrapper(
            schedules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schedules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            schedules.update,
        )
        self.list = to_raw_response_wrapper(
            schedules.list,
        )
        self.delete = to_raw_response_wrapper(
            schedules.delete,
        )


class AsyncSchedulesResourceWithRawResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.create = async_to_raw_response_wrapper(
            schedules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schedules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            schedules.update,
        )
        self.list = async_to_raw_response_wrapper(
            schedules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schedules.delete,
        )


class SchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.create = to_streamed_response_wrapper(
            schedules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schedules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            schedules.update,
        )
        self.list = to_streamed_response_wrapper(
            schedules.list,
        )
        self.delete = to_streamed_response_wrapper(
            schedules.delete,
        )


class AsyncSchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.create = async_to_streamed_response_wrapper(
            schedules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schedules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            schedules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schedules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedules.delete,
        )
