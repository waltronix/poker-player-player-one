ranks = [ 0, 1, 2, 3, 4, 5 ]
straights = []
for i in range(13):
    straight = [(j + i) % 13 for j in range(5)]
    straight.sort()
    print(i, straight)
