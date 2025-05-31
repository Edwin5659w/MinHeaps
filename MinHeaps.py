class Tarea:
    def _init_(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def _lt_(self, other):
        return self.prioridad < other.prioridad

    def _str_(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"

class MinHeap:
    def __init__(self, max_size):
        self.heap = [None] * max_size
        self.size = 0
        self.max_size = max_size

    def parent_index(self, i):
        return (i - 1) // 2

    def left_child_index(self, i):
        return 2 * i + 1

    def right_child_index(self, i):
        return 2 * i + 2

    def is_leaf(self, i):
        return self.left_child_index(i) >= self.size

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
