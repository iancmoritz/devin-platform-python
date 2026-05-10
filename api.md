# Enterprise

Types:

```python
from devin_platform.types import (
    AuditLogAction,
    PaginatedAuditLogResponse,
    Role,
    EnterpriseGetQueueStatusResponse,
    EnterpriseListHypervisorsResponse,
    EnterpriseListRolesResponse,
)
```

Methods:

- <code title="get /v3/enterprise/queue">client.enterprise.<a href="./src/devin_platform/resources/enterprise/enterprise.py">get_queue_status</a>() -> <a href="./src/devin_platform/types/enterprise_get_queue_status_response.py">EnterpriseGetQueueStatusResponse</a></code>
- <code title="get /v3/enterprise/audit-logs">client.enterprise.<a href="./src/devin_platform/resources/enterprise/enterprise.py">list_audit_logs</a>(\*\*<a href="src/devin_platform/types/enterprise_list_audit_logs_params.py">params</a>) -> <a href="./src/devin_platform/types/paginated_audit_log_response.py">PaginatedAuditLogResponse</a></code>
- <code title="get /v3/enterprise/hypervisors">client.enterprise.<a href="./src/devin_platform/resources/enterprise/enterprise.py">list_hypervisors</a>(\*\*<a href="src/devin_platform/types/enterprise_list_hypervisors_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise_list_hypervisors_response.py">EnterpriseListHypervisorsResponse</a></code>
- <code title="get /v3/enterprise/roles">client.enterprise.<a href="./src/devin_platform/resources/enterprise/enterprise.py">list_roles</a>(\*\*<a href="src/devin_platform/types/enterprise_list_roles_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise_list_roles_response.py">EnterpriseListRolesResponse</a></code>

## Consumption

Types:

```python
from devin_platform.types.enterprise import ConsumptionListConsumptionCyclesResponse
```

Methods:

- <code title="get /v3/enterprise/consumption/cycles">client.enterprise.consumption.<a href="./src/devin_platform/resources/enterprise/consumption/consumption.py">list_consumption_cycles</a>(\*\*<a href="src/devin_platform/types/enterprise/consumption_list_consumption_cycles_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption_list_consumption_cycles_response.py">ConsumptionListConsumptionCyclesResponse</a></code>

### AcuLimits

#### Devin

Types:

```python
from devin_platform.types.enterprise.consumption.acu_limits import DevinGetAcuLimitsResponse
```

Methods:

- <code title="get /v3/enterprise/consumption/acu-limits/devin">client.enterprise.consumption.acu_limits.devin.<a href="./src/devin_platform/resources/enterprise/consumption/acu_limits/devin/devin.py">get_acu_limits</a>(\*\*<a href="src/devin_platform/types/enterprise/consumption/acu_limits/devin_get_acu_limits_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/acu_limits/devin_get_acu_limits_response.py">DevinGetAcuLimitsResponse</a></code>

##### Organizations

Methods:

- <code title="delete /v3/enterprise/consumption/acu-limits/devin/organizations/{org_id}">client.enterprise.consumption.acu_limits.devin.organizations.<a href="./src/devin_platform/resources/enterprise/consumption/acu_limits/devin/organizations.py">delete_acu_limit</a>(org_id) -> None</code>
- <code title="put /v3/enterprise/consumption/acu-limits/devin/organizations/{org_id}">client.enterprise.consumption.acu_limits.devin.organizations.<a href="./src/devin_platform/resources/enterprise/consumption/acu_limits/devin/organizations.py">set_acu_limit</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/consumption/acu_limits/devin/organization_set_acu_limit_params.py">params</a>) -> None</code>

### Daily

Types:

```python
from devin_platform.types.enterprise.consumption import Consumption
```

Methods:

- <code title="get /v3/enterprise/consumption/daily">client.enterprise.consumption.daily.<a href="./src/devin_platform/resources/enterprise/consumption/daily.py">get_daily_consumption</a>(\*\*<a href="src/devin_platform/types/enterprise/consumption/daily_get_daily_consumption_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/enterprise/consumption/daily/organizations/{org_id}">client.enterprise.consumption.daily.<a href="./src/devin_platform/resources/enterprise/consumption/daily.py">get_org_daily_consumption</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/consumption/daily_get_org_daily_consumption_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/enterprise/consumption/daily/service-users/{service_user_id}">client.enterprise.consumption.daily.<a href="./src/devin_platform/resources/enterprise/consumption/daily.py">get_service_user_daily_consumption</a>(service_user_id, \*\*<a href="src/devin_platform/types/enterprise/consumption/daily_get_service_user_daily_consumption_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/enterprise/consumption/daily/sessions/{session_id}">client.enterprise.consumption.daily.<a href="./src/devin_platform/resources/enterprise/consumption/daily.py">get_session_daily_consumption</a>(session_id, \*\*<a href="src/devin_platform/types/enterprise/consumption/daily_get_session_daily_consumption_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/enterprise/consumption/daily/users/{user_id}">client.enterprise.consumption.daily.<a href="./src/devin_platform/resources/enterprise/consumption/daily.py">get_user_daily_consumption</a>(user_id, \*\*<a href="src/devin_platform/types/enterprise/consumption/daily_get_user_daily_consumption_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>

## GitProviders

Types:

```python
from devin_platform.types.enterprise import GitProviderListConnectionsResponse
```

Methods:

- <code title="get /v3/enterprise/git-providers/connections">client.enterprise.git_providers.<a href="./src/devin_platform/resources/enterprise/git_providers.py">list_connections</a>(\*\*<a href="src/devin_platform/types/enterprise/git_provider_list_connections_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/git_provider_list_connections_response.py">GitProviderListConnectionsResponse</a></code>

## IdpGroups

Types:

```python
from devin_platform.types.enterprise import (
    IdpGroupResponse,
    IdpGroupListIdpGroupsResponse,
    IdpGroupRegisterIdpGroupsResponse,
)
```

Methods:

- <code title="delete /v3/enterprise/idp-groups/{idp_group_name}">client.enterprise.idp_groups.<a href="./src/devin_platform/resources/enterprise/idp_groups.py">delete_idp_group</a>(idp_group_name) -> <a href="./src/devin_platform/types/enterprise/idp_group_response.py">IdpGroupResponse</a></code>
- <code title="get /v3/enterprise/idp-groups">client.enterprise.idp_groups.<a href="./src/devin_platform/resources/enterprise/idp_groups.py">list_idp_groups</a>(\*\*<a href="src/devin_platform/types/enterprise/idp_group_list_idp_groups_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/idp_group_list_idp_groups_response.py">IdpGroupListIdpGroupsResponse</a></code>
- <code title="post /v3/enterprise/idp-groups">client.enterprise.idp_groups.<a href="./src/devin_platform/resources/enterprise/idp_groups.py">register_idp_groups</a>(\*\*<a href="src/devin_platform/types/enterprise/idp_group_register_idp_groups_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/idp_group_register_idp_groups_response.py">IdpGroupRegisterIdpGroupsResponse</a></code>

## IPAccessList

Types:

```python
from devin_platform.types.enterprise import IPAccessListResponse
```

Methods:

- <code title="delete /v3/enterprise/ip-access-list">client.enterprise.ip_access_list.<a href="./src/devin_platform/resources/enterprise/ip_access_list.py">clear_access_list</a>() -> <a href="./src/devin_platform/types/enterprise/ip_access_list_response.py">IPAccessListResponse</a></code>
- <code title="get /v3/enterprise/ip-access-list">client.enterprise.ip_access_list.<a href="./src/devin_platform/resources/enterprise/ip_access_list.py">get_access_list</a>() -> <a href="./src/devin_platform/types/enterprise/ip_access_list_response.py">IPAccessListResponse</a></code>
- <code title="put /v3/enterprise/ip-access-list">client.enterprise.ip_access_list.<a href="./src/devin_platform/resources/enterprise/ip_access_list.py">replace_access_list</a>(\*\*<a href="src/devin_platform/types/enterprise/ip_access_list_replace_access_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/ip_access_list_response.py">IPAccessListResponse</a></code>

## Knowledge

Types:

```python
from devin_platform.types.enterprise import FolderTree
```

Methods:

- <code title="get /v3/enterprise/knowledge/folders">client.enterprise.knowledge.<a href="./src/devin_platform/resources/enterprise/knowledge/knowledge.py">list_folders</a>() -> <a href="./src/devin_platform/types/enterprise/folder_tree.py">FolderTree</a></code>

### Notes

Types:

```python
from devin_platform.types.enterprise.knowledge import (
    KnowledgeNote,
    KnowledgeNoteCreate,
    PaginatedKnowledgeNoteResponse,
)
```

Methods:

- <code title="post /v3/enterprise/knowledge/notes">client.enterprise.knowledge.notes.<a href="./src/devin_platform/resources/enterprise/knowledge/notes.py">create</a>(\*\*<a href="src/devin_platform/types/enterprise/knowledge/note_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>
- <code title="get /v3/enterprise/knowledge/notes/{note_id}">client.enterprise.knowledge.notes.<a href="./src/devin_platform/resources/enterprise/knowledge/notes.py">retrieve</a>(note_id) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>
- <code title="put /v3/enterprise/knowledge/notes/{note_id}">client.enterprise.knowledge.notes.<a href="./src/devin_platform/resources/enterprise/knowledge/notes.py">update</a>(note_id, \*\*<a href="src/devin_platform/types/enterprise/knowledge/note_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>
- <code title="get /v3/enterprise/knowledge/notes">client.enterprise.knowledge.notes.<a href="./src/devin_platform/resources/enterprise/knowledge/notes.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/knowledge/note_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/knowledge/paginated_knowledge_note_response.py">PaginatedKnowledgeNoteResponse</a></code>
- <code title="delete /v3/enterprise/knowledge/notes/{note_id}">client.enterprise.knowledge.notes.<a href="./src/devin_platform/resources/enterprise/knowledge/notes.py">delete</a>(note_id) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>

## Members

Types:

```python
from devin_platform.types.enterprise import PaginatedIdpGroupUser
```

Methods:

- <code title="get /v3/enterprise/members/idp-users">client.enterprise.members.<a href="./src/devin_platform/resources/enterprise/members/members.py">list_idp_group_users</a>(\*\*<a href="src/devin_platform/types/enterprise/member_list_idp_group_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/paginated_idp_group_user.py">PaginatedIdpGroupUser</a></code>

### IdpGroups

Types:

```python
from devin_platform.types.enterprise.members import (
    IdpGroup,
    IdpGroupUpdateRole,
    PaginatedIdpGroup,
    RoleAssignment,
)
```

Methods:

- <code title="get /v3/enterprise/members/idp-groups/{idp_group_name}">client.enterprise.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/members/idp_groups.py">retrieve</a>(idp_group_name) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>
- <code title="patch /v3/enterprise/members/idp-groups/{idp_group_name}">client.enterprise.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/members/idp_groups.py">update</a>(idp_group_name, \*\*<a href="src/devin_platform/types/enterprise/members/idp_group_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>
- <code title="get /v3/enterprise/members/idp-groups">client.enterprise.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/members/idp_groups.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/members/idp_group_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/paginated_idp_group.py">PaginatedIdpGroup</a></code>
- <code title="delete /v3/enterprise/members/idp-groups/{idp_group_name}">client.enterprise.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/members/idp_groups.py">delete</a>(idp_group_name) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>
- <code title="post /v3/enterprise/members/idp-groups/{idp_group_name}">client.enterprise.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/members/idp_groups.py">assign</a>(idp_group_name, \*\*<a href="src/devin_platform/types/enterprise/members/idp_group_assign_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>

### ServiceUsers

Types:

```python
from devin_platform.types.enterprise.members import (
    PaginatedServiceUser,
    ServiceUser,
    ServiceUserUpdateRole,
)
```

Methods:

- <code title="get /v3/enterprise/members/service-users/{service_user_id}">client.enterprise.members.service_users.<a href="./src/devin_platform/resources/enterprise/members/service_users.py">retrieve</a>(service_user_id) -> <a href="./src/devin_platform/types/enterprise/members/service_user.py">ServiceUser</a></code>
- <code title="patch /v3/enterprise/members/service-users/{service_user_id}">client.enterprise.members.service_users.<a href="./src/devin_platform/resources/enterprise/members/service_users.py">update</a>(service_user_id, \*\*<a href="src/devin_platform/types/enterprise/members/service_user_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/service_user.py">ServiceUser</a></code>
- <code title="get /v3/enterprise/members/service-users">client.enterprise.members.service_users.<a href="./src/devin_platform/resources/enterprise/members/service_users.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/members/service_user_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/paginated_service_user.py">PaginatedServiceUser</a></code>
- <code title="delete /v3/enterprise/members/service-users/{service_user_id}">client.enterprise.members.service_users.<a href="./src/devin_platform/resources/enterprise/members/service_users.py">delete</a>(service_user_id) -> <a href="./src/devin_platform/types/enterprise/members/service_user.py">ServiceUser</a></code>
- <code title="post /v3/enterprise/members/service-users/{service_user_id}">client.enterprise.members.service_users.<a href="./src/devin_platform/resources/enterprise/members/service_users.py">assign</a>(service_user_id, \*\*<a href="src/devin_platform/types/enterprise/members/service_user_assign_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/service_user.py">ServiceUser</a></code>

### Users

Types:

```python
from devin_platform.types.enterprise.members import (
    IdpRoleAssignment,
    PaginatedUser,
    User,
    UserUpdateRole,
    UserRetrieveResponse,
    UserInviteResponse,
)
```

Methods:

- <code title="get /v3/enterprise/members/users/{user_id}">client.enterprise.members.users.<a href="./src/devin_platform/resources/enterprise/members/users.py">retrieve</a>(user_id) -> <a href="./src/devin_platform/types/enterprise/members/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /v3/enterprise/members/users/{user_id}">client.enterprise.members.users.<a href="./src/devin_platform/resources/enterprise/members/users.py">update</a>(user_id, \*\*<a href="src/devin_platform/types/enterprise/members/user_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/user.py">User</a></code>
- <code title="get /v3/enterprise/members/users">client.enterprise.members.users.<a href="./src/devin_platform/resources/enterprise/members/users.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/members/user_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/paginated_user.py">PaginatedUser</a></code>
- <code title="delete /v3/enterprise/members/users/{user_id}">client.enterprise.members.users.<a href="./src/devin_platform/resources/enterprise/members/users.py">delete</a>(user_id) -> <a href="./src/devin_platform/types/enterprise/members/user.py">User</a></code>
- <code title="post /v3/enterprise/members/users">client.enterprise.members.users.<a href="./src/devin_platform/resources/enterprise/members/users.py">invite</a>(\*\*<a href="src/devin_platform/types/enterprise/members/user_invite_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/user_invite_response.py">UserInviteResponse</a></code>

## Metrics

Types:

```python
from devin_platform.types.enterprise import (
    ActiveUserMetrics,
    PrMetrics,
    SearchMetrics,
    SessionCountsBySize,
    SessionMetrics,
    UsageMetrics,
    MetricGetDailyActiveUsersResponse,
    MetricGetMonthlyActiveUsersResponse,
    MetricGetSessionMetricsByCategoryResponse,
    MetricGetWeeklyActiveUsersResponse,
)
```

Methods:

- <code title="get /v3/enterprise/metrics/active-users">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_active_users</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/active_user_metrics.py">ActiveUserMetrics</a></code>
- <code title="get /v3/enterprise/metrics/dau">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_daily_active_users</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_daily_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/metric_get_daily_active_users_response.py">MetricGetDailyActiveUsersResponse</a></code>
- <code title="get /v3/enterprise/metrics/mau">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_monthly_active_users</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_monthly_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/metric_get_monthly_active_users_response.py">MetricGetMonthlyActiveUsersResponse</a></code>
- <code title="get /v3/enterprise/metrics/prs">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_pr_metrics</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_pr_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/pr_metrics.py">PrMetrics</a></code>
- <code title="get /v3/enterprise/metrics/searches">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_search_metrics</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_search_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/search_metrics.py">SearchMetrics</a></code>
- <code title="get /v3/enterprise/metrics/sessions">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_session_metrics</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_session_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_metrics.py">SessionMetrics</a></code>
- <code title="get /v3/enterprise/metrics/sessions-by-category">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_session_metrics_by_category</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_session_metrics_by_category_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/metric_get_session_metrics_by_category_response.py">MetricGetSessionMetricsByCategoryResponse</a></code>
- <code title="get /v3/enterprise/metrics/usage">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_usage_metrics</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_usage_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/usage_metrics.py">UsageMetrics</a></code>
- <code title="get /v3/enterprise/metrics/wau">client.enterprise.metrics.<a href="./src/devin_platform/resources/enterprise/metrics.py">get_weekly_active_users</a>(\*\*<a href="src/devin_platform/types/enterprise/metric_get_weekly_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/metric_get_weekly_active_users_response.py">MetricGetWeeklyActiveUsersResponse</a></code>

## OrgGroupLimits

Types:

```python
from devin_platform.types.enterprise import OrgGroupsConfig
```

Methods:

- <code title="get /v3/enterprise/org-group-limits">client.enterprise.org_group_limits.<a href="./src/devin_platform/resources/enterprise/org_group_limits.py">get_org_group_config</a>() -> <a href="./src/devin_platform/types/enterprise/org_groups_config.py">OrgGroupsConfig</a></code>
- <code title="put /v3/enterprise/org-group-limits">client.enterprise.org_group_limits.<a href="./src/devin_platform/resources/enterprise/org_group_limits.py">update_org_group_config</a>(\*\*<a href="src/devin_platform/types/enterprise/org_group_limit_update_org_group_config_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/org_groups_config.py">OrgGroupsConfig</a></code>

## Organizations

Types:

```python
from devin_platform.types.enterprise import Organization, OrganizationListResponse
```

Methods:

- <code title="post /v3/enterprise/organizations">client.enterprise.organizations.<a href="./src/devin_platform/resources/enterprise/organizations/organizations.py">create</a>(\*\*<a href="src/devin_platform/types/enterprise/organization_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organization.py">Organization</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}">client.enterprise.organizations.<a href="./src/devin_platform/resources/enterprise/organizations/organizations.py">retrieve</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organization.py">Organization</a></code>
- <code title="patch /v3/enterprise/organizations/{org_id}">client.enterprise.organizations.<a href="./src/devin_platform/resources/enterprise/organizations/organizations.py">update</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organization_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organization.py">Organization</a></code>
- <code title="get /v3/enterprise/organizations">client.enterprise.organizations.<a href="./src/devin_platform/resources/enterprise/organizations/organizations.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/organization_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}">client.enterprise.organizations.<a href="./src/devin_platform/resources/enterprise/organizations/organizations.py">delete</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organization.py">Organization</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/audit-logs">client.enterprise.organizations.<a href="./src/devin_platform/resources/enterprise/organizations/organizations.py">retrieve_audit_logs</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organization_retrieve_audit_logs_params.py">params</a>) -> <a href="./src/devin_platform/types/paginated_audit_log_response.py">PaginatedAuditLogResponse</a></code>

### GitProviders

#### Permissions

Types:

```python
from devin_platform.types.enterprise.organizations.git_providers import (
    GitPermission,
    GitPermissionBulkCreate,
    PermissionCreateResponse,
    PermissionListResponse,
    PermissionDeleteAllResponse,
)
```

Methods:

- <code title="put /v3/enterprise/organizations/{org_id}/git-providers/permissions">client.enterprise.organizations.git_providers.permissions.<a href="./src/devin_platform/resources/enterprise/organizations/git_providers/permissions.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/git_providers/permission_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organizations/git_providers/permission_create_response.py">PermissionCreateResponse</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/git-providers/permissions">client.enterprise.organizations.git_providers.permissions.<a href="./src/devin_platform/resources/enterprise/organizations/git_providers/permissions.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/git_providers/permission_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organizations/git_providers/permission_list_response.py">PermissionListResponse</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/git-providers/permissions/{git_permission_id}">client.enterprise.organizations.git_providers.permissions.<a href="./src/devin_platform/resources/enterprise/organizations/git_providers/permissions.py">delete</a>(git_permission_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/git_providers/git_permission.py">GitPermission</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/git-providers/permissions">client.enterprise.organizations.git_providers.permissions.<a href="./src/devin_platform/resources/enterprise/organizations/git_providers/permissions.py">delete_all</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/git_providers/permission_delete_all_response.py">PermissionDeleteAllResponse</a></code>

### Members

Methods:

- <code title="get /v3/enterprise/organizations/{org_id}/members/idp-users">client.enterprise.organizations.members.<a href="./src/devin_platform/resources/enterprise/organizations/members/members.py">retrieve_idp_users</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/member_retrieve_idp_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/paginated_idp_group_user.py">PaginatedIdpGroupUser</a></code>

#### IdpGroups

Methods:

- <code title="get /v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}">client.enterprise.organizations.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/organizations/members/idp_groups.py">retrieve</a>(idp_group_name, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>
- <code title="post /v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}">client.enterprise.organizations.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/organizations/members/idp_groups.py">update</a>(idp_group_name, \*, org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/members/idp_group_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/members/idp-groups/{idp_group_name}">client.enterprise.organizations.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/organizations/members/idp_groups.py">delete</a>(idp_group_name, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/members/idp_group.py">IdpGroup</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/members/idp-groups">client.enterprise.organizations.members.idp_groups.<a href="./src/devin_platform/resources/enterprise/organizations/members/idp_groups.py">retrieve_idp_groups</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/members/idp_group_retrieve_idp_groups_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/paginated_idp_group.py">PaginatedIdpGroup</a></code>

#### ServiceUsers

Methods:

- <code title="post /v3/enterprise/organizations/{org_id}/members/service-users/{service_user_id}">client.enterprise.organizations.members.service_users.<a href="./src/devin_platform/resources/enterprise/organizations/members/service_users.py">update</a>(service_user_id, \*, org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/members/service_user_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/service_user.py">ServiceUser</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/members/service-users/{service_user_id}">client.enterprise.organizations.members.service_users.<a href="./src/devin_platform/resources/enterprise/organizations/members/service_users.py">delete</a>(service_user_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/members/service_user.py">ServiceUser</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/members/service-users">client.enterprise.organizations.members.service_users.<a href="./src/devin_platform/resources/enterprise/organizations/members/service_users.py">retrieve_service_users</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/members/service_user_retrieve_service_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/paginated_service_user.py">PaginatedServiceUser</a></code>

#### Users

Methods:

- <code title="post /v3/enterprise/organizations/{org_id}/members/users/{user_id}">client.enterprise.organizations.members.users.<a href="./src/devin_platform/resources/enterprise/organizations/members/users.py">update</a>(user_id, \*, org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/members/user_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/user.py">User</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/members/users">client.enterprise.organizations.members.users.<a href="./src/devin_platform/resources/enterprise/organizations/members/users.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/members/user_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/members/paginated_user.py">PaginatedUser</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/members/users/{user_id}">client.enterprise.organizations.members.users.<a href="./src/devin_platform/resources/enterprise/organizations/members/users.py">delete</a>(user_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/members/user.py">User</a></code>

### Metrics

Methods:

- <code title="get /v3/enterprise/organizations/{org_id}/metrics/usage">client.enterprise.organizations.metrics.<a href="./src/devin_platform/resources/enterprise/organizations/metrics.py">retrieve_usage</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/metric_retrieve_usage_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/usage_metrics.py">UsageMetrics</a></code>

### Tags

Types:

```python
from devin_platform.types.enterprise.organizations import Tags, TagsCreate
```

Methods:

- <code title="put /v3/enterprise/organizations/{org_id}/tags">client.enterprise.organizations.tags.<a href="./src/devin_platform/resources/enterprise/organizations/tags/tags.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/tag_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/tags.py">Tags</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/tags">client.enterprise.organizations.tags.<a href="./src/devin_platform/resources/enterprise/organizations/tags/tags.py">list</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/tags.py">Tags</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/tags/{tag}">client.enterprise.organizations.tags.<a href="./src/devin_platform/resources/enterprise/organizations/tags/tags.py">delete</a>(tag, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/tags.py">Tags</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/tags">client.enterprise.organizations.tags.<a href="./src/devin_platform/resources/enterprise/organizations/tags/tags.py">delete_all</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/tags.py">Tags</a></code>

#### Default

Types:

```python
from devin_platform.types.enterprise.organizations.tags import DefaultTag
```

Methods:

- <code title="put /v3/enterprise/organizations/{org_id}/tags/default">client.enterprise.organizations.tags.default.<a href="./src/devin_platform/resources/enterprise/organizations/tags/default.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/enterprise/organizations/tags/default_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/default_tag.py">DefaultTag</a></code>
- <code title="get /v3/enterprise/organizations/{org_id}/tags/default">client.enterprise.organizations.tags.default.<a href="./src/devin_platform/resources/enterprise/organizations/tags/default.py">list</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/default_tag.py">DefaultTag</a></code>
- <code title="delete /v3/enterprise/organizations/{org_id}/tags/default">client.enterprise.organizations.tags.default.<a href="./src/devin_platform/resources/enterprise/organizations/tags/default.py">delete_all</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/organizations/tags/default_tag.py">DefaultTag</a></code>

## Playbooks

Types:

```python
from devin_platform.types.enterprise import (
    PaginatedPlaybookResponse,
    PlaybookCreate,
    PlaybookResponse,
)
```

Methods:

- <code title="post /v3/enterprise/playbooks">client.enterprise.playbooks.<a href="./src/devin_platform/resources/enterprise/playbooks.py">create</a>(\*\*<a href="src/devin_platform/types/enterprise/playbook_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>
- <code title="get /v3/enterprise/playbooks/{playbook_id}">client.enterprise.playbooks.<a href="./src/devin_platform/resources/enterprise/playbooks.py">retrieve</a>(playbook_id) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>
- <code title="put /v3/enterprise/playbooks/{playbook_id}">client.enterprise.playbooks.<a href="./src/devin_platform/resources/enterprise/playbooks.py">update</a>(playbook_id, \*\*<a href="src/devin_platform/types/enterprise/playbook_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>
- <code title="get /v3/enterprise/playbooks">client.enterprise.playbooks.<a href="./src/devin_platform/resources/enterprise/playbooks.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/playbook_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/paginated_playbook_response.py">PaginatedPlaybookResponse</a></code>
- <code title="delete /v3/enterprise/playbooks/{playbook_id}">client.enterprise.playbooks.<a href="./src/devin_platform/resources/enterprise/playbooks.py">delete</a>(playbook_id) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>

## Sessions

Types:

```python
from devin_platform.types.enterprise import (
    PaginatedSessionResponse,
    SessionAttachment,
    SessionPullRequest,
    SessionResponse,
    SessionRetrieveAttachmentsResponse,
)
```

Methods:

- <code title="get /v3/enterprise/sessions/{devin_id}">client.enterprise.sessions.<a href="./src/devin_platform/resources/enterprise/sessions/sessions.py">retrieve</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/session_retrieve_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>
- <code title="get /v3/enterprise/sessions">client.enterprise.sessions.<a href="./src/devin_platform/resources/enterprise/sessions/sessions.py">list</a>(\*\*<a href="src/devin_platform/types/enterprise/session_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/paginated_session_response.py">PaginatedSessionResponse</a></code>
- <code title="get /v3/enterprise/sessions/{devin_id}/attachments">client.enterprise.sessions.<a href="./src/devin_platform/resources/enterprise/sessions/sessions.py">retrieve_attachments</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/session_retrieve_attachments_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_retrieve_attachments_response.py">SessionRetrieveAttachmentsResponse</a></code>

### Insights

Types:

```python
from devin_platform.types.enterprise.sessions import (
    PaginatedSessionInsightsResponse,
    SessionInsights,
    SessionInsightsGenerate,
    SessionInsightsNoteUsageItem,
)
```

Methods:

- <code title="get /v3/enterprise/sessions/{devin_id}/insights">client.enterprise.sessions.insights.<a href="./src/devin_platform/resources/enterprise/sessions/insights.py">list</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/sessions/insight_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/session_insights.py">SessionInsights</a></code>
- <code title="post /v3/enterprise/sessions/{devin_id}/insights/generate">client.enterprise.sessions.insights.<a href="./src/devin_platform/resources/enterprise/sessions/insights.py">generate</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/sessions/insight_generate_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/session_insights_generate.py">SessionInsightsGenerate</a></code>

### Messages

Types:

```python
from devin_platform.types.enterprise.sessions import PaginatedSessionMessage, SessionMessageCreate
```

Methods:

- <code title="post /v3/enterprise/sessions/{devin_id}/messages">client.enterprise.sessions.messages.<a href="./src/devin_platform/resources/enterprise/sessions/messages.py">create</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/sessions/message_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>
- <code title="get /v3/enterprise/sessions/{devin_id}/messages">client.enterprise.sessions.messages.<a href="./src/devin_platform/resources/enterprise/sessions/messages.py">list</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/sessions/message_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/paginated_session_message.py">PaginatedSessionMessage</a></code>

### Tags

Types:

```python
from devin_platform.types.enterprise.sessions import SessionTagsResponse, SessionTagsUpdate
```

Methods:

- <code title="put /v3/enterprise/sessions/{devin_id}/tags">client.enterprise.sessions.tags.<a href="./src/devin_platform/resources/enterprise/sessions/tags.py">create</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/sessions/tag_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/session_tags_response.py">SessionTagsResponse</a></code>
- <code title="get /v3/enterprise/sessions/{devin_id}/tags">client.enterprise.sessions.tags.<a href="./src/devin_platform/resources/enterprise/sessions/tags.py">list</a>(devin_id, \*\*<a href="src/devin_platform/types/enterprise/sessions/tag_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/session_tags_response.py">SessionTagsResponse</a></code>

# Organizations

## Attachments

Types:

```python
from devin_platform.types.organizations import AttachmentUploadResponse
```

Methods:

- <code title="get /v3/organizations/{org_id}/attachments/{uuid}/{name}">client.organizations.attachments.<a href="./src/devin_platform/resources/organizations/attachments.py">download</a>(name, \*, org_id, uuid) -> object</code>
- <code title="post /v3/organizations/{org_id}/attachments">client.organizations.attachments.<a href="./src/devin_platform/resources/organizations/attachments.py">upload</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/attachment_upload_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/attachment_upload_response.py">AttachmentUploadResponse</a></code>

## Consumption

### Daily

Methods:

- <code title="get /v3/organizations/{org_id}/consumption/daily">client.organizations.consumption.daily.<a href="./src/devin_platform/resources/organizations/consumption/daily.py">get</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/consumption/daily_get_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/organizations/{org_id}/consumption/daily/service-users/{service_user_id}">client.organizations.consumption.daily.<a href="./src/devin_platform/resources/organizations/consumption/daily.py">get_service_user</a>(service_user_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/consumption/daily_get_service_user_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/organizations/{org_id}/consumption/daily/sessions/{session_id}">client.organizations.consumption.daily.<a href="./src/devin_platform/resources/organizations/consumption/daily.py">get_session</a>(session_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/consumption/daily_get_session_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>
- <code title="get /v3/organizations/{org_id}/consumption/daily/users/{user_id}">client.organizations.consumption.daily.<a href="./src/devin_platform/resources/organizations/consumption/daily.py">get_user</a>(user_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/consumption/daily_get_user_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/consumption/consumption.py">Consumption</a></code>

## Knowledge

Methods:

- <code title="get /v3/organizations/{org_id}/knowledge/folders">client.organizations.knowledge.<a href="./src/devin_platform/resources/organizations/knowledge/knowledge.py">get_folders</a>(org_id) -> <a href="./src/devin_platform/types/enterprise/folder_tree.py">FolderTree</a></code>

### Notes

Methods:

- <code title="post /v3/organizations/{org_id}/knowledge/notes">client.organizations.knowledge.notes.<a href="./src/devin_platform/resources/organizations/knowledge/notes.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/knowledge/note_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>
- <code title="get /v3/organizations/{org_id}/knowledge/notes/{note_id}">client.organizations.knowledge.notes.<a href="./src/devin_platform/resources/organizations/knowledge/notes.py">retrieve</a>(note_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>
- <code title="put /v3/organizations/{org_id}/knowledge/notes/{note_id}">client.organizations.knowledge.notes.<a href="./src/devin_platform/resources/organizations/knowledge/notes.py">update</a>(note_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/knowledge/note_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>
- <code title="get /v3/organizations/{org_id}/knowledge/notes">client.organizations.knowledge.notes.<a href="./src/devin_platform/resources/organizations/knowledge/notes.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/knowledge/note_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/knowledge/paginated_knowledge_note_response.py">PaginatedKnowledgeNoteResponse</a></code>
- <code title="delete /v3/organizations/{org_id}/knowledge/notes/{note_id}">client.organizations.knowledge.notes.<a href="./src/devin_platform/resources/organizations/knowledge/notes.py">delete</a>(note_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/knowledge/knowledge_note.py">KnowledgeNote</a></code>

## Metrics

Types:

```python
from devin_platform.types.organizations import (
    MetricGetDailyActiveUsersResponse,
    MetricGetMonthlyActiveUsersResponse,
    MetricGetWeeklyActiveUsersResponse,
)
```

Methods:

- <code title="get /v3/organizations/{org_id}/metrics/active-users">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_active_users</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/active_user_metrics.py">ActiveUserMetrics</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/dau">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_daily_active_users</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_daily_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/metric_get_daily_active_users_response.py">MetricGetDailyActiveUsersResponse</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/mau">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_monthly_active_users</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_monthly_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/metric_get_monthly_active_users_response.py">MetricGetMonthlyActiveUsersResponse</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/prs">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_pr_metrics</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_pr_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/pr_metrics.py">PrMetrics</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/searches">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_search_metrics</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_search_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/search_metrics.py">SearchMetrics</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/sessions">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_session_metrics</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_session_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_metrics.py">SessionMetrics</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/usage">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_usage_metrics</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_usage_metrics_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/usage_metrics.py">UsageMetrics</a></code>
- <code title="get /v3/organizations/{org_id}/metrics/wau">client.organizations.metrics.<a href="./src/devin_platform/resources/organizations/metrics.py">get_weekly_active_users</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/metric_get_weekly_active_users_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/metric_get_weekly_active_users_response.py">MetricGetWeeklyActiveUsersResponse</a></code>

## Playbooks

Methods:

- <code title="post /v3/organizations/{org_id}/playbooks">client.organizations.playbooks.<a href="./src/devin_platform/resources/organizations/playbooks.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/playbook_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>
- <code title="get /v3/organizations/{org_id}/playbooks/{playbook_id}">client.organizations.playbooks.<a href="./src/devin_platform/resources/organizations/playbooks.py">retrieve</a>(playbook_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>
- <code title="put /v3/organizations/{org_id}/playbooks/{playbook_id}">client.organizations.playbooks.<a href="./src/devin_platform/resources/organizations/playbooks.py">update</a>(playbook_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/playbook_update_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>
- <code title="get /v3/organizations/{org_id}/playbooks">client.organizations.playbooks.<a href="./src/devin_platform/resources/organizations/playbooks.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/playbook_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/paginated_playbook_response.py">PaginatedPlaybookResponse</a></code>
- <code title="delete /v3/organizations/{org_id}/playbooks/{playbook_id}">client.organizations.playbooks.<a href="./src/devin_platform/resources/organizations/playbooks.py">delete</a>(playbook_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/playbook_response.py">PlaybookResponse</a></code>

## Schedules

Types:

```python
from devin_platform.types.organizations import Schedule, ScheduleListResponse
```

Methods:

- <code title="post /v3/organizations/{org_id}/schedules">client.organizations.schedules.<a href="./src/devin_platform/resources/organizations/schedules.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/schedule_create_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/schedule.py">Schedule</a></code>
- <code title="get /v3/organizations/{org_id}/schedules/{schedule_id}">client.organizations.schedules.<a href="./src/devin_platform/resources/organizations/schedules.py">retrieve</a>(schedule_id, \*, org_id) -> <a href="./src/devin_platform/types/organizations/schedule.py">Schedule</a></code>
- <code title="patch /v3/organizations/{org_id}/schedules/{schedule_id}">client.organizations.schedules.<a href="./src/devin_platform/resources/organizations/schedules.py">update</a>(schedule_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/schedule_update_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/schedule.py">Schedule</a></code>
- <code title="get /v3/organizations/{org_id}/schedules">client.organizations.schedules.<a href="./src/devin_platform/resources/organizations/schedules.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/schedule_list_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /v3/organizations/{org_id}/schedules/{schedule_id}">client.organizations.schedules.<a href="./src/devin_platform/resources/organizations/schedules.py">delete</a>(schedule_id, \*, org_id) -> <a href="./src/devin_platform/types/organizations/schedule.py">Schedule</a></code>

## Secrets

Types:

```python
from devin_platform.types.organizations import Secret, SecretListResponse
```

Methods:

- <code title="post /v3/organizations/{org_id}/secrets">client.organizations.secrets.<a href="./src/devin_platform/resources/organizations/secrets.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/secret_create_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/secret.py">Secret</a></code>
- <code title="get /v3/organizations/{org_id}/secrets">client.organizations.secrets.<a href="./src/devin_platform/resources/organizations/secrets.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/secret_list_params.py">params</a>) -> <a href="./src/devin_platform/types/organizations/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /v3/organizations/{org_id}/secrets/{secret_id}">client.organizations.secrets.<a href="./src/devin_platform/resources/organizations/secrets.py">delete</a>(secret_id, \*, org_id) -> <a href="./src/devin_platform/types/organizations/secret.py">Secret</a></code>

## Sessions

Types:

```python
from devin_platform.types.organizations import SessionListAttachmentsResponse
```

Methods:

- <code title="post /v3/organizations/{org_id}/sessions">client.organizations.sessions.<a href="./src/devin_platform/resources/organizations/sessions/sessions.py">create</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/session_create_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>
- <code title="get /v3/organizations/{org_id}/sessions/{devin_id}">client.organizations.sessions.<a href="./src/devin_platform/resources/organizations/sessions/sessions.py">retrieve</a>(devin_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>
- <code title="get /v3/organizations/{org_id}/sessions">client.organizations.sessions.<a href="./src/devin_platform/resources/organizations/sessions/sessions.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/session_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/paginated_session_response.py">PaginatedSessionResponse</a></code>
- <code title="post /v3/organizations/{org_id}/sessions/{devin_id}/archive">client.organizations.sessions.<a href="./src/devin_platform/resources/organizations/sessions/sessions.py">archive</a>(devin_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>
- <code title="get /v3/organizations/{org_id}/sessions/{devin_id}/attachments">client.organizations.sessions.<a href="./src/devin_platform/resources/organizations/sessions/sessions.py">list_attachments</a>(devin_id, \*, org_id) -> <a href="./src/devin_platform/types/organizations/session_list_attachments_response.py">SessionListAttachmentsResponse</a></code>
- <code title="delete /v3/organizations/{org_id}/sessions/{devin_id}">client.organizations.sessions.<a href="./src/devin_platform/resources/organizations/sessions/sessions.py">terminate</a>(devin_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/session_terminate_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>

### Insights

Methods:

- <code title="get /v3/organizations/{org_id}/sessions/{devin_id}/insights">client.organizations.sessions.insights.<a href="./src/devin_platform/resources/organizations/sessions/insights.py">retrieve</a>(devin_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/sessions/session_insights.py">SessionInsights</a></code>
- <code title="get /v3/organizations/{org_id}/sessions/insights">client.organizations.sessions.insights.<a href="./src/devin_platform/resources/organizations/sessions/insights.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/organizations/sessions/insight_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/paginated_session_insights_response.py">PaginatedSessionInsightsResponse</a></code>
- <code title="post /v3/organizations/{org_id}/sessions/{devin_id}/insights/generate">client.organizations.sessions.insights.<a href="./src/devin_platform/resources/organizations/sessions/insights.py">generate</a>(devin_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/sessions/session_insights_generate.py">SessionInsightsGenerate</a></code>

### Messages

Methods:

- <code title="get /v3/organizations/{org_id}/sessions/{devin_id}/messages">client.organizations.sessions.messages.<a href="./src/devin_platform/resources/organizations/sessions/messages.py">list</a>(devin_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/sessions/message_list_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/paginated_session_message.py">PaginatedSessionMessage</a></code>
- <code title="post /v3/organizations/{org_id}/sessions/{devin_id}/messages">client.organizations.sessions.messages.<a href="./src/devin_platform/resources/organizations/sessions/messages.py">send</a>(devin_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/sessions/message_send_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/session_response.py">SessionResponse</a></code>

### Tags

Methods:

- <code title="get /v3/organizations/{org_id}/sessions/{devin_id}/tags">client.organizations.sessions.tags.<a href="./src/devin_platform/resources/organizations/sessions/tags.py">retrieve</a>(devin_id, \*, org_id) -> <a href="./src/devin_platform/types/enterprise/sessions/session_tags_response.py">SessionTagsResponse</a></code>
- <code title="post /v3/organizations/{org_id}/sessions/{devin_id}/tags">client.organizations.sessions.tags.<a href="./src/devin_platform/resources/organizations/sessions/tags.py">append</a>(devin_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/sessions/tag_append_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/session_tags_response.py">SessionTagsResponse</a></code>
- <code title="put /v3/organizations/{org_id}/sessions/{devin_id}/tags">client.organizations.sessions.tags.<a href="./src/devin_platform/resources/organizations/sessions/tags.py">replace</a>(devin_id, \*, org_id, \*\*<a href="src/devin_platform/types/organizations/sessions/tag_replace_params.py">params</a>) -> <a href="./src/devin_platform/types/enterprise/sessions/session_tags_response.py">SessionTagsResponse</a></code>

# Beta1

## Enterprise

Types:

```python
from devin_platform.types.beta1 import PaginatedResponse
```

Methods:

- <code title="get /v3beta1/enterprise/guardrail-violations">client.beta1.enterprise.<a href="./src/devin_platform/resources/beta1/enterprise/enterprise.py">list_guardrail_violations</a>(\*\*<a href="src/devin_platform/types/beta1/enterprise_list_guardrail_violations_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/paginated_response.py">PaginatedResponse</a></code>

### Organizations

Methods:

- <code title="get /v3beta1/enterprise/organizations/{org_id}/guardrail-violations">client.beta1.enterprise.organizations.<a href="./src/devin_platform/resources/beta1/enterprise/organizations.py">list_guardrail_violations</a>(org_id, \*\*<a href="src/devin_platform/types/beta1/enterprise/organization_list_guardrail_violations_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/paginated_response.py">PaginatedResponse</a></code>

### ServiceUsers

#### APIKeys

Types:

```python
from devin_platform.types.beta1.enterprise.service_users import (
    APIKey,
    APIKeyWithToken,
    APIKeyListResponse,
)
```

Methods:

- <code title="post /v3beta1/enterprise/service-users/{service_user_id}/api-keys">client.beta1.enterprise.service_users.api_keys.<a href="./src/devin_platform/resources/beta1/enterprise/service_users/api_keys.py">create</a>(service_user_id, \*\*<a href="src/devin_platform/types/beta1/enterprise/service_users/api_key_create_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/enterprise/service_users/api_key_with_token.py">APIKeyWithToken</a></code>
- <code title="get /v3beta1/enterprise/service-users/{service_user_id}/api-keys">client.beta1.enterprise.service_users.api_keys.<a href="./src/devin_platform/resources/beta1/enterprise/service_users/api_keys.py">list</a>(service_user_id, \*\*<a href="src/devin_platform/types/beta1/enterprise/service_users/api_key_list_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/enterprise/service_users/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v3beta1/enterprise/service-users/{service_user_id}/api-keys/{api_key_id}">client.beta1.enterprise.service_users.api_keys.<a href="./src/devin_platform/resources/beta1/enterprise/service_users/api_keys.py">revoke</a>(api_key_id, \*, service_user_id) -> <a href="./src/devin_platform/types/beta1/enterprise/service_users/api_key.py">APIKey</a></code>
- <code title="post /v3beta1/enterprise/service-users/{service_user_id}/api-keys/{api_key_id}/rotate">client.beta1.enterprise.service_users.api_keys.<a href="./src/devin_platform/resources/beta1/enterprise/service_users/api_keys.py">rotate</a>(api_key_id, \*, service_user_id, \*\*<a href="src/devin_platform/types/beta1/enterprise/service_users/api_key_rotate_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/enterprise/service_users/api_key_with_token.py">APIKeyWithToken</a></code>

## Organizations

### Repositories

Types:

```python
from devin_platform.types.beta1.organizations import RepositoryListResponse
```

Methods:

- <code title="get /v3beta1/organizations/{org_id}/repositories">client.beta1.organizations.repositories.<a href="./src/devin_platform/resources/beta1/organizations/repositories/repositories.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/beta1/organizations/repository_list_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/organizations/repository_list_response.py">RepositoryListResponse</a></code>

#### Indexing

Types:

```python
from devin_platform.types.beta1.organizations.repositories import (
    RepoIndexJob,
    RepoIndexingStatus,
    RepositoryIndexing,
    IndexingListResponse,
    IndexingBulkIndexResponse,
    IndexingBulkRemoveResponse,
)
```

Methods:

- <code title="get /v3beta1/organizations/{org_id}/repositories/indexing">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">list</a>(org_id, \*\*<a href="src/devin_platform/types/beta1/organizations/repositories/indexing_list_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/indexing_list_response.py">IndexingListResponse</a></code>
- <code title="put /v3beta1/organizations/{org_id}/repositories/indexing">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">bulk_index</a>(org_id, \*\*<a href="src/devin_platform/types/beta1/organizations/repositories/indexing_bulk_index_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/indexing_bulk_index_response.py">IndexingBulkIndexResponse</a></code>
- <code title="delete /v3beta1/organizations/{org_id}/repositories/indexing">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">bulk_remove</a>(org_id, \*\*<a href="src/devin_platform/types/beta1/organizations/repositories/indexing_bulk_remove_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/indexing_bulk_remove_response.py">IndexingBulkRemoveResponse</a></code>
- <code title="get /v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">get_status</a>(repository_path, \*, org_id) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/repo_indexing_status.py">RepoIndexingStatus</a></code>
- <code title="put /v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">index</a>(repository_path, \*, org_id, \*\*<a href="src/devin_platform/types/beta1/organizations/repositories/indexing_index_params.py">params</a>) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/repository_indexing.py">RepositoryIndexing</a></code>
- <code title="delete /v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">remove</a>(repository_path, \*, org_id) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/repository_indexing.py">RepositoryIndexing</a></code>
- <code title="delete /v3beta1/organizations/{org_id}/repositories/{repository_path}/indexing/branches/{branch_name}">client.beta1.organizations.repositories.indexing.<a href="./src/devin_platform/resources/beta1/organizations/repositories/indexing.py">remove_branch</a>(branch_name, \*, org_id, repository_path) -> <a href="./src/devin_platform/types/beta1/organizations/repositories/repository_indexing.py">RepositoryIndexing</a></code>
