import random
word_list='words.txt'
def hangman():
    inFile=open(word_list,'r')
    line=inFile.readline()
    wordlist=line.split()
    print(len(wordlist),'words loaded')

    word=random.choice(wordlist)
    turns=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word = " "
        for letter in word:
            if letter in guessmade:
                main_word= main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print('You Won !!!')
            break
        print('Guess the words',main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print('Enter valid entry :')
            guess=input()

        if guess not in word:
            turns=turns-1
            if turns==9:
                print('\n9 turns left !!!')
                print('------------')
            if turns==8:
                print('\n8 turns left !!!')
                print('------------')
                print('     O      ')
            if turns==7:
                print('\n7 turns left !!!')
                print('------------')
                print('     O      ')
                print('     |      ')
            if turns==6:
                print('\n6 turns left !!!')
                print('------------')
                print('     O      ')
                print('     |      ')
                print('    /       ')
            if turns==5:
                print('\n5 turns left !!!')
                print('------------')
                print('     O      ')
                print('     |      ')
                print('    / \     ')
            if turns==4:
                print('\n4 turns left !!!')
                print('------------')
                print('    \O      ')
                print('     |      ')
                print('    / \     ')
            if turns==3:
                print('\n3 turns left !!!')
                print('------------')
                print('    \O/     ')
                print('     |      ')
                print('    / \     ')
            if turns==2:
                print('\n2 turns left !!!')
                print('------------')
                print('    \O/  |  ')
                print('     |      ')
                print('    / \     ')
            if turns==1:
                print('\n1 turns left !!! hangman on his last breath')
                print('------------')
                print('    \O/__|  ')
                print('     |      ')
                print('    / \     ')
            if turns==0:
                print('You Loose')
                print('You let a good man die')
                break

name=input('ENTER YOUR NAME ->')
print('Welcome',name,'!')
print('-------------------------')
print(name,'!!! try to guess the word in less than 10 attempts')
hangman()
