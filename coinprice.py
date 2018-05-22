# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:02:34 2018

@author: pmancini

"""

import requests
    
class Measure:
  url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
  response = ''
  
  def Reload(self, rm, maxValue):
    self.url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    self.response = requests.get(self.url)

  def Update(self):
    self.response = requests.get(self.url)
    if self.response.status_code != 500:
      rate = self.response.json()['bpi'] ['USD'] ['rate']
      return rate
    else:
      rate="Server Error"
      return rate

  def GetString(self):
    return 'Bitcoin Price'

  def ExecuteBang(self, args):
    pass

  def Finalize(self):
    pass

def main():
  print(Measure.Update(Measure))
  
if __name__ == "__main__":
    main()