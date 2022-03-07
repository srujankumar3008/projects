from tkinter import *
from PIL import ImageTk, Image


class resume_window:
    def __init__(self, master):
        self.master=master
        self.master.geometry("1000x600")
        self.master.title("Resume")
#comments
        

        Label(self.master,text="Name",bd=11,relief=RAISED,bg="red",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        F0=Label(self.master,text="Email: email@email.com",bd=5,font=("times new roman",30,"bold"),relief=RAISED,bg="yellow")
        F0.place(x=0,y=73,height=60,relwidth=1)
        F1=LabelFrame(self.master,bd=10,relief=GROOVE,text="RESUME",font=("times new roman",15,"bold"),fg="black",bg="red")
        F1.place(x=0,y=133,relwidth=1,height=100)
        
        Button(F1,text="Education",command=self.education,bg="yellow",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        
        Button(F1,text="Programming Languages",command=self.programming_lang,bg="yellow",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=1,padx=10,pady=15)
        
        Button(F1,text="Software tools",command=self.sw_tools,bg="yellow",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=15)
        
        Button(F1,text="Projects",command=self.projects,bg="yellow",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=15)
        
        Button(F1,text="Certificates",command=self.certificate,bg="yellow",bd=5,fg="black",width=20,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=15)

           
        Button(F1,text="Exit",command=self.master.destroy,bg="yellow",bd=5,fg="black",width=10,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=15)
        

        # Notepad Area ....................................
        
        F4=LabelFrame(self.master,bd=10,relief=RAISED)
        F4.place(x=0,y=233,relwidth=1,relheight=1)
        
        
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.welcome(string='KANNADIGA')
        
        
        
      
    def certificate(self):
        global my_img1,my_img2,my_img3
        self.txtarea.delete('1.0',END)
        self.welcome(string='CERTIFICATES')

        my_img3 = ImageTk.PhotoImage((Image.open('img1.jpg')).resize((1000,650),Image.ANTIALIAS))
        my_img1 = ImageTk.PhotoImage((Image.open('img2.jpg')).resize((500,650),Image.ANTIALIAS))
        my_img2 = ImageTk.PhotoImage((Image.open('img3.jpg')).resize((500,650),Image.ANTIALIAS))

        self.txtarea.image_create(END, image=my_img1)
        self.txtarea.image_create(END, image=my_img2)
        self.txtarea.image_create(END, image=my_img3)
        
        
        
    def education(self):
        self.txtarea.delete('1.0',END)
        self.welcome(string='EDUCATION')
        self.txtarea.insert(END ,'''•  add info
''')
 
    
    def welcome(self,string):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\n_________________________________________________________________________________________________________________________________________________________________\n")
        self.txtarea.insert(END,f"\t\t\t\t\t\t\t\t\t|| {string} ||")
    
    def programming_lang(self):
        
        self.txtarea.delete('1.0',END)
        self.welcome(string='PROGRAMMING LANGUAGES')
        self.txtarea.insert(END,'''o    add info''')
       
        
        
        
    def clear_notebook(self):
        self.txtarea.delete('1.0',END)
        self.welcome(string='RESUME')
    
    def sw_tools(self):
        self.txtarea.delete('1.0',END)
        self.welcome(string='SOFTWARE TOOLS')
        self.txtarea.insert(END,'''o	add info
''')

    def projects(self):            
        self.txtarea.delete('1.0',END)
        self.welcome(string='PROJECTS')
        self.txtarea.insert(END,'''o	add info''')


root=Tk()
obj=resume_window(root)
root.attributes('-fullscreen', True)
root.mainloop()
