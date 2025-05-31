class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, other):
        return self.prioridad < other.prioridad

    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"

class MinHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.heap = [0] * maxSize

    def parentIndex(self, i):
        return (i - 1) // 2

    def leftChildIndex(self, i):
        return 2 * i + 1

    def rightChildIndex(self, i):
        return 2 * i + 2

    def isLeaf(self, i):
        return self.leftChildIndex(i) >= self.size

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        if self.size >= self.maxSize:
            print("Heap lleno")
            return
        
        self.heap[self.size] = value
        current = self.size

        while current > 0 and self.heap[current] < self.heap[self.parentIndex(current)]:
            self.swap(current, self.parentIndex(current))
            current = self.parentIndex(current)

        self.size += 1

    def minHeapify(self, i):
        if not self.isLeaf(i):
            left = self.leftChildIndex(i)
            right = self.rightChildIndex(i)
            smallest = i

            if left < self.size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.swap(i, smallest)
                self.minHeapify(smallest)

    def extractMin(self):
        if self.size <= 0:
            print("Heap vacío")
            return None
        
        min = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.minHeapify(0)
        return min
    
    def extractMax(self):
        if self.size <= 0:
            print("Heap vacío")
            return None
        max_index = 0
        for i in range(1, self.size):
            if self.heap[i] > self.heap[max_index]:
                max_index = i
        max_value = self.heap[max_index]
        self.heap[max_index] = self.heap[self.size - 1]
        self.size -= 1
        self.minHeapify(max_index)
        return max_value

# Imprime todas las tareas en el heap (no necesariamente ordenadas)
    def printHeap(self):
        for i in range(self.size):
            print(self.heap[i])

    # Extrae e imprime todas las tareas en orden de prioridad
    def extract_all(self):
        print("\nExtrayendo todas las tareas ordenadas por prioridad:")
        while self.size > 0:
            tarea = self.extractMin()
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
    max_tarea = min_heap.extractMin()
    print(max_tarea)

    print("\nExtrayendo la tarea con menor prioridad:")
    min_tarea = min_heap.extractMax()
    print(min_tarea)

    min_heap.extract_all()

