def main():
    inputs = input().split()
    s = int(inputs[0])
    t = int(inputs[1])
    f = int(inputs[2])
    r = s + t + f
    if r > 23:
        r = r - 24
    elif r < 0:
        r = r + 24
    elif r == 24:
        r = 0
    print(str(r))
if __name__ == "__main__":
    main()