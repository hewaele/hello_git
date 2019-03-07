def quotient(a, b):
    #判断b是否为除数
    if b == 0:
        return 'b can not a zero'
    result = a / b

    return result

if __name__ == "__main__":
    a = quotient(2, 3)
    print(a)