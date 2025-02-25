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