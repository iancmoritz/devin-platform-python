# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import (
    AuditLogAction,
    enterprise_list_roles_params,
    enterprise_list_audit_logs_params,
    enterprise_list_hypervisors_params,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .playbooks import (
    PlaybooksResource,
    AsyncPlaybooksResource,
    PlaybooksResourceWithRawResponse,
    AsyncPlaybooksResourceWithRawResponse,
    PlaybooksResourceWithStreamingResponse,
    AsyncPlaybooksResourceWithStreamingResponse,
)
from .idp_groups import (
    IdpGroupsResource,
    AsyncIdpGroupsResource,
    IdpGroupsResourceWithRawResponse,
    AsyncIdpGroupsResourceWithRawResponse,
    IdpGroupsResourceWithStreamingResponse,
    AsyncIdpGroupsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .git_providers import (
    GitProvidersResource,
    AsyncGitProvidersResource,
    GitProvidersResourceWithRawResponse,
    AsyncGitProvidersResourceWithRawResponse,
    GitProvidersResourceWithStreamingResponse,
    AsyncGitProvidersResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .ip_access_list import (
    IPAccessListResource,
    AsyncIPAccessListResource,
    IPAccessListResourceWithRawResponse,
    AsyncIPAccessListResourceWithRawResponse,
    IPAccessListResourceWithStreamingResponse,
    AsyncIPAccessListResourceWithStreamingResponse,
)
from .members.members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from .org_group_limits import (
    OrgGroupLimitsResource,
    AsyncOrgGroupLimitsResource,
    OrgGroupLimitsResourceWithRawResponse,
    AsyncOrgGroupLimitsResourceWithRawResponse,
    OrgGroupLimitsResourceWithStreamingResponse,
    AsyncOrgGroupLimitsResourceWithStreamingResponse,
)
from .sessions.sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from .knowledge.knowledge import (
    KnowledgeResource,
    AsyncKnowledgeResource,
    KnowledgeResourceWithRawResponse,
    AsyncKnowledgeResourceWithRawResponse,
    KnowledgeResourceWithStreamingResponse,
    AsyncKnowledgeResourceWithStreamingResponse,
)
from .consumption.consumption import (
    ConsumptionResource,
    AsyncConsumptionResource,
    ConsumptionResourceWithRawResponse,
    AsyncConsumptionResourceWithRawResponse,
    ConsumptionResourceWithStreamingResponse,
    AsyncConsumptionResourceWithStreamingResponse,
)
from ...types.audit_log_action import AuditLogAction
from .organizations.organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ...types.paginated_audit_log_response import PaginatedAuditLogResponse
from ...types.enterprise_list_roles_response import EnterpriseListRolesResponse
from ...types.enterprise_get_queue_status_response import EnterpriseGetQueueStatusResponse
from ...types.enterprise_list_hypervisors_response import EnterpriseListHypervisorsResponse

__all__ = ["EnterpriseResource", "AsyncEnterpriseResource"]


class EnterpriseResource(SyncAPIResource):
    @cached_property
    def consumption(self) -> ConsumptionResource:
        return ConsumptionResource(self._client)

    @cached_property
    def git_providers(self) -> GitProvidersResource:
        return GitProvidersResource(self._client)

    @cached_property
    def idp_groups(self) -> IdpGroupsResource:
        return IdpGroupsResource(self._client)

    @cached_property
    def ip_access_list(self) -> IPAccessListResource:
        return IPAccessListResource(self._client)

    @cached_property
    def knowledge(self) -> KnowledgeResource:
        return KnowledgeResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def org_group_limits(self) -> OrgGroupLimitsResource:
        return OrgGroupLimitsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def playbooks(self) -> PlaybooksResource:
        return PlaybooksResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnterpriseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return EnterpriseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnterpriseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return EnterpriseResourceWithStreamingResponse(self)

    def get_queue_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseGetQueueStatusResponse:
        """
        Get the queue status for an enterprise.

        Returns the total number of queued sessions (status: new, resuming, claimed) and
        a status indicator (normal/elevated/high).

        This endpoint is useful for enterprise admins to monitor queue health and set up
        alerts for capacity issues.
        """
        return self._get(
            "/v3/enterprise/queue",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseGetQueueStatusResponse,
        )

    def list_audit_logs(
        self,
        *,
        action: Optional[AuditLogAction] | Omit = omit,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedAuditLogResponse:
        """
        List audit logs for the enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/audit-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "after": after,
                        "first": first,
                        "order": order,
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    enterprise_list_audit_logs_params.EnterpriseListAuditLogsParams,
                ),
            ),
            cast_to=PaginatedAuditLogResponse,
        )

    def list_hypervisors(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        status: Literal["available", "restarting", "disconnected", "terminated", "draining", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseListHypervisorsResponse:
        """
        List Hypervisors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/hypervisors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                        "status": status,
                    },
                    enterprise_list_hypervisors_params.EnterpriseListHypervisorsParams,
                ),
            ),
            cast_to=EnterpriseListHypervisorsResponse,
        )

    def list_roles(
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
    ) -> EnterpriseListRolesResponse:
        """
        Get roles for this enterprise

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/enterprise/roles",
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
                    enterprise_list_roles_params.EnterpriseListRolesParams,
                ),
            ),
            cast_to=EnterpriseListRolesResponse,
        )


class AsyncEnterpriseResource(AsyncAPIResource):
    @cached_property
    def consumption(self) -> AsyncConsumptionResource:
        return AsyncConsumptionResource(self._client)

    @cached_property
    def git_providers(self) -> AsyncGitProvidersResource:
        return AsyncGitProvidersResource(self._client)

    @cached_property
    def idp_groups(self) -> AsyncIdpGroupsResource:
        return AsyncIdpGroupsResource(self._client)

    @cached_property
    def ip_access_list(self) -> AsyncIPAccessListResource:
        return AsyncIPAccessListResource(self._client)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResource:
        return AsyncKnowledgeResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def org_group_limits(self) -> AsyncOrgGroupLimitsResource:
        return AsyncOrgGroupLimitsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def playbooks(self) -> AsyncPlaybooksResource:
        return AsyncPlaybooksResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnterpriseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnterpriseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnterpriseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncEnterpriseResourceWithStreamingResponse(self)

    async def get_queue_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseGetQueueStatusResponse:
        """
        Get the queue status for an enterprise.

        Returns the total number of queued sessions (status: new, resuming, claimed) and
        a status indicator (normal/elevated/high).

        This endpoint is useful for enterprise admins to monitor queue health and set up
        alerts for capacity issues.
        """
        return await self._get(
            "/v3/enterprise/queue",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseGetQueueStatusResponse,
        )

    async def list_audit_logs(
        self,
        *,
        action: Optional[AuditLogAction] | Omit = omit,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        time_after: Optional[int] | Omit = omit,
        time_before: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedAuditLogResponse:
        """
        List audit logs for the enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/audit-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "action": action,
                        "after": after,
                        "first": first,
                        "order": order,
                        "time_after": time_after,
                        "time_before": time_before,
                    },
                    enterprise_list_audit_logs_params.EnterpriseListAuditLogsParams,
                ),
            ),
            cast_to=PaginatedAuditLogResponse,
        )

    async def list_hypervisors(
        self,
        *,
        after: Optional[str] | Omit = omit,
        first: int | Omit = omit,
        status: Literal["available", "restarting", "disconnected", "terminated", "draining", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseListHypervisorsResponse:
        """
        List Hypervisors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/hypervisors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "first": first,
                        "status": status,
                    },
                    enterprise_list_hypervisors_params.EnterpriseListHypervisorsParams,
                ),
            ),
            cast_to=EnterpriseListHypervisorsResponse,
        )

    async def list_roles(
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
    ) -> EnterpriseListRolesResponse:
        """
        Get roles for this enterprise

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/enterprise/roles",
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
                    enterprise_list_roles_params.EnterpriseListRolesParams,
                ),
            ),
            cast_to=EnterpriseListRolesResponse,
        )


class EnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

        self.get_queue_status = to_raw_response_wrapper(
            enterprise.get_queue_status,
        )
        self.list_audit_logs = to_raw_response_wrapper(
            enterprise.list_audit_logs,
        )
        self.list_hypervisors = to_raw_response_wrapper(
            enterprise.list_hypervisors,
        )
        self.list_roles = to_raw_response_wrapper(
            enterprise.list_roles,
        )

    @cached_property
    def consumption(self) -> ConsumptionResourceWithRawResponse:
        return ConsumptionResourceWithRawResponse(self._enterprise.consumption)

    @cached_property
    def git_providers(self) -> GitProvidersResourceWithRawResponse:
        return GitProvidersResourceWithRawResponse(self._enterprise.git_providers)

    @cached_property
    def idp_groups(self) -> IdpGroupsResourceWithRawResponse:
        return IdpGroupsResourceWithRawResponse(self._enterprise.idp_groups)

    @cached_property
    def ip_access_list(self) -> IPAccessListResourceWithRawResponse:
        return IPAccessListResourceWithRawResponse(self._enterprise.ip_access_list)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithRawResponse:
        return KnowledgeResourceWithRawResponse(self._enterprise.knowledge)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._enterprise.members)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._enterprise.metrics)

    @cached_property
    def org_group_limits(self) -> OrgGroupLimitsResourceWithRawResponse:
        return OrgGroupLimitsResourceWithRawResponse(self._enterprise.org_group_limits)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._enterprise.organizations)

    @cached_property
    def playbooks(self) -> PlaybooksResourceWithRawResponse:
        return PlaybooksResourceWithRawResponse(self._enterprise.playbooks)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._enterprise.sessions)


class AsyncEnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

        self.get_queue_status = async_to_raw_response_wrapper(
            enterprise.get_queue_status,
        )
        self.list_audit_logs = async_to_raw_response_wrapper(
            enterprise.list_audit_logs,
        )
        self.list_hypervisors = async_to_raw_response_wrapper(
            enterprise.list_hypervisors,
        )
        self.list_roles = async_to_raw_response_wrapper(
            enterprise.list_roles,
        )

    @cached_property
    def consumption(self) -> AsyncConsumptionResourceWithRawResponse:
        return AsyncConsumptionResourceWithRawResponse(self._enterprise.consumption)

    @cached_property
    def git_providers(self) -> AsyncGitProvidersResourceWithRawResponse:
        return AsyncGitProvidersResourceWithRawResponse(self._enterprise.git_providers)

    @cached_property
    def idp_groups(self) -> AsyncIdpGroupsResourceWithRawResponse:
        return AsyncIdpGroupsResourceWithRawResponse(self._enterprise.idp_groups)

    @cached_property
    def ip_access_list(self) -> AsyncIPAccessListResourceWithRawResponse:
        return AsyncIPAccessListResourceWithRawResponse(self._enterprise.ip_access_list)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithRawResponse:
        return AsyncKnowledgeResourceWithRawResponse(self._enterprise.knowledge)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._enterprise.members)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._enterprise.metrics)

    @cached_property
    def org_group_limits(self) -> AsyncOrgGroupLimitsResourceWithRawResponse:
        return AsyncOrgGroupLimitsResourceWithRawResponse(self._enterprise.org_group_limits)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._enterprise.organizations)

    @cached_property
    def playbooks(self) -> AsyncPlaybooksResourceWithRawResponse:
        return AsyncPlaybooksResourceWithRawResponse(self._enterprise.playbooks)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._enterprise.sessions)


class EnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

        self.get_queue_status = to_streamed_response_wrapper(
            enterprise.get_queue_status,
        )
        self.list_audit_logs = to_streamed_response_wrapper(
            enterprise.list_audit_logs,
        )
        self.list_hypervisors = to_streamed_response_wrapper(
            enterprise.list_hypervisors,
        )
        self.list_roles = to_streamed_response_wrapper(
            enterprise.list_roles,
        )

    @cached_property
    def consumption(self) -> ConsumptionResourceWithStreamingResponse:
        return ConsumptionResourceWithStreamingResponse(self._enterprise.consumption)

    @cached_property
    def git_providers(self) -> GitProvidersResourceWithStreamingResponse:
        return GitProvidersResourceWithStreamingResponse(self._enterprise.git_providers)

    @cached_property
    def idp_groups(self) -> IdpGroupsResourceWithStreamingResponse:
        return IdpGroupsResourceWithStreamingResponse(self._enterprise.idp_groups)

    @cached_property
    def ip_access_list(self) -> IPAccessListResourceWithStreamingResponse:
        return IPAccessListResourceWithStreamingResponse(self._enterprise.ip_access_list)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithStreamingResponse:
        return KnowledgeResourceWithStreamingResponse(self._enterprise.knowledge)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._enterprise.members)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._enterprise.metrics)

    @cached_property
    def org_group_limits(self) -> OrgGroupLimitsResourceWithStreamingResponse:
        return OrgGroupLimitsResourceWithStreamingResponse(self._enterprise.org_group_limits)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._enterprise.organizations)

    @cached_property
    def playbooks(self) -> PlaybooksResourceWithStreamingResponse:
        return PlaybooksResourceWithStreamingResponse(self._enterprise.playbooks)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._enterprise.sessions)


class AsyncEnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

        self.get_queue_status = async_to_streamed_response_wrapper(
            enterprise.get_queue_status,
        )
        self.list_audit_logs = async_to_streamed_response_wrapper(
            enterprise.list_audit_logs,
        )
        self.list_hypervisors = async_to_streamed_response_wrapper(
            enterprise.list_hypervisors,
        )
        self.list_roles = async_to_streamed_response_wrapper(
            enterprise.list_roles,
        )

    @cached_property
    def consumption(self) -> AsyncConsumptionResourceWithStreamingResponse:
        return AsyncConsumptionResourceWithStreamingResponse(self._enterprise.consumption)

    @cached_property
    def git_providers(self) -> AsyncGitProvidersResourceWithStreamingResponse:
        return AsyncGitProvidersResourceWithStreamingResponse(self._enterprise.git_providers)

    @cached_property
    def idp_groups(self) -> AsyncIdpGroupsResourceWithStreamingResponse:
        return AsyncIdpGroupsResourceWithStreamingResponse(self._enterprise.idp_groups)

    @cached_property
    def ip_access_list(self) -> AsyncIPAccessListResourceWithStreamingResponse:
        return AsyncIPAccessListResourceWithStreamingResponse(self._enterprise.ip_access_list)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        return AsyncKnowledgeResourceWithStreamingResponse(self._enterprise.knowledge)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._enterprise.members)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._enterprise.metrics)

    @cached_property
    def org_group_limits(self) -> AsyncOrgGroupLimitsResourceWithStreamingResponse:
        return AsyncOrgGroupLimitsResourceWithStreamingResponse(self._enterprise.org_group_limits)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._enterprise.organizations)

    @cached_property
    def playbooks(self) -> AsyncPlaybooksResourceWithStreamingResponse:
        return AsyncPlaybooksResourceWithStreamingResponse(self._enterprise.playbooks)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._enterprise.sessions)
