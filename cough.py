def main():
    print(cough(3))


def cough(n):
    res = ''
    for i in range(n):
        res += 'cough '

    return res

if __name__ == "__main__":
    main()