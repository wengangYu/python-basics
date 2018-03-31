#标志法 流程控制
p = True
while p :
    p = input("请输入一种配料： ")
    if p == "quit":
        print("sorry")
        p = False
    else:
        print("我们会在披萨中添加"+p)