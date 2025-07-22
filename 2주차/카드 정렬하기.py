import sys
import heapq

N = int(sys.stdin.readline().strip())
card_piles = []
for _ in range(N):
    heapq.heappush(card_piles, int(sys.stdin.readline().strip()))

sort_count = 0
while len(card_piles) > 1:
    card_pile_1 = heapq.heappop(card_piles)
    sort_count += card_pile_1
    card_pile_2 = heapq.heappop(card_piles)
    sort_count += card_pile_2
    heapq.heappush(card_piles, card_pile_1 + card_pile_2)

print(sort_count)