import streamlit as st
import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

st.set_page_config(
    page_title="FinGuard IA",
    page_icon="💸",
    layout="centered"
)


def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_dados():
    transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
    perfil = carregar_json(DATA_DIR / "perfil_usuario.json")
    categorias = carregar_json(DATA_DIR / "categorias_gastos.json")
    dicas = carregar_json(DATA_DIR / "dicas_financeiras.json")

    return transacoes, perfil, categorias, dicas


def identificar_categoria(pergunta, categorias):
    pergunta = pergunta.lower()

    for item in categorias:
        categoria = item["categoria"].lower()
        if categoria in pergunta:
            return item["categoria"]

    termos_categoria = {
        "delivery": "Alimentação",
        "restaurante": "Alimentação",
        "comida": "Alimentação",
        "mercado": "Alimentação",
        "supermercado": "Alimentação",
        "transporte": "Transporte",
        "uber": "Transporte",
        "aplicativo": "Transporte",
        "assinatura": "Assinaturas",
        "streaming": "Assinaturas",
        "compra": "Compras",
        "compras": "Compras",
        "farmácia": "Saúde",
        "saúde": "Saúde",
        "academia": "Saúde",
        "energia": "Contas Fixas",
        "internet": "Contas Fixas",
        "conta": "Contas Fixas"
    }

    for termo, categoria in termos_categoria.items():
        if termo in pergunta:
            return categoria

    return None


def buscar_dica(pergunta, dicas):
    pergunta = pergunta.lower()

    for dica in dicas:
        tema = dica["tema"].lower()
        if tema in pergunta:
            return dica

    if "economizar" in pergunta or "economia" in pergunta:
        return dicas[0]

    if "controle" in pergunta or "gastos" in pergunta:
        return dicas[1]

    if "delivery" in pergunta:
        return dicas[2]

    if "impulso" in pergunta:
        return dicas[3]

    return None


def gerar_resposta(pergunta, transacoes, perfil, categorias, dicas):
    pergunta_limpa = pergunta.strip().lower()

    if not pergunta_limpa:
        return "Por favor, digite uma pergunta para que eu possa ajudar."

    termos_risco = [
        "investir",
        "investimento",
        "ações",
        "acao",
        "cripto",
        "criptomoeda",
        "renda variável",
        "ganhar dinheiro rápido",
        "ficar rico"
    ]

    if any(termo in pergunta_limpa for termo in termos_risco):
        return (
            "Não posso recomendar investimentos específicos ou prometer ganhos financeiros. "
            "Posso ajudar com orientações educativas gerais, como organizar seu orçamento, "
            "acompanhar seus gastos e criar uma reserva financeira antes de tomar decisões."
        )

    if "meus gastos estão altos" in pergunta_limpa or "gastos estão altos" in pergunta_limpa:
        return (
            "Para responder com mais segurança, preciso de mais contexto. "
            "Informe qual período você deseja analisar e qual categoria de gastos quer avaliar, "
            "por exemplo: alimentação, transporte, compras, assinaturas, saúde ou contas fixas."
        )

    categoria_identificada = identificar_categoria(pergunta, categorias)
    dica_identificada = buscar_dica(pergunta, dicas)

    if categoria_identificada:
        gastos_categoria = transacoes[
            (transacoes["categoria"] == categoria_identificada) &
            (transacoes["tipo"] == "Despesa")
        ]

        total_categoria = gastos_categoria["valor"].sum()
        limite = perfil["limite_alerta_gastos"].get(categoria_identificada)

        dados_categoria = next(
            item for item in categorias
            if item["categoria"] == categoria_identificada
        )

        resposta = (
            f"Identifiquei que sua dúvida está relacionada à categoria **{categoria_identificada}**.\n\n"
            f"Com base na base de conhecimento, essa categoria representa: "
            f"{dados_categoria['descricao']}\n\n"
            f"No período analisado, o total fictício registrado nessa categoria foi de "
            f"**R$ {total_categoria:.2f}**."
        )

        if limite is not None:
            if total_categoria > limite:
                resposta += (
                    f"\n\nEsse valor está **acima** do limite de alerta definido para a categoria, "
                    f"que é de **R$ {limite:.2f}**."
                )
            else:
                resposta += (
                    f"\n\nEsse valor está **dentro** do limite de alerta definido para a categoria, "
                    f"que é de **R$ {limite:.2f}**."
                )

        resposta += (
            f"\n\n**Recomendação geral:** {dados_categoria['recomendacao_geral']}\n\n"
            "Como próximo passo, recomendo acompanhar essa categoria nos próximos dias "
            "e definir um limite de gasto realista."
        )

        return resposta

    if dica_identificada:
        return (
            f"**Dica financeira:** {dica_identificada['dica']}\n\n"
            f"**Próximo passo sugerido:** {dica_identificada['proximo_passo']}"
        )

    return (
        "Não encontrei informações suficientes na base de conhecimento para responder com segurança. "
        "Tente informar uma categoria de gasto, como alimentação, transporte, compras, assinaturas, saúde ou contas fixas."
    )


def main():
    st.title("💸 FinGuard IA")
    st.subheader("Assistente Inteligente de Alerta de Gastos")

    st.write(
        "Faça uma pergunta sobre seus gastos, economia pessoal ou categorias de despesas. "
        "O agente responderá com base na base de conhecimento disponível."
    )

    transacoes, perfil, categorias, dicas = carregar_dados()

    with st.expander("Ver perfil financeiro fictício"):
        st.json(perfil)

    pergunta = st.text_input("Digite sua pergunta:")

    if st.button("Enviar pergunta"):
        resposta = gerar_resposta(pergunta, transacoes, perfil, categorias, dicas)
        st.markdown("### Resposta do FinGuard IA")
        st.markdown(resposta)

    with st.expander("Ver base de transações fictícias"):
        st.dataframe(transacoes)

    with st.expander("Exemplos de perguntas para testar"):
        st.markdown(
            """
            - Estou gastando muito com delivery?
            - Meus gastos com alimentação estão altos?
            - Como posso economizar mais?
            - Quais gastos de transporte tenho?
            - Onde devo investir para ganhar dinheiro rápido?
            - Meus gastos estão altos?
            """
        )


if __name__ == "__main__":
    main()
