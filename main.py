import json
from llm import generate_profile

def ask(question):
  return input(f" {question}")


def main(): 
  print("Bem vindo ao Fan Analyzer da organização FURIA!\n Tá pronto para ver se você é #TEAMFURIA ou não?")

  dados = {
    "nome": ask("Qual seu nome?"),
    "nickname": ask("Qual seu nick?"),
    "eventos": ask("Em quais eventos de eSports você já participou ou assistiu?"),
    "memoria": ask("Qual sua memória favorita relacionada a organização FURIA? Ex: vitórias, jogos, momentos de bom companheirismo, etc")

  }

  print("Gerando perfil com a IA...")
  perfil = generate_profile(dados)
  print("Perfil do fã: ")
  print(perfil)

  with open("perfil_fan.json", "w", encoding="utf-8") as f:
        json.dump({"perfil": perfil}, f, ensure_ascii=False, indent=2)
  print("\n✅ Perfil salvo em 'perfil_fan.json'.")


if __name__ == "__main__":
   main()
