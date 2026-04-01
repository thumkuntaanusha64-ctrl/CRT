def reverse_number(n: int) -> int:
    lol = str(n)
    josh = lol[::-1]
    france =  int(josh)
    return france

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))