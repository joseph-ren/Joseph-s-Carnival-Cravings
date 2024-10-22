#Joseph #storeAssign.py #user orders food items at Joseph's Carnival.
                        #Their order will appear in a table next to the menu
                        #and brings them to the final checkout page after clicking "Finish"
                        #If they want to remove an item, they can click the delete button next to the item.
from pygame import *
font.init()
screen=display.set_mode((800, 600))
#first screen
page="intro"
#fonts
openSans=font.SysFont("Open Sans", 30)
openSansSmall=font.SysFont("Open Sans", 25)
#images
carApple=image.load("caramel.png")
cottonCandy=image.load("cottonCandy.jpg")
fries=image.load("fries.png")
nachos=image.load("nachos.png")
smoothie=image.load("smoothie.png")
popcorn=image.load("popcorn.png")
pretzel=image.load("pretzel.png")
checkMark=image.load("checkMark.jpg")
#menu click positions
btn1=Rect(20, 5, 92, 80)
btn2=Rect(20, 90, 80, 80)
btn3=Rect(20, 175, 102, 80)
btn4=Rect(20, 260, 121, 80)
btn5=Rect(20, 345, 103, 80)
btn6=Rect(20, 430, 103, 80)
btn7=Rect(20, 515, 104, 80)
checkout=Rect(591, 505, 75, 30) #button to checkout order
#tracks and deletes order and price
food=[]
price=[]
delete=[]
running=True
while running:
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN and evt.button==1:
            click=True
    mx, my=mouse.get_pos()

    if page=="intro":
        screen.fill((132, 112, 255))
        #menu
        screen.blit(carApple, (20, 5))
        screen.blit(cottonCandy, (20, 90))
        screen.blit(fries, (20, 175))
        screen.blit(nachos, (20, 260))
        screen.blit(smoothie, (20, 345))
        screen.blit(popcorn, (20, 430))
        screen.blit(pretzel, (20, 515))
        draw.rect(screen, (255, 255, 255), (400, 50, 300, 500))#shows order
        orderTitle=openSans.render("Joseph's Carnival Cravings ", True, (0))#order title
        screen.blit(orderTitle, (417, 75))
        checkoutButton=openSans.render("Checkout", True, (0)) #checkout button
        screen.blit(checkoutButton, (595, 520, 75, 30))
        if len(food)<16:
            #user's order
            if btn1.collidepoint(mx, my):
                draw.rect(screen, (0), btn1, 2)#shows outline when hovered over
                if click:
                    food.append("Caramel Apple")
                    price.append(1.00)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)#delete button position
                    delete.append(deleteButton)               
            if btn2.collidepoint(mx, my):
                draw.rect(screen, (0), btn2, 2)
                if click:
                    food.append("Cotton Candy")
                    price.append(1.50)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)
                    delete.append(deleteButton)
            if btn3.collidepoint(mx, my):
                draw.rect(screen, (0), btn3, 2)
                if click:
                    food.append("Fries")
                    price.append(3.50)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)
                    delete.append(deleteButton)
            if btn4.collidepoint(mx, my):
                draw.rect(screen, (0), btn4, 2)
                if click:
                    food.append("Nachos")
                    price.append(5.50)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)
                    delete.append(deleteButton)
            if btn5.collidepoint(mx, my):
                draw.rect(screen, (0), btn5, 2)
                if click:
                    food.append("Smoothie")
                    price.append(4.50)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)
                    delete.append(deleteButton)
            if btn6.collidepoint(mx, my):
                draw.rect(screen, (0), btn6, 2)
                if click:
                    food.append("Popcorn")
                    price.append(5.00)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)
                    delete.append(deleteButton)
            if btn7.collidepoint(mx, my):
                draw.rect(screen, (0), btn7, 2)
                if click:
                    food.append("Pretzel")
                    price.append(2.50)
                    deleteButton=Rect(670, ((len(food)-1)*20+120), 15, 15)
                    delete.append(deleteButton)
            if checkout.collidepoint(mx, my):
                draw.rect(screen, (0), (588, 513, 106, 30), 2)
                if click:
                    page="final"
        else:
            draw.rect(screen, (255, 0, 0), (588, 513, 106, 30), 2)
            if checkout.collidepoint(mx, my):
                draw.rect(screen, (255, 0, 0), (588, 513, 106, 30), 4)
                if click:
                    page="final"
        #subtotal, tax, and total
        subTotal="{:.2f}".format(sum(price))
        subTotalPic=openSans.render("Subtotal:  $ "+subTotal, True, (0))
        screen.blit(subTotalPic, (417, 450))
        tax="{:.2f}".format(sum(price)*0.13)
        taxPic=openSans.render("Tax:          $ "+tax, True, (0))
        screen.blit(taxPic, (417, 470))
        total="{:.2f}".format(sum(price)+sum(price)*0.13)
        totalPic=openSans.render("Total:        $ "+total, True, (0))
        screen.blit(totalPic, (417, 490))
        #orders being shown
        for i in range(len(food)):
            text=openSansSmall.render(food[i], True, (0))
            screen.blit(text, (417, i*20+120))
            #location of delete button
            draw.rect(screen, (0), Rect(delete[i-1]), 2)
            draw.line(screen, (0), (670, i*20+120), (685, i*20+135), 2)
            draw.line(screen, (0), (670, i*20+135), (685, i*20+120), 2)
        #prices being shown
        for i in range(len(price)):
            line="{:.2f}".format(price[i])
            cost=openSansSmall.render(line, True, (0))
            screen.blit(cost, (600, i*20+120))
        #deleting items
        for i in range(len(food)):
            if delete[i-1].collidepoint(mx, my):
                draw.rect(screen, (255, 0, 0), delete[i-1], 2)
                if click:
                    del delete[len(food)-1]
                    del food[i-1]
                    del price[i-1]
    #final receipt
    elif page=="final":
        screen.fill((164, 211, 238))
        draw.rect(screen, (255, 255, 255), (250, 50, 300, 500))#shows order
        orderTitle=openSans.render("Joseph's Carnival Cravings", True, (0))#order title on receipt
        screen.blit(orderTitle, (268, 75))
        receiptTitle=openSans.render("Receipt", True, (0))#receipt title
        screen.blit(receiptTitle, (360, 100))
        finishButton=openSans.render("Finish", True, (0))#finish button
        screen.blit(finishButton, (480, 500))
        wid=finishButton.get_width() #width of finish button
        height=finishButton.get_height() #height of finish button
        finish=Rect(473, 493, wid+10, height+10)
        goBackPosition=Rect(475, 455, wid+10, height+10)
        goBack=openSans.render(" Back ", True, (0))#go back button
        screen.blit(goBack, (479, 460))
        if goBackPosition.collidepoint(mx, my):
            draw.rect(screen, (0), (473, 453, wid+10, height+10), 2)
            if click:
                page="intro"
        #shows user's final receipt
        subTotal="{:.2f}".format(sum(price))
        subTotalPic=openSans.render("Subtotal:  $ "+subTotal, True, (0))
        screen.blit(subTotalPic, (260, 450))
        tax="{:.2f}".format(sum(price)*0.13)
        taxPic=openSans.render("Tax:          $ "+tax, True, (0))
        screen.blit(taxPic, (260, 470))
        total="{:.2f}".format(sum(price)+sum(price)*0.13)
        totalPic=openSans.render("Total:        $ "+total, True, (0))
        screen.blit(totalPic, (260, 490))
        for i in range(len(food)):
            text=openSansSmall.render(food[i], True, (0))
            screen.blit(text, (260, i*20+120))             
        for i in range(len(price)):
            line="{:.2f}".format(price[i])
            cost=openSansSmall.render(line, True, (0))
            screen.blit(cost, (500, i*20+120))
        #finish button
        if finish.collidepoint(mx, my):
            draw.rect(screen, (0), finish, 2)
            if click:
                page="end"

    #thank you screen
    else:
        screen.fill((92, 172, 238))
        screen.blit(checkMark, (359, 150))
        confirmation=openSans.render("Order received!", True, (0))#order confirmation
        screen.blit(confirmation, (330, 260))
        thankYou=openSans.render("Thank you for ordering at Joseph's Carnival Cravings", True, (0))
        screen.blit(thankYou, (150, 290))
        #home button
        home=openSans.render("Home", True, (0))
        screen.blit(home, (380, 330))
        homePosition=Rect(380, 330, 50, 10)
        if homePosition.collidepoint(mx, my):
            draw.rect(screen, (0), (375, 325, 65, 28), 2)
            if click:
                page="intro"
                food=[]
                price=[]
                delete=[]
    display.flip()
quit()
