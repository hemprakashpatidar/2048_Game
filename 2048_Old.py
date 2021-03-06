# -*- coding: utf-8 -*-
"""2048.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SXlEku0A6-F-79mrYIoKIfvWWvcvacM-

2048 Game
"""

import random

class games():
  def __init__(self):
    self.arrs=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    self.flag=0
  
  def print_game(self):
    for i in self.arrs:
      print(i)
  
  def check_over(self):
    for i in range(3):
      for j in range(4):
        if ((self.arrs[i][j]==self.arrs[i+1][j]) or self.arrs[i][j]==0):
          return 0
       
    for i in range(4):
      for j in range(3):
        if ((self.arrs[i][j]==self.arrs[i][j+1]) or self.arrs[i][j]==0):
          return 0
    return 1    
  
  def check_empty(self):
    empty_list=[]
    for i in range(4):
      for j in range(4):
        if self.arrs[i][j]==0:
          temp=[i,j]
          empty_list.append(temp)
    return empty_list

  def new_random(self):
    tem=self.check_empty()
    new=random.randint(0,len(tem)-1)
    '''if random.random() <= 0.2:
      self.arrs[tem[new][0]][tem[new][1]]=4
    else:
      '''
    self.arrs[tem[new][0]][tem[new][1]]=2
#move down
  def move_down(self):
    for i in range(4):
      if self.arrs[3][i]==0:
        self.arrs[3][i]=self.arrs[2][i]
        self.arrs[2][i]=0
        self.flag=1
      if self.arrs[3][i]==self.arrs[2][i]:
        self.arrs[3][i]*=2
        self.arrs[2][i]=0
        self.flag=1
      
      if self.arrs[2][i]==0:
        self.arrs[2][i]=self.arrs[1][i]
        self.arrs[1][i]=0
        self.flag=1
      if self.arrs[2][i]==self.arrs[1][i]:
        self.arrs[2][i]*=2
        self.arrs[1][i]=0
        self.flag=1
      
      if self.arrs[1][i]==0:
        self.arrs[1][i]=self.arrs[0][i]
        self.arrs[0][i]=0
        self.flag=1
      if self.arrs[1][i]==self.arrs[0][i]:
        self.arrs[1][i]*=2
        self.arrs[0][i]=0
        self.flag=1
  def move_downs(self):
    self.flag=0
    self.move_down()
    self.move_down()
    self.move_down()
    if self.flag==1:
      self.new_random()
#move up
  def move_up(self):
    for i in range(4):
      if self.arrs[0][i]==0:
        self.arrs[0][i]=self.arrs[1][i]
        self.arrs[1][i]=0
        self.flag=1
      if self.arrs[0][i]==self.arrs[1][i]:
        self.arrs[0][i]*=2
        self.arrs[1][i]=0
        self.flag=1
      
      if self.arrs[1][i]==0:
        self.arrs[1][i]=self.arrs[2][i]
        self.arrs[2][i]=0
        self.flag=1
      if self.arrs[1][i]==self.arrs[2][i]:
        self.arrs[1][i]*=2
        self.arrs[2][i]=0
        self.flag=1
      
      if self.arrs[2][i]==0:
        self.arrs[2][i]=self.arrs[3][i]
        self.arrs[3][i]=0
        self.flag=1
      if self.arrs[2][i]==self.arrs[3][i]:
        self.arrs[2][i]*=2
        self.arrs[3][i]=0
        self.flag=1
  def move_ups(self):
    self.flag=0
    self.move_up()
    self.move_up()
    self.move_up()
    if self.flag==1:
      self.new_random()

#move right
  def move_right(self):
    for i in range(4):
      if self.arrs[i][3]==0:
        self.arrs[i][3]=self.arrs[i][2]
        self.arrs[i][2]=0
        self.flag=1
      if self.arrs[i][3]==self.arrs[i][2]:
        self.arrs[i][3]*=2
        self.arrs[i][2]=0
        self.flag=1
      
      if self.arrs[i][2]==0:
        self.arrs[i][2]=self.arrs[i][1]
        self.arrs[i][1]=0
        self.flag=1
      if self.arrs[i][2]==self.arrs[i][1]:
        self.arrs[i][2]*=2
        self.arrs[i][1]=0
        self.flag=1
      
      if self.arrs[i][1]==0:
        self.arrs[i][1]=self.arrs[i][0]
        self.arrs[i][0]=0
        self.flag=1
      if self.arrs[i][1]==self.arrs[i][0]:
        self.arrs[i][1]*=2
        self.arrs[i][0]=0
        self.flag=1
  def move_rights(self):
    self.flag=0
    self.move_right()
    self.move_right()
    self.move_right()
    if self.flag==1:
      self.new_random()

#move left
  def move_left(self):
    for i in range(4):
      if self.arrs[i][0]==0:
        self.arrs[i][0]=self.arrs[i][1]
        self.arrs[i][1]=0
        self.flag=1
      if self.arrs[i][0]==self.arrs[i][1]:
        self.arrs[i][0]*=2
        self.arrs[i][1]=0
        self.flag=1
      
      if self.arrs[i][1]==0:
        self.arrs[i][1]=self.arrs[i][2]
        self.arrs[i][2]=0
        self.flag=1
      if self.arrs[i][1]==self.arrs[i][2]:
        self.arrs[i][1]*=2
        self.arrs[i][2]=0
        self.flag=1
      
      if self.arrs[i][2]==0:
        self.arrs[i][2]=self.arrs[i][3]
        self.arrs[i][3]=0
        self.flag=1
      if self.arrs[i][2]==self.arrs[i][3]:
        self.arrs[i][2]*=2
        self.arrs[i][3]=0
        self.flag=1
  def move_lefts(self):
    self.flag=0
    self.move_left()
    self.move_left()
    self.move_left()
    if self.flag==1:
      self.new_random()

def game():
  gg=games()
  gg.new_random()
  gg.new_random()
  gg.print_game()
  play=0
  while(play==0):
    
    direction=input()
    print("   ")
    if direction=='d':
      gg.move_rights()
    if direction=='a':
      gg.move_lefts()
    if direction=='w':
      gg.move_ups()
    if direction=='s':
      gg.move_downs()
    
    gg.print_game()

    play=gg.check_over()

game()
