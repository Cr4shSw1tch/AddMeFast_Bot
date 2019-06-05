# -*- coding: utf-8 -*-
from tkinter import *
from selenium import webdriver
import time
import random

root = Tk()
root.title("AddMeFast Bot")

root.geometry("400x320+500+250")
root.resizable(FALSE,FALSE)

baslik = Label(root,text = "AddMeFast Bot!",
               fg="green",
               bd=10,
               font=("Helvetica",20,"bold",))
baslik.pack()

lutfen = Label(root,text = "If reCAPTCHA is exiting, enter 60 seconds !",
               fg="red",
               font=("Helvetica",10,"bold","underline"))
lutfen.pack(padx=0)

############GOOGLE##################

Email = Label(root,text = "Gmail :",
              fg="green",
              anchor="w",
              width="400",
              bd=5,
              font=("Helvetica",10,"bold"))
Email.pack(padx=10)

emailgiris = Entry(root,width=60)
emailgiris.pack()

password = Label(root,text = "Password :",
                 fg="green",
                 anchor="w",
                 width="400",
                 bd=5,
                 font=("Helvetica",10,"bold"))
password.pack(padx=10)

sifregiris = Entry(root,width=60, show="*")
sifregiris.pack()

############ADD ME FAST##################

ademail = Label(root,text = "AddMeFast Email :",
              fg="green",
              anchor="w",
              width="400",
              bd=5,
              font=("Helvetica",10,"bold"))
ademail.pack(padx=10)

ademail = Entry(root,width=60)
ademail.pack()

adpass = Label(root,text = "Password :",
                 fg="green",
                 anchor="w",
                 width="400",
                 bd=5,
                 font=("Helvetica",10,"bold"))
adpass.pack(padx=10)

adpass = Entry(root,width=60, show="*")
adpass.pack()

def google():

    browser = webdriver.Firefox()

    # GOOGLE

    window_before = browser.window_handles[0]

    browser.get("https://accounts.google.com/ServiceLogin/signinchooser?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(5)

    email = browser.find_element_by_name("identifier")
    email.send_keys(emailgiris.get())

    ileri = browser.find_element_by_xpath("// *[ @ id = 'identifierNext']")
    ileri.click()
    time.sleep(3)

    password = browser.find_element_by_name("password")
    password.send_keys(sifregiris.get())

    ileri2 = browser.find_element_by_xpath("//*[@id='passwordNext']")
    ileri2.click()

    # ADDMEFAST

    browser.get("http://addmefast.com/")
    time.sleep(15)

    email = browser.find_element_by_xpath("//*[@id='wrapper']/section[2]/div/form/ul/li[1]/input[1]")
    password = browser.find_element_by_xpath("//*[@id='wrapper']/section[2]/div/form/ul/li[2]/input")

    email.send_keys(ademail.get())
    password.send_keys(adpass.get())
    login_button = browser.find_element_by_xpath("//*[@id='wrapper']/section[2]/div/form/ul/li[3]/input")
    login_button.click()
    time.sleep(3)

    i = 0

    while i < 9000:

        try:

            window_before = browser.window_handles[0]
            browser.switch_to_window(window_before)

            time.sleep(3)
            browser.get("http://addmefast.com/free_points/youtube_subscribe")
            time.sleep(8)

            like = browser.find_element_by_link_text("Subscribe")
            like.click()
            time.sleep(10)

            window_after = browser.window_handles[1]
            browser.switch_to_window(window_after)

            sub = browser.find_element_by_xpath("//*[@id='subscribe-button']")
            sub.click()

            #Random sayı üretme
            time.sleep(random.randint(5, 10))

            browser.close()
            i += 1

        except  Exception as e:

            window_on = browser.window_handles[1]
            browser.switch_to_window(window_on)

            browser.close()
            i += 1

buton = Button(root,bg="green",text="Start!",fg="white",bd=5,command = google,height=0,
               font=("Helvetica",10,"bold"))
buton.pack(side = "right",padx=20)

yapımcı = Label(root,text = "Cr4sh-Sw1tch",
               fg="black",
               bd=0,
               font=("Helvetica",10,"bold",))
yapımcı.pack(side = "left",padx=20)

root.mainloop()