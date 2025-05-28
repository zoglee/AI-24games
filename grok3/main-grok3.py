from itertools import permutations

def solve_24_game(numbers):
    # 输入验证：必须是4个正整数
    if len(numbers) != 4 or not all(isinstance(n, int) and n > 0 for n in numbers):
        return "输入无效，需要4个正整数"
    
    # 定义运算符
    operators = ['+', '-', '*', '/']
    
    # 计算两个数的运算结果
    def calculate(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return None  # 除数为0
            return a / b
    
    # 递归函数：从当前数字列表中计算24
    def dfs(nums, path):
        # 基线条件：只剩一个数字，检查是否接近24
        if len(nums) == 1:
            if abs(nums[0] - 24) < 1e-6:  # 容忍浮点误差
                return path
            return None
        
        # 选择两个不同的数字进行运算
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # i + 1 确保不重复选择同一数字
                a, b = nums[i], nums[j]
                # 剩余数字
                remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                
                for op in operators:
                    result = calculate(a, b, op)
                    if result is None:  # 跳过除以0的情况
                        continue
                    # 构建算式
                    new_path = f"({a} {op} {b})" if not path else f"({path} {op} {b})"
                    # 递归处理剩余数字和新结果
                    solution = dfs(remaining + [result], new_path)
                    if solution:
                        return solution
        return None
    
    # 尝试所有数字排列
    for perm in permutations(numbers):
        solution = dfs(list(perm), "")
        if solution:
            return solution
    
    return "没有可能"

# 测试用例
test_cases = [
    [4, 5, 6, 7],
    [1, 2, 3, 4],
    [1, 1, 1, 1],
    [3, 3, 8, 8]
]

for case in test_cases:
    result = solve_24_game(case)
    print(f"输入: {case}")
    print(f"输出: {result}")
    print()
