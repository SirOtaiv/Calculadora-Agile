from classes.Calculadora import Calculadora

if __name__ == "__main__":
    calc = Calculadora()

    # Testando as operações
    calc.add([1, 2, 3])  # Soma
    calc.sub([10, 2, 3])  # Subtração
    calc.multi([2, 3, 4])  # Multiplicação
    try:
        calc.divid([100, 5, 2])  # Divisão
        calc.divid([100, 5, 0])  # Tentativa de divisão por zero
    except ValueError as e:
        print(e)