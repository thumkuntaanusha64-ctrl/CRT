def count_digits(n: int) -> int:
    lo = str(n)
    return len(lo)
    pass

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))