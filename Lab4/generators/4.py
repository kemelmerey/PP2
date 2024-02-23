#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
#Test it with a "for" loop and print each of the yielded values.
A = int(input())
B = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = A
    return self

  def __next__(self):
    if ((self.a >= A) and (self.a <= B)):
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x * x)