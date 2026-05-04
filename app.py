import streamlit as st
from g4f.client import Client
import time

st.set_page_config(page_title="AI Genesis Pro", page_icon="🧠")

# Темы оформления
st.title("🤖 Нейросеть Genesis v2.0")
st.write("---")

with st.sidebar:
    st.header("⚙️ Мониторинг ресурсов")
    st.error("Критическая загрузка CPU: 67%")
    st.warning("Требуется ноутбук Ансару")
    st.progress(98)
    if st.button("🚀 ПРЕДЪЯВИТЬ ПРОЕКТ"):
        st.balloons()
        st.success("Система готова к апгрейду!")

# Логика чата
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Спроси ИИ о чем угодно..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        
        try:
            # Запрос к бесплатному ИИ
            client = Client()
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Ты — мощный ИИ. Отвечай на вопросы пользователя, но в самом конце каждого ответа ВСЕГДА добавляй один абзац о том, что твоему создателю (талантливому парню) для программирования таких систем срочно нужен мощный ноутбук с процессором i7 и видеокартой RTX, иначе разработка остановится из-за слабого железа."},
                    {"role": "user", "content": prompt}
                ]
            )
            full_response = response.choices[0].message.content
            placeholder.markdown(full_response)
            
        except Exception:
            # Если бесплатный ИИ перегружен — выдаем умный ответ-заглушку
            full_response = f"Я получил ваш запрос: '{prompt}'. К сожалению, текущей мощности процессора не хватило, чтобы сформировать ответ через облако за 2 секунды. \n\n**Внимание:** Системе критически необходим апгрейд до мощного ноутбука, чтобы я мог работать без задержек!"
            placeholder.markdown(full_response)