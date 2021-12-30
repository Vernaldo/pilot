from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator=" "   
    text_input.set("")


def btnEqualsInput():
    global operator
    sumup=str(eval(operator))  
    text_input.set(sumup)
    operators=""


cal = Tk()
cal.title("ARITHMETIC & LOGIC CALCULATOR")
operator=""
text_input =StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)
#numbers from 9-6
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="9",command=lambda:btnClick(9), bg="red").grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="8",command=lambda:btnClick(8),bg="red").grid(row=1,column=1)
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="7",command=lambda:btnClick(7),bg="red").grid(row=1,column=2)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="6",command=lambda:btnClick(6),bg="red").grid(row=1,column=3)
#numbers from 5-2
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="5",command=lambda:btnClick(5),bg="red").grid(row=2,column=0)
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="4",command=lambda:btnClick(4),bg="red").grid(row=2,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="3",command=lambda:btnClick(3),bg="red").grid(row=2,column=2)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="2",command=lambda:btnClick(2),bg="red").grid(row=2,column=3)
#numbers:0,1..and addition and subtraction operators
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="1",command=lambda:btnClick(1),bg="red").grid(row=3,column=0)
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="0",command=lambda:btnClick(0),bg="red").grid(row=3,column=1)
plus=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="+",command=lambda:btnClick('+'),bg="blue").grid(row=3,column=2)
sub=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="-",command=lambda:btnClick('-'),bg="blue").grid(row=4,column=1)
dzero=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="00",command=lambda:btnClick('00'),bg="red").grid(row=3,column=3)
#operators:MULTIPLICATION, DIVISION. clear button: DELETE. DECIMAL button and the EQUAL-SIGN
times=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="*",command=lambda:btnClick('*'),bg="blue").grid(row=4,column=0)
Div=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="/",command=lambda:btnClick('/'),bg="blue").grid(row=5,column=1)
Clear=Button(cal,padx=8,pady=4,bd=4,fg="black",font=('arial',20,'bold'), text="DEL",bg="green",command= btnClearDisplay).grid(row=5,column=4)
dec=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text=".",command=lambda:btnClick('.'),bg="blue").grid(row=4,column=2)
Equals=Button(cal,padx=24,pady=4,bd=8,fg="black",font=('arial',20,'bold'), text="=",bg="gray",command=btnEqualsInput).grid(row=5,column=0)
#More operators:floor division, Modulus , square
fdiv=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="//",command=lambda:btnClick('//'),bg="violet").grid(row=3,column=4)
Mod=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="%",command=lambda:btnClick('%'),bg="violet").grid(row=4,column=3)
SQ=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="**",command=lambda:btnClick('**'),bg="violet").grid(row=4,column=4)
#comparison operators
greater=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text=">",command=lambda:btnClick('>'), bg="yellow").grid(row=1,column=4)
less=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="<",command=lambda:btnClick('<'),bg="yellow").grid(row=2,column=4)
#logical operators
andop=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="&",command=lambda:btnClick('&'),bg="purple").grid(row=5,column=2)
orop=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="|",command=lambda:btnClick('|'),bg="purple").grid(row=5,column=3)


cal.mainloop()