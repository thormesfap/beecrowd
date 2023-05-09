while True:
    try:
        n1, n2 = [int(x) for x in input().split()]
        print( n1 ^ n2)
    except:
        break