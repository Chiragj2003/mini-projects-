from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter
import speedtest

a=0
b=0
c=0


def check():
    st = speedtest.Speedtest()
    a=st.download()
    b=st.upload()
    print("Download speed = ",a/500000,"Mbps")
    print("Uplode speed = ",b/500000,"Mbps")
    server_names = []
    st.get_servers(server_names)
    c=st.results.ping
    print(c,"ms")
    speed_test(a,b,c)

def speed_test(a,b,c):
    e=int(a/500000)
    f=int(b/500000)
    g=int(c)
    d=int ((e+f)/2)
    root = Tk()
    root.title('speed Testing')
    root.geometry('400x650')
    root.configure(bg='white')
    ####icon

    #######image_______
    download=Label(root,text='SPEED TEST ',font="arial 30 bold ",bg="red",fg='white').place(x=70,y=30)
   
    #######Label1_____________
    download2=Label(root,text='Your internet speed is ',font="arial 17 bold ",bg="white").place(x=60,y=90)
    Label(root,text=d,font="arial 110 bold",bg="white").place(x=80,y=260)
    Label(root,text='Mbps',font="arial 22 bold ",bg="white").place(x=255,y=260)
    #######Label2__________
    
    Label(root,text='Latency',font="arial 15 bold ",bg="white").place(x=50,y=430)
    Label(root,text='Uplod ',font="arial 15 bold ",bg="white").place(x=250,y=430)
    ####Label3____________
    Label(root,text='Upload  ',font="arial 12 normal ",bg="white").place(x=50,y=470)
    Label(root,text='Download ',font="arial 12 normal ",bg="white").place(x=150,y=470)
    Label(root,text='Ping ',font="arial 12 normal ",bg="white").place(x=250,y=470)
    ########Label4___________
    unloaded=Label(root,text=e,font="arial 20 bold ",bg="white")
    unloaded.place(x=50,y=500)
    loaded=Label(root,text=f,font="arial 20 bold ",bg="white")
    loaded.place(x=150,y=500)
    speed=Label(root,text=g,font="arial 20 bold ",bg="white")
    speed.place(x=250,y=500)
    #######Label5________________
    unloaded1=Label(root,text='Mbps ',font="arial 10 normal ",bg="white")
    unloaded1.place(x=83,y=511)
    loaded1=Label(root,text='Mbps',font="arial 10 normal ",bg="white")
    loaded1.place(x=183,y=511)
    speed1=Label(root,text='ms ',font="arial 10 normal ",bg="white")
    speed1.place(x=290,y=511)
    
    #button
    Button2=Button(root,text="Run Speed Test",bg='sky blue',font="arial 18 bold",bd=0,activebackground='white',cursor='cross',command=check)
    Button2.place(x=85,y=560)

    #########label7_____________________
    Label1=Label(root,text='Power by - ',font="arial 12 bold ",bg="white")
    Label1.place(x=70,y=620)
    Label2=Label(root,text='Chirag Joshi ',font="arial 13 bold ",bg="white",fg='red')
    Label2.place(x=160,y=620)
    root.mainloop()

speed_test(a,b,c)