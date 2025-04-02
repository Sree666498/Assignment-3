from collections import deque

def merge_sorted_queues(q1, q2):
    """Merge two sorted queues into one sorted queue."""
    merged = deque()
    while q1 and q2:
        if q1[0] < q2[0]:
            merged.append(q1.popleft())
        else:
            merged.append(q2.popleft())
    # Add remaining elements (if any)
    merged.extend(q1)
    merged.extend(q2)
    return merged

def bottom_up_merge_sort(items):
    """Perform bottom-up merge sort using queues."""
    # Step 1: Initialize each element in its own queue
    queues = deque(deque([item]) for item in items)
    
    # Step 2: Iteratively merge pairs of queues until one remains
    while len(queues) > 1:
        new_queues = deque()
        while len(queues) > 1:
            q1 = queues.popleft()
            q2 = queues.popleft()
            new_queues.append(merge_sorted_queues(q1, q2))
        if queues:  # If an odd queue remains, carry it forward
            new_queues.append(queues.popleft())
        queues = new_queues
    
    # Step 3: Return the sorted result
    return list(queues[0]) if queues else []

# Example usage:
arr = [5, 3, 8, 6, 2, 7, 4, 1]
sorted_arr = bottom_up_merge_sort(arr)
print(sorted_arr)
