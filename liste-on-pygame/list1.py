

participant = ['(Moderator)']
a = input('enter name of the participants please, try 0 to stop')

while a != '0':
    
    if a in participant:
        a = input('enter name of the participants please, try 0 to stop')

    else:
        participant.append(a)


participant.sort()


print(participant)
    
