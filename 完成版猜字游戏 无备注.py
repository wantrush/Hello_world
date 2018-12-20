print("~~~~~~~~~~~~~~~~要开始喽~~~~~~~~~~~~~~~~~~~~")
import random
secret=random.randint(1,100)
temp=input("请输入一个100以内的整数")


while temp.isdigit()==False:
    print("打别的干嘛！请输入数字！")
    temp=input()
    guess=temp
guess=int(temp)
while guess!=secret:
    if guess>secret:
        print("大了大了！！再小点~~")
    else:
        print("小了小了~~~再大点！！")
    temp=input()
    while temp.isdigit()==False:
        print("打别的干嘛！请输入数字！")
        temp=input()
        guess=temp
    guess=int(temp)
if guess==secret:
    print("兄弟~有点意思！！哈哈哈！厉害")
print("游戏结束~")
