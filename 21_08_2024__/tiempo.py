from time import sleep
def tiempo_pizza(pizza):
    return 20 + len(pizza["ingredientes"])*2

def aceptarPedido(pizza):
    print("Estamos ordenando su pizza...")
    print(f"Su pizza estará lista en {tiempo_pizza(pizza)} minutos")
    sleep(1)
    print("Su pedido está confirmado. Gracias por preferir pizza JAT")
    sleep(1)
