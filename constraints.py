# constraints.py
# contains definitions of constraints for use with 'ot.py'
# constraints are all functions that take in a candidate form and
#   return the number of times that form violates the constraint
# almost all of these constraints begin by searching a candidate for
#   the position and type of its foot; the rest is mostly counting

def aL(l):
  for item in l:
    if isinstance(item, tuple):
      return l.index(item)
      
def aR(l):
  for item in l:
    if isinstance(item, tuple):
      return (len(l)-1)-l.index(item)
      
def I(l):
  for item in l:
    if isinstance(item, tuple):
      if item==(1,0):
        return 1
      else:
        return 0
        
def Nf(l):
  for item in l:
    if isinstance(item, tuple):
      if l.index(item)==(len(l)-1):
        return 1
      else:
        return 0
        
def T(l):
  for item in l:
    if isinstance(item, tuple):
      if item==(0,1):
        return 1
      else:
        return 0
        
def Np(l):
  for item in l:
    if isinstance(item, tuple):
      if (l.index(item)==(len(l)-1) and item==(1,0)):
	return 1
      elif (l.index(item)==(len(l)-2) and item==(0,1)):
        return 1
      else:
	return 0
	
def NRT(l):
  for item in l:
    if isinstance(item, tuple):
      if (l.index(item)==(len(l)-1) and item==(1,0)):
		return 1
      else:
        return 0

def NLI(l):
  for item in l:
    if isinstance(item, tuple):
      if (l.index(item)==0 and item==(0,1)):
        return 1
      else:
        return 0
        
def Final(l):
  for item in l:
    if isinstance(item, tuple):
      if l.index(item)!= (len(l)-1):
        return 1
      else:
	    return 0
	    
def Initial(l):
  for item in l:
    if isinstance(item, tuple):
      if l.index(item)!= 0:
        return 1
      else:
      	return 0