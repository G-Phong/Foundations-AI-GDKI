# Define your domain here
domains_WP = {'A': {'0','S','D','P'},
              'B': {'0','S','D','P'},
              'C': {'0','S','D','P'},
              'D': {'0','S','D','P'},
              'E': {'0','S','D','P'},
              'F': {'0','S','D','P'},
              'G': {'0','S','D','P'}, 
              'H': {'0','S','D','P'},
}
#Test-Ausgabe:
#for keys,values in domains_WP.items():
#    print(keys,':',values)

#Knoten des Graphen sind die Students A-H mit den Domänen Nichts 0, Singing S, Dancing D, Comedy C und Piano P
#für die Anzahl-constraints kann man dann count() nutzen

_________

#Shortcut (Crtl + /) einkommentieren und auskommentieren
# Define your constraints here
constraint1_WP = Constraint(('A','B','C','D','E','F','G','H'), 
                            lambda a, b, c, d, e, f, g, h: a == b == c == d == e == f == g == h != 0)

#constraint2_WP = Constraint(('A','B','C','D','E','F','G','H'), 
                           # lambda a, b, c, d, e, f, g, h: ) 

constraint3_WP = Constraint(('Sing', 'Dance', 'Comed', 'Piano'), 
                            lambda sing, dance, comed, piano: count(sing) > 1 and count(dance) > 1 and count(comed) > 1 and count(piano) > 1) 

#constraint4_WP = Constraint(('Cost'), lambda cost: cost <= 400)

constraint5_WP = Constraint(('Sing'), lambda sing: count(sing) >= 3) 

# constraint6_WP = Constraint(('A','B','C','D','E','F','G','H','Sing', 'Dance', 'Comed', 'Piano'), if(dancing=performed) dancing >= 2)

# constraint7_WP = Constraint(('A','B','C','D','E','F','G','H','Sing', 'Dance', 'Comed', 'Piano'), (if(comedy=performed) comedy == 2 or comedy == 3)
                            
# constraint8_WP = Constraint(('F', 'C3'), (if piano = performed) piano == 1)
                            
# constraint9_WP = Constraint(('F', 'C3'), if(piano = performed) piano == 2)
                            
# constraint10_WP = Constraint(('A', 'H'), A together with H)
                            
# constraint11_WP = Constraint(('F', 'G', 'H'), not together)
                            
# constraint12_WP = Constraint(('B', 'D'), B and D do not dance at all)
                            
# constraint13_WP = Constraint(('A', 'C'), A and C do not comedy at all)
                            
# constraint14_WP = Constraint(('E', 'G'), E and G want to sing)
                            
#constraint15_WP = Constraint(('A','B','C','D','E','F','G','H'), lambda a, b, c, d, e, f, g, h:...)


________


# Combine Constraints and set up the csp for Problem 2.1
# TODO:
csp_21_constraints = [constraint1_WP,  constraint2_WP,  constraint5_WP,  constraint6_WP,
                      constraint7_WP,  constraint9_WP,  constraint10_WP, constraint11_WP,
                      constraint12_WP, constraint13_WP, constraint14_WP]
csp_21 = NaryCSP(domains_WP, csp_21_constraints) 

# Combine Constraints and set up the csp for Problem 2.2
# TODO:
csp_22_constraints = [constraint1_WP,  constraint3_WP,  constraint4_WP,  constraint5_WP,
                      constraint6_WP,  constraint7_WP,  constraint8_WP, constraint10_WP,
                      constraint11_WP, constraint12_WP, constraint14_WP]
csp_22 = NaryCSP(domains_WP, csp_22_constraints) 


# Combine Constraints and set up the csp for Problem 2.3
# TODO:
csp_23_constraints = [constraint1_WP,  constraint3_WP,  constraint4_WP,  constraint5_WP,
                      constraint6_WP,  constraint7_WP,  constraint9_WP, constraint10_WP,
                      constraint11_WP, constraint12_WP, constraint13_WP]
csp_23 = NaryCSP(domains_WP, csp_23_constraints) 
# NOT SATISFIABLE!!!!!!!!!!!!!!!!!!

# Combine Constraints and set up the csp for Problem 2.4
# TODO:
csp_24_constraints = [constraint1_WP,  constraint2_WP,  constraint3_WP,  constraint6_WP,
                      constraint7_WP,  constraint11_WP,  constraint12_WP, constraint13_WP,
                      constraint14_WP]
csp_24 = NaryCSP(domains_WP, csp_24_constraints) 


# Combine Constraints and set up the csp for Problem 2.5
# TODO:
csp_25_constraints = [constraint1_WP,  constraint2_WP,  constraint4_WP,  constraint5_WP,
                      constraint6_WP,  constraint7_WP,  constraint9_WP, constraint10_WP,
                      constraint11_WP, constraint12_WP, constraint13_WP, constraint14_WP]
csp_25 = NaryCSP(domains_WP, csp_25_constraints)  


# Combine Constraints and set up the csp for Problem 2.6
# TODO:
csp_26_constraints = [constraint1_WP,  constraint2_WP,  constraint4_WP,  constraint5_WP,
                      constraint6_WP,  constraint7_WP,  constraint10_WP, constraint11_WP,
                      constraint12_WP, constraint13_WP, constraint14_WP, constraint15_WP]
csp_26 = NaryCSP(domains_WP, csp_26_constraints) 
