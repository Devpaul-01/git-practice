def longest(n):
    parantheses = ["()"] * n
    new_par = "".join(parantheses)
    full_length = n * 2   # total chars in a valid parentheses sequence
    
    substrings = []
    for i in range(len(new_par)):
        for j in range(i+1, len(new_par)+1):
            substrings.append(new_par[i:j])
    
    # only keep substrings of full_length
    candidates = [par for par in substrings if len(par) == full_length]
    
    passed = []
    for par in candidates:
        stack = []
        valid = True
        for a in par:
            if a == "(":
                stack.append(a)
            else:
                if not stack:
                    valid = False
                    break
                stack.pop()
        if valid and not stack:
            passed.append(par)
    
    return passed

print(longest(9))