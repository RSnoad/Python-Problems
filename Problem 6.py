sumlist = []
def sumofsquares(*args):
    for i in args:
        i = i ** 2
        sumlist.append(i)
    return sum(sumlist)


def squareofsums(*args):
    return(sum(args)**2)


print(squareofsums(*range(1, 101)) - sumofsquares(*range(1, 101) ))