def sumofcalib():
    sum=0
    f=open('./check.txt')
    p=f.readlines()
    for i in p :
        result=""
        for j in i:
            if j.isnumeric():
                result+=j
        sum+=int(result[:1]+result[-1:])
    return sum
print(sumofcalib())