import math

def baskara(a, b, c):
    delta = b**2 - (4 * a * c)
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a

    return x1, x2

def main():
    x1, x2= baskara(1, -7, 12)
    print(x1, x2)

if __name__ == "__main__":
    main()



