class LinearPQ:
    def __init__(self):
        self.data = []
        self.position_map = {}

    def insert(self, node: int, priority: float):
        self.data.append((node, priority))
        self.position_map[node] = len(self.data) - 1

    def decrease_key(self, node: int, new_priority: float):
        position = self.position_map[node]
        self.data[position] = (node, new_priority)

    def delete_min(self):
        min_index = 0
        current_index = 0
        for node in self.data:
            if node[1] < self.data[min_index][1]:
                min_index = current_index
            current_index += 1

        node = self.data.pop(min_index)[0]
        del self.position_map[node]

        if min_index < len(self.data):
            for n, position in self.position_map.items():
                if position > min_index:
                    self.position_map[n] -= 1

        return node

    def is_empty(self):
        return not self.data

    def __str__(self):
        return f"{self.data}"


class HeapPQ:
    def __init__(self):
        self.heap = []
        self.position_map = {}

    def insert(self, node: int, priority: float):
        self.heap.append((node, priority))
        index = len(self.heap) - 1
        self.position_map[node] = index
        self._bubble_up(index)

    def delete_min(self):
        if len(self.heap) == 0:
            return None

        self._swap(0, len(self.heap) - 1)
        min_node = self.heap.pop()[0]
        del self.position_map[min_node]

        if len(self.heap) > 0:
            self._sift_down(0)

        return min_node

    def decrease_key(self, node: int, new_priority: float):
        index = self.position_map[node]
        self.heap[index] = (node, new_priority)
        self._bubble_up(index)

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][1] < self.heap[parent_index][1]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        length = len(self.heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < length and self.heap[smallest][1] > self.heap[left_child][1]:
                smallest = left_child
            if right_child < length and self.heap[smallest][1] > self.heap[right_child][1]:
                smallest = right_child
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        self.position_map[self.heap[index1][0]] = index1
        self.position_map[self.heap[index2][0]] = index2

    def is_empty(self):
        return not self.heap

    def __str__(self):
        return f"{self.heap}"


