from tkinter import *
from PIL import ImageTk, Image

def education():
    F4=Tk()
    #F4.geometry("600x400")
    F4.title("Education")
    
        
        
    scrol_y=Scrollbar(F4,orient=VERTICAL)
    txtarea=Text(F4,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)
    txtarea.delete('1.0',END)
    
    txtarea.insert(END ,'''•   Pursuing B.Tech in Information Science(ISE) at University Visvesvaraya          college of Engineering. 
•   12th from Mes KK Pu College. 
•   S S L C from The New Cambridge High School
''')

def programming_lang():
    F4=Tk()
    #F4.geometry("600x400")
    F4.title("programming_lang")
    
        
        
    scrol_y=Scrollbar(F4,orient=VERTICAL)
    txtarea=Text(F4,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)
        
    txtarea.delete('1.0',END)
        
    txtarea.insert(END,'''o	C
o	C++
o	HTML,CSS
o	Python: Completed an online non-credit Specilization authorized by                       University of Michigan and offered through                                     Coursera(coursera.org/verify/specialization/RZ8M44P94CY2). 
''')

def sw_tools():
    F4=Tk()
    #F4.geometry("600x400")
    F4.title("Software tools")
    
        
        
    scrol_y=Scrollbar(F4,orient=VERTICAL)
    txtarea=Text(F4,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)
    txtarea.delete('1.0',END)
    
    txtarea.insert(END,'''o	Google Cloud Console: Participated in Google Cloud Ready Program and was able to get hands on experience in the cloud console. 
o	Robotic Process Automation: Have worked on Web scrapping and process automation using the UI Path tool. 
''')

def projects():
    F4=Tk()
    #F4.geometry("600x400")
    F4.title("Projects")
    
        
        
    scrol_y=Scrollbar(F4,orient=VERTICAL)
    txtarea=Text(F4,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)
    
    txtarea.delete('1.0',END)
    
    txtarea.insert(END,'''o	Website: Have created a website using HTML for the front end and php for the backend 
''')


root=Tk()

root.title("Resume")
Label(root,text="Srujan Kumar R",bd=11,relief=RAISED,bg="#4E342E",fg="#F2F2F2",font=("times new roman",30,"bold","italic"),pady=2).pack(fill=X)
        
        
F0=Label(root,text="Email: srujanravi30@gmail.com",bd=5,font=("times new roman",30,"bold","italic"),relief=RAISED,bg="#4E342E",fg="#F2F2F2")
F0.pack(fill=X)
F1=LabelFrame(root,bd=10,relief=GROOVE,text="RESUME",font=("times new roman",15,"bold","italic"),fg="GOLD",bg="#4E342E")
F1.pack(fill=X)
        
Button(F1,text="Education",command=education,bg="#C9C0BB",bd=5,fg="black",width=10,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        
Button(F1,text="Programming Languages",command=programming_lang,bg="#C9C0BB",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=1,padx=10,pady=15)
        
Button(F1,text="Software tools",command=sw_tools,bg="#C9C0BB",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=15)
        
Button(F1,text="Projects",command=projects,bg="#C9C0BB",bd=5,fg="black",width=10,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=15)
        
#Button(F1,text="Certificates",command=certificate,bg="yellow",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=15)

Button(F1,text="Exit",command=root.destroy,bg="#C9C0BB",bd=5,fg="black",width=10,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=15)


root.mainloop()
