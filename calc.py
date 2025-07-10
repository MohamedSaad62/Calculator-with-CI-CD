def calculate(a: int, op: str, b: int) -> int:
    if op == '+':
        return a + b
    else:
        raise ValueError(f"Unsupported operation: {op}")

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    op = input("Enter operator (+): ")
    b = int(input("Enter second number: "))

    try:
        result = calculate(a, op, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)
