def main():
    x = int(input())
    for i in range(x):
        # leia a nova variávek
        inp = int(input())
        # imprima a resposta
        if inp == 0:
            print("NULL")
        elif inp % 2 == 0:
            if inp > 0:
                print("EVEN POSITIVE")
                continue
            print("EVEN NEGATIVE")
        else:
            if inp > 0:
                print("ODD POSITIVE")
                continue
            print("ODD NEGATIVE")
if __name__ == "__main__":
    main()