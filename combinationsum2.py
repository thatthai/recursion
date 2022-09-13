def combinationSum2(candidates, target):
    result = []
    combinationSumRecu(candidates, result, 0, [], target)
    return result

def combinationSumRecu(candidates, result, start, intermediate, target):
    if target == 0:
        result.append(list(intermediate))
    if start < len(candidates) and candidates[start] <= target:
        intermediate.append(candidates[start])
        combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
        intermediate.pop()
        prev = candidates[start]
    start += 1
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
candidates, target = arr, int(inp[0])
result = combinationSum2(candidates, target)     
print(result)       