# 🌤️ Assistente Inteligente de Clima

Este projeto consiste em um sistema automatizado e integrado que une uma aplicação cliente local desenvolvida em **Python** a um fluxo de trabalho orquestrado no **n8n**. O objetivo principal é capturar a intenção de consulta de um utilizador para uma determinada cidade, buscar os dados meteorológicos em tempo real por meio de uma API pública e processar essas informações através de um motor de regras customizado em **JavaScript** para fornecer recomendações personalizadas de roupas e atividades.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

O ecossistema foi projetado utilizando o conceito de microsserviços desacoplados e comunicação baseada em eventos via requisições HTTP assíncronas. 

> **Fluxo da Aplicação:**
> 1. **Cliente Python:** Envia a cidade digitada via HTTP POST.
> 2. **n8n (Webhook Receptor):** Recebe o dado no modo *Production* e mantém a conexão aberta.
> 3. **API Open-Meteo:** O n8n faz a requisição para buscar as coordenadas e o clima atual.
> 4. **n8n (Nó Code - JavaScript):** Atua como um Sistema Especialista (Rule-Based AI), analisando os dados brutos e definindo as recomendações de vestuário.
> 5. **n8n (Respond to Webhook):** Devolve a resposta estruturada em JSON.
> 6. **Cliente Python:** Exibe a recomendação no terminal e salva os dados no arquivo local `historico.txt`.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Cliente:** Python 3.x (Responsável pelo loop do menu, inputs, requisições HTTP locais e gerência do arquivo de log).
* **Plataforma de Automação:** n8n (Configurado em modo *Published* para execução contínua e assíncrona).
* **Linguagem de Backend / Regras:** JavaScript / Node.js (Executado de forma nativa e isolada dentro do ecossistema n8n).
* **Provedor de Dados:** API Open-Meteo (Acesso a dados climáticos globais em tempo real sem necessidade de autenticação).
* **Persistência de Dados:** Sistema de Arquivos Nativo (`historico.txt`).

---


## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python instalado na máquina.
* n8n rodando localmente ou na nuvem.
* Biblioteca `requests` do Python instalada:
  ```bash
  pip install requests


## Estrutura do n8n
<img width="986" height="286" alt="image" src="https://github.com/user-attachments/assets/84523d3e-04c8-4752-b79e-be0038244a8e" />
