from itertools import permutations, product
import operator

def solve_24(numbers):
    """
    解决24点游戏问题
    输入: 4个整数的列表
    输出: 包含这4个整数结果为24的算式字符串，或None表示无解
    """
    if len(numbers) != 4:
        return None
    
    # 定义运算符
    ops = ['+', '-', '*', '/']
    op_funcs = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    # 尝试所有数字排列
    for perm in permutations(numbers):
        a, b, c, d = perm
        
        # 尝试所有运算符组合
        for op1, op2, op3 in product(ops, repeat=3):
            # 尝试不同的括号组合
            expressions = [
                # ((a op1 b) op2 c) op3 d
                (lambda: op_funcs[op3](op_funcs[op2](op_funcs[op1](a, b), c), d),
                 f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"),
                
                # (a op1 (b op2 c)) op3 d
                (lambda: op_funcs[op3](op_funcs[op1](a, op_funcs[op2](b, c)), d),
                 f"({a} {op1} ({b} {op2} {c})) {op3} {d}"),
                
                # (a op1 b) op2 (c op3 d)
                (lambda: op_funcs[op2](op_funcs[op1](a, b), op_funcs[op3](c, d)),
                 f"({a} {op1} {b}) {op2} ({c} {op3} {d})"),
                
                # a op1 ((b op2 c) op3 d)
                (lambda: op_funcs[op1](a, op_funcs[op3](op_funcs[op2](b, c), d)),
                 f"{a} {op1} (({b} {op2} {c}) {op3} {d})"),
                
                # a op1 (b op2 (c op3 d))
                (lambda: op_funcs[op1](a, op_funcs[op2](b, op_funcs[op3](c, d))),
                 f"{a} {op1} ({b} {op2} ({c} {op3} {d}))")
            ]
            
            for calc_func, expr_str in expressions:
                try:
                    result = calc_func()
                    # 检查结果是否接近24（考虑浮点数精度）
                    if abs(result - 24) < 1e-9:
                        return expr_str
                except (ZeroDivisionError, ValueError, OverflowError):
                    # 忽略除零错误和其他数学错误
                    continue
    
    return None

def main():
    """主函数，用于测试"""
    print("24点游戏求解器")
    print("输入4个整数，程序将找到结果为24的算式")
    print("=" * 40)
    
    # 测试用例
    test_cases = [
        [1, 1, 8, 8],
        [4, 1, 8, 7],
        [1, 2, 3, 4],
        [3, 3, 8, 8],
        [1, 1, 1, 1],
        [5, 5, 5, 1]
    ]
    
    for case in test_cases:
        result = solve_24(case)
        print(f"输入: {case}")
        if result:
            print(f"解: {result}")
        else:
            print("解: None (无解)")
        print("-" * 30)
    
    # 交互式输入
    print("\n请输入4个整数（用空格分隔）:")
    try:
        user_input = input().strip()
        if user_input:
            numbers = list(map(int, user_input.split()))
            if len(numbers) == 4:
                result = solve_24(numbers)
                print(f"\n输入: {numbers}")
                if result:
                    print(f"解: {result}")
                else:
                    print("解: None (无解)")
            else:
                print("请输入恰好4个整数")
    except ValueError:
        print("输入格式错误，请输入4个整数")
    except KeyboardInterrupt:
        print("\n程序退出")

if __name__ == "__main__":
    main()
