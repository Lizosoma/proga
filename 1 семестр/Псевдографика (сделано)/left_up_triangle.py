from testsystem import test

def triangle_2(n):

   s = ''
   for i in range(n, 0, -1):
      s += 'x' * i + '\n'
   return s

print(triangle_2(5))

test(triangle_2, 'left_up_triangle.json')
