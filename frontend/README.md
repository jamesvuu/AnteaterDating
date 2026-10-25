# Anteater Dating frontend

Next.js and TypeScript client for Anteater Dating, with Mantine UI components and a Django REST API.

See the [project overview](../README.md), [local setup guide](../docs/setup.md), and [development notes](../docs/development.md).

```bash
cp .env.example .env.local
yarn install --frozen-lockfile
yarn dev
```

Configure and start the backend before testing authenticated features. The API base URL is read from `NEXT_PUBLIC_BACKEND_URL`.

| Command | Purpose |
| --- | --- |
| `yarn dev` | Start the development server |
| `yarn build` | Build the production client |
| `yarn start` | Serve an existing production build |
| `yarn lint` | Run the configured linter |
