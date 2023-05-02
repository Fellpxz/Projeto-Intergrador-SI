def mp10_nivel(mp10):
    if mp10 <= 50:
        print("O MP10 está bom, não oferece problemas para a saúde.\n")
        return "bom"
    elif mp10 <= 100:
        print("O MP10 está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        return "moderado"
    elif mp10 <= 150:
        print("O MP10 está ruim, Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        return "ruim"
    elif mp10 <= 250:
        print("O MP10 está muito ruim, Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        return "muito ruim"
    else:
        print("O valor está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        return "pessimo"



def mp25_nivel(mp25):
    if mp25 <= 25:
        print("O MP2.5 está bom, não oferece problemas para a saúde.\n")
        return "bom"
    elif mp25 <= 50:
        print("O MP2.5 está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        return "moderado"
    elif mp25 <= 75:
        print("O MP2.5 está ruim, Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        return "ruim"
    elif mp25 <= 125:
        print("O MP2.5 está muito ruim, Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        return "muito ruim"
    else:
        print("O MP2.5 está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        return "pessimo"



def o3_nivel(o3):
    if o3 <= 100:
        print("O O3 está bom, não oferece problemas para a saúde.\n")
        return "bom"
    elif o3 <= 130:
        print("O O3 está moderado, pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        return "moderado"
    elif o3 <= 160:
        print("O O3 está ruim, toda a população pode apresentar sintomas como tosse seca, cansaço, dor de cabeça e irritação nos olhos. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        return "ruim"
    elif o3 <= 200:
        print("O O3 está muito ruim, toda a população pode apresentar sintomas mais intensos como falta de ar, chiado no peito e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        return "muito ruim"
    else:
        print("O O3 está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n" )
        return "pessimo"
    
  
    
def co_nivel(co):
    if co <= 9:
        print("O CO está bom, não oferece problemas para a saúde.\n")
        return "bom"
    elif co <= 11:
        print("O CO está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como dor de cabeça, náusea e tontura.\n")
        return "moderado"
    elif co <= 13:
        print("O CO está ruim, Toda a população pode apresentar sintomas como dor de cabeça, náusea, tontura e ainda desorientação e confusão. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        return "ruim"
    elif co <= 15:
        print("O CO está muito ruim, Toda a população pode apresentar agravamento dos sintomas como dor de cabeça, náusea, tontura, desorientação e confusão, e ainda problemas cardíacos. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        return "muito ruim"
    else:
        print("O CO valor está péssimo, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares, além de afetar a função pulmonar. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n")
        return "pessimo"
    


def no2_nivel(no2):
    if no2 <= 100:
        print("O NO2 está bom, não oferece problemas para a saúde. \n")
        return "bom"
    elif no2 <= 240:
        print("O NO2 está moderado, pessoas com doenças respiratórias e cardíacas podem apresentar sintomas como tosse, falta de ar e irritação nos olhos. A população em geral não é afetada. \n")
        return "moderado"
    elif no2 <= 320:
        print("O NO2 está ruim, toda a população pode apresentar sintomas como tosse, falta de ar e irritação nos olhos. Pessoas com doenças respiratórias e cardíacas podem apresentar efeitos mais sérios na saúde. \n")
        return "ruim"
    elif no2 <= 1130:
        print("O NO2 está muito ruim, toda a população pode apresentar agravamento dos sintomas como tosse, falta de ar e irritação nos olhos, além de dores de cabeça. Efeitos ainda mais graves na saúde de pessoas com doenças respiratórias e cardíacas. \n")
        return "muito ruim"
    else:
        print("O NO2 está péssimo, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares, além de afetar a função pulmonar. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n")
        return "pessimo"



def so2_nivel(so2):
    if so2 <= 20:
        print("O SO2 está bom, não oferece problemas para a saúde. \n")
        return "bom"
    elif so2 <= 40:
        print("O SO2 está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar irritação nos olhos, nariz e garganta. \n")
        return "moderado"
    elif so2 <= 365:
        print("O SO2 está ruim, Toda a população pode apresentar irritação nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde. \n")
        return "ruim"
    elif so2 <= 800:
        print("O SO2 está muito ruim, toda a população pode apresentar agravamento dos sintomas como tosse, falta de ar e irritação nos olhos, além de dores de cabeça. Efeitos ainda mais graves na saúde de pessoas com doenças respiratórias e cardíacas. \n")
        return "muito ruim"
    else:
        print("O SO2 está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n")
        return "pessimo"


def verificar(mp10_resultado, mp25_resultado, o3_resultado, co_resultado, no2_resultado, so2_resultado):
    if mp10_resultado == "bom" and mp25_resultado == "bom" and o3_resultado == "bom" and co_resultado == "bom" and no2_resultado == "bom" and so2_resultado == "bom":
        print("O índice geral de qualidade do ar é bom. E não oferece risco algum a saúde! \n")
        
    elif mp10_resultado in ["moderado"] or mp25_resultado in ["moderado"] or o3_resultado in ["moderado"] or co_resultado in ["moderado"] or no2_resultado in ["moderado"] or so2_resultado in ["moderado"]:

        print("O valor do índice está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar irritação nos olhos, nariz e garganta. \n")

    elif mp10_resultado in ["ruim"] or mp25_resultado in ["ruim"] or o3_resultado in ["ruim"] or co_resultado in ["ruim"] or no2_resultado in ["ruim"] or so2_resultado in ["ruim"]:

        print("O valor do índice está ruim, Toda a população pode apresentar irritação nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde. \n")
        
    elif mp10_resultado in ["muito ruim"] or mp25_resultado in ["muito ruim"] or o3_resultado in ["muito ruim"] or co_resultado in ["muito ruim"] or no2_resultado in ["muito ruim"] or so2_resultado in ["muito ruim"]:

        print("O valor do índice está muito ruim, toda a população pode apresentar agravamento dos sintomas como tosse, falta de ar e irritação nos olhos, além de dores de cabeça. Efeitos ainda mais graves na saúde de pessoas com doenças respiratórias e cardíacas. \n")

    else:
        print("O valor do índice está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n")       




while True:
    try:
        mp10 = int(input("Digite o valor do MP10 em microgramas: "))
        if mp10 < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

        mp25 = int(input("Digite o valor do MP2.5 em microgramas: "))
        if mp25 < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

        o3 = int(input("Digite o valor do O3 em microgramas: "))
        if o3 < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

        co = int(input("Digite o valor do CO em PPM: "))
        if co < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

        no2 = int(input("Digite o valor do NO2 em microgramas: "))
        if no2 < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

        so2 = int(input("Digite o valor do SO2 em microgramas: "))
        if so2 < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

        print("")


    except ValueError:
        print("Valor inválido. Certifique-se de que o valor inserido seja um número.")
        continue

    # calcular nível de MP10 e imprimir
    mp10_resultado = mp10_nivel(mp10)

    # calcular nível de MP25 e imprimir
    mp25_resultado = mp25_nivel(mp25)

    # calcular nível de O3 e imprimir
    o3_resultado = o3_nivel(o3)

    # calcular nível de CO e imprimir
    co_resultado = co_nivel(co)
   
    # calcular nível de NO2 e imprimir
    no2_resultado = no2_nivel(no2)
    
    # calcular nível de SO2 e imprimir
    so2_resultado = so2_nivel(so2)

    verificar(mp10_resultado, mp25_resultado, o3_resultado, co_resultado, no2_resultado, so2_resultado)
 

    while True:
        resposta = input("Deseja usar a aplicação novamente? (S/N)").lower()
        if resposta == 'n':
            break
        elif resposta == 's':
            break
        else:
            print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")
            continue

    if resposta == 'n':
        break
    else:
        continue