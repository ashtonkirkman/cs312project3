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
