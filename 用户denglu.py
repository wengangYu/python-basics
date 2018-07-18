#需求 让用户输入用户名 和密码（提示错误3次）
n = 3
admin = input("请输入您的用户名：")
mima = input("请输入您的密码：")
while n > 0:
    if admin != "yuwenagng" or mima != "123456":
        print("输入错误，请重新输入，还剩余%s次"%n)
        admin = input("请输入您的用户名：")
        mima = input("请输入您的密码：")
        n = n - 1
        if n == 0:
            print('输入次数过多,请明天再试')
    if admin == "yuwengang" and mima == "123456":
        print("登录成功")
        break


