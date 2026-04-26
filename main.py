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

def div(a: int, b: int) -> float:
    """兩數相除"""
    if b == 0:
        raise ValueError("除數不能為 0！")
    return a / b

def power(a: float, b: float) -> float:
    """次方：a 的 b 次方"""
    return a ** b

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

    # 測試除法功能
    result = div(10, 2)
    print(f"10 / 2 = {result}")

    # 測試次方功能（使用者輸入）
    print("\n--- 次方計算 ---")
    a = float(input("請輸入底數 a："))
    b = float(input("請輸入次數 b："))
    result = power(a, b)
    print(f"{a} 的 {b} 次方 = {result}")

    print("\n專案初始化成功！✅")

if __name__ == "__main__":
    main()
