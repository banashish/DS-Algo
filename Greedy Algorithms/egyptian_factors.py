import math as m

def main(num,den):
    ans = []
    while num != 0:
        x = m.ceil(den/num)
        ans.append(x)
        num = num * x - den
        den = den * x 

    for i in ans:
        print("1/{0}".format(i),end=" ")



if __name__ == '__main__':
    num = 6
    den = 14
    main(num,den)