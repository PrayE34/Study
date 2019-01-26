from tkinter import *
import calendar
import datetime

class TkinterCalendar(calendar.Calendar):
    def formatmonth(self, master, year, month, days):
        dates = self.monthdatescalendar(year, month)

        frame = Frame(master)

        self.labels = []

        for r, week in enumerate(dates):
            labels_row = []
            for c, date in enumerate(week):
                if date.month != month:
                    label = Button(frame, text=date.strftime(' '), width=10, height=5, relief='solid', bd=0, bg = '#ffb700',font='size 10 bold'
                                   , padx=0,pady=0,anchor='w')
                    label.grid(row=r, column=c)
                else:
                    label = Button(frame,fg='white',
                    text=date.strftime('%d\n\n\n\n'), width=10, height=5, relief='solid', bd=0,bg = '#ffb700',font='size 10 bold'
                                   , padx=0, pady=0,command=mInfoWindow)
                    label.grid(row=r, column=c)

                if c == 6:
                    label['fg'] = '#585858'

                if c == 0:
                    label['fg'] = '#c82d39'

                if days == date.day:
                    label['bg'] = '#820000'

                labels_row.append(label)
            self.labels.append(labels_row)

        return frame, self.labels

def pBtn():
    global year
    global month
    if month == 12:
        year += 1
        month = 1
        mLabel.config(text = month)
        Date, labels = frame, labels = tkcalendar.formatmonth(Window, year, month, days)
        Date.place(x=29, y=170)
    else:
        month += 1
        mLabel.config(text = month)
        Date, labels = frame, labels = tkcalendar.formatmonth(Window, year, month, days)
        Date.place(x=29, y=170)

def mBtn():
    global year
    global month
    if month == 1:
        year -= 1
        month = 12
        mLabel.config(text=month)
        Date, labels = frame, labels = tkcalendar.formatmonth(Window, year, month, days)
        Date.place(x=29, y=170)
    else:
        month -= 1
        mLabel.config(text=month)
        Date, labels = frame, labels = tkcalendar.formatmonth(Window, year, month, days)
        Date.place(x=29, y=170)
#월 넘기기 버튼

def mInfoWindow():
    global InfoWindow
    InfoWindow = Tk()
    InfoWindow.title("일정등록")
    InfoWindow['bg'] = '#fcfcf7'
    InfoWindow.geometry("400x400")  # 창 크기 조절
    InfoWindow.resizable(False, False)  # 창 크기 조절 락

    global entName
    global addMoney
    global minusMoney

    name = Frame(InfoWindow, relief="solid", bg='#fcfcf7')
    Label(name, text="일정 이름", font="size 15 bold", width=30, bg='#fcfcf7').grid(row=0, column=0)
    entName = Entry(name, width=35, bg='#ffb700', fg='white', relief='sunken', font="size 13 bold")
    entName.grid(row=1, column=0)
    name.place(x=20, y=40)

    Money = Frame(InfoWindow, relief="solid", bg='#fcfcf7')
    Label(Money, text="수익", font="size 15 bold", width=15, bg='#fcfcf7').grid(row=0, column=0)
    addMoney = Entry(Money, width=15, bg='#ffb700', fg='white', relief='sunken', font="size 13 bold")
    addMoney.grid(row=1, column=0)
    Label(Money, text="지출", font="size 15 bold", width=15, bg='#fcfcf7').grid(row=0, column=1)
    minusMoney = Entry(Money, width=15, bg='#ffb700', fg='white', relief='sunken', font="size 13 bold")
    minusMoney.grid(row=1, column=1)
    Money.place(x=15, y=160)

    Button(InfoWindow, text='입력', width=15, command=Display).place(x=50, y=300)
    Button(InfoWindow, text='취소', width=15, command=close_InfoWindow).place(x=235, y=300)

    InfoWindow.mainloop()

def close_InfoWindow():
    global InfoWindow
    InfoWindow.destroy()

def Display():
    global entName
    global addMoney
    global minusMoney
    global labels
    String = "%d\n\n" + entName.get() + "\n" + addMoney.get() + "\n"
    labels[0][0]['text'] = String
    close_InfoWindow()

year = datetime.datetime.now().year
month = datetime.datetime.now().month
days = datetime.datetime.now().day

Window = Tk()
Window.title('일정 및 비용 관리 프로그램 v1.0')
Window.geometry("640x790") #창 크기 조절
Window.resizable(False, False) #창 크기 조절 락
Window['bg']='#ffb700'

Main = Frame(Window,width=640,height=600,bg='#ffb700')
Main.pack()

mLabel = Label(Window, text=month, font='size 50', fg='white', bg='#ffb700', bd=0)
mLabel.place(x=42, y=31)

buttenSet = Frame(Window,bg='#ffb700',bd=1,width=120,heigh=50)
Button(buttenSet,text="◀",bg='#ffb700',relief='solid',bd=0,fg='white', command = mBtn).pack(side="left")
Label(buttenSet,text="     ",bg='#ffb700',bd=0,fg='white').pack(side="left")
Button(buttenSet,text="▶",bg='#ffb700',relief='solid',bd=0,fg='white', command = pBtn).pack(side="left")
buttenSet.place(x=473,y=80)

Weeks = Frame(Window)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'S',fg='#820000',relief='solid',bd=0,anchor='n',padx=0,pady=0
      ,highlightbackground="#b46262",highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=0)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'M',fg='white',relief='solid',bd=0,anchor='n',padx=0,pady=0
      ,highlightbackground="#b46262",highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=1)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'T',fg='white',relief='solid',bd=0,anchor='n',padx=0,pady=0
      , highlightbackground="#b46262", highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=2)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'W',fg='white',relief='solid',bd=0,anchor='n',padx=0,pady=0
      , highlightbackground="#b46262", highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=3)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'T',fg='white',relief='solid',bd=0,anchor='n',padx=0,pady=0
      , highlightbackground="#b46262", highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=4)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'F',fg='white',relief='solid',bd=0,anchor='n',padx=0,pady=0
      , highlightbackground="#b46262", highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=5)
Label(Weeks, bg='#ffb700', width=9,font='size 11 bold', text = 'S',fg='#414141',relief='solid',bd=0,anchor='n',padx=0,pady=0
      , highlightbackground="#b46262", highlightcolor="#b46262", highlightthickness=1).grid(row=0, column=6)
Weeks.place(x=30,y=130)
#요일 뿌려줌
Date = Frame(Window)
tkcalendar = TkinterCalendar(calendar.SUNDAY)

Date, labels = frame, labels = tkcalendar.formatmonth(Window,year,month,days)
Date.place(x=29,y=170)

Info = Frame(Window,height=200,bg='black',bd=0)

a = Label(Info,text=' 지난 지출 : ',width=25,height=2,font=('휴먼편지체',17,'bold'),bg = '#f5f7f7',bd=0,padx=0,pady=0,anchor='w',fg='#313131').grid(row=0,column=0)
b = Label(Info,text=' 예상 지출 : ',width=25,height=2,font=('휴먼편지체',17,'bold'),bg = '#f5f7f7',bd=0,padx=0,pady=0,anchor='w',fg='#313131').grid(row=0,column=1)
c = Label(Info,text=' 현재 잔액 : ',width=25,height=2,font=('휴먼편지체',17,'bold'),bg = '#f5f7f7',bd=0,padx=0,pady=0,anchor='w',fg='#313131').grid(row=1,column=0)
d = Label(Info,text=' 남은 금액 : ',width=25,height=2,font=('휴먼편지체',17,'bold'),bg = '#f5f7f7',bd=0,padx=0,pady=0,anchor='w',fg='#313131').grid(row=1,column=1)

Info.place(x=0,y=690)

Window.mainloop()
