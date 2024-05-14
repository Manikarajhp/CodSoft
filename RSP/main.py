from pygame import *
import random,time
init()
width=500
height=700
win=display.set_mode((width,height))
#font decleration
font=font.Font("freesansbold.ttf",22)
#image loding section
start_btn=image.load("start.png")
start_btn=transform.scale(start_btn,(126,126))
rock_img=image.load("fist.png")
five_img=image.load("five.png")
two_img=image.load("two.png")
replay_btn=image.load("replay.png")
replay_btn=transform.scale(replay_btn,(64,64))
cross_btn=image.load("cross.png")
start=1
comp_choose=0
choose=0
comp_score=0
player_score=0
def rand_comp():
    return random.randint(0,2)
def game():
    global start,choose,comp_choose,player_score,comp_score
    while 1:
        win.fill("yellow")
        for eve in event.get():
            if eve.type==QUIT:
                quit()
            if eve.type==MOUSEBUTTONDOWN:
                if eve.button==1:
                    pos=mouse.get_pos()
                    if start==1:
                        if (((width/2)-63)<pos[0]<((width/2)+63)) and ((height/2)-63<pos[1]<(height/2)+63):
                            start=0
                    if start==0:
                        if (((width/2-32))<pos[0]<((width/2+32))) and ((400)<pos[1]<(400+128)):
                            choose=1
                            comp_choose=rand_comp()
                        if (((width/2-128))<pos[0]<((width/2-64))) and ((400)<pos[1]<(400+128)):
                            choose=0
                            comp_choose=rand_comp()
                        if (((width/2+64))<pos[0]<((width/2+128))) and ((400)<pos[1]<(400+128)):
                            choose=2
                            comp_choose=rand_comp()
                        #For player score manage
                        if choose==0 and comp_choose==2:
                            player_score+=1
                        if choose==1 and comp_choose==0:
                            player_score+=1
                        if choose==2 and comp_choose==1:
                            player_score+=1
                        #For computer score manage
                        if comp_choose==0 and choose==2:
                            comp_score+=1
                        if comp_choose==1 and choose==0:
                            comp_score+=1
                        if comp_choose==2 and choose==1:
                            comp_score+=1
                    if start==2:
                        if ((width/2)-40<pos[0]<(width/2)+32) and ((height/2)-63<pos[1]<(height/2)+32):
                            player_score=0
                            comp_score=0
                            start=0  
                        if ((width/2)-40<pos[0]<(width/2)+32) and ((height/2)<pos[1]<(height/2)+32):
                            print(pos,"POS")
                            quit()
        if start==1:
            win.blit(start_btn,((width/2)-63,(height/2)-63))
            txt_note1=font.render("Note:If you scored 10 you will win",True,("black"))
            win.blit(txt_note1,(90,(height/2)-100))
            txt_note2=font.render("otherwise computer win.",True,("black"))
            win.blit(txt_note2,(140,(height/2)-75))
        elif start==2:
            if  player_score==10:
                txt_win=font.render("You win.",True,("black"))
                win.blit(txt_win,((width/2)-50,(height/2)-90))
            else:
                txt_win=font.render("Computer win.",True,("black"))
                win.blit(txt_win,((width/2)-80,(height/2)-90))
            win.blit(replay_btn,((width/2)-40,(height/2)-63))
            win.blit(cross_btn,((width/2)-40,(height/2)))
        else:
            txt_you=font.render("YOU:",True,("black"))
            win.blit(txt_you,(90,100))
            txt_comp=font.render("COMPUTER:",True,("black"))
            win.blit(txt_comp,(300,100))
            win.blit(rock_img,((width/2-32),400))
            win.blit(two_img,((width/2-128),400))
            win.blit(five_img,((width/2+64),400))
            txt_you_score=font.render(str(player_score),True,("black"))
            win.blit(txt_you_score,(110,250))
            txt_comp_score=font.render(str(comp_score),True,("black"))
            win.blit(txt_comp_score,(350,250))
            if choose==0:
                win.blit(two_img,(80,150))
            if choose==1:
                win.blit(rock_img,(80,150))
            if choose==2:
                win.blit(five_img,(80,150))
            if comp_choose==0:
                win.blit(two_img,(330,150))
            if comp_choose==1:
                win.blit(rock_img,(330,150))
            if comp_choose==2:
                win.blit(five_img,(330,150))
        if player_score==10 or comp_score==10:
            start=2
        display.update()
game()
    
