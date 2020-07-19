def main ():
    n=int(input())
    for num in range(1, n+1):
        l = (num, num**2, num**3)
        l2 = (num, num**2+1,num**3+1)
        print (l)
        print (l2)

if __name__ == "__main__":
    main()