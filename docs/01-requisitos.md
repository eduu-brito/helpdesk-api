# Requisitos do Sistema

## Escopo da versão 1.0

Nesta primeira versão, o sistema permitirá:

- Autenticação de usuários.
- Gerenciamento de usuários.
- Gerenciamento de chamados.
- Comentários em chamados.
- Dashboard básico com estatísticas.

## Objetivo

Desenvolver uma API REST para gerenciamento de chamados de suporte de TI, permitindo que usuários registrem problemas, técnicos acompanhem os atendimentos e administradores gerenciem o sistema.
Este projeto tem como objetivo aplicar boas práticas de desenvolvimento de APIs utilizando Python, FastAPI e MySQL.

## Tipos de usuários
### Usuário

Responsável por abrir e acompanhar seus chamados.

### Técnico

Responsável por atender e resolver chamados.

### Administrador

Responsável pelo gerenciamento de usuários e do sistema.

## Funcionalidades
### Autenticação
 - Login
 - Logout

### Gerenciamento de Usuários
 - Cadastrar usuário
 - Editar usuário
 - Excluir usuário
 - Listar usuários

### Gerenciamento de Chamados
 - Abrir chamado
 - Editar chamado
 - Alterar status
 - Alterar prioridade
 - Fechar chamado
 - Cancelar chamado
 - Atribuir técnico
 - Listar chamados
 - Visualizar detalhes do chamado

### Comentários
 - Adicionar e visualizar comentários

### Dashboard
 - Total de chamados
 - Chamados abertos
 - Chamados em andamento
 - Chamados resolvidos
 - Chamados fechados

## Regras de negócio

- Apenas administradores podem cadastrar, editar e excluir usuários.
- Um usuário pode visualizar apenas os chamados que criou.
- Um chamado deve possuir título, descrição, prioridade e categoria.
- Chamados fechados não podem ser editados.
- Um técnico só pode alterar chamados atribuídos a ele.
- O status inicial de todo chamado deve ser "Aberto".