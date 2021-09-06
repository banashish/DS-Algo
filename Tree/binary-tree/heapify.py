from heapq import heapify,heappush,heappop

def main():
    heap = []
    heapify(heap)
    heappush(heap,10)
    heappush(heap, 30)
    heappush(heap, 20)
    heappush(heap, 400)
    print(heap[0])
    print(heap)
    print(heappop(heap))
    print(heap)


if __name__ == '__main__':
    main()