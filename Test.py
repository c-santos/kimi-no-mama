
import pygame

inv = []


#Code below will add an item to that list.
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_x]:
            if len(inv) < 6:
                    inv.append("someItem")              
            else:
                    print("No inventory space")
#This code will remove the most recently added item:
    if key_pressed[pygame.K_z]:
            inv.pop()
    if key_pressed[pygame.K_c]:
            print(inv)