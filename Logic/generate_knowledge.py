from field_var import field_var

def goesAfter(Auto1, Auto2, Auto3):
    pass

def generate_knowledge(conf):
    #conf is a list, e.g. ['right of way', 'empty', '', '']
    #field_var(n,x) entspricht V_n,x 
    #e.g. field_var(2,0) -> vehicle 2 (top) does not exist
    # e.g. field_var(0,1) -> vehicle 0 (bottom) drives first
    
    kb = [] 
    hilfsliste = []
    k = 0
    for i in range(0,4):
        if conf[i] == 'empty':
            new_proposition = field_var(i,0) # Vi0 
            kb.append(new_proposition)
            k += 1

    #1st rule: Right-of-Way sign (Vorfahrtsstraße) -> drives BEFORE ALL other vehicles
        if conf[i] == 'right of way':
            #new_proposition = field_var(i,1) #vehicle i drives FIRST
            #kb.append(new_proposition)
            hilfsliste.append(i)
            conf[i] = 'empty'
            print(hilfsliste)
            
        
    for rudi in range(0,4):
        if conf[rudi] == 'stop':
            kb.append(field_var(rudi,4-k))
            conf[rudi] = 'empty'

    for karl in range(0,4):   
        for i in range(0,4):
        #3rd rule: If 2 vehicles have no signs -> Right before Left

            if i == 3:
                ralf = 0
            else:
                ralf = i + 1    
            
            if conf[ralf] == 'empty' and conf[i] == '':
                hilfsliste.append(i)
                conf[i] = 'empty'
            
    #new_proposition = field_var(i, 
        
                                        
    #hier durch Hilfsliste gehen und das in die KB hauen
    for j in range(0,len(hilfsliste)):
        kb.append(field_var(hilfsliste[j],j+1))
    print(hilfsliste)

    #4th rule: No two vehicles pass at the same time
#         vehicle_solution = [a,b,c,d] -> kein Wert in der Liste darf gleich sein!! Bedingung enthalten in Regel 1,2,3

#       print(conf[i]) #print() zum Testen -> Ausgabe in Logic_Exercise.ipynb ganz unten unter "feed..."
    return kb
