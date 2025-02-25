# Módulo de gestión de pedidos
class Pedido:
    def __init__(self, cliente, pizzas):
        self.cliente = cliente
        self.pizzas = pizzas
        self.estado = "Pendiente"
    
    def procesar_pedido(self):
        self.estado = "En preparación"
        print(f"Pedido para {self.cliente} en preparación...")
    
    def completar_pedido(self):
        self.estado = "Completado"
        print(f"Pedido para {self.cliente} completado!")

    # Módulo de preparación de pizzas
class Pizza:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def preparar(self, inventario):
        for ingrediente in self.ingredientes:
            if inventario.verificar_ingrediente(ingrediente):
                inventario.utilizar_ingrediente(ingrediente)
            else:
                print(f"Falta {ingrediente}, no se puede preparar la pizza {self.nombre}")
                return False
        print(f"Pizza {self.nombre} preparada!")
        return True
