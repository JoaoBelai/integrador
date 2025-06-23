# 🏆 Projeto Integrador - E-commerce de Itens Históricos do Esporte - Legacy Locker

Este projeto foi desenvolvido como parte do Projeto Integrador do SENAI. A proposta era criar um **e-commerce visual** utilizando apenas **HTML e CSS**, complementado por automações em **C** e **Python** voltadas para o controle de estoque e notificações.

> ⚠️ **Importante**: Este site é apenas **visual** e **não possui funcionalidades completas** de um e-commerce real (como carrinho de compras, login ou banco de dados). O objetivo foi simular a interface de um sistema de vendas.

---

## 📌 Objetivo

Desenvolver uma interface de loja virtual com foco em produtos históricos do esporte — como camisas autografadas, bolas icônicas, tênis autografados e relíquias esportivas — e integrar soluções externas para controle e notificação de estoque.

---

## 🧱 Tecnologias Utilizadas

- **HTML5 / CSS3** – Estrutura e visual do site
- **C** – Monitoramento físico do estoque com sensores simulados
- **Python** – Envio automatizado de alertas por WhatsApp e e-mail
- **OpenSSL** – Criação de um certificado SSL autoassinado para simular uma conexão segura

---

## 🌐 Funcionalidades

### 🎨 Site Visual (HTML e CSS)
- Interface estilizada de uma loja virtual com páginas de produtos, destaques e formulário de cadastro.
- Design inspirado em grandes sites de e-commerce com foco esportivo.
- Construída sem uso de frameworks.

### 🔐 Certificado SSL Autoassinado
- Geração de certificado para simulação de uma conexão segura (HTTPS).
- Processo feito via terminal utilizando `openssl`.

### 📦 Monitoramento de Estoque (C)
- Código em C que simula sensores em uma esteira de estoque.
- Mede o nível de itens disponíveis e exporta os dados para uma planilha.

### 📲 Notificações Automáticas (Python)
- Scripts em Python que:
  - Enviam mensagens por WhatsApp usando bibliotecas como `pyautogui`.
  - Disparam e-mails informando o nível do estoque.

---

## 🎨 Link do Figma
- https://www.figma.com/design/hpXqQBsXZemDNmlvrSKUDA/Untitled?node-id=444-1726&t=2u9sK1bZjvJsKh0G-0
