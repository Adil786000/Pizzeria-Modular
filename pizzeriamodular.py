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
# Módulo de gestión de inventario
class Inventario:
    def __init__(self):
        self.ingredientes = {"queso": 10, "tomate": 10, "harina": 10}
    
    def verificar_ingrediente(self, ingrediente):
        return self.ingredientes.get(ingrediente, 0) > 0
    
    def utilizar_ingrediente(self, ingrediente):
        if self.verificar_ingrediente(ingrediente):
            self.ingredientes[ingrediente] -= 1

# Módulo de pagos
class Pago:
    def __init__(self, pedido, cantidad):
        self.pedido = pedido
        self.cantidad = cantidad
    
    def procesar(self):
        print(f"Pago de {self.cantidad}€ por el pedido de {self.pedido.cliente} realizado con éxito.")
        self.pedido.completar_pedido()
