# Local setup

Run the commands below from the repository root unless another directory is specified. These instructions reflect the checked-in configuration; end-to-end sign-in and messaging still have the integration gaps listed in [development notes](development.md).

## 1. Backend dependencies

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env-example .env
```

On Windows, activate with `.venv\Scripts\activate`.

## 2. Database and environment

Create a local PostgreSQL database and role with permission to use it. Set these values in `backend/.env`:

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Unique local Django signing key |
| `DEBUG` | Use `1` for local development; see the parsing caveat below |
| `DB_NAME` | Local database name |
| `DB_USER` | PostgreSQL role |
| `DB_PASSWORD` | Password for that role |
| `DB_HOST` | Usually `localhost` |
| `BACKEND_URL` | `http://localhost:8000` |
| `FRONTEND_URL` | `http://localhost:3000` |

Generate a local key after installing dependencies:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Paste it into `.env`. The database port is currently fixed to `5432` in Django settings. `DEBUG` is currently read as a string, so `DEBUG=False` is still truthy; this configuration needs adjustment before deployment.

## 3. Google sign-in configuration

The backend reads a Google OAuth **web application** client configuration from `backend/client_secret.json`. Obtain that file from your own Google Cloud project and keep it local. Configure the OAuth consent screen and any required test users for your development project.

The code currently constructs `http://localhost:8000/auth/callback` while the Django route ends in `/auth/callback/`. Align those paths and register the identical redirect URI in the OAuth client before testing sign-in. For local HTTP testing only, oauthlib may require `OAUTHLIB_INSECURE_TRANSPORT=1`; never enable that for a deployed service.

There is no separate DUO integration in this repository.

## 4. Initialize and run the backend

With PostgreSQL running and `.env` configured:

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

## 5. Start the frontend

In a second terminal, from the repository root:

```bash
cd frontend
cp .env.example .env.local
yarn install --frozen-lockfile
yarn dev
```

The frontend uses `NEXT_PUBLIC_BACKEND_URL=http://localhost:8000`. Restart the development server after changing environment values. Use `localhost` consistently because the backend's CORS configuration allows `http://localhost:3000`.

Open `http://localhost:3000`. Sign-in requires your configured OAuth client and an account accepted by the backend's UCI email check.
