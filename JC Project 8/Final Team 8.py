#final draft code


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import smtplib
import imghdr
import socket
from email.message import EmailMessage
root = Tk()
root.title("FOUNDIT - The Digital Lost and Found")
root.geometry("1000x600")
root.resizable(False,False)


no = 0

#defining the background image
global bg_root
bg=Image.open(r'C:/Users/keeru/Documents/JC Project 8/bg6.png')
bg=bg.resize((1000,600))

bg_root=ImageTk.PhotoImage(bg)

#create a label
global rootlabel
rootlabel=Label(root, image=bg_root)
rootlabel.place(x=0,y=0,relwidth=1,relheight=1)

#SQL Connection 
import mysql.connector as mys
mycon=mys.connect(host='localhost',
                  user='root',
                  password='root',
                  database='project')
if mycon.is_connected():
    print("Success")

mycur=mycon.cursor()
mycur.execute('SELECT * FROM std')
rstd=mycur.fetchall()
rstdcount=0
for i in rstd:
    rstdcount+=1

#FUNC TO BROWSE THROUGH IMAGES
filename=''
def img():
    global ri
    ri=Toplevel()
    ri.title('BROWSE THROUGH FILES')
    root.withdraw()
    ri.minsize(400,200)



    ri.configure(background='DeepSkyBlue4')

    ri.imgframe=LabelFrame(ri,bg='DeepSkyBlue4',fg='white', relief='raised',text='CHOOSE A FILE TO UPLOAD')


    ri.imgframe.grid(column=0,row=1,padx=20,pady=20)
    
    
    def fileDialog():
        global filename
        filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File")
        ri.label = Label(ri.imgframe, text = "")
        ri.label.grid(column = 1, row = 2)

        ri.label.configure(text = filename)
        ri.imgframe1=LabelFrame(ri,bg='DeepSkyBlue4',fg='white',relief='raised',text='PICTURE')
        ri.imgframe1.grid(column=0,row=30,padx=20,pady=20)
             

        img = Image.open(filename)
        img = img.resize((320, 250))
        photo = ImageTk.PhotoImage(img)

        ri.label2 = Label(ri.imgframe1,image=photo)
        ri.label2.image = photo
        ri.label2.pack()
        okbutton=Button(ri,text='OK',command=picadd)
        
        okbutton.grid(column=100,row=190,ipadx=20)
    def button():
        button=Button(ri.imgframe,text="BROWSE",command=fileDialog)
        button.grid(column=1,row=1,padx=20)
    
    button()
    
    return filename

    ri.mainloop()


#SEND EMAILS
def ccpem():
    try:
        global send
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)

        server.login("foundit101221@gmail.com", "zwmelnakkqbtgjws")

        msg=EmailMessage()
        msg['Subject']='Credit Score Update'
        msg['From']="foundit101221@gmail.com"
        msg['To']=send
        msg.set_content("""Hey,
                        CONGRATULATIONS!!! You have a credit score of 1000.
                        Here is a small gift from us to you for all the hard work you've done...
                        Have a beautiful day :)""")


        with open(r'C:/Users/keeru/Documents/JC Project 8/CCPAPP.png','rb') as f:
            file_data=f.read()
            file_type=imghdr.what(f.name)
            file_name=f.name

        msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

        server.send_message(msg)
        server.quit()
    except:
        messagebox.showwarning('An error has occurred while sending the reward email. kindly check the email given.' )
        

    
def emailidf(n):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("foundit101221@gmail.com", "zwmelnakkqbtgjws")
        server.sendmail(
            "foundit101221@gmail.com",
            str(n),'''Subject:News regarding your lost item

        Hello,
        Your item has been found. Please collect it at the office between 12pm to 7pm, one day after you recieve this email.        
        We request you to come with this mail as confirmation for the item collection.

        Thank you
        Have a nice day''')
        messagebox.showinfo("Email ID","The email has been sent")
        server.quit()
    except:
        messagebox.showwarning('Oops!','We will contact the person to get the right email')

###
def emailidl(n):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("foundit101221@gmail.com", "zwmelnakkqbtgjws")
        server.sendmail(
            "foundit101221@gmail.com",
            str(n),'''Subject:News regarding the found item

        Hello,
        The item you found has been recognised as lost by the owner. Kindly submit the item by tomorrow in the admin office between 12pm to 7pm.
        Kindly show this mail before submitting the item for your credit points to be added.
        
        Thank you 
        Have a nice day''')
        messagebox.showinfo("Email ID","The email has been sent")
        server.quit()
    except:
        messagebox.showwarning('Oops!','We will contact the person to get the right email')

    
messagef='''Hello,
Your item has been found please come and collect it \nfrom the office between 12pm to 7pm one day after you recieve this email.        
We request you to come with this mail as confirmation for the item collection.
Thank you 
Have a nice day!!!
'''
messagel='''Hello
The item you found has been recognised as lost by the owner. \nKindly submit the item by tomorrow in the admin office between 12pm to 7pm.
Kindly show this mail before submitting the item for your credit points to be added.
Thank you 
Have a nice day!!!
'''

#PROFILE TAB
def profile(u):
    global profileframe
    global pf_frame
    global bg_root
    profileframe=Label(top, image=bg_root)#,text='ACCOUNT DETAILS',font=20)
    profileframe.place(x=0,y=0,relwidth=1,relheight=1)


    stmt='select * from std where uname=\''+u+'\''
    cur.execute(stmt)
    pro=cur.fetchall()
    labelf=LabelFrame(profileframe,bg='DeepSkyBlue4',relief='raised',font=(10),fg='white',text='ACCOUNT DETAILS')
    labelf.pack()
    txt='\nFIRST NAME         :'+pro[0][1]+'\n\n\nLAST NAME            :'+pro[0][2]+'\n\n\nUSER NAME       :'+pro[0][3]+'\n\n\nPASSWORD        :'+pro[0][4]+'\n\n\nEMAIL    :'+str(pro[0][6])+'\n\n\nCREDIT POINTS      :'+str(pro[0][5])
    labelp=Label(labelf,bg='DeepSkyBlue4',fg='white', text=txt, font=("Helvetica, 14"))
    labelp.pack()
    


#Making the titlebar 
title = LabelFrame(root, bg = "DeepSkyBlue4", relief = "raised")
title.pack(expand=1, fill="x", side=TOP, anchor=NW)

foundit = Label(title, text = "FOUNDIT!", font=("Helvetica, 34"), bg = "DeepSkyBlue4", fg = "white")
foundit.pack()



#HIDE ALL FRAMES _ ADMIN WINDOW
def hide_all_frames():
   pass

#email window
def emf(n):
    k=Toplevel()
    k.title('SEND EMAIL')
    root.withdraw()
    k.minsize(400,300)
    k.configure(background='DeepSkyBlue4')
    txt=''' WHEN YOU CLICK OK BUTTON, WE WILL SEND AN EMAIL TO '''+n+''' WITH THE FOLLOWING AS CONTENT:\n'''+messagef+'\n DO WISH TO CONTINUE???'
    k.txtframe=LabelFrame(k,bg='DeepSkyBlue4',relief='raised')
    k.txtframe.pack()
    k.txt=Label(k.txtframe,bg='DeepSkyBlue4',fg='white',text=txt,font=20)
    k.txt.pack()
    k.email=Button(k,text='OK',padx=40,pady=5,command=lambda:emailidf(n))
    k.email.pack()
    k.mainloop()
    k.destroy()

###
def eml(n):
    k=Toplevel()
    k.title('SEND EMAIL')
    root.withdraw()
    k.minsize(400,300)
    k.configure(background='DeepSkyBlue4')
    txt=''' WHEN YOU CLICK OK BUTTON, WE WILL SEND AN EMAIL TO '''+n+''' WITH THE FOLLOWING AS CONTENT:\n'''+messagel+'\n DO WISH TO CONTINUE???'
    k.txtframe=LabelFrame(k,bg='DeepSkyBlue',relief='raised')
    k.txtframe.pack()
    k.txt=Label(k.txtframe,bg='DeepSkyBlue4',fg='white',text=txt,font=20)
    k.txt.pack()
    k.email=Button(k,text='OK',padx=40,pady=5,command=lambda:emailidl(n))
    k.email.pack()
    k.mainloop()
##    k.destroy()

def detailsl(event):
    r=Toplevel()
    r.title('DETAILS ABOUT ITEM')
    root.withdraw()
    r.minsize(400,300)
    r.configure(background='DeepSkyBlue4')
    r.detframe=LabelFrame(r,bg='DeepSkyBlue4',fg='white',font=(10),relief='raised',text='DETAILS')
    r.detframe.pack()
    item=trv.selection()
    
    for i in item:
        stmt='select * from lost where item_id='+i
    mycur.execute(stmt)
    ril=mycur.fetchall()
    
    for j in ril:
         txt='ITEM ID         : '+str(j[0])+'\n\n CATEGORY         :'+str(j[1])+'\n\n ITEM NAME       :'+str(j[2])+'\n\n DESCRIPTION         :'+str(j[3])+'\n\n LAST KNOWN LOACTION     :'+str(j[4])+'\n\n EMAIL          :'+str(j[5])

         n=j[5]
         break
    r.label=Label(r.detframe,bg='DeepSkyBlue4',fg='white',text=txt,padx=20,pady=20)
    r.label.pack(ipady=10)
    r.resizable(False,False)
    r.emailb=Button(r,text="SEND EMAIL!", padx=40,pady=5,command=lambda:emf(n))
    r.emailb.pack(ipady=10)
    r.mainloop()
#SHOW DETAILS OF ITEM--FOUND WINDOW __USER
def detailsf(event):
    r=Toplevel()
    r.title('DETAILS ABOUT ITEM')
    root.withdraw()
    r.geometry('600x550')
    r.configure(background='DeepSkyBlue4')
    detframe=LabelFrame(r,bg='DeepSkyBlue4',fg='white', font=(10),relief='raised',text='DETAILS')
    detframe.pack(ipady=10)
    item=trv_found.selection()
    for i in item:
        stmt='select * from found where item_id='+i
    mycur.execute(stmt)
    ril=mycur.fetchall()
    for j in ril:
         txt='ITEM ID       : '+str(j[0])+'\n\n CATEGORY        :'+str(j[1])+'\n\n ITEM NAME       :'+str(j[2])+'\n\n DESCRIPTION       :'+str(j[3])+'\n\n FOUND LOACTION       :'+str(j[4])+'\n\n EMAIL        :'+str(j[5])#+'\n\n PICTURE:'+str(j[6])
         m=j[6]
         n=j[5]
         break
    
    label=Label(detframe,bg='DeepSkyBlue4',fg='white',text=txt,padx=20,pady=10)
    label.pack()
    imgframe=LabelFrame(r,bg='DeepSkyBlue4',font=(10),fg='white',relief='raised',text='PICTURE')

    imgframe.pack()
    img=Image.open(m,'r')
    img=img.resize((320,250))
    photo=ImageTk.PhotoImage(img)
    label2=Label(imgframe,image=photo)
    label2.image=photo
    label2.pack()
    r.resizable(False,False)
    email=Button(r,text="SEND EMAIL!", padx=40,pady=5,command=lambda:eml(n))
    email.pack(ipady=10)
    r.mainloop()
# CHANGE PASS IN DB
def pass_db():
    global cur
    global e
    global u_entry

    cur=mycon.cursor()
    c='select * from std'
    cur.execute(c)
    w=(cur.fetchall())
    global u
    u=u_entry.get()
    u_entry.pack()

    
    for i in w:
        
        if i[3]==u:
            e=i[-1]
            
            break
    xyz()
    
    
    
    
    
#FORGOT PASSWORD
def forgot():
    global z
    z=Toplevel()
    z.title('FORGOT PASSWORD?')
##    root.withdraw()
    z.geometry('510x200')
    z.resizable(width=False,height=False)
    z.configure(background='DeepSkyBlue4')
    txtframe=LabelFrame(z,relief='raised',bg='DeepSkyBlue4',font=10,fg='white',text='WE NEED YOUR USERNAME TO SEND YOU AN OTP')
    txtframe.pack()
    ulabel=Label(txtframe,bg='DeepSkyBlue4',font=10,fg='white',text='Enter your user name :')
    ulabel.pack()
    global u_entry
    u_entry=Entry(txtframe,width=40)
    u_entry.pack()
    
    z.resizable(False, False)
    z.k=Button(txtframe,text='ok',command=lambda:pass_db())
    z.k.pack(pady=10)
    
    cur=mycon.cursor()
def xyz():
    global e
    global z
    z.geometry('800x350')
    try: 
        t='''Once you click the OK button, \nyou will be sent an email to your registered Email Id -'''+str(e)+''' \nwith the ONE TIME PASSWORD. \n You can enter the OTP in the 'OTP' window to be able to create a new Password\n Do you wish to continue?'''
        tlabel=Label(z,text=t,font=(7),fg='white',bg='DeepSkyBlue4')
        tlabel.pack()
        ok=Button(z,text='OK',padx=40,pady=5,command=otp)
        ok.pack()
    except:
        messagebox.showwarning("ERROR!",'Please Enter the Valid UserName')
        z.deiconify()
    
    z.mainloop()
#OTP
def otp():
    global z
    z.destroy()
    import random
    o=random.randint(1111,10000)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("foundit101221@gmail.com", "zwmelnakkqbtgjws")
    global e
    server.sendmail(
        "foundit101221@gmail.com",
        str(e),'''Subject:One Time Password  
Hello,
The OTP for your Log-in is :'''+str(o)+'''

Thank you
Have a nice day''')
    messagebox.showinfo("OTP ","OTP has been sent to your Email ID")
    server.quit()
    global p
    p=Toplevel()
    p.title('OTP')
##    root.withdraw()
    p.geometry('350x200')
    p.configure(background='DeepSkyBlue4')
    otp_frame=LabelFrame(p,relief='raised',bg='DeepSkyBlue4')
    otp_frame.pack()
    otp_label=Label(otp_frame,bg= 'DeepSkyBlue4',fg='white', text='Enter the OTP you have recieved :',font=(7))
    otp_label.pack()
    otp_entry=Entry(otp_frame,width=40)
    otp_entry.pack()
    
    op=Button(otp_frame,text='ok',command=lambda:abc(otp_entry.get(),o,e))
    op.pack()
#
def abc(eg,o,e):

    
    
    if eg==str(o):
        global z
        
        z.destroy()
        global p
        p.destroy()
        global y
        y=Toplevel()
        y.title('CREATE NEW PASSWORD')
        y.geometry('450x350')
        y.configure(background='DeepSkyBlue4')
        frame=LabelFrame(y,relief='raised')
        frame.pack()
        newpass=Label(frame,font=(7),text='Enter the New Password')
        newpass.pack()
        newpass_entry=Entry(frame,width=40)
        newpass_entry.pack()
        
        cnewpass=Label(frame ,font=(7),text='Confirm the New Password')
        cnewpass.pack()

        cnewpass_entry=Entry(frame,width=40)
        cnewpass_entry.pack()
        

        q=Button(y,text='ok',command=lambda:ck(newpass_entry.get(),cnewpass_entry.get()))
        q.pack()
        
    else:
        messagebox.showwarning("Error!", "WRONG OTP ENTERED! Please try again!")
    
def ck(np,cnp):
    
        if np==cnp:
            global y
            y.destroy()
            cur.execute('update std set pass=%s where email=%s',(np,str(e)))
            mycon.commit()
            messagebox.showinfo('NEW PASSWORD SET SUCCESSFULLY!','You can now LOG-IN with your Account using the New Password.')
        else:
            messagebox.showwarning("Error!", "Enter the Same Password while Confirming! Please try again!")
        
    

    
#ADD STUDENT CHECK UP
def sdcheck_func():


    global std
        

        
    mycur_std_new=mycon.cursor()#temp repository
    mycur_std_new.execute("select * from std")
    rs=mycur_std_new.fetchall()
    
    rcountstd_new=0
    for r in rs:
        rcountstd_new=rcountstd_new+1
    
    import random
    r = random.randint(111111,200000)
    


    try:
        

        sql = "INSERT INTO std (idno,fname,lname,uname,pass,ccp,email)VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val = [r,fname_entry.get(),lname_entry.get(),uname_entry.get(),pass_entry.get(),ccp_entry.get(),email_entry.get()]
        q=val[5]
        if ccp_entry.get()=='':
            val[5]=0
        if fname_entry.get()=='' or lname_entry.get()=='' or uname_entry.get()=='' or pass_entry.get()=='' or email_entry.get()=='':
            messagebox.showwarning('Error!','Please do not leave any Information Blank!\nPlease Try again')
            admin.deiconify()
        
        else:
            
            
            
            
            mycur_std_new.execute(sql,val)
            mycon.commit()

            messagebox.showinfo("Success","Report successfully made!")
            
            admin.deiconify()

            fname_entry.delete(0, END)
            lname_entry.delete(0, END)
            uname_entry.delete(0, END)
            pass_entry.delete(0, END)
            ccp_entry.delete(0, END)
            email_entry.delete(0, END)
        
    except IndexError:
        messsagebox.showwarning("ERROR!",'We cannot update a Non-Existant Record! Try again.')

#SEARCH STD
def search_std():
    try:
        s = searchstd_entry.get()
        x = s[0]+"%"

        mycur_std.execute("SELECT * FROM std WHERE fname LIKE '"+x+"'")
        rs=mycur_std.fetchall()



        
        for j in trv_std.get_children(): #clearing the treeview
            trv_std.delete(j)
        for i in rs: #Adding filtered records back into treeview
            trv_std.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    except:
        messagebox.showwarning('Error!',' Please type what you want to search.')
        admin.deiconify()

#DELETE STD RECORD
def delete_std():
    try:
        x = trv_std.selection()[0]
        trv_std.delete(x) 
        mycur_std.execute("delete from std where idno={}".format(x))
        mycon.commit()
        


        messagebox.showinfo("Success","Record succussfully deleted!")
        global admin
        admin.deiconify()
    except:
        messagebox.showwarning('ERROR!','Please select what you want to Delete!')
        admin.deiconify()


#UPDATE DB
def update_func():
    #clear entry boxes
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    uname_entry.delete(0, END)
    pass_entry.delete(0, END)
    ccp_entry.delete(0, END)
    email_entry.delete(0, END)
    #grab record no.
    selected=trv_std.focus()
    #grab record values
    values = trv_std.item(selected,'values')
    try:
    #output to entry boxes
        fname_entry.insert(0,values[1])
        lname_entry.insert(0,values[2])
        uname_entry.insert(0,values[3])
        pass_entry.insert(0,values[4])
        email_entry.insert(0,values[6])
        ccp_entry.insert(0,values[5])
        global save_ud
        save_ud = Button(add_frame, text = "Save update", command = supdate)
        save_ud.grid(row=88, column=8,padx=3)
        update.grid_forget()
    except IndexError:
        messagebox.showwarning("ERROR!",'Please select the Student whose Credentials have to be updated! ')
        global admin
        admin.deiconify()

#SAVE UPDATE
def supdate():
    #Grab record no.
    selected=trv_std.focus()
    r = trv_std.selection()[0]
    #save new data
    trv_std.item(selected, text="",values=(r,fname_entry.get(),lname_entry.get(),uname_entry.get(),pass_entry.get(),ccp_entry.get(),email_entry.get()))
    
    #Saving the data in sql
    mycur_std.execute("UPDATE std SET idno=%s, fname=%s, lname=%s, uname=%s, pass=%s, ccp=%s, email=%s WHERE idno=%s",
                      (r, fname_entry.get(),lname_entry.get(), uname_entry.get(), pass_entry.get(), ccp_entry.get(), email_entry.get(), r))
    mycon.commit()

    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    uname_entry.delete(0, END)
    pass_entry.delete(0, END)
    ccp_entry.delete(0, END)
    email_entry.delete(0, END)

    update.grid(row=88,column=8,padx=10)
    save_ud.grid_forget()
    messagebox.showinfo("Success!", "Update saved")
    admin.deiconify()


#STUDENT DB FRAME
def sdb_func():
    
    global mycur_std
    mycur_std=mycon.cursor()#temp repository
    mycur_std.execute("select * from std order by idno")
    rs=mycur_std.fetchall()
    global rcountstd
    rcountstd=0
    for r in rs:
        rcountstd=rcountstd+1

    global bg
    bg=bg.resize((1400,600))
    bg_admin=ImageTk.PhotoImage(bg)
    
    global stud_base
    stud_base = Label(admin, image=bg_admin )
    stud_base.image=bg_admin
    stud_base.grid(row=2, column = 0, sticky="nsew", ipady=200)#Main frame (light blue)

 
    global Frame1

    Frame1 = LabelFrame(stud_base, text="Current Users", bg="DeepSkyBlue4",fg='white')
    Frame1.grid(row=3,column=0,sticky="ew",ipadx=504)

    #Creating Scrollbar
    tree_scroll = Scrollbar(Frame1)
    tree_scroll.pack(side=RIGHT,fill=Y)
    

    
    global trv_std
    trv_std=ttk.Treeview(Frame1, selectmode="browse",yscrollcommand=tree_scroll.set)
    trv_std.pack(expand="TRUE",fill="x",anchor="n")

    #Configure the scrollbar
    tree_scroll.config(command=trv_std.yview)
    
    
    
    
    trv_std["columns"]=("1","2","3","4","5","6","7")
    trv_std["show"]="headings"
    trv_std.column("1",width=10,anchor="c")
    trv_std.column("2",width=50,anchor="c")
    trv_std.column("3",width=50,anchor="c")
    trv_std.column("4",width=50,anchor="c")
    trv_std.column("5",width=50,anchor="c")
    trv_std.column("6",width=50,anchor="c")
    trv_std.column("7",width=50,anchor="c")

    trv_std.heading("1",text="ID")
    trv_std.heading("2",text="First Name")
    trv_std.heading("3",text="Last Name")
    trv_std.heading("4",text="Username")
    trv_std.heading("5",text="Password")
    trv_std.heading("6",text="Credit Score")
    trv_std.heading("7",text="Contact Info")

    for i in rs:
        trv_std.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

 



    Frame2 = LabelFrame(stud_base,bg="white")
    Frame2.grid(row=23,column=0,padx=20,pady = 10)

    global searchstd_entry
    searchstd_entry = Entry(Frame2, width = 40)
    searchstd_entry.grid(row=23,column=0, padx=2)


    search = Button(Frame2, text="Search",command=search_std)
    search.grid(row=23,column=1,ipadx=5,ipady=5,padx = 2)

    delete = Button(Frame2, text="Delete record",command=delete_std)
    delete.grid(row=23,column=2, pady = 10, padx = 10,ipadx=5,ipady=5)
    
    global add_frame

    add_frame = LabelFrame(stud_base, text = "Add New Student", bg="white")
    add_frame.grid(row=24,column=0, pady=30,ipadx=10,ipady=10)
    

    fname_label = Label(add_frame, text = "Enter first name: ")
    lname_label = Label(add_frame, text = "Enter last name: ")
    uname_label = Label(add_frame, text = "Enter username: ")
    pass_label = Label(add_frame, text = "Enter password:")
    email_label = Label(add_frame, text = "Enter email address:")
    ccp_label = Label(add_frame, text = "Enter credit points:")

    global fname_entry
    global lname_entry
    global uname_entry
    global pass_entry
    global email_entry
    global ccp_entry

    fname_entry = Entry(add_frame, width = 40)
    lname_entry = Entry(add_frame, width = 40)
    uname_entry = Entry(add_frame, width = 40)
    pass_entry = Entry(add_frame, width = 40)
    email_entry  = Entry(add_frame, width = 40)
    ccp_entry = Entry(add_frame, width = 40)
    ccp_entry.insert(0, "0")
    
    global update
    update = Button(add_frame, text = "Update record", command = update_func)
    update.grid(row=88,column=8,padx=10)

    

    sbutton = Button(add_frame, text = "Add Student", command = sdcheck_func)
    sbutton.grid(row = 88, column =12)


    fname_label.grid(row = 82, column = 6)
    lname_label.grid(row = 83, column = 6)
    uname_label.grid(row = 84, column = 6)
    pass_label.grid(row = 82, column = 10)
    email_label.grid(row = 83, column = 10)
    ccp_label.grid(row = 84, column = 10)

    fname_entry.grid(row = 82, column = 8)
    lname_entry.grid(row = 83, column = 8)
    uname_entry.grid(row = 84, column = 8)
    pass_entry.grid(row = 82, column = 12)
    email_entry.grid(row = 83 ,column = 12)
    ccp_entry.grid(row = 84, column = 12)





#SEARCH LOST ITEMS
def searchil():
    s = searchl_entry.get()
    x = s[0]+"%"

    mycur.execute("SELECT * FROM lost WHERE item LIKE '"+x+"'")
    rs=mycur.fetchall()

    for j in trv.get_children(): #clearing the treeview
        trv.delete(j)
    for i in rs: #Adding filtered records back into treeview
        trv.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))

    







#DELETE LOST ITEMS
def deletei1():
    try:
        x = trv.selection()[0]
        trv.delete(x) 
        mycur.execute("delete from lost where item_id={}".format(x))
        mycon.commit()
        messagebox.showinfo('Succes!','Record has been deleted succesfully!')
        global admin
        admin.deiconify()
    except:
        messagebox.showwarning('ERROR!','Please select what you want to delete!')
        admin.deiconify()




    

#LOST DATABASE FRAME
def ldb_func():
    global ldb
    global bg
    bg=bg.resize((1400,800))
    bg_admin=ImageTk.PhotoImage(bg)
    
    ldb = Label(admin, image=bg_admin)
    ldb.image=bg_admin
    ldb.grid(row=2, column = 0, sticky="nsew", ipady=200)
    global ldb_frame
    ldb_frame = LabelFrame(ldb, bg="white")
    ldb_frame.grid(row=3,column=0,sticky="ew",ipadx=530)

    global mycur
    mycur=mycon.cursor()#temp repository
    mycur.execute("select * from Lost")
    rs=mycur.fetchall()
    global rcount
    rcount=0
    for r in rs:
        rcount=rcount+1



    losttrv_scroll = Scrollbar(ldb_frame)
    losttrv_scroll.pack(side=RIGHT, fill=Y)
    global trv
    trv=ttk.Treeview(ldb_frame, selectmode="browse",yscrollcommand=losttrv_scroll.set)
    trv.pack(expand="TRUE",fill="x",anchor="n")
    losttrv_scroll.config(command=trv.yview)
    
    trv["columns"]=("1","2","3","4","5","6")
    trv["show"]="headings"
    trv.column("1",width=30,anchor="c")
    trv.column("2",width=50,anchor="c")
    trv.column("3",width=50,anchor="c")
    trv.column("4",width=50,anchor="c")
    trv.column("5",width=50,anchor="c")
    trv.column("6",width=50,anchor="c")

    trv.heading("1",text="Item_id")
    trv.heading("2",text="Category")
    trv.heading("3",text="Item")
    trv.heading("4",text="Description")
    trv.heading("5",text="Last Known Location")
    trv.heading("6",text="Contact Info")
  

    for i in rs:
        trv.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))


    Frame2 = LabelFrame(ldb,text="Search and Delete",bg="white")
    Frame2.grid(row=23,column=0,pady=50)

    global searchl_entry
    searchl_entry = Entry(Frame2, width = 40)
    searchl_entry.grid(row=23,column=0, padx=2)


    search = Button(Frame2, text="Search",command=searchil)
    search.grid(row=23,column=1,ipadx=5,ipady=5,padx = 2)

    delete = Button(Frame2, text="Delete record",command=deletei1)
    delete.grid(row=23,column=2, pady = 10, padx = 10,ipadx=5,ipady=5)


    
#SEARCH FOUND ITEMS
def searchif():
    s = searchf_entry.get()
    x = s[0]+"%"

    mycurf.execute("SELECT * FROM found WHERE item LIKE '"+x+"'")
    rs=mycurf.fetchall()

    for j in trv_found.get_children(): #clearing the treeview
        trv_found.delete(j)
    for i in rs: #Adding filtered records back into treeview
        trv_found.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))


#DELETE FOUND ITEMS --- ADMIN WINDOW
def deletei2():
    
    try:
        x = trv_found.selection()[0]
        trv_found.delete(x) 
        mycurf.execute("delete from found where item_id={}".format(x))
        mycon.commit()
        messagebox.showinfo('Succes!','Record has been deleted succesfully!')
        global admin
        admin.deiconify()
    except:
        messagebox.showwarning('ERROR','Please select what you want to delete!')
        
        admin.deiconify()

        



#FOUND DATABASE FRAME --- ADMIN WINDOW
def fdb_func():
    global fdb
    global bg
    bg=bg.resize((1400,800))
    bg_ad=ImageTk.PhotoImage(bg)
    fdb = Label(admin, image=bg_ad)
    fdb.image=bg_ad
    fdb.grid(row=2, column = 0, sticky="nsew", ipady=200)
    global fdb_frame
    fdb_frame = LabelFrame(fdb, bg="white")
    fdb_frame.grid(row=3,column=0,sticky="ew",ipadx=503)

    global mycurf
    mycurf=mycon.cursor()#temp repository
    mycurf.execute("select * from Found")
    rs=mycurf.fetchall()
    global rcountf
    rcountf=0
    for r in rs:
        rcountf=rcountf+1
    

    foundtrv_scroll = Scrollbar(fdb_frame)
    foundtrv_scroll.pack(side=RIGHT, fill=Y)
    global trv_found
    trv_found=ttk.Treeview(fdb_frame, selectmode="browse",yscrollcommand=foundtrv_scroll.set)
    trv_found.pack(expand="TRUE",fill="x",anchor="n")
    foundtrv_scroll.config(command=trv_found.yview)
    
    trv_found["columns"]=("1","2","3","4","5","6",'7')
    trv_found["show"]="headings"
    trv_found.column("1",width=30,anchor="c")
    trv_found.column("2",width=50,anchor="c")
    trv_found.column("3",width=50,anchor="c")
    trv_found.column("4",width=50,anchor="c")
    trv_found.column("5",width=50,anchor="c")
    trv_found.column("6",width=50,anchor="c")
    trv_found.column("7",width=50,anchor="c")
    
    trv_found.heading("1",text="Item_id")
    trv_found.heading("2",text="Category")
    trv_found.heading("3",text="Item")
    trv_found.heading("4",text="Description")
    trv_found.heading("5",text="Last Known Location")
    trv_found.heading("6",text="Contact Info")
    trv_found.heading("7",text="Picture")

    for i in rs:
        trv_found.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
 

    Frame2 = LabelFrame(fdb,text = "Search and Delete",bg="white")
    Frame2.grid(row=23,column=0,pady=50)

    global searchf_entry
    searchf_entry = Entry(Frame2, width = 40)
    searchf_entry.grid(row=23,column=0, padx=2)


    search = Button(Frame2, text="Search",command=searchif)
    search.grid(row=23,column=1,ipadx=5,ipady=5,padx = 2)

    delete = Button(Frame2, text="Delete record",command=deletei2)
    delete.grid(row=23,column=2, pady = 10, padx = 10,ipadx=5,ipady=5)

#SEARCHING THE CREDIT POINTS TABLE
def search_ccp():
    s = sname_entry.get()
    try:
        x = s[0]+"%"
    except:
        messagebox.showwarning('Error!','Please type to Search!')
        admin.deiconify()
        s=sname_entry.get()
    x=s[0]+'%'
    mycur_ccp.execute("SELECT * FROM std WHERE fname LIKE '"+x+"'")
    rs=mycur_ccp.fetchall()



    
    for j in ccp_trv.get_children(): #clearing the treeview
        ccp_trv.delete(j)
    for i in rs: #Adding filtered records back into treeview
        ccp_trv.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        
        
    
    

#UPDATE CCPOINTS --- ADMIN FUNCTION
def update_ccpoints():
    myc=mycon.cursor()
    
    if option.get()=='Stationary':
        
        
        #Grab record no.
        selected=ccp_trv.focus()
        #grab record values
        values = ccp_trv.item(selected,'values')
        try:
            global rccps
            
            rccps = ccp_trv.selection()[0]
            fn = values[1]
            ln = values[2]
            un = values[3]
            ps = values[4]
            s = values[5]
            e = values[6]
            try:
                s = int(s) + 10
            except:
                s=10
            #save new data
            ccp_trv.item(selected, text="",values=(rccps,fn,ln,un,ps,s,e))
            
            #Saving the data in sql
            mycur_ccp.execute("UPDATE std SET ccp=%s WHERE idno=%s",
                              (s, rccps))
            mycon.commit()

        except:
            messagebox.showwarning('ERROR!','Please select the Student whose Credit score has to be changed!')
            admin.deiconify()

        
       
        
        
        
    if option.get()=='Valueables':
        #Grab record no.
        selected=ccp_trv.focus()
        #grab record values
        values = ccp_trv.item(selected,'values')
        try:
            global rccpv
            rccpv = ccp_trv.selection()[0]
            fn = values[1]
            ln = values[2]
            un = values[3]
            ps = values[4]
            v = values[5]
            e = values[6]
            try :
                v=int(v)+50
            except:
                v=50
        
        
        #save new data
            ccp_trv.item(selected, text="",values=(rccpv,fn,ln,un,ps,v,e))
            
            #Saving the data in sql
            mycur_ccp.execute("UPDATE std SET ccp=%s WHERE idno=%s",
                              (v, rccpv))
            mycon.commit()
        except:
            messagebox.showwarning('ERROR!','Please select the Student whose Credit scoore has to be changed!')
            admin.deiconify()

        
       
    if option.get()=='Other':
        #Grab record no.
        selected=ccp_trv.focus()
        try:
            
            #grab record values
            values = ccp_trv.item(selected,'values')
            global rccp
            rccp = ccp_trv.selection()[0]
            fn = values[1]
            ln = values[2]
            un = values[3]
            ps = values[4]
            o = values[5]
            e = values[6]
            try:
                o = int(o) + 20
            except:
                o=20

        
        
            #save new data
            ccp_trv.item(selected, text="",values=(rccp,fn,ln,un,ps,o,e))
            
            #Saving the data in sql
            mycur_ccp.execute("UPDATE std SET ccp=%s WHERE idno=%s",
                              (o, rccp))
            mycon.commit()
        except:
            messagebox.showwarning('ERROR!','Please select the Student whose Credit scoore has to be changed!')
            admin.deiconify()

       



#CREDIT POINTS - VIEW AND UPDATE --- ADMIN WINDOW
def ccpoints_func():
    global bg
    bg=bg.resize((1400,600))
    bg_admi=ImageTk.PhotoImage(bg)
    ccpf=Label(admin,image=bg_admi)
    ccpf.image=bg_admi
    ccpf.grid(row=2,column=0,ipady=250,sticky='nsew')
    global ccpoints_frame
    ccpoints_frame = LabelFrame(ccpf, text = "Update Credit Points", bg="DeepSkyBlue4",fg='white',font=(7))
    ccpoints_frame.grid(row=2, column = 0, sticky="nsew")
    global ccpoints_db
    global cptree_frame
    cptree_frame = LabelFrame(ccpoints_frame)
    cptree_frame.grid(row=4,column=0,sticky="ew",ipadx=503)

    
    global mycur_ccp
    mycur_ccp=mycon.cursor()#temp repository
    mycur_ccp.execute("select * from std")
    rs=mycur_ccp.fetchall()
    for i in rs:
        if i[5]>=1000:
            global send
            send=i[6]
            ccpem()
            code=i[0]
            mycur_ccp.execute('Update std set ccp=0 where idno={}'.format(code))
            break
    global rcountf
    rcountf=0
    for r in rs:
        rcountf=rcountf+1
    

    ccptrv_scroll = Scrollbar(cptree_frame)
    ccptrv_scroll.pack(side=RIGHT, fill=Y)
    global ccp_trv
    ccp_trv=ttk.Treeview(cptree_frame, selectmode="browse",yscrollcommand=ccptrv_scroll.set)
    ccp_trv.pack(expand="TRUE",fill="x",anchor="n")
    ccptrv_scroll.config(command=ccp_trv.yview)
    
    ccp_trv["columns"]=("1","2","3","4","5","6","7")
    ccp_trv["show"]="headings"
    ccp_trv.column("1",width=20,anchor="c")
    ccp_trv.column("2",width=50,anchor="c")
    ccp_trv.column("3",width=50,anchor="c")
    ccp_trv.column("4",width=50,anchor="c")
    ccp_trv.column("5",width=50,anchor="c")
    ccp_trv.column("6",width=50,anchor="c")
    ccp_trv.column("7",width=50,anchor="c")
    ccp_trv.heading("1",text="ID")
    ccp_trv.heading("2",text="First Name")
    ccp_trv.heading("3",text="Last Name")
    ccp_trv.heading("4",text="Username")
    ccp_trv.heading("5",text="Password")
    ccp_trv.heading("6",text="Credit Score")
    ccp_trv.heading("7",text="Contact Info")

    for i in rs:
        ccp_trv.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))




    update_ccpoints_frame = LabelFrame(ccpf, bg="white")
    update_ccpoints_frame.grid(row=23,column=0)



    category = Label(update_ccpoints_frame, text = "Select category of item:")
    category.grid(row = 52, column = 10)
    global option
    option = StringVar()
    options = OptionMenu(update_ccpoints_frame, option, "Stationary", "Valueables", "Other")
    options.grid(row = 52, column = 14)
    sname = Label(update_ccpoints_frame, text = "Enter name of student:")
    sname.grid(row = 54, column = 10)
    global sname_entry 
    sname_entry = Entry(update_ccpoints_frame, width = 50)
    sname_entry.grid(row = 54, column = 14)
    name_search = Button(update_ccpoints_frame, text = "SEARCH", command=search_ccp)
    name_search.grid(row=56, column=14)

    ud_ccp = Button(update_ccpoints_frame, text = "UPDATE CREDIT SCORE", command=update_ccpoints)
    ud_ccp.grid(row = 56, column=16)




#ADMIN - Check
def ADMIN_func():
    global uframe
    if no==1:
        uframe.forget()
#default entry box content
    def handle_focus_in(_):
        userA.delete(0, tk.END)
        userA.config(fg='black')

    def handle_focus_out(_):
        if userA.get()=="":
            userA.delete(0, tk.END)
            userA.config(fg='grey')
        
            userA.insert(0, "@Admin")

    def handle_enter(txt):
        print(userA.get())
        handle_focus_out('dummy')
    
    
    global aframe
    aframe = LabelFrame(main_frame, bg="DeepSkyBlue4", borderwidth=0)
    aframe.pack()
    userA = Entry(aframe, width="28",font=("Arial",16),fg="grey")
    userA.pack(padx=8,pady=20)
    userA.insert(0, "@Admin")
#default entry box content function binding 
    userA.bind("<FocusIn>", handle_focus_in)
    userA.bind("<FocusOut>", handle_focus_out)
    userA.bind("<Return>", handle_enter)

    def handle_focus_in_pword(_):
        pwordA.delete(0, tk.END)
        pwordA.config(fg='black')

    def handle_focus_out_pword(_):
        if pwordA.get()=="":
            pwordA.delete(0, tk.END)
            pwordA.config(fg='grey')
        
            pwordA.insert(0, "Password")

    def handle_enter_pword(txt):
        print(pwordA.get())
        handle_focus_out('dummy')

    pwordA = Entry(aframe, width="28",font=("Arial",16),fg="grey",show='*')
    pwordA.pack(side="top")
    pwordA.insert(0, "Password")

    pwordA.bind("<FocusIn>", handle_focus_in_pword)
    pwordA.bind("<FocusOut>", handle_focus_out_pword)
    pwordA.bind("<Return>", handle_enter_pword)



    def Enter():
        if userA.get() == "Admin1" and pwordA.get() == "12345":
            global admin
            admin = Toplevel()
            admin.geometry("1345x975")
            title = LabelFrame(admin, bg = "DeepSkyBlue4", relief = "raised")
            title.grid(row = 0, column = 0, sticky="ew")
            admin.grid_columnconfigure(0, weight=1)

            foundit = Label(title, text = "FOUNDIT!", font=("Helvetica, 34"), bg = "DeepSkyBlue4", fg = "white")
            foundit.grid(row = 1, column = 7, padx=60, pady=25)
            
            
            #logout and menu
            logout = Button(title, text = "LOGOUT", font=("18"),relief="raised", bd="2", command=root.destroy)
            logout.grid(row=1, column = 13, padx=800, pady=25)

            #Adding the menu bar
            menu = LabelFrame(admin, bg="gray100")
            menu.grid(row = 1, column = 0, sticky="ew")
            
            student_menu = Button(menu, text = "STUDENT", bg = "DeepSkyBlue4", fg="white", font=("18"),relief="raised", bd="2", command=sdb_func)
            student_menu.grid(row = 1, column=0, sticky = "W")
            lost_menu = Button(menu, text = "LOST", bg = "DeepSkyBlue4", fg="white", font=("18"),relief="raised", bd="2", command=ldb_func)
            lost_menu.grid(row = 1, column=1, sticky = "ew")
            found_menu = Button(menu, text = "FOUND", bg = "DeepSkyBlue4", fg="white", font=("18"),relief="raised", bd="2", command=fdb_func)
            found_menu.grid(row = 1, column=2, sticky = "ew")
            CCpoints_menu = Button(menu, text = "CREDIT POINTS", bg = "DeepSkyBlue4", fg="white", font=("18"),relief="raised", bd="2", command=ccpoints_func)
            CCpoints_menu.grid(row = 1, column=3, sticky = "W")

            #student menu is default menu
            sdb_func()








            
            
            
        else:
            messagebox.showwarning("Error!", "Invalid credentials! Please try again!")
        

    go = Button(aframe, text = "Log In", font="14", bg="white",padx=100,pady=7, relief="raised",command = Enter)
    go.pack(pady=10)

    uswitch = Button(aframe, text="Login as User", bg="white", font=14, command=USER_func)
    uswitch.pack(pady=5)





#SEARCH FUNCTION -- USER WINDOW
def search_func():
    s = search_found.get()
    x = s[0]+"%"

    mycurf.execute("SELECT * FROM Found WHERE item LIKE '"+x+"'")
    rs=mycurf.fetchall()



    
    for j in trv_found.get_children(): #clearing the treeview
        trv_found.delete(j)
    for i in rs: #Adding filtered records back into treeview
        trv_found.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))




#SEARCH ITEM(FOUND) --- USER WINDOW
def searchf_func():
    s = search_lost.get()
    x = s[0]+"%"

    mycur.execute("SELECT * FROM Lost WHERE item LIKE '"+x+"'")
    rs=mycur.fetchall()



    
    for j in trv.get_children(): #clearing the treeview
        trv.delete(j)
    for i in rs: #Adding filtered records back into treeview
        trv.insert("","end",iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))




#memory address
def picadd():
    global report_frame
    top.withdraw()
    global ri
    ri.destroy()
    pic_add=Label(report_frame,bg='DeepSkyBlue4',text='',fg='white')
    pic_add.configure(text=filename)
    pic_add.grid(row=89,column=8)
    top.deiconify()




#FOUND AN ITEM --- USER WINDOW
def found_user():
    global mycur
    mycur=mycon.cursor()#temp repository
    mycur.execute("select * from lost")
    rs=mycur.fetchall()
    global rcount
    rcount=0
    for r in rs:
        rcount=rcount+1
    
    global foundframe
    global fdb_frame

    global bg
    bg=bg.resize((1400,800))
    bg_root=ImageTk.PhotoImage(bg)
    
    
    foundframe=Label(top, image=bg_root)
    foundframe.image=bg_root
    foundframe.place(x=0,y=0,relwidth=1,relheight=1)


    title = LabelFrame(foundframe, bg = "DeepSkyBlue4", relief = "raised")
    title.grid(row=1,column=0,sticky='ew',ipadx=510)

    foundit = Label(title, text = "FOUNDIT!", font=("Helvetica, 34"), bg = "DeepSkyBlue4", fg = "white")
    foundit.pack()

    fdb_frame = LabelFrame(foundframe, text="List Of Currently Lost Items",bg="DeepSkyBlue4",fg='white',font=10)
    fdb_frame.grid(row=3,column=0,sticky="ew",ipadx=510)

    losttrv_scroll = Scrollbar(fdb_frame)
    losttrv_scroll.pack(side=RIGHT, fill=Y)
    global trv
    trv=ttk.Treeview(fdb_frame, selectmode="browse",yscrollcommand=losttrv_scroll.set)
    trv.pack(expand="TRUE",fill="x",anchor="n")
    losttrv_scroll.config(command=trv.yview)
    
    trv["columns"]=("1","2","3","4","5","6")
    trv["show"]="headings"
    trv.column("1",width=20,anchor="c")
    trv.column("2",width=48,anchor="c")
    trv.column("3",width=48,anchor="c")
    trv.column("4",width=48,anchor="c")
    trv.column("5",width=48,anchor="c")
    trv.column("6",width=48,anchor="c")
    
    trv.heading("1",text="Item_id")
    trv.heading("2",text="Category")
    trv.heading("3",text="Item")
    trv.heading("4",text="Description")
    trv.heading("5",text="Last Known Location")
    trv.heading("6",text="Contact Info")
    

    trv.bind('<<TreeviewSelect>>',detailsl)
        

    global report_frame
    report_frame = LabelFrame(foundframe, text = "Report an item you found here!",bg='DeepSkyBlue4', fg='white', padx=10,pady=10,font=(10))
    report_frame.grid(row=23,column=0,pady=5 )
    search_frame = LabelFrame(foundframe, text = "Search for your item here!", padx = 10, pady=10,bg="DeepSkyBlue4",fg='white',font=(10))
    search_frame.grid(row=20,column=0,pady=5)
            
    global search_lost
    search_lost = Entry(search_frame, width = 50)
    search_lost.grid(row = 52, column = 11)


    Label9 = Label(report_frame,bg='DeepSkyBlue4',fg='white', text = "Select category of the item:",font=10)
    Label9.grid(row = 82, column = 6)
    global missing
    missing = StringVar()
    options9 = OptionMenu(report_frame, missing, "Stationary", "Valueables", "Other")
    options9.grid(row = 82, column = 8)

    
    name_label = Label(report_frame,bg='DeepSkyBlue4', fg='white',text = "Enter the name of the item:")#,font=10)
    des_label = Label(report_frame,bg='DeepSkyBlue4', fg='white',text = "Enter a description of the item:")#,font=10)
    loc_label = Label(report_frame,bg='DeepSkyBlue4', fg='white',text = "Enter the location of the item where you found it:")#,font=10)
    email_label = Label(report_frame,bg='DeepSkyBlue4', fg='white',text = "Enter your email address:")#,font=10)
    pic_label=Label(report_frame,bg='DeepSkyBlue4',fg='white',text="Insert an Image of the Item:")#,font=10)

    
    global name_entry
    global des_entry
    global loc_entry
    global email_entry
    global pic_entry
    global filename

    
    name_entry = Entry(report_frame, width = 45)
    des_entry = Entry(report_frame, width = 45)
    loc_entry = Entry(report_frame, width = 45)
    email_entry = Entry(report_frame, width = 45)


    pic_entry=Button(report_frame,text="BROWSE",command=img)
    top.deiconify()
    
    

           

    Search = Button(search_frame, text = "SEARCH", command = searchf_func)
    Report = Button(report_frame, text = "REPORT", command = reportf_func)
    


    Search.grid(row = 52, column = 14)
    Report.grid(row = 88, column =15)
   
    
    name_label.grid(row = 83, column = 6)
    des_label.grid(row = 84, column = 6)
    loc_label.grid(row = 85, column = 6)
    email_label.grid(row = 86, column =6)
    pic_label.grid(row=88,column=6)
    
    name_entry.grid(row = 83, column = 8)
    des_entry.grid(row = 84, column = 8)
    loc_entry.grid(row = 85, column = 8)
    email_entry.grid(row = 86,column = 8)
    pic_entry.grid(row=88,column=8)
##    pic_add.grid(row=89,column=8) 

#REPORT ITEM(FOUND) --- USER WINDOW
def reportf_func():
    mycur_report_found=mycon.cursor()
    import random
    r = random.randint(111111,200000)

    
    global rcountf
    
    sql = "INSERT INTO Found (item_id,category,item,description,found_location,email,pic)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    global filename
##    print(filename)
    val = (r,missing.get(),name_entry.get(),des_entry.get(),loc_entry.get(),email_entry.get(),filename)
    if missing.get()!='' and name_entry.get()!='' and des_entry.get()!='' and loc_entry.get()!='' and email_entry.get()!='' and filename!='':
        global report_frame
        filename=val[5]
        

        mycur_report_found.execute(sql,val)
        mycon.commit()
        

        messagebox.showinfo("Success","Report successfully made!")
        top.deiconify()
        mycon.commit()
    else:
        messagebox.showwarning('ERROR!','Do not leave any Information blank!')
        top.deiconify()
    

#LOST AN ITEM --- USER WINDOW
def lost_user():
    
    global mycurf
    mycurf=mycon.cursor()#temp repository
    mycurf.execute("select * from found")
    rs=mycurf.fetchall()
    global rcountf
    rcountf=0
    for r in rs:
        rcountf=rcountf+1
    global lostframe
    global ldb_frame
    global b
    b=Image.open(r'C:/Users/keeru/Documents/JC Project 8/bg6.png')
    b=b.resize((1500,800))
    bg_lost=ImageTk.PhotoImage(b)
    lostframe=Label(top, image=bg_lost)
    lostframe.image=bg_lost
    lostframe.place(x=0,y=0,relwidth=1,relheight=1)
    title = LabelFrame(lostframe, bg = "DeepSkyBlue4", relief = "raised")
    title.grid(row=1,column=0,sticky='ew')

    foundit = Label(title, text = "FOUNDIT!", font=("Helvetica, 34"), bg = "DeepSkyBlue4", fg = "white")
    foundit.pack()
    
    ldb_frame = LabelFrame(lostframe, text="List Of Currently Found Items",bg="DeepSkyBlue4",fg='white',font=15)
    ldb_frame.grid(row=3,column=0,sticky="ew",ipadx=490)

    foundtrv_scroll = Scrollbar(ldb_frame)
    foundtrv_scroll.pack(side=RIGHT, fill=Y)
    global trv_found
    trv_found=ttk.Treeview(ldb_frame, selectmode="browse",yscrollcommand=foundtrv_scroll.set)
    trv_found.pack(expand="TRUE",fill="x",anchor="n")
    foundtrv_scroll.config(command=trv_found.yview)
    
    trv_found["columns"]=("1","2","3","4","5","6",'7')
    trv_found["show"]="headings"
    trv_found.column("1",width=10,anchor="c")
    trv_found.column("2",width=45,anchor="c")
    trv_found.column("3",width=45,anchor="c")
    trv_found.column("4",width=45,anchor="c")
    trv_found.column("5",width=45,anchor="c")
    trv_found.column("6",width=45,anchor="c")
    trv_found.column("7",width=55,anchor="c")
    
    
    trv_found.heading("1",text="Item_id")
    trv_found.heading("2",text="Category")
    trv_found.heading("3",text="Item")
    trv_found.heading("4",text="Description")
    trv_found.heading("5",text="Found Location")
    trv_found.heading("6",text="Contact Info")
    trv_found.heading("7",text="Picture")
    
    

    trv_found.bind('<<TreeviewSelect>>',detailsf)



    


    report_frame = LabelFrame(lostframe, text = "Report an item you lost here!", padx=10, bg="DeepSkyBlue4",fg='white',font=15)
    report_frame.grid(row=23,column=0,pady=10)
    search_frame = LabelFrame(lostframe, text = "Search for your item here!", padx = 10, bg="DeepSkyBlue4" ,font=15,fg='white')
    search_frame.grid(row=20,column=0,pady=5)
            

    global search_found
    search_found = Entry(search_frame, width = 50)
    search_found.grid(row = 52, column = 11)
    


    Label9 = Label(report_frame, bg='DeepSkyBlue4',fg='white',text = "Select category of the item:",font=10)
    Label9.grid(row = 82, column = 6)
    global missing
    missing = StringVar()
    options9 = OptionMenu(report_frame, missing, "Stationary", "Valueables", "Other")
    options9.grid(row = 82, column = 8)

    
    name_label = Label(report_frame, bg='DeepSkyBlue4',fg='white',text = "Enter the name of the item:",font=10)
    des_label = Label(report_frame, bg='DeepSkyBlue4',fg='white',text = "Enter a description of the item:",font=10)
    loc_label = Label(report_frame,bg='DeepSkyBlue4', fg='white',text = "Enter the location of the item when you last saw it:",font=10)
    email_label = Label(report_frame,bg='DeepSkyBlue4', fg='white',text = "Enter your email Address:",font=10)
    

    
    global name_entry
    global des_entry
    global loc_entry
    global email_entry
    

    
    name_entry = Entry(report_frame, width = 45)
    des_entry = Entry(report_frame, width = 45)
    loc_entry = Entry(report_frame, width = 45)
    email_entry = Entry(report_frame, width = 45)
    
    

            
    Search = Button(search_frame, text = "SEARCH", command = search_func)
    Report = Button(report_frame, text = "REPORT", command = report_func)
    


    Search.grid(row = 52, column = 14)
    Report.grid(row = 88, column =14)
   
    
    name_label.grid(row = 83, column = 6)
    des_label.grid(row = 84, column = 6)
    loc_label.grid(row = 85, column = 6)
    email_label.grid(row = 86, column =6)
    

    
    name_entry.grid(row = 83, column = 8)
    des_entry.grid(row = 84, column = 8)
    loc_entry.grid(row = 85, column = 8)
    email_entry.grid(row = 86,column = 8)
   

            


#REPORT FUNCTION -- LOST USER WINDOW
def report_func():
    mycur_report_lost=mycon.cursor()
    import random
    r = random.randint(111111,200000)
    global rcount
    global trv
    
    sql = "INSERT INTO Lost (item_id,category,item,description,last_known_location,email)VALUES(%s,%s,%s,%s,%s,%s)"
    val = (r,missing.get(),name_entry.get(),des_entry.get(),loc_entry.get(),email_entry.get())
    if missing.get()!='' and name_entry.get()!='' and des_entry.get()!='' and loc_entry.get()!='' and email_entry.get()!='':
        mycur_report_lost.execute(sql,val)
        mycon.commit()
    

        messagebox.showinfo("Success","Report successfully made!")
        top.deiconify()    
    else:
         messagebox.showwarning('ERROR!','Do not leave any Information blank!')
         top.deiconify()

    

def error():
    
    #Lost menu is default menu
    homepage()



#USER - Check
def USER_func():
    global no
    global aframe
    aframe.forget()

    global main_frame
    main_frame.place(x=490,y=150)
    global uframe
    uframe = LabelFrame(main_frame, bg="DeepSkyBlue4",borderwidth=0)
    uframe.pack()
#default grey text entry box for UserB
    def handle_focus_in_userB(_):
        userB.delete(0, tk.END)
        userB.config(fg='black')

    def handle_focus_out_userB(_):
        if userB.get()=="":
            userB.delete(0, tk.END)
            userB.config(fg='grey')
        
            userB.insert(0, "@User")

    def handle_enter_userB(txt):
        print(userB.get())
        handle_focus_out('dummy')

    userB = Entry(uframe, width="28",font=("Arial",16),fg="grey")
    userB.pack(padx=8,pady=20)
    userB.insert(0, "@Username")

#Default greyed out entry box content binding
    userB.bind("<FocusIn>", handle_focus_in_userB)
    userB.bind("<FocusOut>", handle_focus_out_userB)
    userB.bind("<Return>", handle_enter_userB)
    
#default grey text entry box for pwordB
    def handle_focus_in_pwordB(_):
        pwordB.delete(0, tk.END)
        pwordB.config(fg='black')

    def handle_focus_out_pwordB(_):
        if pwordB.get()=="":
            pwordB.delete(0, tk.END)
            pwordB.config(fg='grey')
        
            pwordB.insert(0, "Password")

    def handle_enter_pwordB(txt):
        print(pwordB.get())
        handle_focus_out('dummy')

    pwordB = Entry(uframe, width="28",font=("Arial",16),fg="grey",show='*')
    pwordB.pack(side="top")
    pwordB.insert(0, "Password")

#Default greyed out entry box content binding
    pwordB.bind("<FocusIn>", handle_focus_in_pwordB)
    pwordB.bind("<FocusOut>", handle_focus_out_pwordB)
    pwordB.bind("<Return>", handle_enter_pwordB)



    def Enter1():
        global cur
        cur=mycon.cursor()
        stmt='select * from std'
        cur.execute(stmt)
        std=cur.fetchall()
        c=0
        
        global u
        u=userB.get()
        for i in std:
            if i[3]==userB.get() and i[4]==pwordB.get():
                c=1
                
                homepage()
                
    

    


        
        if c==0:
            messagebox.showwarning("Error!", "Invalid credentials! Please try again!")

    go = Button(uframe, text = "Log In", font="14", bg="white",padx=100,pady=7, relief="raised",command = Enter1)
    go.pack(pady=10)

    bframe = LabelFrame(uframe, bg="DeepSkyBlue4", borderwidth=0)
    bframe.pack(pady=15)

    Button3=Button(bframe,text='Forgot Pasword?',font=14, bg="white",relief="raised",command=lambda:forgot())
    Button3.grid(row=11, column=2, ipady=5)

    signup_butt = Button(bframe, text = "Sign up!", font=14, bg="white", relief="raised", command=lambda:signup_func())
    signup_butt.grid(row = 11, column = 3, padx=5,ipady=5, sticky="e")

    aswitch = Button(uframe, text = "Login as Admin", bg="white", font="14",command=lambda:ADMIN_func())
    aswitch.pack()

    global no
    no = 1




#SIGN UP FUNCTION
def signup_func():
    global signup
    signup = Toplevel()
    signup.title('SIGN-UP!')
    signup.geometry('550x350')
    signup.configure(background='DeepSkyBlue4')
    fname_label = Label(signup, text = "Enter your First name: ",bg='DeepSkyBlue4',fg='white')
    lname_label=Label(signup,text='Enter your Last name:',bg='DeepSkyBlue4',fg='white')
    uname_label = Label(signup, text = "Enter username: ",bg='DeepSkyBlue4',fg='white')
    pass_label = Label(signup, text = "Enter password: ",bg='DeepSkyBlue4',fg='white')
    cpass_label = Label(signup, text = "confirm password: ",bg='DeepSkyBlue4',fg='white')
    email_label = Label(signup, text = "Enter email address:",bg='DeepSkyBlue4',fg='white')

    global sfname_entry
    global slname_entry
    global suname_entry
    global spass_entry
    global scpass_entry
    global semail_entry 

    sfname_entry = Entry(signup, width = 50)
    slname_entry = Entry(signup, width = 50)
    suname_entry = Entry(signup, width = 50)
    spass_entry = Entry(signup, width = 50)
    scpass_entry = Entry(signup, width = 50)
    semail_entry = Entry(signup, width = 50)

    sbutton = Button(signup, text = "Sign up!", command = scheck_func)
    sbutton.grid(row = 90, column =8)
    
    fname_label.grid(row = 82, column = 6,ipadx=10,ipady=10)
    lname_label.grid(row = 83, column = 6,ipadx=10,ipady=10)
    uname_label.grid(row = 84, column = 6,ipadx=10,ipady=10)
    pass_label.grid(row = 85, column = 6,ipadx=10,ipady=10)
    cpass_label.grid(row = 86, column = 6,ipadx=10,ipady=10)
    email_label.grid(row = 87, column = 6,ipadx=10,ipady=10)

    sfname_entry.grid(row = 82, column = 8)
    slname_entry.grid(row = 83, column = 8)
    suname_entry.grid(row = 84, column = 8)
    spass_entry.grid(row = 85, column = 8)
    scpass_entry.grid(row = 86, column = 8)
    semail_entry.grid(row = 87, column = 8)
    signup.resizable(False, False)
    

#SIGN UP - CHECK INFO
def scheck_func():
    
    
    global std
    s=spass_entry.get()
    sc=scpass_entry.get()
    if sc!= s:
        messagebox.showwarning("Error!", "Passwords are not matching! Please retry.")
        global signup
        signup.deiconify()
        
        
    else:
       import random
       r = random.randint(111111,200000)
       stmt='INSERT INTO STD (idno,fname,lname,uname,pass,ccp,email)VALUES(%s,%s,%s,%s,%s,0,%s) '
       global rstdcount
       vals=(r,sfname_entry.get(),slname_entry.get(),suname_entry.get(),spass_entry.get(),semail_entry.get())
       if sfname_entry.get()!='' and slname_entry.get()!='' and suname_entry.get()!='' and  spass_entry.get()!='' and semail_entry.get()!='':
           mycur.execute(stmt,vals)
           mycon.commit()
           rstdcount+=1
           messagebox.showinfo('Account Creation Successful','ACCOUNT SUCCESSFULLY CREATED!\n You can now LOG-IN with your Account.')
           signup.withdraw()
       else:
           messagebox.showwarning('ERROR!','Please do not leave any Information Blank!')
           signup.deiconify()
            

#new window----lost
def homepage():
    window=Toplevel()
    window.title("Menu")
    #window.title("FOUNDIT - The Digital Lost and Found")
    window.geometry("1000x600")
    window.resizable(width=False, height=False)

   #defining the background image
    global ph
    ph=Image.open(r'C:/Users/keeru/Documents/JC Project 8/bg6.png')
    ph=ph.resize((1000,600))
    pho=ImageTk.PhotoImage(ph)

    #create a label
    global my_label
    my_label=Label(window, image=pho)
    my_label.image=pho
    my_label.place(x=0,y=0)#,relwidth=1,relheight=1)

    #window.configure(background="Wheat")
    my_text=Label(window,text="Welcome to FOUNDIT, what are you looking for?",font=("Helvetica",30),bg = "DeepSkyBlue4", fg = "white")
    my_text.pack(pady=20)

    def open():
        global top
        top=Toplevel()
        top.title("LOST")
        top.geometry("1300x700")
        top.configure(background="DeepSkyBlue4")
        lost_user()
        top.resizable(False, False)
        b2=Button(top,text="Back",font=("Helvetica",18),padx=10,pady=10,fg="white",bg="DeepSkyBlue4",command=top.destroy)
        b2.place(x=640,y=630)

    #new window----found
    def op():
        global top
        top=Toplevel()
        top.title("FOUND")
        top.geometry("1300x700")
        top.configure(background="DeepSkyBlue4")
        found_user()
        top.resizable(False, False)
        b1=Button(top,text="Back",font=("Helvetica",18),padx=20,pady=10,fg="white",bg="DeepSkyBlue4",command=top.destroy)
        b1.place(x=650,y=620)

    #new window----View profile
    def prof():
        global top
        top=Toplevel()
        top.title("Profile")
        top.geometry("600x500")
        top.configure(background="DeepSkyBlue4")
        global u
        
        profile(u)
        top.resizable(False, False)
        b2=Button(top,text="Back",font=("Helvetica",18),padx=20,pady=10,fg="white",bg='DeepSkyBlue4',command=top.destroy)
        b2.place(x=230,y=420)



    #buttons
        
    lostbut=Button(window, text="I lost an item",font=("Helvetica",22),bg="DeepSkyBlue4",fg="alice blue",padx=20,pady=15,command=open)
    lostbut.place(relx=0.5,rely=0.2,anchor=CENTER)
    foundbut=Button(window, text="I found an item",font=("Helvetica",22),padx=20,pady=15,bg="DeepSkyBlue4",fg="alice blue",command=op)
    foundbut.place(relx=0.5,rely=0.4,anchor=CENTER)
    profilebut=Button(window, text="View profile :)",font=("Helvetica",22),padx=20,pady=15,bg="DeepSkyBlue4",fg="alice blue",command=prof)
    profilebut.place(relx=0.5,rely=0.6,anchor=CENTER)                             
    backbut=Button(window, text="back",font=("Helvetica",22),padx=30,pady=15,bg="DeepSkyBlue4",fg="alice blue",command=root.destroy)
    backbut.place(relx=0.5,rely=0.8,anchor=CENTER)

    
#mainframe, login

main_frame = LabelFrame(root,font=15, bg="DeepSkyBlue4",fg="white")
main_frame.place(x=490,y=190)

login = Label(main_frame, text = "Log In", font=("Times New Roman", 34), bg="DeepSkyBlue4", fg="white")
login.pack()

k = Label(main_frame, text="login here using your username and password.",font=14,bg="DeepSkyBlue4", fg="white")
k.pack(side="top")

ADMIN_func()
root.mainloop()



