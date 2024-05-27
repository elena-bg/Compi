class SymbolTable:
    def __init__(self):
        self.symbols = {}  # Diccionario para almacenar los símbolos por ámbito
        self.functions = {} # 
        self.gint = 1000
        self.gfl = 2000
        self.lint = 3000
        self.lfl = 4000
        self.tint = 5000
        self.tflo = 6000
        self.tbool = 7000
        self.ctint = 8000
        self.ctfl = 9000
        self.ctstr = 10000
        self.op_dict = {
            '+' : 1,
            '-' : 2,
            '*' : 3,
            '/' : 4,
            '<' : 5,
            '>' : 6,
            '==' : 7,
            '!=' : 8,
            '(' : 9,
            ')' : 10,
            '<=' : 11,
            '>=' : 12,
            'if' : 13,
            'else' : 14,
            '=' : 15,
            '%' : 16,
            'print' : 17,
            'ERA': 18,
            'PARAM': 19,
            'GOSUB': 20,
            'RET': 21
        }
        self.cuadruplo = []
        self.saltos = []
        self.operando = []
        self.tipos = []
        self.operador = []
        self.constantes = {}
        self.cubito = cubo()
        self.cont = 0
        self.temporals = []
        self.param_count = 0  # Para llevar la cuenta de los parámetros
        self.activation_stack = []  # Pila para los espacios de activación
        self.pila_retorno = []  # Pila para manejar los retornos de las funciones
        
        
    def reservar_espacio_activacion(self, function_name):
        # Puedes usar un diccionario para almacenar el espacio de activación
        print("Holis")
        print(self.cuadruplo)
        espacio_activacion = {
            'vars': {},
            'temporals': {}
        }
        # Añadir el espacio de activación a la pila
        self.activation_stack.append(espacio_activacion)
        print("ActivStack: ", self.activation_stack)
        
    def ooop(self, value):
        for key, val in self.op_dict.items():
            if val == value:
                return key
        return None

    """
        def print_function(self):
        if len(self.operando) > 0:
            value = self.operando.pop()
            if value in self.constantes:
                const = self.constantes[value]['id']
                print(f"{const}")
            else:
                for key, val in self.symbols.items():
                    if val['memoria'] == value:
                        print(f"{val['valor']}")
                        break
        else:
            print("Error: No hay valor para imprimir")
    """

        

    def print_function(self):
        self.operador.append('print')
        exists = any(item.get('memoria') == self.operando[-1] for item in self.symbols.values())

        if exists:
            operator = self.operador.pop()
            #print("operator: ", operator)
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
               
    def add_temporal(self, nombre, tipo, scope, memoria):
        newId = nombre + str(memoria)
        self.symbols[newId] = {'tipo': tipo, 'scope': scope, 'memoria' : memoria, 'valor' : 0}

    def push_sumas(self):
        if len(self.operador) > 0:
            if self.operador[-1] == 1  or self.operador[-1] == 2:
                right_op = self.operando.pop()
                right_type = self.tipos.pop()
                left_op = self.operando.pop()
                left_type = self.tipos.pop()
                operator = self.operador.pop()
                typo = self.cubito.consultar_cubo(self.ooop(operator), left_type, right_type)
                resultado = 0
                if typo == "error":
                    raise ValueError("An Error ocurred")
                else:
                    if typo == "int": 
                        resultado = self.tint
                        self.tint += 1
                        self.add_temporal('ti', 'int', 0, resultado)
                    elif typo == "float": 
                        resultado = self.tflo
                        self.tflo += 1
                        self.add_temporal('tf', 'float', 0, resultado)
                    elif typo == "bool": 
                        resultado = self.tflo
                        self.tflo += 1
                        self.add_temporal('tb', 'bool', 0, resultado)
                quad = (operator, left_op, right_op, resultado)
                self.cuadruplo.append(quad)
                self.cont += 1
                self.operando.append(resultado)
                self.tipos.append(typo)
                #for i in range (len(self.cuadruplo)): 
                    #print(self.cuadruplo[i], "\n")
            
    def push_multi(self):
        if len(self.operador) > 0:
            if self.operador[-1] in [3, 4, 16]:
                if len(self.operando) < 2:  # Verificar si hay al menos dos operandos en la pila
                    raise IndexError("Not enough operands for operation")
                right_op = self.operando.pop()
                right_type = self.tipos.pop()
                left_op = self.operando.pop()
                left_type = self.tipos.pop()
                operator = self.operador.pop()
                typo = self.cubito.consultar_cubo(self.ooop(operator), left_type, right_type)
                resultado = 0
                if typo == "error":
                    raise ValueError("An Error ocurred")
                else:
                    if typo == "int": 
                        resultado = self.tint
                        self.tint += 1
                        self.add_temporal('ti', 'int', 0, resultado)
                    elif typo == "float": 
                        resultado = self.tflo
                        self.tflo += 1
                        self.add_temporal('tf', 'float', 0, resultado)
                    elif typo == "bool": 
                        resultado = self.tbool
                        self.tbool += 1
                        self.add_temporal('tb', 'bool', 0, resultado)
                quad = (operator, left_op, right_op, resultado)
                self.cuadruplo.append(quad)
                self.cont += 1
                self.operando.append(resultado)
                self.tipos.append(typo)
                #for i in range (len(self.cuadruplo)): 
                    #print(self.cuadruplo[i], "\n")
            
    def push_mayor_menor(self):
        if len(self.operador) > 0:
            if self.operador[-1] in [5, 6, 7, 8, 11, 12]:
                right_op = self.operando.pop()
                right_type = self.tipos.pop()
                left_op = self.operando.pop()
                left_type = self.tipos.pop()
                operator = self.operador.pop()
                typo = self.cubito.consultar_cubo(self.ooop(operator), left_type, right_type)
                resultado = 0
                if typo == "error":
                    raise ValueError("An Error ocurred")
                else:
                    if typo == "int": 
                        resultado = self.tint
                        self.tint += 1
                        self.add_temporal('ti', 'int', 0, resultado)
                    elif typo == "float": 
                        resultado = self.tflo
                        self.tflo += 1
                        self.add_temporal('tf', 'float', 0, resultado)
                    elif typo == "bool": 
                        resultado = self.tbool
                        self.add_temporal('tb', 'bool', 0, resultado)
                        self.tbool += 1
                quad = (operator, left_op, right_op, resultado)
                self.cuadruplo.append(quad)
                self.cont += 1
                self.operando.append(resultado)
                self.tipos.append(typo)
                #for i in range (len(self.cuadruplo)): 
                    #print(self.cuadruplo[i], "\n")
          
    def push_parentesis(self, par_izq):
        self.operador.append(self.op_dict[par_izq])
    def pop_parentesis(self):
        self.operador.pop()


    def push_operador(self, op):
        self.operador.append(self.op_dict[op])
    
    def push_factor(self, factor, tipo, isConst):
        if isConst == False:
            try:
                #print(self.symbols)
                self.operando.append(self.symbols[factor]['memoria'])
                self.tipos.append(self.symbols[factor]['tipo'])
            except:
                raise KeyError(f"Symbol '{factor}' not in this scope")
        if tipo == 'float' and isConst: 
            self.constantes[self.ctfl] = {'id': factor}
            self.operando.append(self.ctfl)
            self.tipos.append('float')
            self.ctfl += 1
            if self.ctfl >= 10000:
                print('memoria llena:)')
        if tipo == 'int' and isConst: 
            self.constantes[self.ctint] = {'id': factor}
            self.operando.append(self.ctint)
            self.tipos.append('int')
            self.ctint += 1
            if self.ctint >= 9000:
                print('memoria llena:)')
        if tipo == 'string' and isConst: 
            self.constantes[self.ctstr] = {'id': factor}
            self.operando.append(self.ctstr)
            self.tipos.append('string')
            self.ctstr += 1
            if self.ctstr >= 11000:
                print('memoria llena:)')
            
            
    def assign(self, new_op, new_oper):
        #print("--------------assign------------------")
        self.operando.append(self.symbols[new_op]['memoria'])
        self.tipos.append(self.symbols[new_op]['tipo'])
        self.operador.append(self.op_dict[new_oper])
        
        operator = self.operador.pop()
        operator2 = self.ooop(operator)
        op1type = self.tipos.pop()
        operando1 = self.operando.pop()
        target = self.operando.pop()
        targetype = self.tipos.pop()
        #print(operator2, op1type, targetype)
        resultype = self.cubito.consultar_cubo(operator2, op1type, targetype)
        if resultype == 'error':
            raise ValueError("no che puede")
        else: 
            quad = (operator, target, None, operando1)
            self.cuadruplo.append(quad)
            self.cont += 1
            #print(self.cuadruplo)
        
        
    
    def memory(self, nombre):
        if self.symbols[nombre]['tipo'] == 'int' and self.symbols[nombre]['scope'] == 0:
            self.symbols[nombre]['memoria'] = self.gint
            self.gint += 1
            if self.gint >= 2000:
                print("memoria llena :)")
        if self.symbols[nombre]['tipo'] == 'float' and self.symbols[nombre]['scope'] == 0:
            self.symbols[nombre]['memoria'] = self.gfl
            self.gfl += 1
            if self.gfl >= 3000:
                print("memoria llena :)")
        if self.symbols[nombre]['tipo'] == 'int' and self.symbols[nombre]['scope'] != 0:
            self.symbols[nombre]['memoria'] = self.lint
            self.lint += 1
            if self.gint >= 4000:
                print("memoria llena :)")
        if self.symbols[nombre]['tipo'] == 'float' and self.symbols[nombre]['scope'] != 0:
            self.symbols[nombre]['memoria'] = self.lfl
            self.lfl += 1
            if self.lfl >= 5000:
                print("memoria llena :)")
                
                
    def add_symbol(self, nombre, tipo, scope):
        new_names = nombre.split(",")
        for new_name in new_names:
            if new_name in self.symbols and self.symbols[new_name]["scope"] == scope and self.symbols[new_name]["scope"] == 0:
                raise ValueError(f"Error: El símbolo '{new_name}' ya está declarado en el ámbito '{scope}'")
            # Añade el símbolo al ámbito correspondiente
            self.symbols[new_name] = {"tipo": tipo, "scope": scope, "memoria": 0, "valor": 0}    # Crea un nuevo diccionario para el nuevo ámbito
            self.memory(new_name)
            #print(self.symbols)
            
    def function_call(self, function_name):
        if function_name not in self.functions:
            raise ValueError(f"Error: La función '{function_name}' no está declarada")

        # Paso 1: Generar ERA (Espacio de Activación)
        #El cuadruplo ERA reserva espacio para las variables locales y temporales de la función. 
        quad = (18, function_name, None, None)
        self.cuadruplo.append(quad)

        # Paso 2: Pasar parámetros
        for param in self.functions[function_name]['params']:
            if len(self.operando) == 0:
                raise ValueError("No hay suficientes parámetros en la pila")
            arg = self.operando.pop()
            quad = (self.op_dict['PARAM'], arg, None, f'param{self.param_count}')
            self.cuadruplo.append(quad)
            self.param_count += 1

        # Paso 3: Generar GOSUB (Ir a Subrutina)
        quad = (20, function_name, None, None)
        self.cuadruplo.append(quad)

        # Paso 4: Resetear contador de parámetros
        self.param_count = 0
   

    
    def add_func(self, nombre, params, vars, scope):
        print("params: ", params)
        parametros = []
        variables = []
        if nombre in self.functions:
            raise ValueError(f"Error: La función '{nombre}' ya está declarada en el ámbito '{scope}'")
        #quad = (18, nombre, None, None)
        #self.cuadruplo.append(quad)
        if params or vars:
            if vars:
                new_variables = vars[3:].replace(";", ",").replace(":", ",")
                print("new variables: ", new_variables)
                variables_list = new_variables.split(",")
                print("variables list: ", new_variables)
                for var in variables_list:
                    if var in self.symbols:
                        variables.append(var)
            if params and isinstance(params, str):
                new_parametros = params.replace(";", ",").replace(":", ",")
                print("new parametros: ", new_variables)
                parametros_list = new_parametros.split(",")
                print("parametros list: ", new_variables)
                for param in parametros_list:
                    if param in self.symbols:
                        parametros.append(param)
                        
            self.functions[nombre] = {
                "params": parametros,
                "vars": variables,
            }
        else:
            self.functions[nombre] = {
                "params": [],
                "vars": [],
            }
    
    """
    def add_func(self, nombre, params, vars, scope):
        print("params: ", params)
        # 1. Insertar el nombre de la función en la tabla de funciones (DirFunc) y verificar semántica
        if nombre in self.functions:
            raise ValueError(f"Error: La función '{nombre}' ya está declarada en el ámbito '{scope}'")

        # 2. Insertar cada parámetro en la tabla de variables actual (local)
        # 3. Insertar el tipo de cada parámetro en la tabla de parámetros
        parametros = []
        if params:
            param_list = params.split(',')
            print("param_list: ", param_list)
            for param in param_list:
                # Verificar que el parámetro tenga el formato correcto
                parts = param.strip().split()
                if len(parts) != 2:
                    raise ValueError(f"Formato de parámetro incorrecto: '{param}'")
                tipo, nombre_param = parts
                self.add_symbol(nombre_param, tipo, scope)
                parametros.append((nombre_param, tipo))

        # 4. Insertar en DirFunc el número de parámetros definidos
        num_params = len(parametros)

        # 5. Insertar en DirFunc el número de variables locales definidas
        num_vars = 0
        if vars:
            vars_list = vars.split(',')
            for var in vars_list:
                tipo, nombre_var = var.split()
                self.add_symbol(nombre_var, tipo, scope)
                num_vars += 1

        # 6. Insertar en DirFunc el contador actual de cuadruplos (CONT)
        start_quad = len(self.cuadruplo)

        # 7. Liberar la tabla de variables actual (local)
        # Esto se haría al final de la función, en `end_function`

        # Añadir la función a la tabla de funciones (DirFunc)
        self.functions[nombre] = {
            'params': parametros,
            'num_params': num_params,
            'num_vars': num_vars,
            'start_quad': start_quad,
            'end_quad': None,
            'num_temp': 0  # Inicialmente 0, se actualizará en end_function
        }
    """
        
        
            
    # Método para finalizar la definición de una función
    def end_function(self):
        # Generar el cuadruplo RET para indicar el retorno de la función
        quad = (self.op_dict['RET'], None, None, None)
        self.cuadruplo.append(quad)

        # Actualizar el número de temporales utilizados en la función
        num_temp = self.tint - 5000  # Suponiendo que los temporales empiezan en 5000
        current_function = list(self.functions.keys())[-1]
        self.functions[current_function]['num_temp'] = num_temp
        self.functions[current_function]['end_quad'] = len(self.cuadruplo)

        # Liberar la tabla de variables actual (local)
        self.symbols = {k: v for k, v in self.symbols.items() if v['scope'] != current_function}
        
    def function_call(self, function_name):
        # 1. Verificar que la función existe en la tabla de funciones (DirFunc)
        if function_name not in self.functions:
            raise ValueError(f"Error: La función '{function_name}' no está declarada")

        # 2. Generar acción ERA (Expansión de Registro de Activación)
        quad = (self.op_dict['ERA'], function_name, None, None)
        self.cuadruplo.append(quad)
        
        # Iniciar el contador de parámetros (k) en 1
        k = 1
        param_types = [param[1] for param in self.functions[function_name]['params']]

        # 3. Argumento = PilaO.Pop(), TipoArgumento = PTypes.Pop()
        for param_type in param_types:
            if function_name not in self.functions:
                raise ValueError(f"Error: La función '{function_name}' no está declarada")

        quad = (self.op_dict['ERA'], function_name, None, None)
        self.cuadruplo.append(quad)

        for param in self.functions[function_name]['params']:
            if len(self.operando) == 0:
                raise ValueError("No hay suficientes parámetros en la pila")
            arg = self.operando.pop()
            quad = (self.op_dict['PARAM'], arg, None, f'param{self.param_count}')
            self.cuadruplo.append(quad)
            self.param_count += 1

        quad = (self.op_dict['GOSUB'], function_name, None, None)
        self.cuadruplo.append(quad)

        self.param_count = 0

    
    def fill(self, index, value):
        op, left, right, _ = self.cuadruplo[index]
        self.cuadruplo[index] = (op, left, right, value)
    
    def ifSt(self):
        #print(f"------------------IF STATEMENT------------ \n",  self.tipos)
        # Paso 1: Evaluación de la condición
        exp_type = self.tipos.pop()
        if exp_type != "bool":
            raise ValueError("No es un bool")
        else:
            result = self.operando.pop()
            quad = ("GotoF", result, None, None)
            #self.saltos.append(self.cont - 1)
            self.cuadruplo.append(quad)
            self.saltos.append(len(self.cuadruplo) - 1)
            #self.cont += 1
    
    def endIf(self):
        # Paso 2: Finalización de la condición
        end = self.saltos.pop()
        quad = list(self.cuadruplo[end])
        quad[3] = len(self.cuadruplo)
        self.cuadruplo[end] = tuple(quad)
        #self.fill(end + 1 , self.cont -1)
        #self.fill(end , self.cont)
    
        
    def elseSt(self):
        # Generar cuádruplo Goto para saltar al final del else
        quad = ("Goto", None, None, None)
        self.cuadruplo.append(quad)
        #self.cont += 1
        # Guardar el índice del cuádruplo Goto
        false_jump = self.saltos.pop()
        quad = list(self.cuadruplo[false_jump])
        quad[3] = len(self.cuadruplo)

        self.cuadruplo[false_jump] = tuple(quad)
        self.saltos.append(len(self.cuadruplo) - 1)
        #self.saltos.append(self.cont - 1)
        # Completar el cuádruplo GotoF del if statement
        #self.fill(false_jump + 1, self.cont)
        
    def whileSt(self):
        #print("-----------INICIA WHILE----------")
        # Paso 1: Guardar el inicio del bucle
        self.saltos.append(len(self.cuadruplo) - 1)
        
    def whileIf(self):
        #print(f"------------------evalua cond------------ \n",  self.tipos)
        # Paso 1: Evaluación de la condición
        self.saltos.append(len(self.cuadruplo) - 1)
        #exp_type = self.tipos.pop()
        #if exp_type != "bool":
            #raise ValueError("No es un bool")
        #else:
            #result = self.operando.pop()
            #quad = ("GotoF", result, None, None)
            #self.saltos.append(self.cont - 1)
            #self.cuadruplo.append(quad)
            #for i in range (len(self.cuadruplo)):
                #print(i, self.cuadruplo[i], "\n")
            #self.cont += 1
    
    def end_while(self):
        # Paso 3: Finalización del bucle
        end = self.saltos.pop()
        return_to = self.saltos.pop() + 1
        quad = ("Goto", None, None, return_to)
        self.cuadruplo.append(quad)
        #self.cont += 1
        quad = list(self.cuadruplo[end])
        quad[3] = len(self.cuadruplo)
        self.cuadruplo[end] = tuple(quad)
        #self.fill(end + 1, self.cont - 1) #maybe end +1
        #for i in range (len(self.cuadruplo)):
            #print(i, self.cuadruplo[i], "\n")
        
    
    
    def forSt(self, assign):
        print("inicio for")
        # Paso 1: Inicialización del índice
        #quad = (15, assign[0], assign[1], None)
        #self.cuadruplo.append(quad)
        # Paso 2: Guardar el inicio del bucle
        self.saltos.append(len(self.cuadruplo))
        
    def for_condition(self):
        # Paso 3: Evaluación de la condición
        exp_type = self.tipos.pop()
        if exp_type != "bool":
            raise ValueError("No es un bool")
        else:
            result = self.operando.pop()
            quad =("GotoF", result, None, None)
            self.cuadruplo.append(quad)
            self.saltos.append(len(self.cuadruplo) - 1)
    
    def for_increment(self, var, oper=None, expr=None):
        if oper == "++":
            quad = ("+", var, "1", var)
        elif oper == "--":
            quad = ("-", var, "1", var)
        elif oper in ["+=", "-="]:
            quad = (oper[0], var, expr, var)
        else:
            raise ValueError("Operador de incremento no soportado")
        
        self.cuadruplo.append(quad)
        
    def end_for(self):
        # Paso 4: Finalización del bucle
        end = self.saltos.pop()
        return_to = self.saltos.pop()
        quad = ("Goto", None, None, return_to)
        self.cuadruplo.append(quad)
        quad = list(self.cuadruplo[end])
        quad[3] = len(self.cuadruplo)
        self.cuadruplo[end] = tuple(quad)
        for i in range (len(self.cuadruplo)): 
            print(i, self.cuadruplo[i], "\n")
    

    def print_symbols(self):
            for nombre, info in self.symbols.items():
                print(f" Nombre variable: {nombre}: Tipo: {info['tipo']}, Scope: {info['scope']}")
                
    def print_funs(self):
        for nombre, info in self.functions.items():
            print(f"Functions: {nombre}: Parameters: {info['params']}, Variables: {info['vars']}")
   
            
    def pop_symbols(self, parametros, variables):
        if parametros: 
            for parametro in parametros:
                del self.symbols[parametro]
        if variables: 
            for variable in variables:
                del self.symbols[variable]       
             
    def pop_func(self, nombre):
        self.pop_symbols(self.functions[nombre]['params'], self.functions[nombre]['vars'])
        del self.functions[nombre]
        
    def pasar_parametro(self, arg, param_name):
        print("pasar params")
        if not self.activation_stack:
            raise ValueError("No hay espacio de activación disponible para pasar parámetros")

        # Obtener el espacio de activación actual
        espacio_activacion = self.activation_stack[-1]
        # Almacenar el parámetro en el espacio de activación
        espacio_activacion['vars'][param_name] = arg
        
    def buscar_funcion(self, nombre):
        print("loop", self.cuadruplo)
        for i in range(len(self.cuadruplo)):
            print("test loop")
            if self.cuadruplo[i][0] == 18 and self.cuadruplo[i][1] == nombre:
                print("cuad i0: ", self.cuadruplo[i][0])
                print("cuad i1: ", self.cuadruplo[i][1])
                print("i + 1: ", i + 1)
                return i + 1
        raise ValueError(f"Función {nombre} no encontrada")
    


    def maquina(self): 
        quad = 0
        #print("DELUSSION: ", len(self.cuadruplo))
        while quad < len(self.cuadruplo):
            oper1 = self.cuadruplo[quad][1]
            oper2 = self.cuadruplo[quad][2]
            result = self.cuadruplo[quad][3]

            constant_key = [key for key, value in self.constantes.items() if key == oper1]

            oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]

            #operador =
            if self.cuadruplo[quad][0] == 15:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper1]
                #print("ck: ", constant_key)
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                #print("mq: ", oper2_key)
                if constant_key:
                    symbol_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                    str_symbol_key = symbol_key[0]
                    str_constant_key = constant_key[0]
                    self.symbols[str_symbol_key]["valor"] = self.constantes[str_constant_key]["id"]

                elif oper1 >= 5000:
                    symbol_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                    str_symbol_key = symbol_key[0]
                    self.symbols[str_symbol_key]["valor"] = self.temporals[-1]

                elif oper1 < 5000:
                    str_oper_key = oper2_key[0]
                    symbol_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                    str_symbol_key = symbol_key[0]
                    self.symbols[str_symbol_key]["valor"] = self.symbols[str_oper_key]["valor"]


            #operator is +
            elif self.cuadruplo[quad][0] == 1:
                print("Rolis Quad: ", quad)
                #print("oper1: ", oper1, " oper2: ", oper2)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]

                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) + int(self.constantes[str_constant_key]["id"]))

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) + int(self.symbols[str_oper2_key]["valor"]))

                #operador -
            elif self.cuadruplo[quad][0] == 2:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]

                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) - int(self.constantes[str_constant_key]["id"]))

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) - int(self.symbols[str_oper2_key]["valor"]))

            #operator is *
            elif self.cuadruplo[quad][0] == 3:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) * int(self.constantes[str_constant_key]["id"]))


                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) * int(self.symbols[str_oper2_key]["valor"]))

            #operator is /
            elif self.cuadruplo[quad][0] == 4:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) / int(
                        self.constantes[str_constant_key]["id"]))

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) / int(self.symbols[str_oper2_key]["valor"]))

            # operator is <
            elif self.cuadruplo[quad][0] == 5:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]
                result_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                str_result_key = result_key[0]
                print(constant_key, oper2_key, oper1_key, str_oper1_key, result_key, str_result_key)
                if constant_key:
                    str_constant_key = constant_key[0]
                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) < int(
                        self.constantes[str_constant_key]["id"])
                    print("AAAAAAH", self.symbols[str_result_key]["valor"])

                elif oper2_key:
                    str_oper2_key = oper2_key[0]

                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) < int(self.symbols[str_oper2_key]["valor"])
                    print("AAAAAAH", self.symbols[str_result_key]["valor"])

            #operator is >
            elif self.cuadruplo[quad][0] == 6:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]
                result_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                str_result_key = result_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]

                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) > int(
                        self.constantes[str_constant_key]["id"])

                elif oper2_key:
                    str_oper2_key = oper2_key[0]

                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) > int(self.symbols[str_oper2_key]["valor"])

            # operator is >=
            elif self.cuadruplo[quad][0] == 12:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]
                result_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                str_result_key = result_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]
                    #print("op 1: ", self.symbols[str_oper1_key]["valor"])
                    #print("op 2: ", self.constantes[str_constant_key]["id"])
                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) >= int(
                        self.constantes[str_constant_key]["id"])

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    #print("op 1: ", self.symbols[str_oper1_key]["valor"])
                    #print("op 2: ", self.symbols[str_oper2_key]["valor"])
                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) >= int(
                        self.symbols[str_oper2_key]["valor"])

            # operator is <=
            elif self.cuadruplo[quad][0] == 11:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]
                result_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                str_result_key = result_key[0]
                if constant_key:
                    str_constant_key = constant_key[0]
                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) <= int(
                        self.constantes[str_constant_key]["id"])

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) <= int(
                        self.symbols[str_oper2_key]["valor"])

            # operator is %
            elif self.cuadruplo[quad][0] == 3:
                print("Rolis Quad: ", quad)
                constant_key = [key for key, value in self.constantes.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memoria') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]
                    self.temporals.append(
                        int(self.symbols[str_oper1_key]["valor"]) % int(self.constantes[str_constant_key]["id"]))


                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(
                        int(self.symbols[str_oper1_key]["valor"]) % int(self.symbols[str_oper2_key]["valor"]))

            elif self.cuadruplo[quad][0] == "print":
                print("Rolis Quad: ", quad)
                result_key = [key for key, value in self.symbols.items() if value.get('memoria') == result]
                constant_key = [key for key, value in self.constantes.items() if key == result]

                if result_key:
                    str_result_key = result_key[0]
                    result = self.symbols[str_result_key]["valor"]

                elif constant_key:
                    str_constant_key = constant_key[0]
                    result = self.constantes[str_constant_key]["id"]


                print(result) #VALOR FINAL

            elif self.cuadruplo[quad][0] == self.op_dict['ERA']:
                print(f"ERA: Reservar espacio para la función {oper1}")
                self.reservar_espacio_activacion(oper1)

            elif self.cuadruplo[quad][0] == self.op_dict['PARAM']:
                print(f"PARAM: Pasar parámetro {oper1} como {result}")
                self.pasar_parametro(oper1, result)

            elif self.cuadruplo[quad][0] == self.op_dict['GOSUB']:
                self.pila_retorno.append(quad + 1)
                print(f"GOSUB: Saltar a la función {oper1}, dirección de retorno {quad + 1}")
                quad = self.buscar_funcion(oper1)
                print(f"GOSUB: Nueva dirección {quad}")
                continue

            elif self.cuadruplo[quad][0] == self.op_dict['RET']:
                if self.pila_retorno:
                    quad = self.pila_retorno.pop()
                    self.activation_stack.pop()  # Eliminar el espacio de activación actual
                    print(f"RET: Retornar a la dirección {quad}")
                    continue
                else:
                    raise ValueError("Error: Pila de retorno vacía al intentar retornar de una función")

            elif self.cuadruplo[quad][0] == "GotoF":
                result_key = "tb" + str(self.cuadruplo[quad-1][3])
                print("ROLIS2: ", result_key)
                resultado = self.symbols[result_key]["valor"]
                if type(resultado) == bool:
                    if resultado == False:
                        quad = self.cuadruplo[quad][3]
                        continue

            elif self.cuadruplo[quad][0] == "Goto":
                print("Rolis Quad: ", quad)
                quad = self.cuadruplo[quad][3]
                print("ROLIS3: ", quad)
                continue

            print("LENNN: ", len(self.cuadruplo))
            quad += 1
                
        

class cubo:
    def __init__(self): 
        self.tip = ["int", "float", "bool"]
        self.oper = ["+", "-", "*", "/", "==", "!=", "<", "<=", ">", ">=", '=', '%']
        # Crear la estructura vacía del cubo
        self.cubo_semantico = {op: {t1: {t2: None for t2 in self.tip} for t1 in self.tip} for op in self.oper}
        
        # Operaciones aritméticas
        self.cubo_semantico["+"]["int"]["int"] = "int"
        self.cubo_semantico["+"]["int"]["float"] = "float"
        self.cubo_semantico["+"]["float"]["int"] = "float"
        self.cubo_semantico["+"]["float"]["float"] = "float"

        self.cubo_semantico["-"]["int"]["int"] = "int"
        self.cubo_semantico["-"]["int"]["float"] = "float"
        self.cubo_semantico["-"]["float"]["int"] = "float"
        self.cubo_semantico["-"]["float"]["float"] = "float"

        self.cubo_semantico["*"]["int"]["int"] = "int"
        self.cubo_semantico["*"]["int"]["float"] = "float"
        self.cubo_semantico["*"]["float"]["int"] = "float"
        self.cubo_semantico["*"]["float"]["float"] = "float"

        self.cubo_semantico["/"]["int"]["int"] = "float"  # Asumimos que / siempre produce un float
        self.cubo_semantico["/"]["int"]["float"] = "float"
        self.cubo_semantico["/"]["float"]["int"] = "float"
        self.cubo_semantico["/"]["float"]["float"] = "float"
        
        self.cubo_semantico["%"]["int"]["int"] = "int"  # <-- Añadido

        # Operaciones de comparación
        self.cubo_semantico["=="]["int"]["int"] = "bool"
        self.cubo_semantico["=="]["int"]["float"] = "bool"
        self.cubo_semantico["=="]["float"]["int"] = "bool"
        self.cubo_semantico["=="]["float"]["float"] = "bool"
        self.cubo_semantico["=="]["bool"]["bool"] = "bool"

        self.cubo_semantico["!="]["int"]["int"] = "bool"
        self.cubo_semantico["!="]["int"]["float"] = "bool"
        self.cubo_semantico["!="]["float"]["int"] = "bool"
        self.cubo_semantico["!="]["float"]["float"] = "bool"
        self.cubo_semantico["!="]["bool"]["bool"] = "bool"

        self.cubo_semantico["<"]["int"]["int"] = "bool"
        self.cubo_semantico["<"]["int"]["float"] = "bool"
        self.cubo_semantico["<"]["float"]["int"] = "bool"
        self.cubo_semantico["<"]["float"]["float"] = "bool"

        self.cubo_semantico["<="]["int"]["int"] = "bool"
        self.cubo_semantico["<="]["int"]["float"] = "bool"
        self.cubo_semantico["<="]["float"]["int"] = "bool"
        self.cubo_semantico["<="]["float"]["float"] = "bool"

        self.cubo_semantico[">"]["int"]["int"] = "bool"
        self.cubo_semantico[">"]["int"]["float"] = "bool"
        self.cubo_semantico[">"]["float"]["int"] = "bool"
        self.cubo_semantico[">"]["float"]["float"] = "bool"

        self.cubo_semantico[">="]["int"]["int"] = "bool"
        self.cubo_semantico[">="]["int"]["float"] = "bool"
        self.cubo_semantico[">="]["float"]["int"] = "bool"
        self.cubo_semantico[">="]["float"]["float"] = "bool"
        
        # Asignación
        self.cubo_semantico["="]["int"]["int"] = "int"
        self.cubo_semantico["="]["int"]["float"] = "float"  # Permitir asignar float a int para conversiones implícitas
        self.cubo_semantico["="]["float"]["float"] = "float"
        self.cubo_semantico["="]["float"]["int"] = "float"  # Permitir asignar int a float
        self.cubo_semantico["="]["bool"]["bool"] = "bool"

        
    def consultar_cubo(self, operacion, tipo1, tipo2):
        resultado = self.cubo_semantico.get(operacion, {}).get(tipo1, {}).get(tipo2, None)
        if resultado is None:
            return "error"
        return resultado
