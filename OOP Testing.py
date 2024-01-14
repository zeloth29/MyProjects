green = 2
class Gecko():
  def __init__(self, myColour, myName):
    self.PColour = myColour
    self.PName = myName
  def setColour(self, myColour):
    self.PColour = myColour
  def setName(self, myName):
    self.PName = myName
  def getName(self):
    return self.PName
  def getColour(self):
    return self.PColour

Darwin = Gecko ("Green","Darwin")
def Info(Gecko):
  print("The Gecko's colour is", Gecko.getColour())
  print("The Gecko's name is", Gecko.getName())


Info(Darwin)