# Arquitetura do FinGuard funcionamento conceitual do agente FinGuard IA.

```mermaid
flowchart TD
    A[Usuário envia uma pergunta] --> B[Agente identifica a intenção]
    B --> C{Existe contexto suficiente?}
    C -- Não --> D[Agente solicita mais informações]
    C -- Sim --> E[Agente consulta a base de conhecimento]
    E --> F[Agente verifica regras de segurança]
    F --> G{Resposta pode ser gerada com segurança?}
    G -- Não --> H[Agente informa que não possui dados suficientes]
    G -- Sim --> I[Agente responde de forma clara e educativa]
    I --> J[Agente sugere próximo passo]
    J --> K[Fim]
```

## Explicação do fluxo

1. A pessoa usuária envia uma pergunta ao agente.
2. O agente identifica a intenção da pergunta.
3. O agente verifica se possui contexto suficiente para responder.
4. Caso falte informação, ele solicita mais detalhes.
5. Caso tenha informação suficiente, consulta a base de conhecimento.
6. Antes de responder, valida as regras de segurança e anti-alucinação.
7. Se a resposta puder ser gerada com segurança, apresenta uma resposta clara e educativa.
8. Ao final, sugere um próximo passo prático.
