
try:
    from KBC_base import *
    from tkinter import *
    import time, random, datetime
    # *************************************************************************************************************
    choice_q = {lvl_1: easy, lvl_1+lvl_2: med, lvl_1+lvl_2+lvl_3: hard}

    intro = "WELCOME TO KAUN BANEGA CROREPATI.\n\nIntroducing you to the game:\n\
        There are total 15 questions in the game with 3 levels\n\
        each with 5 questions.\nLevel 1: 1,000-"+defam[lvl_1]+ " You will get 45 seconds for an answer\n\
        Level 2: "+defam[lvl_1+1]+ "-"+defam[lvl_1+lvl_2]+ " You will get 60 seconds for an answer\n\
        Level 3: "+defam[lvl_1+lvl_2+1]+ "-1CR Infinite Time\n\
        There are 4 lifelines for your Help\n\
        You may quit at any instant when you don't know the answer.\n\n\
        LET'S PLAY...."

    win = Tk()
    win.title("Kaun Banega Crorepati")
    win.iconbitmap("kbc_logo.ico")
    win.attributes("-fullscreen", default_scr)
    can_1 = Canvas(win, width=1500, height=800, bg="blue")
    can_1.pack()
    img_1 = PhotoImage(file="kbc_logo.png")
    img_can = can_1.create_image(700, 750, image=img_1)
    img_2 = PhotoImage(file="aud-poll.png")
    img_3 = PhotoImage(file="fifty-fifty.png")
    img_4 = PhotoImage(file="ask-expert.png")
    img_5 = PhotoImage(file="flip-ques.png")

    def full(event):
        win.attributes("-fullscreen", True)
    def window(event):
        win.attributes("-fullscreen", False)
        
    win.bind("<F1>", full)
    win.bind("<Escape>", window)
    # ******************************* INTRO - ANIMATION **************************************************************
    d_can = 750
    while d_can != 110:
        can_1.move(img_can, 0, -10)
        time.sleep(0.05)
        d_can -= 10
        win.update()
    can_1.destroy()    

    # ************************* MAIN - FUNCTIONS DEFINED TO START GAME AND CHANGE SETTINGS ***************************
    def main():
        can_1 = Canvas(win, width=1500, height=800, bg="blue")
        can_1.grid(row=0, column=0)
        img_can = can_1.create_image(700, 110, image=img_1)
        introbox = can_1.create_rectangle((310,250),(1100,550), fill='indigo')
        introtxt = can_1.create_text((625,400), text = intro, font=("Comic Sans MS", 12))

        play_1 = can_1.create_rectangle((320,570), (450,600), fill='dark blue')
        play_1_txt = can_1.create_text((380,580), text = "PLAY", font=("Comic Sans MS", 12))

        exit_main = can_1.create_rectangle((620,570), (750,600), fill='dark blue')
        exit_main_txt = can_1.create_text((680,580), text = "EXIT", font=("Comic Sans MS", 12))
        
        setting = can_1.create_rectangle((900,570), (1010,600), fill='dark blue')
        setting_txt = can_1.create_text((960,580), text = "SETTINGS", font=("Comic Sans MS", 12))
    # *********************** WHEN BUTTON 'PLAY' IS CLICKED **********************************************************
        def play():
            can_1.delete("all")
            win.update()
            # *************** VARIABLES AND OBJECTS ***************
            img_can = can_1.create_image(700, 110, image=img_1)
            cirt = can_1.create_oval((675-50,300-50),(675+50,300+50), fill='indigo', outline='yellow') # TIME DISPLAY (SEMI CIRCLE)
            qbox = can_1.create_polygon((250,350),(300,300),(1100,300),(1150,350),(1100,400),(300,400),
            fill='indigo', outline="yellow")
            
            abox = can_1.create_polygon((250,445),(300,410),(650,410),(700,445),(650,480),(300,480),
            fill='indigo', outline="yellow")

            bbox = can_1.create_polygon((700,445),(750,410),(1100,410),(1150,445),(1100,480),(750,480),
            fill='indigo', outline="yellow")
            cbox = can_1.create_polygon((250,445+80),(300,410+80),(650,410+80),(700,445+80),(650,480+80),(300,480+80),
            fill='indigo', outline="yellow")
            dbox = can_1.create_polygon((700,445+80),(750,410+80),(1100,410+80),(1150,445+80),(1100,480+80),(750,480+80),
            fill='indigo', outline="yellow")

            quitbox = can_1.create_rectangle((100,400),(180,450), fill='light blue')
            quittxt = can_1.create_text((140,430),text="QUIT", font=("Algerian",15))

            a1 = can_1.create_text((290,445),text='A', font=("Arial",15), fill='yellow')
            b1 = can_1.create_text((290+450,445),text='B', font=("Arial",15), fill='yellow')
            c1 = can_1.create_text((290,445+80),text='C', font=("Arial",15), fill='yellow')
            d1 = can_1.create_text((290+450,445+80),text='D', font=("Arial",15), fill='yellow')

            ap  = can_1.create_image(350,620, image=img_2)
            fif = can_1.create_image(350+200,620, image=img_3)
            ask = can_1.create_image(350+400,620, image=img_4)
            flp = can_1.create_image(350+600,620, image=img_5)
            
            txt = can_1.create_text((350,275), text='', font=("Arial",12), fill='yellow')    # Amount printed here
            mes = can_1.create_text((860,275), text='', font=("Arial",12), fill='yellow')    # Message printed here
            time_txt = can_1.create_text((675,274),text='', font=("Arial",12), fill='yellow')    # Time printed here
            txtq = can_1.create_text((650,340),text='', font=("Arial",12), fill='yellow')    # Ques printed here
            atxt = can_1.create_text((450,445),text='', font=("Arial",12), fill='yellow')
            btxt = can_1.create_text((900,445),text='', font=("Arial",12), fill='yellow')
            ctxt = can_1.create_text((450,525),text='', font=("Arial",12), fill='yellow')
            dtxt = can_1.create_text((900,525),text='', font=("Arial",12), fill='yellow')

            l = 0                             # NO. OF LIFELINES USED
            j = 1                             # CREATING RANGE OF QUESTIONS FOR RANDOM SELECTION
            la = []                           # LIST OF QUESTIONS GONE
            op = {'A':atxt,'B':btxt,'C':ctxt,'D':dtxt}
            op2 = {'A':abox,'B':bbox,'C':cbox,'D':dbox}
            timex  = {lvl_1 : 45, lvl_1+lvl_2 : 60, lvl_1+lvl_2+lvl_3 : '  '}
            global lifelist, minimum, ans, i, amt, flag

            flag = IntVar(can_1, 0)
            minimum  = '0'                    # MIN. AMOUNT AFTER EACH LEVEL        
            i = 1                             # NO. OF QUESTIONS
            lifelist = []                     # LIST OF LINELINES GONE
            
            # *********** CHECK FN - ANALYSIS THE CLICK AS AN ANSWER ********************
            def check(event):
                global amt
                global flag
                global i
                m = event.x
                n = event.y
                # CLICK IS ASSIGNED AN ANSWER
                if 300 <= m <= 650 and 410 <= n <= 480:
                    ans = ('A')
                elif 750 <= m <= 1100 and 410 <= n <= 480:
                    ans = ('B')
                elif 300 <= m <= 650 and 490 <= n<= 560:
                    ans = ('C')
                elif 750 <= m<= 1100 and 490 <= n <= 560:
                    ans = ('D')
                elif ((m-350)**2 + (n-620)**2 - (40)**2) < 0:
                    ans = ('AP')
                elif ((m-550)**2 + (n-620)**2 - (40)**2) < 0:
                    ans = ('50')
                elif ((m-750)**2 + (n-620)**2 - (40)**2) < 0:
                    ans = ('ASK')
                elif ((m-950)**2 + (n-620)**2 - (40)**2) < 0:
                    ans = ('FLIP')  
                elif 100 <= m <= 180 and 400 <= n <= 450:
                    ans = ('Q')      
                else:
                    ans = ('L')
                win.update()
                # ASSIGNED ANSWER IS EVALUATED
                if ans not in "ABCDQ":
                    if ans in ['AP','50','ASK','FLIP']:
                        if ans not in lifelist:
                            lifelist.append(ans)
                            if ans == 'AP':      # AUDIENCE POLL
                                p = str(random.randrange(70,100))+"% people say: "+choice_q[x][qnow][5]+" is correct"
                                can_1.itemconfig(mes, text=p)
                                ans = 'L'
                                can_1.create_polygon((320,590),(380,650),(350,620),(380,590),(320,650),(350,620), outline='red')
                                win.update()

                            elif ans == '50':    # 50-50
                                can_1.create_polygon((320+200,590),(380+200,650),(350+200,620),(380+200,590),(320+200,650),(350+200,620), outline='red')
                                xx = ord(choice_q[x][qnow][5])-64
                                p = x
                                q = p
                                while p == xx or q == xx or q == p:
                                    p = random.randrange(1,5)
                                    q = random.randrange(1,5)
                                can_1.itemconfig(op[chr(p+64)], text='')
                                can_1.itemconfig(op[chr(q+64)], text='')
                                ans = 'L'
                                win.update()
                            elif ans == 'ASK':   # ASK THE EXPERT
                                p = 'Expert: I think '+choice_q[x][qnow][5]+' would be the correct answer'
                                can_1.itemconfig(mes, text=p)
                                ans = 'L'
                                can_1.create_polygon((320+400,590),(380+400,650),(350+400,620),(380+400,590),(320+400,650),(350+400,620), outline='red')
                                win.update()

                            elif ans == 'FLIP':  # FLIP THE QUES.
                                p= 'New Question will be on Your Screen....\nIs Question ka Sahi Answer Hota: '+choice_q[x][qnow][5]
                                can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'green')
                                can_1.create_polygon((320+600,590),(380+600,650),(350+600,620),(380+600,590),(320+600,650),(350+600,620), outline='red')
                                can_1.itemconfig(mes, text=p)
                                win.update()
                                time.sleep(2)
                                can_1.itemconfig(mes, text='')
                                can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'indigo')
                                ans = ' '
                        else:
                            p='You have used this Lifeline'
                            can_1.itemconfig(mes, text=p)
                            win.update()
                            time.sleep(2)
                            can_1.itemconfig(mes, text='')
                            ans = 'L'
                elif ans == choice_q[x][qnow][5]:
                    
                    can_1.itemconfig(op2[ans], fill = 'orange')
                    win.update()
                    amt = defam[i]
                    time.sleep(2)
                    can_1.itemconfig(op2[ans], fill = 'green')
                    p = "Yes, it's the Right Answer. Well Played!."
                    can_1.itemconfig(mes, text=p)
                    win.update()
                    time.sleep(2)
                    can_1.itemconfig(op2[ans], fill = 'indigo')
                    can_1.itemconfig(mes, text='')
                    i += 1
                    
                elif ans == 'Q':
                    p= 'Is Question ka Sahi Answer Hota:'+choice_q[x][qnow][5]
                    can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'green')
                    can_1.itemconfig(mes, text=p)
                    amt = defam[i-1]
                    i = 16
                    win.update()
                    time.sleep(2)
                    can_1.itemconfig(mes, text='')
                    can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'indigo')
                else:
                    can_1.itemconfig(op2[ans], fill = 'orange')
                    win.update()
                    time.sleep(2)
                    p = "No, it's the wrong answer!!\n Correct answer is "+ choice_q[x][qnow][5]
                    can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'green')
                    can_1.itemconfig(mes, text=p)
                    win.update()
                    time.sleep(2)
                    can_1.itemconfig(op2[ans], fill = 'indigo')
                    can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'indigo')
                    can_1.itemconfig(mes, text='')
                    amt = minimum
                    i = 16
                
                if ans in "ABCDQ ":
                    flag.set(1)
                    
                win.update()         
                

            # ************************** QUESTIONS ARE DISPLAYED ACC. TO LOOP *****************
            for x in [lvl_1, (lvl_1 + lvl_2), (lvl_1 + lvl_2 + lvl_3)]:
                while i <= x:
                    qnow = random.randrange(1, len(choice_q[x])+1)
                    if i > lvl_1+lvl_2:
                        can_1.itemconfig(time_txt, text = '')
                        can_1.delete(cirt)
                        win.update()
                    qstr = choice_q[x][qnow][0]
                    if qstr not in la:        # IF QUESTION WASN'T DISPLAYED
                        flag.set(0)
                        la.append(qstr)
                        can_1.itemconfig(txt,  text = "Amount: "+defam[i])
                        can_1.itemconfig(txtq, text = qstr)
                        can_1.itemconfig(atxt, text = choice_q[x][qnow][1])
                        can_1.itemconfig(btxt, text = choice_q[x][qnow][2])
                        can_1.itemconfig(ctxt, text = choice_q[x][qnow][3])
                        can_1.itemconfig(dtxt, text = choice_q[x][qnow][4])
                        win.update()
                        t1 = datetime.datetime.now()
                        ans = 'L'
                        
                        can_1.bind("<Button-1>", check)
                        while flag.get() != 1:
                            if i <= lvl_1+lvl_2:
                                t2 = datetime.datetime.now()    
                                t = str(timex[x] - (t2-t1).seconds) 
                                can_1.itemconfig(time_txt, text = t)
                                if t == '0':
                                    p = "You have crossed time limit\n"+choice_q[x][qnow][5]+' would be the correct answer'
                                    can_1.itemconfig(mes, text = p)
                                    can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'green')
                                    win.update()
                                    time.sleep(2)
                                    i = 16
                                    amt = minimum
                                    can_1.itemconfig(op2[choice_q[x][qnow][5]], fill = 'indigo')
                                    flag.set(1)                   
                            win.update()
                        can_1.unbind("<Button-1>")
                if i != 16:
                    minimum = defam[i-1]
            # ************************** FINAL RESULT ***************************************
            can_1.delete("all")
            img_can = can_1.create_image(700, 110, image=img_1)            
            introbox = can_1.create_rectangle((310,250),(1100,550), fill='indigo')
            introtxt = can_1.create_text((625,400), text = "You Won:\n"+chr(8377)+amt , font=("Comic Sans MS", 20))
            win.update()
            def end(event):
                can_1.delete(introbox, introtxt)
                win.update()
                d_can = 110
                while d_can != 750:
                    can_1.move(img_can, 0, 10)
                    time.sleep(0.05)
                    d_can += 10
                    win.update()        
                win.destroy()
            can_1.bind("<Button-1>", end)

        # **************************** WHEN BUTTON 'SETTINGS' IS CLICKED *********************
        def user_setting():
            win2 = Tk()
            win2.title("User login")
            win2.iconbitmap("kbc_logo.ico")
            win2.configure(background='blue')
            win2.geometry("300x100")
            label1= Label(win2, text="Enter password below: ", bg='blue', font=("Arial",12), anchor='w')
            label1.grid(row=1, column=1)

            passkey_entry = Entry(win2, show = '*', width=30, font=("Comic Sans MS",12))
            passkey_entry.grid(row=3, column=1)
            
            
            # ENTERED PASSWORD IS CHECKED
            def setting_check():
                pass1 = passkey_entry.get()
                if pass1 == password:
                    can_1.destroy()
                    win.geometry("1500x800")
                    win2.destroy()
                    # CHANGE SETTINGS WINDOW OPENS
                    win.configure(background='blue')
                    label_pic = Label(win, image=img_1, bg='blue')
                    label_pic.grid(row=1, column=3, columnspan=2)
                    win.update()
                    # **** CHANGE NO. OF QUES ****
                    Label(win, text='\n\n'+' * '*100, bg='blue', font=("Arial",12)).grid(row=2, column=1, columnspan=10)
                    Label(win, text='\tNo. of Questions: (>3 each)\tLevel 1', bg='blue', font=("Arial",12)).grid(row=3, column=1)
                    
                    level1 = Entry(win, width=3)
                    level1.grid(row=3, column=2)
                    
                    
                    Label(win, text='\t+\tLevel 2', bg='blue', font=("Arial",12)).grid(row=3, column=3)
                    level2 = Entry(win, width=3)
                    level2.grid(row=3, column=4)

                    
                    Label(win, text='\t+\tLevel 3', bg='blue', font=("Arial",12)).grid(row=3, column=5)
                    level3 = Entry(win, width=3)
                    level3.grid(row=3, column=6)
                    
                    Label(win, text='\t=\t15', bg='blue', font=("Arial",12)).grid(row=3, column=7)
                    Label(win, text=' * '*100, bg='blue', font=("Arial",12)).grid(row=4, column=1, columnspan=10)
                    # **** ADD A QUESTION ****
                    Label(win, text='Add a Question:', bg='blue', font=("Arial",12)).grid(row=5, column=1)

                    selected_lvl = StringVar()
                    selected_lvl.set("Level 1")
                    
                    Label(win, text='Select Level: ', bg='blue', font=("Arial",12)).grid(row=6, column=1)
                    lvl_select = OptionMenu(win, selected_lvl, "Level 1", "Level 2", "Level 3")
                    lvl_select.config(highlightthickness=0)
                    lvl_select.grid(row=7, column=1)
                    
                    new_ques = Entry(win, width=150)
                    new_ques.grid(row=5, column=2, columnspan=6)
                    
                    Label(win, text='A.', bg='blue', font=("Arial",12)).grid(row=6, column=2)
                    op_A = Entry(win, width=20)
                    op_A.grid(row=6, column=3)
                    Label(win, text='B.', bg='blue', font=("Arial",12)).grid(row=6, column=4)
                    op_B = Entry(win, width=20)
                    op_B.grid(row=6, column=5)
                    Label(win, text='C.', bg='blue', font=("Arial",12)).grid(row=7, column=2)
                    op_C = Entry(win, width=20)
                    op_C.grid(row=7, column=3)
                    Label(win, text='D.', bg='blue', font=("Arial",12)).grid(row=7, column=4)
                    op_D = Entry(win, width=20)
                    op_D.grid(row=7, column=5)
                    
                    Label(win, text='Correct Answer: ', bg='blue', font=("Arial",12)).grid(row=8, column=3)
                    cor_ans = Entry(win, width=6)
                    cor_ans.grid(row=8, column=4)

                    Label(win, text=' * '*100, bg='blue', font=("Arial",12)).grid(row=9, column=1, columnspan=10)
                    # **** CHANGE PASSWORD ****
                    Label(win, text='Change Password:', bg='blue', font=("Arial",12)).grid(row=10, column=1)
                    Label(win, text='Current Password:', bg='blue', font=("Arial",12)).grid(row=10, column=2)
                    cur_pass = Entry(win, width=20, show='*')
                    cur_pass.grid(row=10, column=3)
                    Label(win, text='New Password: ', bg='blue', font=("Arial",12)).grid(row=11, column=2)
                    new_pass = Entry(win, width=20, show='*')
                    new_pass.grid(row=11, column=3)
                    Label(win, text='Confirm Password: ', bg='blue', font=("Arial",12)).grid(row=11, column=4)
                    cfm_pass = Entry(win, width=20, show='*')
                    cfm_pass.grid(row=11, column=5)

                    Label(win, text=' * '*100, bg='blue', font=("Arial",12)).grid(row=12, column=1, columnspan=10)

                    change_scr = BooleanVar()
                    change_scr.set(default_scr)
                    Checkbutton(win, text='Use Fullscreen as Default', variable=change_scr, offvalue=False, onvalue=True, bg='blue', font=("Arial",12)).grid(row=13 , column=1)

                    # ENTRIES ARE CHECKED AND SAVED WHEN 'SAVE' IS CLICKED
                    def save_changes():
                        flag2 = 0
                        setting_mes = Label(win, text='', bg='blue', font=('Arial',12))
                        setting_mes.grid(row = 21, column = 3, columnspan=2)
                        
                        level1_txt = level1.get()
                        
                        level2_txt = level2.get()
                        level3_txt = level3.get()
                        if level1_txt == '' and level2_txt == '' and level3_txt == '':
                            pass
                        elif int(level1_txt) and int(level2_txt) and int(level3_txt) and \
                            int(level1_txt) > 3 and int(level1_txt) > 3 and int(level1_txt) > 3 and int(level1_txt)+int(level2_txt)+int(level3_txt)==15:
                            f = open("KBC_base.py", "a")
                            f.write("\nlvl_1,lvl_2,lvl_3 = "+level1_txt+','+level2_txt+','+level3_txt)
                            win.update()
                            f.close()
                        else:
                            flag2 = 1
                        new_ques_txt = new_ques.get()
                        txt_A =op_A.get()
                        txt_B =op_B.get()
                        txt_C =op_C.get()
                        txt_D =op_D.get()
                        correct_txt = cor_ans.get()
                        level_dic = {"Level 1": ['easy', easy],"Level 2": ['med',med],"Level 3": ['hard',hard]}
                        if new_ques_txt == '' and txt_A == '' and txt_B == '' and txt_C == '' and txt_D == '' and correct_txt == '':
                            pass
                        elif len(new_ques_txt)>3 and correct_txt.upper() in 'ABCD':
                            f = open("KBC_base.py", "a")
                            f.write('\n'+level_dic[selected_lvl.get()][0]+"["+str(len(level_dic[selected_lvl.get()][1])+1)+'] = ["'+new_ques_txt+'","'+txt_A+'","'+txt_B+'","'+txt_C+'","'+txt_D+'","'+correct_txt+'"]')
                            win.update()
                            f.close()
                        else:
                            flag2 = 1

                        cur_pass_txt = cur_pass.get()
                        new_pass_txt = new_pass.get()
                        cfm_pass_txt = cfm_pass.get()
                        if cur_pass_txt == new_pass_txt == cfm_pass_txt == '':
                            pass
                        elif cur_pass_txt == password and new_pass_txt == cfm_pass_txt and len(new_pass_txt) > 4:
                            f = open("KBC_base.py", "a")
                            f.write('\npassword = "'+new_pass_txt+'"')
                            f.close()
                        else:
                            flag2 = 1
                        if change_scr.get() != default_scr:
                            f = open("KBC_base.py", "a")
                            f.write('\ndefault_scr = '+str(change_scr.get()))
                            f.close()
                        
                        if flag2 == 0:
                            setting_mes.config(text = ' Your settings are saved. Restart to apply.')
                            win.update()
                            time.sleep(2)
                            main()
                        else:
                            setting_mes.config(text = 'Invalid entry(s) found. Other saved.')
                            win.update()
                            time.sleep(2)
                            setting_mes.config(text = '')
                    win.update()


                    button_back = Button(win, text='BACK', bg='indigo', command=main, font=("Arial",12))    # 'BACK'- ENTRIES ARE NOT SAVED
                    button_back.grid(row=20, column=2)
                    button_apply = Button(win, text='SAVE', bg='indigo', command=save_changes, font=("Arial",12))
                    button_apply.grid(row=20, column=4)

                else:
                    label2 = Label(win2, text='Invalid Password!', bg='blue', font=("Arial",8))
                    label2.grid(column=1,row=4)
                    win2.update()
                    time.sleep(2)
                    label2.config(text='')
            
            button1 = Button(win2, text='Submit',bg='indigo', command=setting_check)
            button1.grid(row=5, column=1)



        
        def intro_check(event):
            x_coords = event.x
            y_coords = event.y

            if 320 <= x_coords <= 450  and  570 <= y_coords <= 600:
                play()
            if 620 <= x_coords <= 750  and  570 <= y_coords <= 600:
                win.destroy()
            elif 900 <= x_coords <= 1010  and  570 <= y_coords <= 600:
                user_setting()
        can_1.bind("<Button-1>", intro_check)

    main()
    win.mainloop()
except:
    import sys
    sys.exit()