N = int(input())

def times(x):
    return (x * 100) - 1

def nearest():
    a = 1
    while N - times(a) > -1:
        if N - times(a) < 100:
            y = times(a + 1) - N
            if y < N - times(a):
                print(times(a+1))
            elif y == N - times(a):
                print(times(a+1))
            else:
                print(times(a))
        a += 1

nearest()