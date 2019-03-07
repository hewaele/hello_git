def quotient(a, b):
    #判断b是否为除数
    if b == 0:
        return 'b can not a zero'
    result = a / b

    return result

if __name__ == "__main__":
    #增加手动输入数字
    a = input("请输入a：")
    b = input("请输入b:")
    c = quotient(a, b)
    print(c)