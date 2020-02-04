#! /usr/bin/env python

def read_data(filename):
        input_source=open(filename,'r')
        input_source.readline()
        return [line.split() for line in input_source]

if __name__=='__main__':
        hosts=read_data('Lemonade1.csv')
        masterlist=read_data('Lemonade2.csv')
        master=dict()
        for index,data in enumerate(masterlist):
                master[data[-1]]=index+1
        for row in hosts:
                try:
                        found="FOUND in masterlist (row %s)"%master[row[-1]]
                except KeyError:
                        found="NOT FOUND in masterlist"
                line=row+[found]
                print ("%s    %s    %s    %s    %s"%tuple(line))
