import sys

on_sleep = int(sys.stdin.readline().strip())
wake = int(sys.stdin.readline().strip())
if on_sleep > wake:
    print(24-on_sleep + wake)
else:
    print(wake-on_sleep)