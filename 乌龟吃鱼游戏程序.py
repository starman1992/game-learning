#游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
"""
假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
当移动到场景边缘，自动向反方向移动
乌龟初始化体力为100（上限）
乌龟每移动一次，体力消耗1
当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
"""

import random as rd
direction_list = [ 'up' , 'down' , 'left' , 'right']
x_min = 0
x_max = 5
y_min = 0
y_max = 5

class Fish:
    def __init__(self):
        self.x = rd.randint(0,10)
        self.y = rd.randint(0,10)
        self.direction = direction_list[rd.randint(0,3)]
        
    def move(self):
        if self.direction == direction_list[0]:
            if self.y != y_max:
                self.y += 1
            else:
                self.direction = direction_list[1]
                self.y -= 1
        elif self.direction == direction_list[1]:
            if self.y != y_min:
                self.y -= 1
            else:
                self.direction == direction_list[0]
                self.y += 1
        elif self.direction == direction_list[2]:
            if self.x != x_min:
                self.x -= 1
            else:
                self.direction = direction_list[3]
                self.x += 1
        elif self.direction == direction_list[3]:
            if self.x != x_max:
                self.x += 1
            else:
                self.direction = direction_list[2]
                self.x -= 1
        return (self.x,self.y)
 
 
class Turtle: 
    def __init__(self):
        self.x = rd.randint(0,10)
        self.y = rd.randint(0,10)
        self.hp = 100
        self.direction = direction_list[rd.randint(0,3)]

    def move(self):
        steps = rd.randint(1,2)
        self.hp -= 1
        if self.direction == direction_list[0]:
            if self.y < y_max - 1:
                self.y += steps;
            elif self.y == y_max - 1:
                if steps == 1:
                    self.y += steps
                else:
                    self.direction = direction_list[1]
            elif self.y == y_max:
                self.y -= steps
                self.direction = direction_list[1]
                 
        elif self.direction == direction_list[1]:
            if self.y > y_min + 1:
                self.y -= steps
            elif self.y == y_min + 1:
                if steps == 1:
                    self.y -= steps
                else:
                    self.direction = direction_list[0]
            elif self.y == y_min:
                self.y += steps
                self.direction = direction_list[0]
        elif self.direction == direction_list[2]:
            if self.x > x_min + 1:
                self.x -= steps
            elif self.x == x_min+1:
                if steps == 1:
                    self.x -= steps
                else:
                    self.direction = direction_list[3]
            elif self.x == x_min:
                self.x += steps;
                self.direction = direction_list[3]
        elif self.direction == direction_list[3]:
            if self.x < x_max - 1:
                self.x += steps
            elif self.x == x_max - 1:
                if steps == 1:
                    self.x += steps;
                else:
                    self.direction = direction_list[2]
            elif self.x == x_max:
                self.x -= steps;
                self.direction = direction_list[2]
        return (self.x,self.y)

    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100
                 
class Game:
    def __init__(self):
        self.fishs = [ Fish() for i in range(10) ]
        self.turtle = Turtle()
     
    def run(self):
        while True:
            if not self.turtle.hp:
                print('乌龟累趴下了')
                break
            if not len(self.fishs):
                print('鱼儿被吃完啦')
                break

            pos_t = self.turtle.move()
            print('乌龟到了%s   余%s血' % (pos_t,self.turtle.hp))
            for each_fish in self.fishs[:]:
                pos_f = each_fish.move()
            #func = lambda temp_fish,t_x = self.turtle.move.x,t_y=self.turtle.move.y : True if temp_fish.x != t_x or temp_fish.y != t_y else False
            #if func:
                #print('鱼被吃掉啦 在位置' + str(pos_t))
            self.fishs = list(filter(func,self.fishs))
            #self.turtle.eat()
            print('***乌龟还剩体力为 %d' % self.turtle.hp )
            print('***还剩 %d 条鱼' % len(self.fishs))            
             
        

game = Game()
game.run()


'''
import random as rd
#定义边界值
bd_x = [0,5]
bd_y = [0,5]

class Fish:
    # 构造函数什么时候执行？   创建对象时执行，__init__属性不应返回除None以外的任何值
    def __init__(self):     #self指的是实例化对象
                            #鱼属性：坐标

        self.x = rd.randint(bd_x[0],bd_x[1])     #出现时坐标范围
        self.y = rd.randint(bd_y[0],bd_y[1])

    def move(self):
        #随机计算方向并移动到新的位置
        step = [-1,1]     #最大移动能力为1
        a = rd.choice(step)
        new_x = self.x + a
        new_y = self.y + (1-abs(a))

        #检查移动后是否超出x边界
        if new_x < bd_x[0]:
            self.x = 2*bd_x[0] - new_x
        elif new_x > bd_x[1]:
            self.x = 2*bd_x[1] - new_x
        else:
            self.x = new_x

        #检查移动后是否超出y边界
        if new_y < bd_y[0]:
            self.y = 2*bd_y[0] - new_y
        elif new_y > bd_y[1]:
            self.y = 2*bd_y[1] - new_y
        else:
            self.y = new_y
        return(self.x,self.y)

class Turtle:
    def __init__(self):
        self.hp = 100
        self.x = rd.randint(bd_x[0],bd_x[1])     #出现时坐标范围
        self.y = rd.randint(bd_y[0],bd_y[1])

    def move(self):
        #随机计算方向并移动到新的位置
        step = [1,2,-1,-2]     #最大移动能力为2,横向和竖向绝对值相加为2
        a = rd.choice([1,2,-1,-2,0,0,0,0])
        new_x = self.x + a
        if not a:
            new_y = self.y + rd.choice(step)
        else:
            new_y = self.y

        #检查移动后是否超出x边界
        if new_x < bd_x[0]:
            self.x = 2*bd_x[0] - new_x
        elif new_x > bd_x[1]:
            self.x = 2*bd_x[1] - new_x
        else:
            self.x = new_x

        #检查移动后是否超出y边界
        if new_y < bd_y[0]:
            self.y = 2*bd_y[0] - new_y
        elif new_y > bd_y[1]:
            self.y = 2*bd_y[1] - new_y
        else:
            self.y = new_y
        
        self.hp -= 1     #体力消耗
        return(self.x,self.y)

    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100

def main():
    turtle = Turtle()
    fishs = [Fish() for i in range(10)]
    #fishs = []
    #for i in range(10):
        #fishs.append(Fish())

    while True:
        if not len(fishs):
            print('鱼都吃完啦')
            break
        if not turtle.hp:
            print('乌龟累趴下啦')
            break
        
        pos_t = turtle.move()     #赋值时给pos也可以执行了1次
        print('乌龟到了%s   余%s血' % (pos_t,turtle.hp))
        for each_fish in fishs[:]:
            #pos_t = turtle.move()     #经过比较，此行执行无论放里面，放外面都只执行1步
            #print('乌龟到了%s   余%s血' % (pos_t,turtle.hp))
            print(each_fish.move())
            if each_fish.move() == pos_t:
                #此处如果用turtle.move带括号则同步10条fish重复10次步数循环，不带则只循环一次，但无法返回值，故前面必须要赋值
                #同样，如果这里上面加each_fish.move()的话则又会执行一步行走，即加上for后面语句为2步
                turtle.eat()
                fishs.remove(each_fish)     #删除被乌龟吃掉的鱼
                print('***有一条鱼儿在'+ str(pos_t) + '被吃掉啦')
                print('***还剩 %d 条鱼' % len(fishs))
                print('***乌龟还剩体力为 %d' % turtle.hp)
                
if __name__ == "__main__":
    print("游戏开始".center(30, "*"))
    main()
'''
