def mp10_nivel(mp10):
    if mp10 <= 50:
        print("O MP10 está bom, não oferece problemas para a saúde.\n")
        resultado = "bom"
    elif mp10 <= 100:
        print("O MP10 está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        resultado = "moderado"
    elif mp10 <= 150:
        print("O MP10 está ruim, Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        resultado = "ruim"
    elif mp10 <= 250:
        print("O MP10 está ruim, Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        resultado = "muito ruim"
    else:
        print("O valor está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        resultado = "pessimo"
    
    return resultado

def mp25_nivel(mp25):
    if mp25 <= 25:
        print("O MP2.5 está bom, não oferece problemas para a saúde.\n")
        resultado = "bom"
    elif mp25 <= 50:
        print("O MP2.5 está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        resultado = "moderado"
    elif mp25 <= 75:
        print("O MP2.5 está ruim, Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        resultado = "ruim"
    elif mp25 <= 125:
        print("O MP2.5 está ruim, Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        resultado = "muito ruim"
    else:
        print("O valor está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        resultado = "pessimo"

    return resultado
    
def o3_nivel(o3):
    if o3 <= 100:
        print("O O3 está bom, não oferece problemas para a saúde.\n")
        resultado = "bom"
    elif o3 <= 130:
        print("O O3 está moderado, pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        resultado = "moderado"
    elif o3 <= 160:
        print("O O3 está ruim, toda a população pode apresentar sintomas como tosse seca, cansaço, dor de cabeça e irritação nos olhos. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        resultado = "ruim"
    elif o3 <= 200:
        print("O O3 está muito ruim, toda a população pode apresentar sintomas mais intensos como falta de ar, chiado no peito e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        resultado = "muito ruim"
    else:
        print("O valor está péssimo, toda a população pode apresentar sérios riscos à saúde, inclusive aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        resultado = "pessimo"
    
    return resultado

def o3_nivel(o3):
    if o3 <= 100:
        print("O O3 está bom, não oferece problemas para a saúde.\n")
        resultado = "bom"
    elif o3 <= 130:
        print("O O3 está moderado, pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        resultado = "moderado"
    elif o3 <= 160:
        print("O O3 está ruim, toda a população pode apresentar sintomas como tosse seca, cansaço, dor de cabeça e irritação nos olhos. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n")
        resultado = "ruim"
    elif o3 <= 200:
        print("O O3 está muito ruim, toda a população pode apresentar sintomas mais intensos como falta de ar, chiado no peito e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        resultado = "muito ruim"
    else:
        print("O valor está péssimo, toda a população pode apresentar sérios riscos à saúde, inclusive aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        resultado = "pessimo"

    return resultado

def co_nivel(co):
    if co <= 9:
        resultado = "bom"
        return "O CO está bom, não oferece problemas para a saúde.\n"
    elif co <= 11:
        resultado = "moderado"
        return "O CO está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como dor de cabeça, náusea e tontura.\n"
    elif co <= 13:
        resultado = "ruim"
        return "O CO está ruim, Toda a população pode apresentar sintomas como dor de cabeça, náusea, tontura e ainda desorientação e confusão. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n"
    elif co <= 15:
        resultado = "muito ruim"
        return "O CO está ruim, Toda a população pode apresentar agravamento dos sintomas como dor de cabeça, náusea, tontura, desorientação e confusão, e ainda problemas cardíacos. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n"
    else:
        resultado = "pessimo"
        return "O valor está péssimo, Toda a população pode apresentar sérios riscos à saúde, incluindo risco de morte.\n"
    
    
def no2_nivel(no2):
    if no2 <= 100:
        resultado = "bom"
        return "O NO2 está bom, não oferece problemas para a saúde.  \n"
    elif no2 <= 240:
        resultado = "moderado"
        return "O NO2 está moderado, pessoas com doenças respiratórias e cardíacas podem apresentar sintomas como tosse, falta de ar e irritação nos olhos. A população em geral não é afetada. \n"
    elif no2 <= 320:
        resultado = "ruim"
        return "O NO2 está ruim, toda a população pode apresentar sintomas como tosse, falta de ar e irritação nos olhos. Pessoas com doenças respiratórias e cardíacas podem apresentar efeitos mais sérios na saúde. \n"
    elif no2 <= 1130:
        resultado = "muito ruim"
        return "O NO2 está muito ruim, toda a população pode apresentar agravamento dos sintomas como tosse, falta de ar e irritação nos olhos, além de dores de cabeça. Efeitos ainda mais graves na saúde de pessoas com doenças respiratórias e cardíacas. \n"
    else:
        resultado = "pessimo"
        return "O valor está péssimo, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares, além de afetar a função pulmonar. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n"
    

def so2_nivel(so2):
    if so2 <= 20:
        return "O SO2 está bom, não oferece problemas para a saúde. \n"
    elif so2 <= 40:
        return "O SO2 está moderado, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar irritação nos olhos, nariz e garganta. \n"
    elif so2 <= 365:
        return "O SO2 está ruim, Toda a população pode apresentar irritação nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde. \n"
    elif so2 <= 800:
        return "O NO2 está muito ruim, toda a população pode apresentar agravamento dos sintomas como tosse, falta de ar e irritação nos olhos, além de dores de cabeça. Efeitos ainda mais graves na saúde de pessoas com doenças respiratórias e cardíacas. \n"
    else:
        return "O valor está péssimo, Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis. \n" 

def verificar_qualidade_ar(resultado):
        
        
        if resultado == "bom" :
            print("O índice geral de qualidade do ar é bom.")

        elif resultado == "moderado":
            print("O índice geral de qualidade do ar é moderado.")

        elif resultado == "ruim":
            print("O índice geral de qualidade do ar é ruim.")

        elif resultado == "muito ruim":
            print("O índice geral de qualidade do ar é muito ruim.")

        elif resultado == "pessimo":
            print("O índice geral de qualidade do ar é péssimo.")


while True:
    try:
        mp10 = int(input("Digite o valor do MP10 em microgramas: "))
        mp25 = int(input("Digite o valor do MP2.5 em microgramas: "))
        o3 = int(input("Digite o valor do O3 em microgramas: "))
        co = int(input("Digite o valor do CO em PPM: "))
        no2 = int(input("Digite o valor do NO2 em microgramas: "))
        so2 = int(input("Digite o valor do SO2 em microgramas: "))
        print("")

        if mp10 < 0 or mp25 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
            print("Valor inválido. Certifique-se de que o valor inserido seja maior ou igual a 0.")
            continue

    except ValueError:
        print("Valor inválido. Certifique-se de que o valor inserido seja um número.")
        continue

    # calcular nível de MP10 e imprimir
    nivel_mp10 = mp10_nivel(mp10)
    print(nivel_mp10)

    # calcular nível de MP25 e imprimir
    nivel_mp25 = mp25_nivel(mp25)
    print(nivel_mp25)
    

    # calcular nível de O3 e imprimir
    o3_nivel(o3)

    # calcular nível de CO e imprimir
    nivel_co = co_nivel(co)
    print(nivel_co)

    # calcular nível de NO2 e imprimir
    nivel_no2 = no2_nivel(no2)
    print(nivel_no2)

    # calcular nível de SO2 e imprimir
    nivel_so2 = so2_nivel(so2)
    print(nivel_so2)

    resultado = [nivel_mp25, nivel_mp10]

    verificar_qualidade_ar(resultado)


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