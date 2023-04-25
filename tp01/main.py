def main():
    for i in range(10):
        print(i)
        if i==53:
            break
    else:
        print("pas trouvé")

if __name__ == '__main__':
    main()


def main01():
    found = False
    for i in range(10):
        print(i)
        if i==3:
            found = True
            break
    
    if found:
        print("ok")

if __name__ == '__main__':
    main()
