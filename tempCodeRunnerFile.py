def print_function(self):
        self.operador.append('print')
        print(self.operador)
        exists = any(item.get('memoria') == self.operando[-1] for item in self.symbols.values())

        if exists:
            operator = self.operador.pop()
            print("operator: ", operator)
            operands = self.operando.pop()
            quad = (operator, None, None, operands)
            self.cuadruplo.append(quad)
            self.cont += 1

        else:
            existsConst = self.constantes.get(self.operando[-1])
            if existsConst:
                operator = self.operador.pop()
                newConst = self.operando.pop()
                constant_key = [key for key, value in self.constantes.items() if key == newConst]
                constant = constant_key[0]
                quad = (operator, None, None, constant)
                self.cuadruplo.append(quad)
                self.cont += 1
                self.tipos.pop()
                print("QUADS Print function: ", self.cuadruplo)
            else:
                print("Does not exist \n")
    