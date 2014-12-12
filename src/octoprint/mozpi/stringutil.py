# -*- coding: utf-8 -*-
import re
class StringUtils:
  @classmethod
  def to_snake(cls, value, upper): 
    if (value == None):
      return None
    if (value == ""):
      return ""

    ret = re.sub(r'([\s|A-Z])', "_\\1",value)
    ret = re.sub(r'([\s])', "",ret)
    ret = re.sub(r'^_', "",ret)
    if (upper):
      ret = ret.upper()
    else:
      ret = ret.lower()
    return ret

if __name__=="__main__":
    print StringUtils.to_snake("FabLab Kamakura", upper=False)
    print StringUtils.to_snake("RPi 1",upper=False)
  

