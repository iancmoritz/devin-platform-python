# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from devin_platform import DevinPlatform, AsyncDevinPlatform
from devin_platform._utils import parse_datetime
from devin_platform.types.organizations import (
    Schedule,
    ScheduleListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
            agent="devin",
            bypass_approval=True,
            create_as_user_id="create_as_user_id",
            frequency="frequency",
            interval_count=0,
            notify_on="always",
            playbook_id="playbook_id",
            schedule_type="recurring",
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            slack_channel_id="slack_channel_id",
            slack_team_id="slack_team_id",
            tags=["string"],
            target_devin_id="target_devin_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DevinPlatform) -> None:
        response = client.organizations.schedules.with_raw_response.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DevinPlatform) -> None:
        with client.organizations.schedules.with_streaming_response.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.schedules.with_raw_response.create(
                org_id="",
                name="name",
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.retrieve(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DevinPlatform) -> None:
        response = client.organizations.schedules.with_raw_response.retrieve(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DevinPlatform) -> None:
        with client.organizations.schedules.with_streaming_response.retrieve(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.schedules.with_raw_response.retrieve(
                schedule_id="sched-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.organizations.schedules.with_raw_response.retrieve(
                schedule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
            agent="devin",
            bypass_approval=True,
            enabled=True,
            frequency="frequency",
            interval_count=0,
            name="name",
            notify_on="always",
            playbook_id="playbook_id",
            prompt="prompt",
            run_as_user_id="run_as_user_id",
            schedule_type="recurring",
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            slack_channel_id="slack_channel_id",
            slack_team_id="slack_team_id",
            tags=["string"],
            target_devin_id="target_devin_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: DevinPlatform) -> None:
        response = client.organizations.schedules.with_raw_response.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: DevinPlatform) -> None:
        with client.organizations.schedules.with_streaming_response.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.schedules.with_raw_response.update(
                schedule_id="sched-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.organizations.schedules.with_raw_response.update(
                schedule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.list(
            org_id="org_id",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.list(
            org_id="org_id",
            limit=1,
            offset=0,
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DevinPlatform) -> None:
        response = client.organizations.schedules.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DevinPlatform) -> None:
        with client.organizations.schedules.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.schedules.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: DevinPlatform) -> None:
        schedule = client.organizations.schedules.delete(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DevinPlatform) -> None:
        response = client.organizations.schedules.with_raw_response.delete(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DevinPlatform) -> None:
        with client.organizations.schedules.with_streaming_response.delete(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.schedules.with_raw_response.delete(
                schedule_id="sched-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.organizations.schedules.with_raw_response.delete(
                schedule_id="",
                org_id="org_id",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
            agent="devin",
            bypass_approval=True,
            create_as_user_id="create_as_user_id",
            frequency="frequency",
            interval_count=0,
            notify_on="always",
            playbook_id="playbook_id",
            schedule_type="recurring",
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            slack_channel_id="slack_channel_id",
            slack_team_id="slack_team_id",
            tags=["string"],
            target_devin_id="target_devin_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.schedules.with_raw_response.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.schedules.with_streaming_response.create(
            org_id="org_id",
            name="name",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.create(
                org_id="",
                name="name",
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.retrieve(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.schedules.with_raw_response.retrieve(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.schedules.with_streaming_response.retrieve(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.retrieve(
                schedule_id="sched-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.retrieve(
                schedule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
            agent="devin",
            bypass_approval=True,
            enabled=True,
            frequency="frequency",
            interval_count=0,
            name="name",
            notify_on="always",
            playbook_id="playbook_id",
            prompt="prompt",
            run_as_user_id="run_as_user_id",
            schedule_type="recurring",
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            slack_channel_id="slack_channel_id",
            slack_team_id="slack_team_id",
            tags=["string"],
            target_devin_id="target_devin_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.schedules.with_raw_response.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.schedules.with_streaming_response.update(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.update(
                schedule_id="sched-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.update(
                schedule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.list(
            org_id="org_id",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.list(
            org_id="org_id",
            limit=1,
            offset=0,
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.schedules.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.schedules.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevinPlatform) -> None:
        schedule = await async_client.organizations.schedules.delete(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        response = await async_client.organizations.schedules.with_raw_response.delete(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Schedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevinPlatform) -> None:
        async with async_client.organizations.schedules.with_streaming_response.delete(
            schedule_id="sched-abc123def456",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Schedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevinPlatform) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.delete(
                schedule_id="sched-abc123def456",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.organizations.schedules.with_raw_response.delete(
                schedule_id="",
                org_id="org_id",
            )
