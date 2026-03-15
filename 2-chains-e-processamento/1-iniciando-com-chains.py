from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

question_template = PromptTemplate(
    input_variables=["nome"],
    template="Olá, eu me chamo {nome}! Conte-me uma piada com meu nome!"
)

temperature = 0.9

model_gemini = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai",
    temperature=0.7,
)

chain = question_template | model_gemini

result = chain.invoke({"nome": "Carlos Trenell"})
print(result.content)