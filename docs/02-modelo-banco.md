# Modelo do Banco de Dados

## Objetivo

Descrever a estrutura do banco de dados utilizada pela aplicação, incluindo tabelas, campos principais e relacionamentos.

---

# Tabelas

## Usuários

| Campo | Tipo | Descrição |
|--------|------|-----------|
| id | INT | Identificador único |
| nome | VARCHAR | Nome do usuário |
| email | VARCHAR | E-mail |
| senha | VARCHAR | Senha criptografada |
| tipo | ENUM | Usuário, Técnico ou Administrador |

---

## Chamados

| Campo | Tipo | Descrição |
|--------|------|-----------|
| id | INT | Identificador único |
| titulo | VARCHAR | Título do chamado |
| descricao | TEXT | Descrição do problema |
| prioridade | ENUM | Baixa, Média, Alta ou Crítica |
| status | ENUM | Status atual (inicia como aberto) |
| data_criacao | DATETIME | Data de abertura |
| data_fechamento | DATETIME | Data de encerramento (opcional) |
| id_usuario | FK | Usuário que abriu o chamado |
| id_tecnico | FK | Técnico responsável (opcional) |
| id_categoria | FK | Categoria do chamado |

---

## Comentários

| Campo | Tipo | Descrição |
|--------|------|-----------|
| id | INT | Identificador único |
| texto | TEXT | Comentário |
| data_criacao | DATETIME | Data do comentário |
| id_usuario | FK | Autor do comentário |
| id_chamado | FK | Chamado relacionado |

---

## Categorias

| Campo | Tipo | Descrição |
|--------|------|-----------|
| id | INT | Identificador único |
| nome | VARCHAR | Nome da categoria |

---

# Relacionamentos

- Um usuário pode abrir vários chamados.
- Um técnico pode atender vários chamados.
- Um chamado pertence a uma categoria.
- Um chamado pode possuir vários comentários.
- Um usuário pode realizar vários comentários.

