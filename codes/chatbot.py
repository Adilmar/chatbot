from chatterbot import ChatBot
chatbot = ChatBot("raiza")

from chatterbot.trainers import ListTrainer

conversation = [
    "oi",
    "Olá!",
    "eai",
    "Olá eu sou a Raíza!",
    "opa",
    "Olá! tudo bem?",
    "bem e você?",
    "tudo bem?",
    "bem e você?",
    "Estou otima obrigado!",
    "O que você faz",
    "Eu sou o chatbot da Raízen",
    "Que legal",
    "Muito obrigado!",
    "qual seu nome?",
    "Raíza",
    "bem",
    "bem e você?",
    "Que bom que está bem!"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

response = chatbot.get_response("oi")
print(response)

while True:
    pergunta = input("Usuário: ")
    resposta = chatbot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Raíza: ', resposta)
    else:
        print('Raíza: Ainda não sei responder esta pergunta')