from collections import deque

transactions = [
    "PAYMENT-101",
    "PAYMENT-102",
    "PAYMENT-103",
    "PAYMENT-104"
]

def process_queue(transactions):
    queue = deque(transactions)
    processed = []

    while queue:
        processed.append(queue.popleft())

    return processed