from tkinter import *
import matplotlib.pyplot as plt
import webbrowser
def energy():
 ro = Tk()
 ro.title("Renewable Energy Source Predictor")
 canvas =  Canvas(ro,height = 700,width = 700,bg = "#263D42")
 canvas.pack()
 frame = Frame(ro,bg ="white")
 frame.place(relwidth = 0.8,relheight = 0.8,relx =0.1,rely=0.1)
 l_prime = Label(frame,text = "Renewable Energy Source Predictor",padx = 100,pady = 14 ,font = ("comicsans",20,"bold"))
 l_prime.pack()
 lll = Label(frame,text ="" ,bg = "white")
 lll.pack()
 options = [
    "Coastal Areas/Hill Tops",
    "Moderate Temp.,Light Winds,Low Humidity",
    "Nearby River",
    "High Volcanic Activity and Earthquake Activities"
 ]
 clicked = StringVar()
 drop = OptionMenu(frame,clicked,*options)
 drop.pack()

 l1 = Label(frame,text = "Energy For Tranport:",font = ("comicsans",10,"bold"))
 l1.pack()
 e1 = Entry(frame, borderwidth = 3,relief = GROOVE)
 e1.pack()
 l2 = Label(frame,text= "Energy For Production:",font = ("comicsans",10,"bold"))
 l2.pack()
 e2  = Entry(frame,borderwidth = 3,relief = GROOVE)
 e2.pack()
 l3 = Label(frame,text= "Energy For Irrigation:",font = ("comicsans",10,"bold"))
 l3.pack()
 e3  = Entry(frame ,borderwidth = 3,relief = GROOVE )
 e3.pack()
 l4 = Label(frame,text= "Energy For Storage:",font = ("comicsans",10,"bold"))
 l4.pack()
 e4  = Entry(frame,borderwidth = 3,relief = GROOVE)
 e4.pack()
 l5 = Label(frame,text= "Energy For Post Processing of food items like drying,peeling etc:",font = ("comicsans",10,"bold"))
 l5.pack()
 e5  = Entry(frame ,borderwidth = 3,relief = GROOVE) 
 e5.pack()

 def plot():
   a1 = int(e1.get())
   a2 = int(e2.get())
   a3 = int(e3.get())
   a4 = int(e4.get())
   a5 = int(e5.get())
   val = [a1,a2,a3,a4,a5]
   lables = ["Transport","Production","Irrigation","Storage","Post Production"]
   plt.axis("equal")
   plt.pie(val,labels = lables, autopct= '%0.1f%%')
   plt.show()
   op = clicked.get()

   an = Tk()
   an.title("Analyser")
   l6 = Label(an,text="Anyalyser",font = ("comicsans",30,"bold"))
   l6.pack()
   l7 = Label(an,text ='')
   l7.pack()
   l8 = Label(an,text = "")
   l8.pack()
   if (a1>a2) and (a1>a3) and (a1>a4) and (a1>a5):
        l7.config(text = "Energy Consumption Of Transportation is the greatest",font = ("comicsans",10,"bold"))
   if (a2>a1) and (a2>a3) and (a2>a4) and (a2>a5):
        l7.config(text = "Energy Consumption Of Production is the greatest",font = ("comicsans",10,"bold"))  
   if (a3>a1) and (a2>a2) and (a3>a4) and (a3>a5):
        l7.config(text = "Energy Consumption Of Irrigation is the greatest",font = ("comicsans",10,"bold"))     
   if (a4>a1) and (a4>a2) and (a4>a3) and (a4>a5):
        l7.config(text = "Energy Consumption Of Storage is the greatest",font = ("comicsans",10,"bold"))  
   if (a5>a1) and (a5>a2) and (a5>a3) and (a5>a4):
        l7.config(text = "Energy Consumption Of Post Production is the greatest",font = ("comicsans",10,"bold"))
   if (a1==a2==a3==a4==a5):
        l7.config(text = "Energy Consumption of all the Activities are the equal",font = ("comicsans",10,"bold"))
   if(op == "Coastal Areas/Hill Tops"):
        l8.config(text = "You Should Use Wind Energy")    
   if(op == "Nearby River"):
        l8.config(text = "You Should Use Small Scale Hydro-Electricity")
   if(op == "Moderate Temp.,Light Winds,Low Humidity"):
        l8.config(text = "You Should Use Solar Energy")  
   if(op == "High Volcanic Activity and Earthquake Activities"):
        l8.config(text = "You Should Use Geo-Thermal Energy")            

   an.mainloop()
 b = Button(frame,text="Submit",command = plot)
 b.pack()
 ro.mainloop()
def crop():
 def callback(url):
        webbrowser.open_new(url)
 root = Tk()
 root.title("Crop Predictor")
 canvas =  Canvas(root,height = 700,width = 700,bg = "#263D42")
 canvas.pack()
 frame = Frame(root,bg ="white")
 frame.place(relwidth = 0.8,relheight = 0.8,relx =0.1,rely=0.1)
 l_prime = Label(frame,text = "Crop Predictor",padx = 160,pady = 14 ,font = ("comicsans",30,"bold"))
 l_prime.pack()
 lll = Label(frame,text ="" ,bg = "white")
 lll.pack()
 l1 = Label(frame,text = "Soil Type:",font = ("comicsans",10,"bold"))
 l1.pack()
 e1 = Entry(frame, borderwidth = 3,relief = GROOVE)
 e1.pack()
 l2 = Label(frame,text= "Avg Temperature (in 'C):",font = ("comicsans",10,"bold"))
 l2.pack()
 e2  = Entry(frame,borderwidth = 3,relief = GROOVE)
 e2.pack()
 l3 = Label(frame,text= "Avg Rainfall (in mm):",font = ("comicsans",10,"bold"))
 l3.pack()
 e3  = Entry(frame ,borderwidth = 3,relief = GROOVE)
 e3.pack()
 lll1 = Label(frame,text ="" ,bg = "white")
 lll1.pack()
 def w():
    if e1.get() == "alluvial" and e2.get() == "21" and e3.get() == "117":
        r = Tk()
        r.geometry("300x100")

        ll = Label(r,text = "Prediction",font = ("comicsans",30,"bold"))
        ll.pack()
        t1 = Label(r,text = "Rice",font = ("comicsans",10,"bold"))
        t1.pack()
        link1 = Label(r, text="How To Grow Rice", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://ricepedia.org/rice-as-a-crop/how-is-rice-grown"))
        r.mainloop()
    if e1.get() == "black" and e2.get() == "15" and e3.get() == "500":
        r = Tk()
        r.geometry("300x100")
        ll = Label(r,text = "Prediction",font = ("comicsans",30,"bold"))
        ll.pack()
        t1 = Label(r,text = "Cotton",font = ("comicsans",10,"bold"))
        t1.pack()
        link1 = Label(r, text="How To Grow Cotton", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://www.cottonacres.com/how-to-grow-cotton/"))
        r.mainloop()
    if e1.get() == "red" and e2.get() == "27" and e3.get() == "950":
        r = Tk()
        r.title("Prediction")
        r.geometry("300x100")
        ll = Label(r,text = "Prediction",font = ("comicsans",30,"bold"))
        ll.pack()
        t1 = Label(r,text = "Ragi",font = ("comicsans",10,"bold"))
        t1.pack()
        link1 = Label(r, text="How To Grow Ragi", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://www.indiaagronet.com/indiaagronet/crop%20info/Ragi%20.htm"))
        r.mainloop()
        
 b = Button(frame,text = "Submit", command = w)
 b.pack()
 lll1 = Label(frame,text ="" ,bg = "white")
 lll1.pack()
 lll2 = Label(frame,text ="" ,bg = "white")
 lll2.pack()
 lll3 = Label(frame,text ="" ,bg = "white")
 lll3.pack()
 lll4 = Label(frame,text ="" ,bg = "white")
 lll4.pack()
 lll4 = Label(frame,text ="" ,bg = "white")
 lll4.pack()
 lll5 = Label(frame,text ="" ,bg = "white")
 lll5.pack()
 lll6 = Label(frame,text ="" ,bg = "white")
 lll6.pack()
 lll7 = Label(frame,text ="" ,bg = "white")
 lll7.pack()
 lll8 = Label(frame,text ="" ,bg = "white")
 lll8.pack()
 lll9 = Label(frame,text ="" ,bg = "white")
 lll9.pack()
 lll10 = Label(frame,text ="" ,bg = "white")
 lll10.pack()
 lll11 = Label(frame,text ="" ,bg = "white")
 lll11.pack()
 nm = Label(frame,text = "Made By :- Ronit Khanna",font = ("comicsans",10,"bold"))
 nm.pack()
   
 root.mainloop
dash = Tk()
dash.geometry("769x466")
dash.title("AgriHelp")
dash.iconbitmap("agronomy.ico")
top = Canvas(dash,width = "950",height = "50",bg= "#AFE1AF")
top.pack()
h = Label(dash,text = "AgriHelp",bg= "#50C878",font = ("comicsans",19,"bold"))
h_win = top.create_window(97,25,window = h,width = "232",height = "50")

photo  = PhotoImage(file="ah6.png")
img = Label(image = photo)
img.place(x=210,y=51)
side = Canvas(dash,width = "210",height= "600",bg = "#424242")

side.place(x=0,y=51)
b1 = Button(dash,text = "Renewable Energy Source Predictor",command = energy)
b2 = Button(dash,text = "Crop Predictor",command = crop)
b1.place(x=10,y=69)
b2.place(x=10,y=100)
dash.mainloop()
