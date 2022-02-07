from tkinter import *

master = Tk()
master.geometry('500x400')
master.title('MadLibs Generator')
Label(master, text='Simple Mad Libs Generator', font='Times 24 italic').pack()
Label(master, text='Choose an ad-lib you want:', font='Helvetica 17 bold').place(x=80, y=80)


def madlib1():
    nounk = input('enter a noun : ')
    nounp = input('enter a noun in plural: ')
    nounk1 = input('enter another noun: ')
    placek = input('enter a place: ')
    adjectivek = input('enter an adjective: ')
    nounk2 = input('enter another noun: ')

    print(
        ' Be kind to your ' + nounk + '-footed' + nounp + ' \n For a duck may be somebody`s' + nounk1 +
        ',\n Be kind to your' + placek + ' in ' + adjectivek + '\n Where the weather is always' + nounk2 +
        '.\n\n You may think that this is the reason,\n Well it is.')


def madlib2():
    noun = input('enter NOUN (PLURAL) : ')
    place = input('enter a color PLACE : ')
    noun1 = input('enter a NOUN :')
    nounpl = input('enter a NOUN(plural) : ')
    noun2 = input('enter another noun : ')
    adjective = input('enter a ADJECTIVE : ')
    verb = input('enter a VERB : ')
    number = input('enter a NUMBER : ')
    adjective2 = input('enter another ADJECTIVE : ')
    body = input('enter a bordy_part : ')
    verb2 = input('enter another VERB : ')

    print(
        'Two ' + noun + ', both alike in dignity, \n In fair' + place +
        ', where we lay our scene,\n From ancient' + noun1 +
        ' break to new mutiny,\n '
        'Where civil blood makes civil hands unclean.\n From forth the fatal loins of these two foes \n A pair of '
        'star - cross`d ' + nounpl +
        'take their life;\n Whole misadventured piteous overthrows\n Do with their ' + noun2 +
        ' bury their parents` strife.\n The fearful passage of their ' + adjective +
        ' love,\n And the continuance of their parents ` rage,\n Which, but their children`s end, nought could' + verb +
        ',\n Is now the ' + number + ' hours ` traffic of our stage;\n The which if youwith ' + adjective2, body +
        'attend, '
        '\n What '
        'here '
        'shall' +
        verb2 +
        ', our toil shall strive to mend.\n')


def madlib3():
    color = input('enter color : ')
    super1 = input('enter something ending with est : ')
    adjective = input('enter aa adjective name: ')
    bodyd = input('enter a body part in plural: ')
    body = input('enter a body part : ')
    nound = input('enter a noun : ')
    animal = input('enter a animal in plural : ')
    ad1 = input('enter an adjective1 : ')
    ad2 = input('enter another adjective : ')
    ad3 = input('enter another adjective : ')

    print(
        'The' + color + 'Dragon is the ' + super1 + 'Dragon of all.\n It has' + adjective, bodyd + ', and a' + body +
        'shaped like a' + nound +
        '.\n It loves to eat' + animal + ', although it will feast on nearly anything.\n It is ' + ad1 + 'and' + ad2 +
        '.\n You must be' + ad3 + 'around it, or you may end up as it`s meal!'
    )


Button(master, text='Be Kind ', font='times 15', command=madlib1, bg='light blue').place(x=80, y=120)
Button(master, text='Romeo and Juliet: Prologue ', font='times 15', command=madlib2, bg='light pink').place(x=80, y=180)
Button(master, text='Dragons ', font='times 15', command=madlib3, bg='light green').place(x=80, y=240)

master.mainloop()
