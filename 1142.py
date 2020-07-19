def main():
    n = int(input())
    x = 1

    for i in range(1, n+1):
        print(str(x)+ " " + str(x+1) + " " + str(x+2) + " PUM")
        x = x+4




if __name__ == "__main__":
    main()