class Calculadora:
    def __init__(self):
        pass

    def add(self, numbers: list[float | int]) -> float:
        result = 0
        for number in numbers:
            result += number
        self.mostrar_resultado("Soma", numbers, result)
        return result

    def sub(self, numbers: list[float | int]) -> float:
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        self.mostrar_resultado("Subtração", numbers, result)
        return result

    def multi(self, numbers: list[float | int]) -> float:
        result = numbers[0]
        for number in numbers[1:]:
            result *= number
        self.mostrar_resultado("Multiplicação", numbers, result)
        return result

    def divid(self, numbers: list[float | int]) -> float:
        result = numbers[0]
        for number in numbers[1:]:
            if number == 0:
                raise ValueError("Divisão por zero não é permitida.")
            result /= number
        self.mostrar_resultado("Divisão", numbers, result)
        return result

    def mostrar_resultado(self, operacao: str, numbers: list[float | int], resultado: float):
        print(f"{operacao} dos números {numbers} é: {resultado}")