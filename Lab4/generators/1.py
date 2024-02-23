#Create a generator that generates the squares of numbers up to some number N.
N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x**2
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)