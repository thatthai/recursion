def pantip(k, arr): #n is partten
    #Code Here
    path = []
    backtracking(arr, path, 0, [] , k)
    return path
    
def backtracking(arr, path, n, cur, k):
    if k == 0:
        if cur != [] :
            path.append(list(cur))
        cur = []
    prev = 0
    if n < len(arr):
        if prev != arr[n]:
            cur.append(arr[n])
            backtracking(arr, path, n + 1, cur, k - arr[n])
            cur.pop()
            prev = arr[n]
        n += 1
        backtracking(arr, path, n, cur, k)

      

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
#pattern = pantip(int(inp[0]), 0, arr, [])
pattern = pantip(int(inp[0]),arr)
for item in pattern :
    for element in item :
        print(element,end = " ")
    print("")
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], len(pattern)))
