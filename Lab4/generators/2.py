#Write a program using generator to print 
#the even numbers between 0 and n in comma separated form where n is input from console.
N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    if (x % 2 == 0):
        print(x)