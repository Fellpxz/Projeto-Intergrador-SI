import mysql.connector

# Configurações de conexão com o banco de dados
config = {
    'host': 'us-cdbr-east-06.cleardb.net',
    'user': 'be4227e4b6f77a',
    'password': 'c1f135ca',
    'database': 'heroku_c9cd53735e57e53'
}

def test_connect():
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**config)

        # Verifica se a conexão foi bem-sucedida
        if conn.is_connected():
            print('Conexão ao banco de dados estabelecida com sucesso.')
            print("")
        else:
            print('Não foi possível estabelecer a conexão ao banco de dados.')

        # Fecha a conexão com o banco de dados
        conn.close()

    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)


def testar_amostra(id):
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**config)

        # Cria um objeto cursor para executar as consultas
        cursor = conn.cursor()

        # Executa uma consulta para recuperar os dados do campo "mp10" da tabela "amostra"
        cursor.execute('SELECT mp10, mp25, o3, co, no2, so2 FROM amostra WHERE id = ' + str(id))

        # Obtém os resultados da consulta
        resultados = cursor.fetchall()

        # Verifica se há resultados
        if resultados:
            # Itera sobre os resultados e realiza as operações desejadas
            for resultado in resultados:
                mp10 = resultado[0]
                mp25 = resultado[1]
                o3 = resultado[2]
                co = resultado[3]
                no2 = resultado[4]
                so2 = resultado[5]
                # Faça o que desejar com o valor de mp10, como cálculos, exibições, etc.
                print("Valor de mp10:", mp10)
                mp10_resultado = mp10_nivel(mp10)
                print("")
                print("Valor de mp25:", mp25)
                mp25_resultado = mp25_nivel(mp25)
                print("")
                print("Valor de o3:", o3)
                o3_resultado = o3_nivel(o3)
                print("")
                print("Valor de co:", co)
                co_resultado = co_nivel(co)
                print("")
                print("valor de no2:", no2)
                no2_resultado = no2_nivel(no2)
                print("")
                print("Valor de so2:", so2)
                so2_resultado = so2_nivel(so2)
                print("")
                verificar(mp10_resultado, mp25_resultado, o3_resultado, co_resultado, no2_resultado, so2_resultado)

        # Fecha a conexão com o banco de dados
        conn.close()
    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)


def ver_amostras():
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**config)

        # Cria um objeto cursor para executar as consultas
        cursor = conn.cursor()

        # Comando Executado!
        cursor.execute("SELECT * FROM amostra ORDER BY id ASC")

        # Obtém os resultados da consulta
        resultados = cursor.fetchall()

        resultado_formatado = []
        if resultados:

            for item in resultados:
                item_formatado =  [str(valor).replace("Decimal", "").replace("(", "").replace(")", "") for valor in item]  
                resultado_formatado.append(item_formatado)
            
            for item in resultado_formatado:
                print(item)
        
        # Fecha a conexão com o banco de dados
        conn.close()
    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)


def criar_amostras(id_res, mp10_res, mp25_res, o3_res, co_res, no2_res, so2_res):
    # Conecta ao banco de dados
    conn = mysql.connector.connect(**config)

    # Cria um objeto cursor para executar as consultas
    cursor = conn.cursor()

    try:
        id_num = int(id_res)
        id_soma = id_num + 1
        # Executa o comando de inserção
        query = "INSERT INTO amostra (id, mp10, mp25, o3, co, no2, so2) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id_soma, mp10_res, mp25_res, o3_res, co_res, no2_res, so2_res)
        cursor.execute(query, values)

        # Confirma as alterações no banco de dados
        conn.commit()

        # Obtém o ID do último elemento inserido
        print("Amostra criada com sucesso. ID:", id_soma)

    except mysql.connector.Error as error:
        print("Erro ao criar a amostra:", error)

    # Fecha a conexão com o banco de dados
    conn.close()

def pegar_ultima():
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**config)

        # Cria um objeto cursor para executar as consultas
        cursor = conn.cursor()

        # Mostrar a ultima amostra
        cursor.execute("SELECT id FROM amostra ORDER BY id DESC LIMIT 1;")

        # Obtém os resultados da consulta
        resultados = cursor.fetchall()

        resultado_formatado = str(resultados[0]).strip('(),')

        return resultado_formatado
        
        # Fecha a conexão com o banco de dados
        conn.close()

    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)
        

def mostrar_ultima():
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**config)

        # Cria um objeto cursor para executar as consultas
        cursor = conn.cursor()

        # Mostrar a ultima amostra
        cursor.execute("SELECT * FROM amostra ORDER BY id DESC LIMIT 1;")

        # Obtém os resultados da consulta
        resultados = cursor.fetchall()

        resultado_formatado = []
        if resultados:

            for item in resultados:
                item_formatado =  [str(valor).replace("Decimal", "").replace("(", "").replace(")", "") for valor in item]  
                resultado_formatado.append(item_formatado)
            
            for item in resultado_formatado:
                print(item)
    
            # Fecha a conexão com o banco de dados
        conn.close()

    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)

def mostrar_selecionada(id):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM amostra WHERE id = {id}")

        resultados = cursor.fetchall()

        resultado_formatado = []
        if resultados:

            for item in resultados:
                item_formatado =  [str(valor).replace("Decimal", "").replace("(", "").replace(")", "") for valor in item]  
                resultado_formatado.append(item_formatado)
            
            for item in resultado_formatado:
                print(item)
    

        conn.close()

    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)


def excluir_amostra(id):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM amostra WHERE id = {id}")
        conn.commit()

        conn.close()
    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)

def editar_amostra(id, mp10, mp25, o3, co, no2, so2):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        

        # Constrói o comando UPDATE com os valores a serem atualizados
        cursor.execute(f"UPDATE amostra SET mp10 = {mp10}, mp25 = {mp25}, o3 = {o3}, co = {co}, no2 = {no2}, so2 = {so2} WHERE id = {id}")
        
        cursor.fetchall()
        conn.commit()

        print("")
        print("Editado com sucesso!")

        conn.close()
    except mysql.connector.Error as error:
        print('Erro ao conectar-se ao banco de dados:', error)


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
        res = int(input("Selecione o que você deseja fazer: \n1- Ver amostras existentes \n2- Testar amostras existentes \n3- Criar novas amostras \n4- Editar amostras existentes \n5- Deletar amostras existentes\n6- Encerrar programa!\nResposta: "))
        print('')

        if res < 1 or res > 6: 
            print("O valor colocado é inválido, tente colocar números dentro das opções indicadas.")
            continue

        else:
            if res == 1:
                ver_amostras()
                print("")

            elif res == 2:
                try:
                    ver_amostras()
                    print()
                    get_id = int(input(f"Selecione o ID da amostra que deseja testar: "))
                    if get_id < 0 or res > 5:
                        print("O valor colocado é inválido, tente colocar números dentro das opções indicadas.")
                    else:
                        testar_amostra(get_id)
                        print("")
                except ValueError:
                    print("O valor colocado é inválido, tente colocar números dentro das opções indicadas.")
            
            elif res == 3:
                get_id = pegar_ultima()
                print("Você está criando uma nova amostra, coloque os valores respectivamente! \n")
                get_mp10 = input("Adcione um valor para o MP10: ")
                get_mp25 = input("Adcione um valor para o MP25: ")
                get_o3 = input("Adcione um valor para o O3: ")
                get_co = input("Adcione um valor para o CO: ")
                get_no2 = input("Adcione um valor para o NO2: ")
                get_so2 = input("Adcione um valor para o SO2: ")

                criar_amostras(get_id, get_mp10, get_mp25, get_o3, get_co, get_no2, get_so2)
                print("")
                mostrar_ultima()
                print("")
            
            elif res == 4:
                ver_amostras()
                print("")
                get_id = int(input("Coloque o ID da tabela que será editada: "))
                print(f"Você está editando a tabela amostra, na linha {get_id} , coloque os valores respectivamente! \n")
                mostrar_selecionada(get_id)
                print("")
                get_mp10 = input("Adcione um valor para o MP10: ")
                get_mp25 = input("Adcione um valor para o MP25: ")
                get_o3 = input("Adcione um valor para o O3: ")
                get_co = input("Adcione um valor para o CO: ")
                get_no2 = input("Adcione um valor para o NO2: ")
                get_so2 = input("Adcione um valor para o SO2: ")

                editar_amostra(get_id, get_mp10, get_mp25, get_o3, get_co, get_no2, get_so2)
                mostrar_selecionada(get_id)
                print("")

            elif res == 5:
                ver_amostras()
                print("")
                get_id = int(input("Adcione o ID da amostra que será exluido: "))
                excluir_amostra(get_id)
                print("")
                ver_amostras()
                print("")
            
            elif res == 6:
                  break



    except ValueError:
        print("O valor colocado é inválido, tente colocar números dentro das opções indicadas.")
        continue

    # Testa a conexão
    #test_connect()

    while True:
        resposta = input("Deseja usar a aplicação novamente? (S/N)").lower()
        if resposta == 'n':
            break
        elif resposta == 's':
            print('')
            break
        else:
            print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")
            continue

    if resposta == 'n':
        break
    else:
        continue
