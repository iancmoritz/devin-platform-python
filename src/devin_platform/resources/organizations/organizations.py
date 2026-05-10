# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .playbooks import (
    PlaybooksResource,
    AsyncPlaybooksResource,
    PlaybooksResourceWithRawResponse,
    AsyncPlaybooksResourceWithRawResponse,
    PlaybooksResourceWithStreamingResponse,
    AsyncPlaybooksResourceWithStreamingResponse,
)
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .attachments import (
    AttachmentsResource,
    AsyncAttachmentsResource,
    AttachmentsResourceWithRawResponse,
    AsyncAttachmentsResourceWithRawResponse,
    AttachmentsResourceWithStreamingResponse,
    AsyncAttachmentsResourceWithStreamingResponse,
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

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def attachments(self) -> AttachmentsResource:
        return AttachmentsResource(self._client)

    @cached_property
    def consumption(self) -> ConsumptionResource:
        return ConsumptionResource(self._client)

    @cached_property
    def knowledge(self) -> KnowledgeResource:
        return KnowledgeResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def playbooks(self) -> PlaybooksResource:
        return PlaybooksResource(self._client)

    @cached_property
    def schedules(self) -> SchedulesResource:
        return SchedulesResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def attachments(self) -> AsyncAttachmentsResource:
        return AsyncAttachmentsResource(self._client)

    @cached_property
    def consumption(self) -> AsyncConsumptionResource:
        return AsyncConsumptionResource(self._client)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResource:
        return AsyncKnowledgeResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def playbooks(self) -> AsyncPlaybooksResource:
        return AsyncPlaybooksResource(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        return AsyncSchedulesResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def attachments(self) -> AttachmentsResourceWithRawResponse:
        return AttachmentsResourceWithRawResponse(self._organizations.attachments)

    @cached_property
    def consumption(self) -> ConsumptionResourceWithRawResponse:
        return ConsumptionResourceWithRawResponse(self._organizations.consumption)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithRawResponse:
        return KnowledgeResourceWithRawResponse(self._organizations.knowledge)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._organizations.metrics)

    @cached_property
    def playbooks(self) -> PlaybooksResourceWithRawResponse:
        return PlaybooksResourceWithRawResponse(self._organizations.playbooks)

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self._organizations.schedules)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._organizations.secrets)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._organizations.sessions)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def attachments(self) -> AsyncAttachmentsResourceWithRawResponse:
        return AsyncAttachmentsResourceWithRawResponse(self._organizations.attachments)

    @cached_property
    def consumption(self) -> AsyncConsumptionResourceWithRawResponse:
        return AsyncConsumptionResourceWithRawResponse(self._organizations.consumption)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithRawResponse:
        return AsyncKnowledgeResourceWithRawResponse(self._organizations.knowledge)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._organizations.metrics)

    @cached_property
    def playbooks(self) -> AsyncPlaybooksResourceWithRawResponse:
        return AsyncPlaybooksResourceWithRawResponse(self._organizations.playbooks)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self._organizations.schedules)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._organizations.secrets)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._organizations.sessions)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def attachments(self) -> AttachmentsResourceWithStreamingResponse:
        return AttachmentsResourceWithStreamingResponse(self._organizations.attachments)

    @cached_property
    def consumption(self) -> ConsumptionResourceWithStreamingResponse:
        return ConsumptionResourceWithStreamingResponse(self._organizations.consumption)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithStreamingResponse:
        return KnowledgeResourceWithStreamingResponse(self._organizations.knowledge)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._organizations.metrics)

    @cached_property
    def playbooks(self) -> PlaybooksResourceWithStreamingResponse:
        return PlaybooksResourceWithStreamingResponse(self._organizations.playbooks)

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self._organizations.schedules)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._organizations.secrets)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._organizations.sessions)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

    @cached_property
    def attachments(self) -> AsyncAttachmentsResourceWithStreamingResponse:
        return AsyncAttachmentsResourceWithStreamingResponse(self._organizations.attachments)

    @cached_property
    def consumption(self) -> AsyncConsumptionResourceWithStreamingResponse:
        return AsyncConsumptionResourceWithStreamingResponse(self._organizations.consumption)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        return AsyncKnowledgeResourceWithStreamingResponse(self._organizations.knowledge)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._organizations.metrics)

    @cached_property
    def playbooks(self) -> AsyncPlaybooksResourceWithStreamingResponse:
        return AsyncPlaybooksResourceWithStreamingResponse(self._organizations.playbooks)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self._organizations.schedules)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._organizations.secrets)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._organizations.sessions)
