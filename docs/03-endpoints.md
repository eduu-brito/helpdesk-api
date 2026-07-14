# Endpoints da API

## Autenticação

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | /login | Realiza autenticação do usuário |

---

## Usuários

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | /usuarios | Cadastra um novo usuário |
| GET | /usuarios | Lista todos os usuários |
| GET | /usuarios/{id} | Busca um usuário |
| PUT | /usuarios/{id} | Atualiza um usuário |
| DELETE | /usuarios/{id} | Remove um usuário |

---

## Chamados

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | /chamados | Abre um chamado |
| GET | /chamados | Lista chamados |
| GET | /chamados/{id} | Busca um chamado |
| PUT | /chamados/{id} | Atualiza um chamado |
| PATCH | /chamados/{id}/status | Altera o status do chamado |

---

## Comentários

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | /comentarios | Adiciona comentário |
| GET | /chamados/{id}/comentarios/ | Lista comentários do chamado |

---

## Dashboard

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | /dashboard | Retorna estatísticas do sistema |