with open('/количество-шагов.txt', 'r') as file:
    a = file.readline()

N = int(a)
x = 0
y = 0

while N > 0:
  # если мы доходим до места, где в правом верхнем углу идет разворот налево
    if x == y and x >= 0:
      while x != -y - 1 and N > 0:      # пока мы не дойдем до места, где нужно свернуть вниз
          N -= 1                        # кол-во шагов будет уменьшаться
          x -= 1                        # x, соответственно, тоже

  # если мы доходим до места, где поворот вниз (левый верх.угол)
    elif x == -y - 1:
      while x != y and x < 0 and N > 0: # пока не дойдем до поворота направо, где значения координат равны
          N -= 1                        # кол-во шагов будет уменьшаться
          y -= 1                        # y, соответственно, тоже

  # если мы доходим до места, где поворот направо (левый нижний угол)
    elif x == y and x < 0:
      while x != -y and N > 0:          # пока не дойдем до поворота вверх (правый ниж.угол)
          N -= 1                        # кол-во шагов будет уменьшаться
          x += 1                        # x увеличивается

  # иначе, это поворот вверх (правый ниж. угол, где x == -y)
    else:
      while x != y and x > 0 and N > 0: # пока не дойдет до поворота налево
          N -= 1                        # кол-во шагов будет уменьшаться
          y += 1                        # y - увеличиваться

with open('/количество-шагов.txt', 'a') as file:
    file.write('\n' + str(x) + ' ' + str(y)) # местоположение робота через N шагов
