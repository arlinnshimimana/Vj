def nieuw_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        print('True')

    else:
         print('false')

print(nieuw_password('langebroek ','heidelberglaan'))
