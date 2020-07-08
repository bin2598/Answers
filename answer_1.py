def server_cost(d1,m1,y1,d2,m2,y2):
    if d1 == d2 and m1 == m2 and y1 == y2:
        return "Server cost Rs. 20"
    elif d1 != d2 and m1 == m2 and y1 == y2:
        d = d2-d1
        cost = 30*d
        return "server cost Rs. ",cost
    elif m1 != m2 and y1 == y2:
        d = abs(m2-m1)
        cost = 1000*d
        return "Server cost Rs. ",cost
    elif y1 != y2:
        d = y2-y1
        return "Server cost Rs. ",20000

if __name__ == '__main__':
    d1M1Y1 = input("Server created date (date month year) :")
    d1M1Y1 = d1M1Y1.split(" ")

    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])

    d2M2Y2 = input("Server deleted date (date month year) :")
    d2M2Y2 = d2M2Y2.split(" ")

    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1,m1,y1,d2,m2,y2)
    print(result)