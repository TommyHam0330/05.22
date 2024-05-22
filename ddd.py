from house import HouseRabbit
from rabbit import Rabbit
from Mountainrabbit import MountainRabbit

a = HouseRabbit(10, 20)
b = MountainRabbit(30, 40)
print(a.shape)
print(a.x_pos, a.y_pos)
a.eat_feed()
print(b.shape)
print(b.x_pos, b.y_pos)
b.eat_grass()