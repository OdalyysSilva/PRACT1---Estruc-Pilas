class pila():
    def __init__(self):
        self.items = []
  
    def insertar(self, letra): # No es necesario declarar explícitamente el valor de una variable antes de usarla
        if len(self.items) < 8: # Capacidad máxima de la pila
            self.items.append(letra) # Guarda elementos
            print(f"Letra '{letra}' insertada en la pila. (Tope = {len(self.items)})")
        else:
            print(f"La pila está llena. No se puede insertar '{letra}'.")
        self.mostrar()  # Mostrar el contenido de la pila después de agregarle
    
    def eliminar(self):
       if self.items:
            letra = self.items.pop() # Quita elementos
            print(f"Letra '{letra}' eliminada de la pila. (Tope = {len(self.items)})")
           # len: Muestra el numero de elementos actuales que están dentro de la pila
       else:
           print("La pila está vacía, no hay nada que eliminar.\n")
        
    def mostrar(self):
        if self.items: # Va actualizando la pila
            print("Pila actual:", self.items, "\n")
        else:
            print("La pila está vacía.")
              
p = pila()  
p.insertar("x")
p.insertar("y")
p.eliminar()
p.eliminar()
p.eliminar()
p.insertar("v")
p.insertar("w")
p.eliminar()
p.insertar("r")
