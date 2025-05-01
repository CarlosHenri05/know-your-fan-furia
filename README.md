# 🧠 Know Your Fan - FURIA Edition

> Ferramenta para coleta e análise de dados de fãs de eSports, com foco na FURIA, utilizando Python e Modelos de Linguagem (LLMs) para validação e enriquecimento de informações.

---

## 🎯 Objetivo

Este projeto visa criar uma solução prática para:

- Coletar dados básicos e comportamentais de fãs da FURIA.
- Analisar perfis e interações a relacionados à FURIA.
- Utilizar LLMs para identificar o nível de engajamento do fã.
- Gerar um perfil estruturado em formato `.json`.

---

## 📁 Estrutura do Projeto

```
know-your-fan-furia/
├── llm.py               # Módulo para validação com LLM
├── main.py              # Script principal para execução
├── perfil_fan.json      # Exemplo de perfil gerado
├── requirements.txt     # Dependências do projeto
└── .gitignore           # Arquivos e pastas ignorados pelo Git
```

---

## ⚙️ Funcionalidades

- **Coleta de Dados**: Entrada de informações como nome, nick, memória favorita sobre o time...
- **Classificação com LLM**: Determinação do nível de engajamento do fã utilizando modelos de linguagem.
- **Geração de Perfil**: Criação de um arquivo `.json` com todas as informações coletadas e analisadas.

---

## 🧪 Tecnologias Utilizadas

- **Python 3.10+**
- **LLM**: `Llama 3.3` utilizando o Groq para integração
- **Manipulação de Dados**: `json`

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/CarlosHenri05/know-your-fan-furia.git
   cd know-your-fan-furia
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script principal:
   ```bash
   python main.py
   ```

---

## 📄 Exemplo de Saída

```json
{
  "nome": "João da Silva",
  "nick": "JoaoPvP",
  "eventos": "Major, LTA Sul",
  "memoria": "FalleN indo para a FURIA"

  {
  "perfil": "E aí, João da Silva, ou melhor, JoaoPvP! Vamos dar uma olhada no seu perfil e ver se você é mesmo um fã da FURIA ou não.\n\nPrimeiramente, você mencionou que seu nickname é JoaoPvP, o que já dá uma dica de que você é um jogador competitivo, provavelmente com experiência em jogos de ação e estratégia. Isso é interessante, pois a FURIA é uma equipe conhecida por sua habilidade em jogos como CS:GO e outros títulos competitivos.\n\nVocê também mencionou que participou de eventos como o Major e a LTA Sul, o que é incrível! Esses eventos são alguns dos mais importantes do calendário de eSports, e é ótimo que você tenha tido a oportunidade de participar deles.\n\nAgora, vamos falar sobre a sua memória favorita: FalleN indo para a FURIA. Isso é interessante, pois FalleN é um dos jogadores mais icônicos da história do CS:GO no Brasil, e sua transferência para a FURIA foi um momento marcante para a equipe. No entanto, isso não necessariamente significa que você é um fã da FURIA, pois FalleN é um jogador muito respeitado e admirado por muitos fãs de eSports.\n\nEm resumo, você parece ter uma boa conexão com o mundo dos eSports, e especialmente com a cena de CS:GO no Brasil. No entanto, não está claro se você é um fã da FURIA ou apenas um fã de FalleN e do eSports em geral. Se eu tivesse que apostar, diria que você é um fã de eSports em geral, mas não necessariamente um fã da FURIA. Você tem algum conhecimento profundo sobre a equipe, como seus jogadores atuais, sua história e seus principais torneios? Se sim, então talvez você seja um fã da FURIA de verdade! Se não, então talvez você seja apenas um fã do eSports em geral. Qual é a sua resposta?"
}
}
```

---

## 📌 Considerações Finais

Este projeto é uma base para entender e analisar o comportamento de fãs de eSports, com foco na FURIA. Futuras melhorias podem incluir:

- Integração com APIs de redes sociais.
- Interface gráfica para facilitar a interação.
- Armazenamento em banco de dados para análise de múltiplos perfis.

---

## 👨‍💻 Autor

Desenvolvido por [Carlos Henrique](https://github.com/CarlosHenri05) como parte de um desafio proposto pela organização FURIA para uma vaga de Assistente de Engenharia de Software.
