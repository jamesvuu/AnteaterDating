# Development notes

## Current integration gaps

These observations come from the checked-in source, not a successful end-to-end run.

- **Message sending:** The frontend posts to `/chat/rooms/{id}/messages/`, but the backend `messages` action currently declares GET only. Message submission needs a backend POST handler before that flow can work.
- **OAuth callback:** The callback URL constructed in `auth_app/views.py` omits the trailing slash present in `auth_app/urls.py`. Align the configured and routed URI before testing authentication.
- **Transport:** The frontend uses REST polling every five seconds. A Channels consumer also exists, but it is not the active frontend message transport. The in-memory channel layer is limited to a single process.
- **Configuration:** Django reads `DEBUG` as a raw string. Frontend configuration exists in both `next.config.js` and `next.config.ts`; reconcile them when updating build configuration.
- **Deployment:** This is a development configuration. Authentication, authorization, dependency versions, and deployment settings need a separate review before a public launch.

## Checks

From `backend/` with the virtual environment active and local configuration ready:

```bash
python manage.py check
python manage.py test
```

Inspect the test modules before treating a passing command as meaningful coverage; existing test files include scaffolding.

From `frontend/` after installing dependencies:

```bash
yarn lint
yarn build
```

These are verification commands, not a claim that the current application passes them.

## Manual verification

Use local test accounts and data:

1. Complete Google sign-in and confirm the authenticated profile loads.
2. Complete onboarding, change profile fields, and verify persistence after reload.
3. Like profiles from two accounts and verify mutual matching.
4. Open the conversation, load message history, and verify message submission after implementing the missing POST handler.
5. Confirm a third account cannot read another pair's messages.

## Documentation cleanup validation

The documentation and environment examples were checked against the current source paths, settings, routes, and frontend environment references. No database credentials or OAuth client were provisioned, and no live user data was used. Runtime integration remains unverified.
