class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, other):
        return self.prioridad < other.prioridad

    def __str__(self):
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

    def insert(self, tarea):
        if self.size >= self.max_size:
            print("Heap lleno. No se puede insertar.")
            return

        self.heap[self.size] = tarea
        current = self.size
        self.size += 1

        while current > 0 and self.heap[current] < self.heap[self.parent_index(current)]:
            self.swap(current, self.parent_index(current))
            current = self.parent_index(current)

    def min_heapify(self, i):
        if not self.is_leaf(i):
            left = self.left_child_index(i)
            right = self.right_child_index(i)
            smallest = i

            if left < self.size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                self.swap(i, smallest)
                self.min_heapify(smallest)

    def extract_min(self):
        if self.size == 0:
            print("Heap vacío.")
            return None

        min_elem = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return min_elem
    
    # Imprime todas las tareas en el heap (no necesariamente ordenadas)
    def printHeap(self):
        for i in range(self.size):
            print(self.heap[i])

    # Extrae e imprime todas las tareas en orden de prioridad
    def extract_all(self):
        print("\nExtrayendo todas las tareas ordenadas por prioridad:")
        while self.size > 0:
            tarea = self.extract_min()
            print(tarea)


# Ejemplo de uso
if __name__ == "__main__":
    max_size = 10
    min_heap = MinHeap(max_size)

    tareas = [
        Tarea("Mercar", 3),
        Tarea("estudiar para el Examen", 4),
        Tarea("Llamar a Mamá", 1),
        Tarea("Pagar los Servicios", 2),
        Tarea("Lavar los Trastes", 8)
    ]

    for tarea in tareas:
        min_heap.insert(tarea)

    print("Contenido del MinHeap:")
    min_heap.printHeap()

    print("\nExtrayendo la tarea con mayor prioridad:")
    max_tarea = min_heap.extract_min()
    print(max_tarea)


    min_heap.extract_all()

