def quotient(a, b):
    #判断b是否为除数
    if b == 0:
        return 'b can not a zero'
    result = a / b

    return result
#创建一个无用的函数用来测试
def branch_test():
    print('branch test success')

#用户1添加了一个新的功能
def user1():
    print("用户1添加了一个新的功能")

#用户2添加了一个新的功能
def user2():
    print("用户2添加的功能")

#添加一个功能测试上传到github
def pust_test():
    print("上传到github成功")

if __name__ == "__main__":

    #增加手动输入数字
    a = int(input("请输入a："))
    b = int(input("请输入b:"))
    c = quotient(a, b)
    print(c)

    
    user1()

    user2()
    push_test()
    print("不添加密匙推送测试")
