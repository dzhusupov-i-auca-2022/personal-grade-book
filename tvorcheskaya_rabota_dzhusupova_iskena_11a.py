import tkinter as tk
win=tk.Tk()
win.title('МОЙ ДНЕВНИК')
win.geometry("400x300+400-100")
win.config(bg='#FFF94F')
dn=tk.Label(win, text='ДНЕВНИК',
            bg='#FFF94F',
            fg='BLACK',
            font=('Berlin Sans FB Demi',15,'bold'),
            )
dn.pack()
target=tk.Tk()
target.geometry("400x300+400-100")
name=tk.Entry(target)
les=tk.Tk()
les.geometry("400x300+400-100")
bio=tk.Tk()
bio.geometry("400x300+400-100")
def targets():
    target.title('МОИ ЦЕЛИ')
    target.geometry("245x400+800-100")
    target.config(bg='#8FC93A')
    tr=tk.Label(target, text='МОИ ЦЕЛИ',
                bg='#8FC93A',
                fg='black',
                font=('Cooper Black',18,'bold'))
    tr.grid(row=0,column=0,columnspan=3)
    name.grid(row=1,column=1,stick='wesn') 
    tk.Button(target,command=getting,text="Поставить цель->",activebackground='#7FBEEB',
              activeforeground='white',bg='#E4CC37',font=('Calibri (Body)',10,'bold')).grid(row=1,column=0,stick='we')
    target.mainloop()
def getting():
    crot=name.get()
    if crot:
        tk.Checkbutton(target,text=crot,bg='#8FC93A',fg='black',font=('Calibri (Body)',10,'bold')).grid(columnspan=2,stick='w')
        name.delete(0,tk.END)
def lessons():
    les.title('МОЕ ДОМАШНЕЕ ЗАДАНИЕ')
    les.geometry("345x300+400-430")
    les.config(bg='#7C0B2B')
    ls=tk.Label(les, text='МОЕ ДОМАШНЕЕ ЗАДАНИЕ',
                bg='#7C0B2B',
                fg='#FFCBDD',
                font=('Arial Black',15,'bold','underline'))
    ls.grid(row=0,column=0,columnspan=2)
    tk.Label(les, text='ИНФОРМАТИКА',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=1,column=0,stick='w')
    tk.Label(les, text='МАТЕМАТИКА',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=2,column=0,stick='w')
    tk.Label(les, text='ФИЗИКА',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=3,column=0,stick='w')
    tk.Label(les, text='ГЕОГРАФИЯ',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=4,column=0,stick='w')
    tk.Label(les, text='ЛИТЕРАТУРА',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=5,column=0,stick='w')
    tk.Label(les, text='ГЕОМЕТРИЯ',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=6,column=0,stick='w')
    tk.Label(les, text='ХИМИЯ',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=7,column=0,stick='w')
    tk.Label(les, text='БИОЛОГИЯ',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=8,column=0,stick='w')
    tk.Label(les, text='КЫРГЫЗСКИЙ ЯЗЫК',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=9,column=0,stick='w')
    tk.Label(les, text='ИСТОРИЯ',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=10,column=0,stick='w')
    tk.Label(les, text='АНГЛ ЯЗЫК',bg='#7C0B2B',fg='#FFCBDD',font=('Arial Black',10,'bold','underline')).grid(row=11,column=0,stick='w')
    for i in range(1,12):
        tk.Entry(les,font=('Arial Black',10,'bold')).grid(row=i,column=1,stick='w')
    les.mainloop()
def biog():
    bio.title('ИНФОРМАЦИЯ')
    bio.geometry("200x200-1000+300")
    bio.config(bg='#70D6FF')
    bg1=tk.Label(bio, text='ЛИЧНАЯ ИНФОРМАЦИЯ',
                bg='#70D6FF',
                fg='#FF70A6',
                font=('Comic Sans MS',11,'bold'))
    nick=tk.Entry(bio,font=('Comic Sans MS',9,'bold')).grid(row=1,column=1)
    urclass=tk.Entry(bio,font=('Comic Sans MS',9,'bold')).grid(row=2,column=1)
    skills=tk.Entry(bio,font=('Comic Sans MS',9,'bold')).grid(row=3,column=1)
    tk.Label(bio,text='ИМЯ:',font=('Comic Sans MS',10,'bold'),
             bg='#70D6FF',fg='#FF70A6').grid(row=1,column=0)
    tk.Label(bio,text='КЛАСС:',font=('Comic Sans MS',10,'bold'),
             bg='#70D6FF',fg='#FF70A6').grid(row=2,column=0)
    tk.Label(bio,text='УМЕНИЯ:',font=('Comic Sans MS',10,'bold'),
             bg='#70D6FF',fg='#FF70A6').grid(row=3,column=0)
    bg1.grid(row=0,column=0,columnspan=2)
    bio.mainloop()
cely=tk.Button(win,text="Цели и Мечты",
               bg='#FFF94F',
               fg='#90A955',
               height=3,
               relief=tk.FLAT,
               font=('Berlin Sans FB Demi',14,'bold'),
               command=targets)
lessons=tk.Button(win,text="Домашнее задание",
               bg='#FFF94F',
               fg='#DB5A42',
               height=3,
               relief=tk.FLAT,
               font=('Berlin Sans FB Demi',14,'bold'),
               command=lessons)
bion=tk.Button(win,text="Личная информация",
               bg='#FFF94F',
               fg='#3B1F2B',
               height=3,
               relief=tk.FLAT,
               font=('Berlin Sans FB Demi',14,'bold'),
               command=biog)
cely.pack()
lessons.pack()
bion.pack()
win.mainloop()
