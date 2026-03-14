from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

system = ("system", "Você é um assistente que responde questões em um estilo {style}")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="engraçado", question="Fale sobre o maior jogador de futebol do mundo")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
answer_gemini = gemini.invoke(messages)
print(answer_gemini.content)