class Tarea:
    def _init_(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def _lt_(self, other):
        return self.prioridad < other.prioridad

    def _str_(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"
