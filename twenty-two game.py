import itertools

TARGET = 24
EPS = 1e-6

def solve24(nums):
    results = set()

    def dfs(values, exprs):
        if len(values) == 1:
            if abs(values[0] - TARGET) < EPS:
                results.add(exprs[0])
            return

        for i in range(len(values)):
            for j in range(len(values)):
                if i == j:
                    continue

                a, b = values[i], values[j]
                ea, eb = exprs[i], exprs[j]

                rest_vals = []
                rest_exprs = []
                for k in range(len(values)):
                    if k != i and k != j:
                        rest_vals.append(values[k])
                        rest_exprs.append(exprs[k])

                ops = [
                    (a + b, f"({ea}+{eb})"),
                    (a - b, f"({ea}-{eb})"),
                    (a * b, f"({ea}*{eb})")
                ]

                if abs(b) > EPS:
                    ops.append((a / b, f"({ea}/{eb})"))

                for v, e in ops:
                    dfs(rest_vals + [v], rest_exprs + [e])

    dfs(nums, list(map(str, nums)))
    return results


if __name__ == "__main__":
    nums = list(map(int, input("Enter four numbers: ").split()))
    ans = solve24(nums)

    if not ans:
        print("No solution")
    else:
        print(f" Found {len(ans)} solutions：\n")
        for i, x in enumerate(sorted(ans), 1):
            print(f"{i}: {x}")
