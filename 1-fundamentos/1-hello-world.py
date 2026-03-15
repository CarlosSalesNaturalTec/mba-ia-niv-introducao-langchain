from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

message = "Olá eu me chamo Carlos Sales. Uma pessoa desenvolvedora preta, brasileira, baiana e soteropolitana. Neste momento eu estou testando a plataforma Langchain e os modelos de LLM da OpenAI e Google GenAI."
temperature_default = 0.7

# Chamada para o modelo GPT-5 Nano da OpenAI
print("Enviando mensagem para o modelo GPT-5 Nano da OpenAI...")

hora_inicial = datetime.now().strftime("%H:%M:%S")
print(f"Hora de início: {hora_inicial}")

model = ChatOpenAI(model="gpt-5-nano", temperature=temperature_default)
try:
    respose = model.invoke(message)
except Exception as e:
    response = f"Ocorreu um erro ao chamar o modelo GPT-5 Nano: {str(e)}"

hora_termino = datetime.now().strftime("%H:%M:%S")
print("OpenAI GPT-5 Nano Response:", response)
print("Hora de término:", hora_termino)
print("Tempo gasto:", (datetime.strptime(hora_termino, "%H:%M:%S") - datetime.strptime(hora_inicial, "%H:%M:%S")))

# Chamada para o modelo Gemini 2.5 Flash da Google GenAI
# =============================================================
print("\nEnviando mensagem para o modelo Gemini 2.5 Flash da Google GenAI...")

hora_inicial = datetime.now().strftime("%H:%M:%S")
print(f"Hora de início: {hora_inicial}")

try:
    model_gemini = init_chat_model(
        model="gemini-2.5-flash",
        model_provider="google_genai",
        temperature=0.5,
    )
    response = model_gemini.invoke(message).content
except Exception as e:
    response = f"Ocorreu um erro ao chamar o modelo Gemini 2.5 Flash: {str(e)}"

hora_termino = datetime.now().strftime("%H:%M:%S")
print("Google Gemini Response:", response)
print("Hora de término:", hora_termino)
print("Tempo gasto:", (datetime.strptime(hora_termino, "%H:%M:%S") - datetime.strptime(hora_inicial, "%H:%M:%S")))



