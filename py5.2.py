age = input('please enter your age:')
paspoort = input('do you have a ducht paspoort:')

if age > str(17) and paspoort == 'yes':
    print('you are allowed vote')
else:
    print('you cannot vote')

