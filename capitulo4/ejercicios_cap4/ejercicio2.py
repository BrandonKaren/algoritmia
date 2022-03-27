can_fly=bool(int(input("¿puede volar?:")))
is_human=bool(int(input("¿es humano?:")))
has_mask=bool(int(input("¿tiene mascara?:")))

if can_fly==True and is_human==True and has_mask==True: 
    print("iroman")
elif can_fly==True and is_human==True and has_mask==False:
    print("captain marvel")

elif can_fly==True and is_human==False and has_mask==True:
    print("ronan accuser")

elif can_fly==True and is_human==False and has_mask==False:
    print("vision")
    
elif can_fly==False and is_human==True and has_mask==True:
    print("spiderman")
    
elif can_fly==False and is_human==True and has_mask==False:
    print("hulk")
    
elif can_fly==False and is_human==False and has_mask==True:
    print("black bolt")
elif can_fly==False and is_human==False and has_mask== False:
      print("thanos")
else:
    print("no existe ningúnsuper heroe")
