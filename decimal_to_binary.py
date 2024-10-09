def dec_bin():
    num = int(input("Enter a number: "))
    number = num
    li = []
    while(num>0):
        rem = num%2
        num = num//2
        li.append(str(rem))
    binary_num = li[ : : -1]
    binary_nu = ""
    
    a = binary_nu.join(binary_num)
    print(f"The binary form of {number} is:",a)
    
dec_bin()