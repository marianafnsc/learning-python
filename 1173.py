def main():
    N=range(0,11)
    x= int(input())

    for i in N:
        N[i] = x
        x = x*2
        print('N[{}] = {}'.format(i,N[i]))


if __name__ == "__main__":
    main()