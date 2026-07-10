# 02 — Base de Conhecimento

## Objetivo da base de conhecimento

A base de conhecimento do FinGuard IA tem como objetivo reunir informações organizadas para apoiar as respostas do agente de forma segura e consistente.

Como o agente atua no contexto financeiro, ele deve consultar os dados disponíveis antes de responder e evitar qualquer informação inventada.

## Arquivos utilizados

A base de conhecimento foi estruturada com arquivos fictícios em CSV e JSON, localizados na pasta `data/`.

## 1. transacoes.csv

Este arquivo contém uma base fictícia de transações financeiras da pessoa usuária.

### Campos do arquivo

- `data`: data da transação;
- `descricao`: descrição do gasto ou receita;
- `categoria`: categoria financeira da transação;
- `valor`: valor da movimentação;
- `tipo`: classificação entre despesa ou receita.

### Finalidade

Esse arquivo permite ao agente identificar gastos por categoria, consultar valores registrados e apoiar análises simples sobre consumo.

## 2. perfil_usuario.json

Este arquivo contém informações fictícias sobre o perfil financeiro da pessoa usuária.

### Informações presentes

- Nome fictício da pessoa usuária;
- Renda mensal;
- Objetivo financeiro;
- Perfil de consumo;
- Limites de alerta por categoria.

### Finalidade

Esse arquivo ajuda o agente a personalizar suas respostas com base no perfil financeiro disponível.

## 3. categorias_gastos.json

Este arquivo contém a descrição das categorias de gastos utilizadas pelo agente.

### Informações presentes

- Nome da categoria;
- Descrição da categoria;
- Risco de excesso;
- Recomendação geral.

### Finalidade

Esse arquivo permite ao agente explicar melhor cada tipo de gasto e sugerir recomendações compatíveis com a categoria analisada.

## 4. dicas_financeiras.json

Este arquivo contém dicas financeiras educativas.

### Informações presentes

- Tema da dica;
- Orientação financeira;
- Próximo passo sugerido.

### Finalidade

Esse arquivo permite ao agente trazer recomendações simples e práticas para apoiar a pessoa usuária.

## Estratégia de uso da base

O FinGuard IA deve seguir a seguinte estratégia:

1. Receber a pergunta da pessoa usuária;
2. Identificar a intenção da pergunta;
3. Verificar se a base possui dados relacionados ao tema;
4. Consultar os arquivos disponíveis;
5. Gerar resposta apenas com base nas informações encontradas;
6. Informar quando não houver dados suficientes.

## Limitações da base

A base utilizada neste projeto é fictícia e foi criada apenas para fins educacionais.

Ela não representa dados reais de clientes, instituições financeiras ou qualquer pessoa física.

## Importância da base para evitar alucinação

Como o agente trabalha com um tema sensível, a base de conhecimento é essencial para reduzir o risco de respostas inventadas.

O agente deve deixar claro quando não encontrar informações suficientes para responder com segurança.
