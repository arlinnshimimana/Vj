from tkinter import*
import Database
import B_Database

def aanbieder_inloggen(inlognaam, inlogcode):
    data = Database.aanbieder_inloggegevens()

    if inlognaam in data:
       if data[inlognaam] == inlogcode:
           aanbiederframe.pack_forget()
           aanbiederHall.pack()
       else:
           foutlabel = Label(master=aanbiederframe, text='incorrecte invoer', foreground="red")
           foutlabel.place(x=25, y=115)
    else:
        foutlabel = Label(master=aanbiederframe,text='incorrecte invoer', foreground="red")
        foutlabel.place(x=25, y=115)
    return

def bezoeker_inloggen(loginfield, loginfield2):
    datat = B_Database.bezoeker_inloggegevens()

    if loginfield in datat:

       if datat[loginfield] == loginfield2:
           bezoekerframe.pack_forget()
           filmframe.pack()
       else:
           foutlabel = Label(master=bezoekerframe, text='incorrecte invoer', foreground="red")
           foutlabel.place(x=25, y=115)
    else:
        foutlabel = Label(master=bezoekerframe, text='incorrecte invoer', foreground="red")
        foutlabel.place(x=35, y=125)
    return

def aanbieder_gegevens():
    inlognam = inlognaam.get()
    inlogcde = inlogcode.get()
    aanbieder_inloggen(inlognam, inlogcde)

def bezoeker_gegevens():
    naam = loginfield.get()
    emaill_adrees = loginfield2.get()
    bezoeker_inloggen(naam, emaill_adrees)

def bezoeker_frame():
    filmframe.pack_forget()
    beginframe.pack_forget()
    bezoekerframe.pack()

def beginFrame():
    mijngebruikers.pack_forget()
    mijnfilms.pack_forget()
    ticketframe.pack_forget()
    beschFilms.pack_forget()
    aanbiederHall.pack_forget()
    filmframe.pack_forget()
    bezoekerframe.pack_forget()
    aanbiederframe.pack_forget()
    beginframe.pack()

def aanbiederFrame():
    aanbiederHall.pack_forget()
    beginframe.pack_forget()
    aanbiederframe.pack()

def filmFrame():
    bezoekerframe.pack_forget()
    filmframe.pack()

def aanbiederhall():
    mijngebruikers.pack_forget()
    mijnfilms.pack_forget()
    beschFilms.pack_forget()
    aanbiederHall.pack()

def beschikbare_films():
    aanbiederHall.pack_forget()
    beschFilms.pack()

def mijnFilms():
    aanbiederHall.pack_forget()
    mijnfilms.pack()

def mijnGebruikers():
    mijnfilms.pack_forget()
    aanbiederHall.pack_forget()
    mijngebruikers.pack()

def ticketFrame():
    filmframe.pack_forget()
    ticketframe.pack()

root = Tk()

beginframe = Frame(master=root)
beginframe.pack()
label1 = Label(master=beginframe, text='Wat ben je? een Bezoeker of een aanbieder')
label1.pack()
button1 = Button(master=beginframe, text='aanbieder', command=aanbiederFrame)
button1.pack(side=LEFT, pady=20)
button2 = Button(master=beginframe, text='bezoeker', command=bezoeker_frame)
button2.pack(side=RIGHT, pady=20)

bezoekerframe = Frame(master=root)
bezoekerframe.pack()
label2 = Label(master=bezoekerframe, text='wat is uw naam?')
label2.pack()
loginfield = Entry(master=bezoekerframe)
loginfield.pack(pady=10, padx=10)
label21= Label(master=bezoekerframe, text='vul uw E-mail in')
label21.pack()
loginfield2 = Entry(master=bezoekerframe)
loginfield2.pack(pady=20, padx=20)
logbut = Button(master=bezoekerframe, text='login', command=bezoeker_gegevens)
logbut.pack(side=RIGHT, pady=20)
bu = Button(master=bezoekerframe, text='back', command=beginFrame)
bu.pack(side=LEFT, pady=20)

aanbiederframe = Frame(master=root)
aanbiederframe.pack()
label3 = Label(master=aanbiederframe, text='vul in naam')
label3.pack()
inlognaam = Entry(master=aanbiederframe)
inlognaam.pack(pady=10, padx=10)
label31 = Label(master=aanbiederframe,text='vule in jouw code')
label31.pack()
inlogcode = Entry(master=aanbiederframe)
inlogcode.pack(pady=10, padx=10)
log = Button(master=aanbiederframe, text='login', command=aanbieder_gegevens)
log.pack(pady=20)
back = Button(master=aanbiederframe, text='back', command=beginFrame)
back.pack(side=RIGHT)

filmframe = Frame(master=root)
filmframe.pack()
label4 = Label(master=filmframe, text='alle films die worden aangebode')
label4.pack()
ba = Button(master=filmframe, text='back', command=bezoeker_frame)
ba.pack(side=LEFT, pady=20)
door = Button(master=filmframe, text='ga door',command=ticketFrame)
door.pack(side=RIGHT, pady=20)


aanbiederHall = Frame(master=root)
aanbiederHall.pack(fill='both', expand=True)
backbutton = Button(master=aanbiederHall, text='back', command=aanbiederFrame)
backbutton.pack(side=RIGHT)
labe5 = Label(master=aanbiederHall, text='Wat wil je zien')
labe5.pack(side=LEFT)
button3 = Button(master=aanbiederHall, text='Beschikbare films', command=beschikbare_films)
button3.pack(pady=20)
button4 = Button(master=aanbiederHall, text='Mijn films',command=mijnFilms)
button4.pack(pady=20)

beschFilms = Frame(master=root)
beschFilms.pack()
label5 = Label(master=beschFilms,text='alle beschikbare films')
label5.pack()
backb = Button(master=beschFilms,text='back', command=aanbiederhall)
backb.pack(side=RIGHT, pady=20)

mijnfilms = Frame(master=root)
mijnfilms.pack()
label7 = Label(master=mijnfilms,text='overzich van mijn films')
label7.pack()
backbutton2= Button(master=mijnfilms,text='back', command=aanbiederhall)
backbutton2.pack(side=LEFT)
button5 = Button(master=mijnfilms,text='mijn gebruikers',command=mijnGebruikers)
button5.pack(side=RIGHT,pady=20)

mijngebruikers = Frame(master=root)
mijngebruikers.pack()
bezoekers_overzicht = Label(master=mijngebruikers, text='Dit is een overzicht van alle bezoekers die mijn films bekijken')
bezoekers_overzicht.pack()
backbutton3 = Button(master=mijngebruikers,text='back',command=aanbiederhall)
backbutton3.pack(side=LEFT)


ticketframe = Frame(master=root)
ticketframe.pack()
label6 = Label(master=ticketframe, text='Dit is jouw code')
label6.pack()

beginFrame()
mainloop()


