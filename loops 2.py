ms=input('enter martial ststus:')
s=input('enter ur gender:')
age=int(input('enter ur age:'))
if(ms=='m')or(ms=='u'and s=='m'and age>30) \
        or (ms=='u'and s=='f' and age>25):
    print('insured')
else:
    print('not insured')