def greet(name: str) -> str:
    """回傳問候語"""
    return f"Hello, {name}! 歡迎使用本專案。"

def add(a: int, b: int) -> int:
    """兩數相加"""
    return a + b

def dif(a: int, b: int) -> int:
    """兩數相減"""
    return a - b

def mul(a: int, b: int) -> int:
    """兩數相乘"""
    return a * b

def main():
    # 測試問候功能
    message = greet("World")
    print(message)

    # 測試加法功能
    result = add(3, 5)
    print(f"3 + 5 = {result}")

    # 測試減法功能
    result = dif(13, 8)
    print(f"13 - 8 = {result}")

    # 測試乘法功能
    result = mul(15, 3)
    print(f"15 * 3 = {result}")

    print("專案初始化成功！✅")

if __name__ == "__main__":
    main()
