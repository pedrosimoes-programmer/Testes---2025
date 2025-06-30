import pandas as pd

#tabela = pd.read_excel("TabelaTeste.xlsx")

#for linha in tabela.index:
#    if tabela.loc[linha, "Quantidade"] > 5:
#        print("Bastante")
#    else:
#        print("Pouco")

tabela2 = pd.read_excel("TabelaTeste2.xlsx")

for linha in tabela2.index:
    país = tabela2.loc[linha, "País"]
    if tabela2.loc[linha, "População"] > 100000000:
        print("O país", país, "tem gente pra caceta!")
    elif tabela2.loc[linha, "População"] < 10000000:
        print("O país", país, "tem pouca gente")
    else:
        print("O país", país, "tá bão!")

