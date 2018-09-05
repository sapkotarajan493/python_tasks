def countstr():
    s = input("Enter sentence: ")
    sb = input("Enter substring: ")
    results = 0
    sub_len = len(sb)
    for i in range(len(s)):
        if s[i:i+sub_len] == sb:
            results += 1
    print(results)


def counting():
    s = input("Enter sentence: ")
    sb = input("Enter substring: ")
    print(s.count(sb))
