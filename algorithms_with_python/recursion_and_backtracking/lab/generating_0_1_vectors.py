def vector_generator(idx, vector):
    if idx >= len(vector):
        print(*vector, sep="")
        return
    for num in range(0, 2):
        vector[idx] = num
        vector_generator(idx + 1, vector)


number = int(input())
vector = [None] * number
vector_generator(0, vector)

