# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.beta1.enterprise.service_users import api_key_list_params, api_key_create_params, api_key_rotate_params
from .....types.beta1.enterprise.service_users.api_key import APIKey
from .....types.beta1.enterprise.service_users.api_key_with_token import APIKeyWithToken
from .....types.beta1.enterprise.service_users.api_key_list_response import APIKeyListResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        service_user_id: str,
        *,
        name: str,
        expires_at: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyWithToken:
        """
        Create a new API key for a service user.

        The caller must have ManageAccountServiceUsers permission.

        Args:
          expires_at: Optional expiration as a UNIX timestamp in seconds. Must be in the future if
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return self._post(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys", service_user_id=service_user_id
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "expires_at": expires_at,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyWithToken,
        )

    def list(
        self,
        service_user_id: str,
        *,
        status: Literal["active", "revoked", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """
        List API keys for a service user, optionally filtered by status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return self._get(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys", service_user_id=service_user_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, api_key_list_params.APIKeyListParams),
            ),
            cast_to=APIKeyListResponse,
        )

    def revoke(
        self,
        api_key_id: str,
        *,
        service_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Revoke an API key for a service user.

        Returns 404 if the key is not found, 409 if already revoked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._delete(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys/{api_key_id}",
                service_user_id=service_user_id,
                api_key_id=api_key_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def rotate(
        self,
        api_key_id: str,
        *,
        service_user_id: str,
        new_key_expires_at: Optional[int] | Omit = omit,
        revoke_current: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyWithToken:
        """Rotate an API key for a service user.

        Creates a new key.

        By default revokes the old key; set revoke_current=false for
        graceful rollover where both keys remain active temporarily. Returns 404 if the
        key is not found, 400 if the key is not active.

        Args:
          new_key_expires_at: Optional expiration for the new key as a UNIX timestamp in seconds. Null for no
              expiration.

          revoke_current: Whether to revoke the current key. Set to False for graceful rollover.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._post(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys/{api_key_id}/rotate",
                service_user_id=service_user_id,
                api_key_id=api_key_id,
            ),
            body=maybe_transform(
                {
                    "new_key_expires_at": new_key_expires_at,
                    "revoke_current": revoke_current,
                },
                api_key_rotate_params.APIKeyRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyWithToken,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devin-platform-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        service_user_id: str,
        *,
        name: str,
        expires_at: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyWithToken:
        """
        Create a new API key for a service user.

        The caller must have ManageAccountServiceUsers permission.

        Args:
          expires_at: Optional expiration as a UNIX timestamp in seconds. Must be in the future if
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return await self._post(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys", service_user_id=service_user_id
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "expires_at": expires_at,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyWithToken,
        )

    async def list(
        self,
        service_user_id: str,
        *,
        status: Literal["active", "revoked", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """
        List API keys for a service user, optionally filtered by status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        return await self._get(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys", service_user_id=service_user_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, api_key_list_params.APIKeyListParams),
            ),
            cast_to=APIKeyListResponse,
        )

    async def revoke(
        self,
        api_key_id: str,
        *,
        service_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Revoke an API key for a service user.

        Returns 404 if the key is not found, 409 if already revoked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._delete(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys/{api_key_id}",
                service_user_id=service_user_id,
                api_key_id=api_key_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def rotate(
        self,
        api_key_id: str,
        *,
        service_user_id: str,
        new_key_expires_at: Optional[int] | Omit = omit,
        revoke_current: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyWithToken:
        """Rotate an API key for a service user.

        Creates a new key.

        By default revokes the old key; set revoke_current=false for
        graceful rollover where both keys remain active temporarily. Returns 404 if the
        key is not found, 400 if the key is not active.

        Args:
          new_key_expires_at: Optional expiration for the new key as a UNIX timestamp in seconds. Null for no
              expiration.

          revoke_current: Whether to revoke the current key. Set to False for graceful rollover.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_user_id:
            raise ValueError(f"Expected a non-empty value for `service_user_id` but received {service_user_id!r}")
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._post(
            path_template(
                "/v3beta1/enterprise/service-users/{service_user_id}/api-keys/{api_key_id}/rotate",
                service_user_id=service_user_id,
                api_key_id=api_key_id,
            ),
            body=await async_maybe_transform(
                {
                    "new_key_expires_at": new_key_expires_at,
                    "revoke_current": revoke_current,
                },
                api_key_rotate_params.APIKeyRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyWithToken,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.revoke = to_raw_response_wrapper(
            api_keys.revoke,
        )
        self.rotate = to_raw_response_wrapper(
            api_keys.rotate,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.revoke = async_to_raw_response_wrapper(
            api_keys.revoke,
        )
        self.rotate = async_to_raw_response_wrapper(
            api_keys.rotate,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.revoke = to_streamed_response_wrapper(
            api_keys.revoke,
        )
        self.rotate = to_streamed_response_wrapper(
            api_keys.rotate,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.revoke = async_to_streamed_response_wrapper(
            api_keys.revoke,
        )
        self.rotate = async_to_streamed_response_wrapper(
            api_keys.rotate,
        )
