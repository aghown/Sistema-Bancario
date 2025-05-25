# 🏦 Sistema Bancário em Python - Versão 1

Este projeto faz parte da trilha de Python da DIO e tem como objetivo aplicar na prática os fundamentos da linguagem através da criação de um **sistema bancário simples**, com funcionalidades reais de um banco digital.

## 💡 Sobre o Projeto

Nesta primeira versão do sistema bancário, desenvolvemos uma aplicação **em linha de comando (CLI)** que simula operações bancárias básicas como depósitos, saques e consulta de extrato.

Este projeto **não possui sistema de login nem controle de múltiplos usuários**. Todos os dados são armazenados em memória durante a execução do programa (sem banco de dados).

## ✅ Funcionalidades Implementadas

### 1. 📥 Operação de Depósito
- Permite ao usuário depositar um valor positivo em sua conta.
- Valores negativos ou iguais a zero **não são aceitos**.
- Cada depósito é registrado no extrato.

### 2. 💸 Operação de Saque
- O usuário pode realizar **até 3 saques por dia**.
- Cada saque tem um limite de **R$ 500,00** por operação.
- O saque só será permitido se houver saldo suficiente.
- Cada saque é registrado no extrato.

### 3. 📄 Operação de Extrato
- Exibe todas as transações realizadas (depósitos e saques).
- Mostra também o saldo atual da conta.

## 🚫 Limitações da Versão 1
- ❌ Não há suporte a múltiplos usuários ou contas.
- ❌ Não há sistema de login ou autenticação.
- ❌ Os dados são perdidos ao encerrar o programa (sem persistência).

## 🔗 Repositórios de Referência

- [Repositório oficial da trilha Python na DIO](https://github.com/digitalinnovationone/trilha-python-dio)
- [Código base do desafio](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)

---

📌 *Este é apenas o começo! Nas próximas versões, o sistema poderá evoluir com suporte a múltiplos usuários, autenticação, persistência de dados e uma interface mais interativa.*

---


