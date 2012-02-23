import inputdata
data = inputdata.raw_scores
import numpy

def main():
   g=exr()

class exr(object):
  
  def __init__(self):
    self.People = data.keys()
    
    self.pap = set()

    
    for i in data.values() :
      for k in i.keys() :
        self.pap.add(k)
        
    print self.pap 
   
    #A = numpy.ndarray(len(self.People),len(self.pap),dtype=float)
    A= numpy.ndarray((len(self.People),len(self.pap)), dtype=float)

   
    #print self.People
   
    #self.paper = data.values
 
  



main()
