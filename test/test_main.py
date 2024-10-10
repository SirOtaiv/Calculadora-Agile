from classes.Calculadora import Calculadora
import pytest

class TestCalculadora:

    def setup_method(self):
        self.calculator = Calculadora()

    def test_add(self):
        assert self.calculator.add([2,3]) == 5

    def test_sub(self):
        assert self.calculator.sub([3,2]) == 1
        
    def test_multi(self):
        assert self.calculator.multi([9,3]) == 27
    
    def test_divid(self):
        assert self.calculator.divid([30,3]) == 10
    
    def test_divid_exception(self):
        with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
            self.calculator.divid([100, 10, 0])
    