from priority_queues import LinearPQ, HeapPQ


def test_insert_linear_pq():
    pq = LinearPQ()
    pq.insert(1, 1)
    pq.insert(2, 2)
    pq.insert(3, 3)
    pq.insert(4, 4)
    pq.insert(5, 5)
    assert pq.data == [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    assert pq.position_map == {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}


def test_decrease_key_linear_pq():
    pq = LinearPQ()
    pq.insert(1, 10)
    pq.insert(2, 5)
    pq.decrease_key(1, 3)
    pq.decrease_key(2, 1)
    assert pq.data == [(1, 3), (2, 1)]


def test_delete_min_linear_pq():
    pq = LinearPQ()
    pq.insert(1, 3.2)
    pq.insert(2, 2.2)
    pq.insert(3, 1.2)
    minimum = pq.delete_min()
    assert minimum == 3


def test_insert_heap_pq():
    pq = HeapPQ()
    pq.insert(1, 1)
    pq.insert(2, 2)
    pq.insert(3, 3)
    pq.insert(4, 4)
    pq.insert(5, 5)
    assert pq.heap == [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    assert pq.position_map == {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}


def test_delete_min_heap_pq():
    pq = HeapPQ()
    pq.insert(1, 3.2)
    pq.insert(2, 2.2)
    pq.insert(3, 1.2)
    pq.insert(4, 4.2)
    minimum = pq.delete_min()
    assert minimum == 3

def test_decrease_key_heap_pq():
    pq = HeapPQ()
    pq.insert(1, 10)
    pq.insert(2, 5)
    pq.decrease_key(1, 3)
    pq.decrease_key(2, 1)
    assert pq.heap == [(2, 1), (1, 3)]
