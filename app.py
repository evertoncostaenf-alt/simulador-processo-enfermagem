import streamlit as st

st.set_page_config(
    page_title="Clínica na Prática",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 CLÍNICA NA PRÁTICA")
st.header("Simulador do Processo de Enfermagem")

st.markdown("### Professor Everton Costa")

st.divider()

st.write(
    "Ferramenta educacional para treinamento do Processo de Enfermagem."
)

st.info(
    "Nesta primeira versão, vamos construir o simulador passo a passo."
)

# =========================================================
# 1. IDENTIFICAÇÃO DO PACIENTE
# =========================================================

st.subheader("👤 Identificação do paciente")

nome = st.text_input("Nome do paciente")

idade = st.number_input(
    "Idade",
    min_value=0,
    max_value=120,
    value=18
)

sexo = st.selectbox(
    "Sexo",
    ["Feminino", "Masculino", "Outro"]
)

queixa = st.text_area(
    "Queixa principal"
)

if st.button("▶️ Iniciar avaliação"):

    st.success("Avaliação iniciada!")

    st.write("**Paciente:**", nome)
    st.write("**Idade:**", idade)
    st.write("**Sexo:**", sexo)
    st.write("**Queixa principal:**", queixa)

# =========================================================
# 2. SINAIS VITAIS
# =========================================================

st.divider()

st.subheader("❤️ Sinais Vitais")

st.write(
    "Registre os sinais vitais apresentados pelo paciente."
)

col1, col2 = st.columns(2)

with col1:

    pressao = st.text_input(
        "🩸 Pressão arterial (mmHg)",
        placeholder="Ex.: 120/80"
    )

    frequencia_cardiaca = st.number_input(
        "❤️ Frequência cardíaca (bpm)",
        min_value=0,
        max_value=250,
        value=80
    )

    frequencia_respiratoria = st.number_input(
        "🫁 Frequência respiratória (irpm)",
        min_value=0,
        max_value=80,
        value=18
    )

with col2:

    spo2 = st.number_input(
        "🫧 Saturação de O₂ (%)",
        min_value=0,
        max_value=100,
        value=98
    )

    temperatura = st.number_input(
        "🌡️ Temperatura (°C)",
        min_value=30.0,
        max_value=45.0,
        value=36.5,
        step=0.1
    )

st.markdown("### 🔎 Avaliação dos sinais vitais")

if st.button("Analisar sinais vitais"):

    alertas = []

    if frequencia_cardiaca > 100:
        alertas.append(
            "❤️ Frequência cardíaca acima de 100 bpm."
        )

    if frequencia_cardiaca < 60:
        alertas.append(
            "❤️ Frequência cardíaca abaixo de 60 bpm."
        )

    if frequencia_respiratoria > 20:
        alertas.append(
            "🫁 Frequência respiratória elevada."
        )

    if frequencia_respiratoria < 12:
        alertas.append(
            "🫁 Frequência respiratória reduzida."
        )

    if spo2 < 95:
        alertas.append(
            "🫧 Saturação de O₂ abaixo de 95%."
        )

    if temperatura >= 37.8:
        alertas.append(
            "🌡️ Temperatura elevada."
        )

    if temperatura < 35.0:
        alertas.append(
            "🌡️ Temperatura abaixo de 35°C."
        )

    if not alertas:

        st.success(
            "✅ Nenhuma alteração foi identificada "
            "pelos critérios básicos deste simulador."
        )

    else:

        st.warning(
            "⚠️ Foram identificados os seguintes pontos:"
        )

        for alerta in alertas:
            st.write(alerta)

# =========================================================
# 3. ANAMNESE
# =========================================================

st.divider()

st.subheader("🔎 Anamnese")

st.write(
    "Realize a coleta das informações clínicas do paciente."
)

st.markdown("### 🗣️ História clínica")

historia_doenca = st.text_area(
    "História da doença atual",
    placeholder=(
        "Descreva quando os sintomas começaram, "
        "como evoluíram, fatores de melhora ou piora "
        "e outras informações relevantes."
    ),
    height=130
)

st.markdown("### 🧬 Antecedentes")

col1, col2 = st.columns(2)

with col1:

    antecedentes = st.text_area(
        "Antecedentes pessoais",
        placeholder=(
            "Doenças anteriores, cirurgias, "
            "internações etc."
        ),
        height=100
    )

    alergias = st.text_area(
        "Alergias",
        placeholder=(
            "Medicamentos, alimentos ou outras alergias."
        ),
        height=100
    )

with col2:

    medicamentos = st.text_area(
        "Medicamentos em uso",
        placeholder=(
            "Nome, dose e frequência, quando conhecidos."
        ),
        height=100
    )

    habitos = st.text_area(
        "Hábitos de vida",
        placeholder=(
            "Tabagismo, álcool, atividade física, "
            "alimentação etc."
        ),
        height=100
    )

st.markdown("### 🧠 Necessidades e sintomas")

col1, col2 = st.columns(2)

with col1:

    intensidade_dor = st.slider(
        "Intensidade da dor",
        min_value=0,
        max_value=10,
        value=0
    )

    qualidade_sono = st.selectbox(
        "Sono",
        [
            "Preservado",
            "Prejudicado",
            "Insônia",
            "Sonolência excessiva"
        ]
    )

with col2:

    alimentacao = st.selectbox(
        "Alimentação",
        [
            "Preservada",
            "Reduzida",
            "Aumentada",
            "Dificuldade para alimentar-se"
        ]
    )

    eliminacoes = st.selectbox(
        "Eliminações",
        [
            "Sem alterações relatadas",
            "Alteração urinária",
            "Alteração intestinal",
            "Alterações urinária e intestinal"
        ]
    )

observacoes_anamnese = st.text_area(
    "Observações adicionais",
    placeholder=(
        "Registre outras informações relevantes da anamnese."
    ),
    height=120
)

if st.button("💾 Registrar anamnese"):

    st.success(
        "✅ Anamnese registrada com sucesso!"
    )

    if intensidade_dor > 0:

        st.info(
            f"Paciente refere dor com intensidade "
            f"{intensidade_dor}/10."
        )

    if qualidade_sono != "Preservado":

        st.warning(
            f"Alteração identificada no sono: "
            f"{qualidade_sono}."
        )

    if alimentacao != "Preservada":

        st.warning(
            f"Alteração identificada na alimentação: "
            f"{alimentacao}."
        )

    if eliminacoes != "Sem alterações relatadas":

        st.warning(
            f"Alteração nas eliminações: "
            f"{eliminacoes}."
        )

# =========================================================
# 4. EXAME FÍSICO
# =========================================================

st.divider()

st.subheader("🩺 Exame Físico")

st.write(
    "Realize o exame físico céfalo-caudal e registre "
    "os achados encontrados."
)

st.markdown("### 👤 Estado geral")

estado_geral = st.selectbox(
    "Estado geral",
    [
        "Bom estado geral",
        "Regular estado geral",
        "Mau estado geral"
    ]
)

nivel_consciencia = st.selectbox(
    "Nível de consciência",
    [
        "Alerta e orientado",
        "Sonolento",
        "Confuso",
        "Agitado",
        "Rebaixamento do nível de consciência"
    ]
)

st.markdown("### 👁️ Pele e mucosas")

col1, col2 = st.columns(2)

with col1:

    coloracao_pele = st.selectbox(
        "Coloração da pele",
        [
            "Normocorada",
            "Pálida",
            "Cianótica",
            "Ictérica",
            "Hiperemiada"
        ]
    )

    hidratacao = st.selectbox(
        "Hidratação",
        [
            "Hidratada",
            "Ressecada",
            "Muito ressecada"
        ]
    )

with col2:

    integridade_pele = st.selectbox(
        "Integridade da pele",
        [
            "Íntegra",
            "Lesão presente",
            "Hiperemia",
            "Edema",
            "Outras alterações"
        ]
    )

    localizacao_lesao = st.text_input(
        "Localização da alteração/lesão",
        placeholder=(
            "Ex.: região sacral, membro inferior direito..."
        )
    )

st.markdown("### 🧠 Cabeça e pescoço")

cabeca_pescoco = st.text_area(
    "Achados de cabeça e pescoço",
    placeholder=(
        "Registre pupilas, cavidade oral, linfonodos, "
        "pescoço e outras alterações."
    ),
    height=100
)

st.markdown("### ❤️ Sistema cardiovascular")

cardiovascular = st.text_area(
    "Achados cardiovasculares",
    placeholder=(
        "Ex.: perfusão periférica, edema, pulsos, "
        "ausculta cardíaca e outras observações."
    ),
    height=100
)

st.markdown("### 🫁 Sistema respiratório")

respiratorio = st.text_area(
    "Achados respiratórios",
    placeholder=(
        "Ex.: padrão respiratório, expansibilidade torácica, "
        "ausculta pulmonar, presença de secreções."
    ),
    height=100
)

st.markdown("### 🩺 Abdome")

abdome = st.text_area(
    "Achados abdominais",
    placeholder=(
        "Ex.: inspeção, palpação, dor, distensão, "
        "ruídos hidroaéreos e outras alterações."
    ),
    height=100
)

st.markdown("### 🧠 Avaliação neurológica")

neurologico = st.text_area(
    "Achados neurológicos",
    placeholder=(
        "Ex.: orientação, força muscular, sensibilidade, "
        "mobilidade, fala e outros achados."
    ),
    height=100
)

st.markdown("### 🦴 Sistema musculoesquelético")

musculoesqueletico = st.text_area(
    "Achados musculoesqueléticos",
    placeholder=(
        "Ex.: mobilidade, amplitude de movimento, "
        "dor, força muscular e limitações."
    ),
    height=100
)

st.markdown("### 📝 Observações gerais")

observacoes_exame = st.text_area(
    "Outros achados do exame físico",
    placeholder=(
        "Registre qualquer outro achado relevante."
    ),
    height=120
)

if st.button("💾 Registrar exame físico"):

    st.success(
        "✅ Exame físico registrado com sucesso!"
    )

    st.write("### Resumo dos achados")

    st.write(
        f"**Estado geral:** {estado_geral}"
    )

    st.write(
        f"**Consciência:** {nivel_consciencia}"
    )

    st.write(
        f"**Coloração da pele:** {coloracao_pele}"
    )

    st.write(
        f"**Hidratação:** {hidratacao}"
    )

    st.write(
        f"**Integridade da pele:** {integridade_pele}"
    )

    if localizacao_lesao:

        st.write(
            f"**Localização da alteração:** "
            f"{localizacao_lesao}"
        )

    if cabeca_pescoco:

        st.write(
            f"**Cabeça e pescoço:** "
            f"{cabeca_pescoco}"
        )

    if cardiovascular:

        st.write(
            f"**Cardiovascular:** "
            f"{cardiovascular}"
        )

    if respiratorio:

        st.write(
            f"**Respiratório:** "
            f"{respiratorio}"
        )

    if abdome:

        st.write(
            f"**Abdome:** {abdome}"
        )

    if neurologico:

        st.write(
            f"**Neurológico:** {neurologico}"
        )

    if musculoesqueletico:

        st.write(
            f"**Musculoesquelético:** "
            f"{musculoesqueletico}"
        )

    if observacoes_exame:

        st.write(
            f"**Observações:** "
            f"{observacoes_exame}"
        )

# =========================================================
# 5. DIAGNÓSTICOS DE ENFERMAGEM
# =========================================================

st.divider()

st.subheader("🧠 Diagnósticos de Enfermagem")

st.write(
    "Com base nos dados coletados na avaliação, selecione "
    "as possibilidades de diagnóstico para estudo."
)

st.info(
    "📚 Ferramenta educacional: as sugestões devem ser "
    "analisadas e validadas pelo estudante/profissional "
    "de acordo com a avaliação clínica e a taxonomia "
    "de enfermagem adotada."
)

st.markdown("### 🔎 Possibilidades para estudo")

diagnosticos = st.multiselect(
    "Selecione os diagnósticos que deseja analisar",
    [
        "Dor aguda",
        "Integridade da pele prejudicada",
        "Risco de lesão por pressão",
        "Padrão respiratório ineficaz",
        "Hipertermia",
        "Déficit no autocuidado",
        "Nutrição desequilibrada",
        "Distúrbio do padrão do sono",
        "Mobilidade física prejudicada",
        "Ansiedade",
        "Risco de queda",
        "Perfusão tissular periférica prejudicada"
    ]
)

if diagnosticos:

    st.markdown("### 📋 Diagnósticos selecionados")

    for diagnostico in diagnosticos:

        with st.expander(f"🩺 {diagnostico}"):

            if diagnostico == "Dor aguda":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "relato de dor, intensidade, localização, "
                    "características e fatores relacionados."
                )

                st.write(
                    "**Avaliar:** intensidade da dor, duração, "
                    "localização, fatores de melhora/piora "
                    "e resposta às intervenções."
                )

            elif diagnostico == "Integridade da pele prejudicada":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "presença de lesão, hiperemia, alteração "
                    "da integridade cutânea ou ferida."
                )

                st.write(
                    "**Avaliar:** localização, extensão, aspecto "
                    "da lesão, pele ao redor e evolução."
                )

            elif diagnostico == "Risco de lesão por pressão":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "imobilidade, alteração da integridade da pele, "
                    "umidade, estado nutricional e outros fatores "
                    "de risco."
                )

                st.write(
                    "**Avaliar:** mobilidade, exposição à umidade, "
                    "condições da pele e fatores de risco individuais."
                )

            elif diagnostico == "Padrão respiratório ineficaz":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "alterações da frequência respiratória, esforço "
                    "respiratório ou alterações observadas no exame."
                )

                st.write(
                    "**Avaliar:** frequência, ritmo, profundidade, "
                    "expansibilidade torácica, ausculta e saturação."
                )

            elif diagnostico == "Hipertermia":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "temperatura corporal elevada e sinais associados."
                )

                st.write(
                    "**Avaliar:** temperatura, presença de calafrios, "
                    "sudorese e outros sinais clínicos."
                )

            elif diagnostico == "Déficit no autocuidado":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "dificuldade ou incapacidade para realizar "
                    "atividades de autocuidado."
                )

                st.write(
                    "**Avaliar:** alimentação, higiene, vestuário, "
                    "eliminação e capacidade funcional."
                )

            elif diagnostico == "Nutrição desequilibrada":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "alterações na alimentação, ingestão inadequada "
                    "ou outras alterações nutricionais."
                )

                st.write(
                    "**Avaliar:** padrão alimentar, ingestão, peso, "
                    "estado nutricional e condições associadas."
                )

            elif diagnostico == "Distúrbio do padrão do sono":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "relato de insônia, sono prejudicado ou alterações "
                    "na qualidade do sono."
                )

                st.write(
                    "**Avaliar:** duração, qualidade, despertares, "
                    "rotina e fatores que interferem no sono."
                )

            elif diagnostico == "Mobilidade física prejudicada":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "limitação de movimentos, redução da força "
                    "ou dificuldade de mobilidade."
                )

                st.write(
                    "**Avaliar:** força muscular, amplitude de movimento, "
                    "marcha e capacidade funcional."
                )

            elif diagnostico == "Ansiedade":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "relatos de preocupação, tensão, medo ou "
                    "manifestações associadas."
                )

                st.write(
                    "**Avaliar:** manifestações físicas, emocionais "
                    "e comportamentais."
                )

            elif diagnostico == "Risco de queda":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "alterações de mobilidade, equilíbrio, "
                    "nível de consciência ou outros fatores de risco."
                )

                st.write(
                    "**Avaliar:** marcha, equilíbrio, ambiente, "
                    "medicações e histórico de quedas."
                )

            elif diagnostico == "Perfusão tissular periférica prejudicada":

                st.write(
                    "**Dados que podem apoiar a análise:** "
                    "alterações de perfusão, edema, coloração, "
                    "temperatura ou pulsos periféricos."
                )

                st.write(
                    "**Avaliar:** pulsos, enchimento capilar, "
                    "coloração, temperatura e presença de edema."
                )

st.divider()

st.subheader("📝 Plano para o diagnóstico")

diagnostico_principal = st.selectbox(
    "Diagnóstico selecionado para planejamento",
    [
        "Selecione uma opção",
        "Dor aguda",
        "Integridade da pele prejudicada",
        "Risco de lesão por pressão",
        "Padrão respiratório ineficaz",
        "Hipertermia",
        "Déficit no autocuidado",
        "Nutrição desequilibrada",
        "Distúrbio do padrão do sono",
        "Mobilidade física prejudicada",
        "Ansiedade",
        "Risco de queda",
        "Perfusão tissular periférica prejudicada"
    ]
)

if diagnostico_principal != "Selecione uma opção":

    st.markdown("### 🎯 Resultado esperado")

    resultado_esperado = st.text_area(
        "Descreva o resultado esperado para o paciente",
        placeholder=(
            "Ex.: redução da intensidade da dor, melhora da "
            "mobilidade, manutenção da integridade da pele..."
        ),
        height=100
    )

    st.markdown("### 🛠️ Intervenções de enfermagem")

    intervencoes = st.text_area(
        "Registre as intervenções de enfermagem planejadas",
        placeholder=(
            "Descreva as intervenções de enfermagem "
            "adequadas ao caso clínico."
        ),
        height=130
    )

    st.markdown("### 📊 Avaliação")

    avaliacao = st.text_area(
        "Registre a evolução/resposta do paciente",
        placeholder=(
            "Descreva a resposta apresentada após as intervenções."
        ),
        height=100
    )

    if st.button("💾 Registrar plano de enfermagem"):

        st.success(
            "✅ Plano de enfermagem registrado para estudo!"
        )

        st.write(
            f"**Diagnóstico:** {diagnostico_principal}"
        )

        if resultado_esperado:

            st.write(
                f"**Resultado esperado:** "
                f"{resultado_esperado}"
            )

        if intervencoes:

            st.write(
                f"**Intervenções:** {intervencoes}"
            )

        if avaliacao:

            st.write(
                f"**Avaliação:** {avaliacao}"
            )

# =========================================================
# 6. RACIOCÍNIO CLÍNICO
# =========================================================

st.divider()

st.subheader("🧠 Raciocínio Clínico")

st.write(
    "Analise os dados coletados e registre o raciocínio "
    "utilizado para selecionar o diagnóstico de enfermagem."
)

st.markdown("### 🔎 Síntese dos achados")

achados_clinicos = st.text_area(
    "Quais são os principais achados identificados?",
    placeholder=(
        "Ex.: paciente apresenta dor 8/10, dificuldade para "
        "deambular, lesão em membro inferior e alteração da pele."
    ),
    height=120
)

st.markdown("### 💭 Justificativa clínica")

justificativa = st.text_area(
    "Justifique a escolha do diagnóstico",
    placeholder=(
        "Explique quais dados da avaliação sustentam "
        "o diagnóstico selecionado."
    ),
    height=140
)

st.markdown("### 🎯 Prioridade")

prioridade = st.radio(
    "Qual a prioridade identificada?",
    [
        "Baixa",
        "Moderada",
        "Alta"
    ],
    horizontal=True
)

st.markdown("### 📚 Reflexão do estudante")

reflexao = st.text_area(
    "O que você consideraria importante investigar ou acompanhar?",
    placeholder=(
        "Registre outros dados que deveriam ser investigados, "
        "monitorados ou reavaliados."
    ),
    height=120
)

if st.button("🧠 Finalizar raciocínio clínico"):

    st.success(
        "✅ Raciocínio clínico registrado com sucesso!"
    )

    st.markdown("### 📋 Resumo")

    if achados_clinicos:

        st.write(
            f"**Achados clínicos:** {achados_clinicos}"
        )

    if justificativa:

        st.write(
            f"**Justificativa:** {justificativa}"
        )

    st.write(
        f"**Prioridade:** {prioridade}"
    )

    if reflexao:

        st.write(
            f"**Reflexão:** {reflexao}"
        )

    st.info(
        "📚 Este simulador possui finalidade educacional. "
        "Os achados, diagnósticos e intervenções devem ser "
        "analisados pelo estudante/profissional e validados "
        "conforme avaliação clínica e protocolos adotados."
    )

st.divider()

st.success(
    "🩺 CLÍNICA NA PRÁTICA — Simulação concluída!"
)

st.caption(
    "Professor Everton Costa • Simulador educacional "
    "do Processo de Enfermagem"
)

st.divider()

st.caption(
    "CLÍNICA NA PRÁTICA • Professor Everton Costa"
)