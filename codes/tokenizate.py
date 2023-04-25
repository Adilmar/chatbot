#import lib nltk e suas variantes
from nltk.tokenize import sent_tokenize, word_tokenize  

texto  = "Oi Adilmar tudo bem ? Estou com problemas na service desk pode me ajudar a resolver o erro no sistema." 

print(":::::SENTENCAS:::::")

#funcao para separar o texto em sentencas 
print(sent_tokenize(texto))                                              

print("\n:::::TOKENIZACAO:::::")

#funcao para tokenizar uma frase 
print(word_tokenize(texto))