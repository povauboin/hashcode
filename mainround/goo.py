#!/usr/bin/env python
# encoding: utf-8

def classer(coord,N):
    classe=[0]*N;
    for i in range(0,N):
       if (coord[i][0]>48.8608): #c'est dans la clase 1 2 3 ou 4
          if(coord[i][1]<2.3023):
             classe[i]=1;
          else:
             if(coord[i][1]<2.3363):
                classe[i]=2;
             else:
                if(coord[i][1]<2.374):
                   classe[i]=3;
                else:
                   classe[i]=4;
       else:
         if(coord[i][1]<2.3023):
             classe[i]=5;
         else:
             if(coord[i][1]<2.3363):
                classe[i]=6;
             else:
                if(coord[i][1]<2.374):
                   classe[i]=7;
                else:
                   classe[i]=8;
    return classe;
