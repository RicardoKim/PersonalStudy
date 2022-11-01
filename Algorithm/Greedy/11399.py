def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    sum = 0
    for i in range(n):
        sum += p[i] * (n - i)
    print(sum)

if __name__ == '__main__':
    main()