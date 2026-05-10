# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ..session_pull_request import SessionPullRequest
from .session_insights_note_usage_item import SessionInsightsNoteUsageItem

__all__ = [
    "SessionInsights",
    "Analysis",
    "AnalysisActionItem",
    "AnalysisClassification",
    "AnalysisIssue",
    "AnalysisNoteUsage",
    "AnalysisSuggestedPrompt",
    "AnalysisSuggestedPromptFeedbackItem",
    "AnalysisTimeline",
]


class AnalysisActionItem(BaseModel):
    action_item: str

    issue_id: Optional[str] = None

    type: Optional[Literal["machine_setup", "repo_config", "knowledge", "prompt_improvement", "other"]] = None


class AnalysisClassification(BaseModel):
    category: str

    confidence: float

    programming_languages: Optional[List[str]] = None

    tools_and_frameworks: Optional[List[str]] = None


class AnalysisIssue(BaseModel):
    id: str

    impact: str

    issue: str

    label: str


class AnalysisNoteUsage(BaseModel):
    bad_usages: Optional[List[SessionInsightsNoteUsageItem]] = None

    good_usages: Optional[List[SessionInsightsNoteUsageItem]] = None


class AnalysisSuggestedPromptFeedbackItem(BaseModel):
    details: str

    excerpt: str

    summary: str

    issue_id: Optional[str] = None


class AnalysisSuggestedPrompt(BaseModel):
    original_prompt: str

    suggested_prompt: str

    feedback_items: Optional[List[AnalysisSuggestedPromptFeedbackItem]] = None


class AnalysisTimeline(BaseModel):
    description: str

    title: str

    color: Optional[str] = None

    issue_id: Optional[str] = None


class Analysis(BaseModel):
    """AI-generated session analysis. None if analysis has not completed."""

    action_items: Optional[List[AnalysisActionItem]] = None

    classification: Optional[AnalysisClassification] = None

    issues: Optional[List[AnalysisIssue]] = None

    note_usage: Optional[AnalysisNoteUsage] = None

    suggested_prompt: Optional[AnalysisSuggestedPrompt] = None

    timeline: Optional[List[AnalysisTimeline]] = None


class SessionInsights(BaseModel):
    """Session details augmented with quantitative metrics and AI analysis.

    Extends SessionResponse with additional fields that require extra queries.
    """

    acus_consumed: float

    created_at: int

    num_devin_messages: int
    """Number of Devin messages sent during the session."""

    num_user_messages: int
    """Number of user messages sent during the session."""

    org_id: str

    pull_requests: List[SessionPullRequest]

    session_id: str

    session_size: Literal["xs", "s", "m", "l", "xl"]
    """Session size classification based on ACU usage and message count."""

    status: Literal["new", "creating", "claimed", "running", "exit", "error", "suspended", "resuming"]

    tags: List[str]

    updated_at: int

    url: str

    analysis: Optional[Analysis] = None
    """AI-generated session analysis. None if analysis has not completed."""

    child_session_ids: Optional[List[str]] = None

    is_advanced: Optional[bool] = None

    is_archived: Optional[bool] = None

    parent_session_id: Optional[str] = None

    playbook_id: Optional[str] = None

    service_user_id: Optional[str] = None

    status_detail: Optional[
        Literal[
            "working",
            "waiting_for_user",
            "waiting_for_approval",
            "finished",
            "inactivity",
            "user_request",
            "usage_limit_exceeded",
            "out_of_credits",
            "out_of_quota",
            "no_quota_allocation",
            "payment_declined",
            "org_usage_limit_exceeded",
            "error",
        ]
    ] = None
    """Additional detail about the session's current status.

    When status is 'running': 'working' (actively working), 'waiting_for_user'
    (needs user input), 'waiting_for_approval' (awaiting action approval in safe
    mode), or 'finished' (task complete). When status is 'suspended': the reason for
    suspension such as 'inactivity', 'user_request', 'usage_limit_exceeded',
    'out_of_credits', 'out_of_quota', 'no_quota_allocation', 'payment_declined',
    'org_usage_limit_exceeded', or 'error'. Only populated on get/list endpoints.
    """

    structured_output: Optional[Dict[str, object]] = None
    """Validated structured output from the session.

    Only populated on get/list endpoints.
    """

    title: Optional[str] = None

    user_id: Optional[str] = None
