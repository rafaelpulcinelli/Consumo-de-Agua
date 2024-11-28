import random

def calcular_agua_peso(peso):
    return peso * 35 / 1000  # 35 ml por kg em litros

def verificar_consumo(consumido, ideal):
    if consumido >= ideal:
        return "Parabéns! Você atingiu sua meta de consumo diário de água."
    else:
        return f"Você precisa beber mais {ideal - consumido:.2f} litros hoje."

def obter_valor_float(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

def mostrar_inspiracao():
    frases = [
        "Bom você se torna! - Luana Carolina",
        "A persistência é o caminho do êxito. - Charles Chaplin",
        "Tudo parece impossível até que seja feito. - Nelson Mandela",
        "Você só falha se parar de tentar. - Albert Einstein",
        "O sucesso é a soma de pequenos esforços repetidos diariamente. - Robert Collier",
        "O futuro depende do que você faz hoje. - Mahatma Gandhi",
        "Não espere por oportunidade. Crie-a. - George Bernard Shaw"
    ]
    print("\n✨ Inspiração do Dia ✨")
    print(random.choice(frases))

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Controle de Consumo de Água!")
    print("Vamos calcular a quantidade ideal de água que você deve consumir por dia.")

    peso = obter_valor_float("Digite seu peso (kg): ")
    ideal = calcular_agua_peso(peso)
    print(f"Sua meta diária de consumo de água é: {ideal:.2f} litros.")

    consumido = obter_valor_float("Digite a quantidade de água consumida hoje (litros): ")
    print(verificar_consumo(consumido, ideal))

    # Exibe uma frase de inspiração
    mostrar_inspiracao()