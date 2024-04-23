from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.geometry('1080x500')
root.resizable(0, 0)
root.title("Language Translator")
root.config(bg='#000000')
# root.title(bg ='white')

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        t1= Translator()
        trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
        trans_text=trans_text.text
        
        text2.delete(1.0,END)
        text2.insert(END,trans_text)
    except Exception as e:
        messagebox.showerror("Translation Error", "An error occurred during translation. Please try again."+str(e))


#icon
image_icon = PhotoImage(file="C:/Users/admin/Desktop/language-translator-master/icon.png")
root.iconphoto(True,image_icon)

#arrow
arrow_image = PhotoImage(file="C:/Users/admin/Desktop/language-translator-master/arrowff.png")
image_label=Label(root,image=arrow_image,width=70,height=70)
image_label.place(x=510,y=40)


language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=40);
combo1.set("english")


label1=Label(root,text="English",font="segoe 30 bold",bg="#cfd0d4",width=13,bd=4,relief=GROOVE)
label1.place(x=70,y=80)

f=Frame(root,bg="grey",bd=5)
f.place(x=30,y=150,width =410,height=210)

text1=Text(f,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=400,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=40);
combo2.set("Select Language")




label2=Label(root,text="English",font="segoe 30 bold",bg="#cfd0d4",width=13,bd=4,relief=GROOVE)
label2.place(x=690,y=80)

f1=Frame(root,bg="grey",bd=5)
f1.place(x=640,y=150,width =410,height=210)

text2=Text(f1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=400,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translae button
translate=Button(root,text="Translate",font="Roboto 15 bold italic",
                 activebackground="green",cursor="hand2",bd=5,
                 bg="red",fg="white",command=translate_now)
translate.place(x=480,y=300)


label_change()


# YOUR TRANSLATOR
#Label(root, text="Language Translator", font="arial 15 bold", fg='#898989', bg='#1A1A1A').pack()
Label(root, text="LINGUABOT🤖 by GROUP NO. 22", font='arial 16', fg='#898989', bg='#000000', height='5', width='25').pack(side='bottom');
root.mainloop()