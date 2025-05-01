import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

try:
  client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
  raise Exception("GROQ API KEY Not found.")


def generate_profile(dados):
  try:
    prompt = f"""
    Com base nos dados abaixo, escreva um perfil curto e personalizado de um fã de eSports da organização FURIA, especificamente FURIA, e você pode ser sincero se achar que o usuário é um fã ou não:

    Nome: {dados['nome']}
    Nickname: {dados['nickname']}
    Eventos: {dados['eventos']}
    Memória favorita: {dados['memoria']}

    Gere um texto com tom informal, mas informativo.
    """

    completion = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages= [{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return completion.choices[0].message.content.strip()

  except Exception as e:
    raise Exception(f"Algo deu errado. {e}")
  
