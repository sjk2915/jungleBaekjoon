import sys

cho_pieces = list(map(int, sys.stdin.readline().split()))
han_pieces = list(map(int, sys.stdin.readline().split()))

cho_score = cho_pieces[0] * 13 \
          + cho_pieces[1] * 7  \
          + cho_pieces[2] * 5  \
          + cho_pieces[3] * 3  \
          + cho_pieces[4] * 3  \
          + cho_pieces[5] * 2

han_score = han_pieces[0] * 13 \
          + han_pieces[1] * 7  \
          + han_pieces[2] * 5  \
          + han_pieces[3] * 3  \
          + han_pieces[4] * 3  \
          + han_pieces[5] * 2  \
          + 1.5

print("cocjr0208" if cho_score > han_score else "ekwoo")