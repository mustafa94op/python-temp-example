#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

#fo = open(TEMP_PATH + "temp", "r")
#temp = fo.read()
#print(temp)


def readTemp():
    fo = open(TEMP_PATH + "temp", "r")
    temp = fo.read()
    return int(temp) 


def averageTemp(n):
    sum=0
    for i in range(n):
        sum = sum + readTemp()
    average = sum/n
    return average


#print(readTemp())


#function  printTemp
#{
       # cat $TEMP_PATH
#}
#sum=0
#for i in {1..10}
#do 
         # echi "$i"
          #temp=(printTemp)
         # sum=((temp+sum))
#done
#echo "$sum/10*0.001 | bc

