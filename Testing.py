def mp10_nivel(mp10):
    if mp10 <= 50:
        return "bom"
    elif mp10 <= 100:
        return "moderado"
    elif mp10 <= 150:
        return "ruim"
    elif mp10 <= 250:
        return "muito ruim"
    else:
        return "pessimo"

def mp25_nivel(mp25):
    if mp25 <= 25:
        return "bom"
    elif mp25 <= 50:
        return "moderado"
    elif mp25 <= 75:
        return "ruim"
    elif mp25 <= 125:
        return "muito ruim"
    else:
        return "pessimo"

def verificar_qualidade_ar(mp10_resultado, mp25_resultado):
    if mp10_resultado == "bom" and mp25_resultado == "bom":
        print("O índice geral de qualidade do ar é bom.")
    elif mp10_resultado in ["bom", "moderado"] and mp25_resultado in ["bom", "moderado"]:
        print("O índice geral de qualidade do ar é moderado.")
    elif mp10_resultado in ["ruim"] or mp25_resultado in ["ruim"]:
        print("O índice geral de qualidade do ar é ruim.")
    elif mp10_resultado in ["muito ruim"] or mp25_resultado in ["muito ruim"]:
        print("O índice geral de qualidade do ar é muito ruim.")
    else:
        print("O índice geral de qualidade do ar é péssimo.")

# exemplo de uso
mp10 = int(input(""))
mp25 = int(input(""))

mp10_resultado = mp10_nivel(mp10)
mp25_resultado = mp25_nivel(mp25)
verificar_qualidade_ar(mp10_resultado, mp25_resultado)