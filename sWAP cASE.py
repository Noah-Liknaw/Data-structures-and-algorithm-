def swap_case(s):
    result = ""
    for c in s:
        result+= c.swapcase()
        
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)