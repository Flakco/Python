def print_rangoli(num):

    import string
    letters = string.ascii_lowercase
    line = []
    for i in range(n):
        s = "-".join(letters[i:n])
        line.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(line[:0:-1]+line))

n = int(input())
print_rangoli(n)