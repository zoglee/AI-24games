from itertools import permutations, product
import operator
import sys

def solve24(nums):
    """
    解决 24 点游戏 (与之前版本相同，无需修改)。
    """
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda x, y: x / y if y != 0 else 999999
    }

    for n in permutations(nums):
        for op_comb in product(ops.keys(), repeat=3):
            # (a op b) op (c op d)
            try:
                if abs(ops[op_comb[1]](ops[op_comb[0]](n[0], n[1]), ops[op_comb[2]](n[2], n[3])) - 24) < 0.001:
                    return f"({n[0]} {op_comb[0]} {n[1]}) {op_comb[1]} ({n[2]} {op_comb[2]} {n[3]})"
            except:
                pass

            # a op ( b op (c op d))
            try:
              if abs(ops[op_comb[0]](n[0], ops[op_comb[1]](n[1], ops[op_comb[2]](n[2], n[3]))) - 24) < 0.001:
                return f"{n[0]} {op_comb[0]} ({n[1]} {op_comb[1]} ({n[2]} {op_comb[2]} {n[3]}))"
            except:
              pass
            
            # (a op (b op c) )op d
            try:
               if abs(ops[op_comb[2]](ops[op_comb[0]](n[0],ops[op_comb[1]](n[1],n[2])),n[3]) -24) < 0.001:
                  return f"({n[0]} {op_comb[0]} ({n[1]} {op_comb[1]} {n[2]})) {op_comb[2]} {n[3]}"
            except:
              pass

            # ((a op b) op c) op d
            try:
              if abs(ops[op_comb[2]](ops[op_comb[1]](ops[op_comb[0]](n[0],n[1]), n[2]), n[3]) -24) < 0.001:
                return f"(({n[0]} {op_comb[0]} {n[1]}) {op_comb[1]} {n[2]}) {op_comb[2]} {n[3]}"
            except:
              pass
              
            # a op ((b op c) op d)
            try:
              if abs(ops[op_comb[0]](n[0], ops[op_comb[2]](ops[op_comb[1]](n[1], n[2]), n[3])) -24) < 0.001:
                return f"{n[0]} {op_comb[0]} (({n[1]} {op_comb[1]} {n[2]}) {op_comb[2]} {n[3]})"
            except:
              pass

    return None


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("用法: python your_script_name.py <num1> <num2> <num3> <num4>")
        sys.exit(1)  # 退出程序，并返回错误码 1

    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
        # 检查数字范围
        if not all(1 <= num <= 9 for num in numbers):
            print("错误：数字必须在 1 到 9 之间。")
            sys.exit(1)
    except ValueError:
        print("错误：请输入有效的整数。")
        sys.exit(1)

    solution = solve24(numbers)

    if solution:
        print(f"找到 24 点解决方案: {solution}")
    else:
        print("无法找到 24 点解决方案。")
