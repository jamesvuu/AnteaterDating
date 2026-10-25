# AnteaterDating

A UCI-focused adaptation of the BruinDating full-stack student matching project.

> **Development status:** Source migration in progress. Not yet built, tested end-to-end, deployed, or approved for real student use. The frontend's original binary image assets and lockfile have not yet been migrated, and existing chat/OAuth integration issues remain.

## Stack
- Frontend: Next.js, React, TypeScript
- Backend: Python, Django REST Framework, Django Channels
- Database: PostgreSQL
- Authentication: Google OAuth, JWT, and UCI email-domain validation
- Features in source: student profiles, onboarding questionnaire, discovery, mutual-like matching, conversation views

## Structure
- `frontend/`: Next.js pages, UI components, and API client
- `backend/`: Django apps for authentication, profiles, matching, and chat
- `docs/`: setup and development notes

## Local development
See [docs/setup.md](docs/setup.md). Create local environment files from the included examples, provision PostgreSQL and a Google OAuth application, then install frontend and backend dependencies. Never commit credentials.

## Before deploying
1. Restore or replace missing original image assets and generate a compatible dependency lockfile.
2. Validate UCI OAuth redirect URIs and the allowed email domains; verify that non-UCI users are rejected.
3. Fix the chat POST handler and reconcile REST polling with the existing Channels consumer.
4. Review token handling, authentication, authorization, privacy, and production security.
5. Run Django checks/tests, frontend lint/build, and end-to-end tests with test accounts.

## Attribution
Adapted with permission from [BruinDating](https://github.com/BruinDating/bruindating), originally created for UCLA CS 35L by Burak Arslan, Charles Zhu, Luke Yamaguchi, Jason Vu, and Xiaojin Zuo. The upstream repository does not declare a license; this adaptation is not presented as independently authored from scratch.
