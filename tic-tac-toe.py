import os

def restart():
    global dict
    global f
    ch=input('\nPlay Again(y/n)...?:')
    ch=str(ch)
    if ch=='y':
        os.system('cls')
        f=0
        dict={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        main()
    else:
        os.sys.exit()

     
def player_X():
    global dict
    n=input('\n\nEnter number of X:')
    n=int(n)
    if n==1 and dict[n]==' ':
        dict[1]='X'
        display()
    elif n==2 and dict[n]==' ':
        dict[2]='X'
        display()
    elif n==3 and dict[n]==' ':
        dict[3]='X'
        display()
    elif n==4 and dict[n]==' ':
        dict[4]='X'
        display()
    elif n==5 and dict[n]==' ':
        dict[5]='X'
        display()
    elif n==6 and dict[n]==' ':
        dict[6]='X'
        display()
    elif n==7 and dict[n]==' ':
        dict[7]='X'
        display()
    elif n==8 and dict[n]==' ':
        dict[8]='X'
        display()
    elif n==9 and dict[n]==' ':
        dict[9]='X'
        display()
    else:
        print('\ninvalid choice')
        player_X()


def player_O():
    global dict
    n=input('\n\nEnter number of O:')
    n= int(n)
    if n==1 and dict[n]==' ':
        dict[1]='O'
        display()
    elif n==2 and dict[n]==' ':
        dict[2]='O'
        display()
    elif n==3 and dict[n]==' ':
            dict[3]='O'
            display()
    elif n==4 and dict[n]==' ':
        dict[4]='O'
        display()
    elif n==5 and dict[n]==' ':
        dict[5]='O'
        display()
    elif n==6 and dict[n]==' ':
        dict[6]='O'
        display()
    elif n==7 and dict[n]==' ':
        dict[7]='O'
        display()
    elif n==8 and dict[n]==' ':
        dict[8]='O'
        display()
    elif n==9 and dict[n]==' ':
        dict[9]='O'
        display()
    else:
        print('\ninvalid choice')
        player_O()


def check():
    global f
    global dict
    f+=1
    if dict[1]==dict[2]==dict[3] and dict[1]==dict[2]==dict[3]!=' ' :
        print(dict[2],'WINS')
        restart()
    if dict[4]==dict[5]==dict[6] and dict[4]==dict[5]==dict[6]!=' ':
        print(dict[5],'WINS')
        restart()
    if dict[7]==dict[8]==dict[9] and dict[7]==dict[8]==dict[9]!=' ':
        print(dict[8],'WINS')
        restart()
    if dict[1]==dict[4]==dict[7] and dict[1]==dict[4]==dict[7]!=' ':
        print(dict[4],'WINS')
        restart()
    if dict[2]==dict[5]==dict[8] and dict[2]==dict[5]==dict[8]!=' ':
        print(dict[5],'WINS')
        restart()
    if dict[3]==dict[6]==dict[9] and dict[3]==dict[6]==dict[9]!=' ':
        print(dict[6],'WINS')
        restart()
    if dict[3]==dict[5]==dict[7] and dict[3]==dict[5]==dict[7]!=' ':
        print(dict[5],'WINS')
        restart()
    if dict[1]==dict[5]==dict[9] and dict[1]==dict[5]==dict[9]!=' ':
        print(dict[5],'WINS')
        restart()
    if f==9:
        print('\nTIE')
        restart()
    print('\n\n----------------------------------------------------------------------------\n')

def display():
    global dict
    print('\n\n')
    print('\t',dict[1],'|',dict[2],'|',dict[3])
    print('\t---+---+--- ')
    print('\t',dict[4],'|',dict[5],'|',dict[6])
    print('\t---+---+--- ')
    print('\t',dict[7],'|',dict[8],'|',dict[9])
    check()

def main():
 global dict
 print('\t\t\t\tGAME INFO\n')
 print('\t\t\t\t*********\n')
 print('The player can choose the numbers and the symbol will be placed in the place of that number\n')
 print('              |     |')
 print('           1  |  2  |  3')
 print('              |     |')
 print('         -----+-----+-----')
 print('              |     |')
 print('           4  |  5  |  6')
 print('              |     |')
 print('         -----+-----+-----')
 print('              |     |')
 print('           7  |  8  |  9')
 print('              |     |')
 c=input('\n\nPress 1 to start and 0 to quit:')
 c=int(c)
 if c==0:
      exit()
 os.system('cls')
 i=1
 while i<=4:
   player_X()
   player_O()
 i+=1
 player_X()

f=0
dict={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
main()

