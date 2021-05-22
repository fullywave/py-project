class Node(object):
  def __init__(self,value)->None
      self._chilren={}
      self._value=value

  def _add_chile(self,char,value,overwrite=False):
      child=self._children.get(char)
      if child is None:
          child=Node(value)
          self._chilren[char]=child

      elif overwrite:
          child._value=value
    
      return child
        