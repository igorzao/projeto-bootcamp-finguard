# FinGuard IA — Assistente Inteligente de Alerta de Gastos

## Sobre o projeto

O FinGuard IA é um assistente virtual com Inteligência Artificial Generativa criado para apoiar pessoas usuárias no controle de gastos pessoais.

O objetivo do agente é analisar dúvidas relacionadas a consumo, orçamento e economia, utilizando uma base de conhecimento organizada para responder de forma simples, educativa e segura.

Este projeto foi desenvolvido como parte do desafio "Construa Seu Assistente Virtual Com Inteligência Artificial", do Bootcamp de Dados da Afya/DIO.

## Problema que o agente resolve

Muitas pessoas têm dificuldade em entender seus próprios hábitos de consumo, identificar gastos excessivos e tomar decisões financeiras melhores no dia a dia.

O FinGuard IA busca ajudar nesse processo, oferecendo alertas, explicações simples e recomendações práticas com base nas informações disponíveis na base de conhecimento.

## Objetivo do assistente

O agente tem como objetivo:

- Identificar possíveis gastos acima do esperado;
- Ajudar a pessoa usuária a economizar;
- Explicar padrões de consumo de forma simples;
- Sugerir próximos passos financeiros;
- Informar quando não possuir dados suficientes para responder;
- Evitar respostas inventadas ou sem base.

## Persona do agente

O FinGuard IA possui uma comunicação formal, educativa, simples e prática.  
Ele atua como um orientador financeiro de apoio, sem substituir um profissional especializado.

## Funcionalidades principais

- Responder dúvidas sobre gastos;
- Consultar informações de uma base de conhecimento;
- Explicar categorias de despesas;
- Sugerir boas práticas de economia;
- Solicitar mais contexto quando necessário;
- Evitar alucinações em cenários de incerteza.

## Arquitetura da solução

Fluxo simplificado:

1. A pessoa usuária envia uma pergunta;
2. O agente verifica se possui contexto suficiente;
3. Caso não tenha contexto, solicita mais informações;
4. Caso tenha contexto, consulta a base de conhecimento;
5. O agente gera uma resposta clara e segura;
6. O agente sugere próximos passos práticos.

## Segurança e limites

Como o tema financeiro é sensível, o agente deve seguir algumas regras:

- Não inventar informações;
- Não prometer resultados financeiros;
- Não recomendar investimentos específicos;
- Não utilizar dados que não estejam na base de conhecimento;
- Informar quando não souber responder;
- Dar orientações apenas educativas e gerais.

## Estrutura do projeto

```text
finguard-ia/
│
├── README.md
├── data/
├── docs/
├── src/
└── assets/
```

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/igorzão/projeto-bootcamp-finguard.git
```

2. Acesse a pasta do projeto:

```bash
cd projeto-bootcamp-finguard
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
streamlit run src/app.py
```

5. Acesse o navegador para interagir com o agente.
