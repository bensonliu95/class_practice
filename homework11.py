for cock in range(1,101):   
    for hen in range(1,101):  
        for chick in range(1,101): 
            if cock * 5 + hen * 3 + chick//3 == 100:
                if cock + hen + chick == 100:
                    print("公雞有%d只\t母雞有%d只\t小雞有%d只"%(cock,hen,chick))

