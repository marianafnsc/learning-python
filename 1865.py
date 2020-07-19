def main():
    N = int(input())

    for i in range(N):
        infos = input()                 #Hulk 5000
        splitted_infos = infos.split()  #["Hulk", "5000"]
        name = splitted_infos[0]        #Hulk
        
        if name == "Thor":
            print("Y")
            continue
        print("N")


if __name__ == "__main__":
    main()