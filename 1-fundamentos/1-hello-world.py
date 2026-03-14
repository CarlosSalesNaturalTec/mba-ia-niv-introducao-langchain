from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
message = model.invoke("Olá eu me chamo Carlos Sales. Uma pessoa desenvolvedora preta, brasileira, baiana e soteropolitana. Neste momento eu estou testando a plataforma Langchain.")

print(message.content)