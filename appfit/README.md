# AppFit

Aplicação de exemplo para gestão de saúde e condicionamento.

## Uso rápido

```bash
cp .env.example .env
docker compose -f infra/docker-compose.yml up --build
```

Acessos:
- API: http://localhost:8000/healthz
- AI: http://localhost:8001
- Web: http://localhost:3000

Credenciais seed: `demo@appfit.io` / `demo123`

Conectar Strava (modo dev): vá em `/settings` na web. Para testes sem Strava, faça upload de um CSV de atividades via rota `/api/v1/strava/sync`.

Aviso: este projeto não é um dispositivo médico. Use com bom senso.
