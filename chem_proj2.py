
covalent_art = """"
_________                     .__                 __    ___.                      .___      
\_   ___ \  _______  _______  |  |   ____   _____/  |_  \_ |__   ____   ____    __| _/______
/    \  \/ /  _ \  \/ /\__  \ |  | _/ __ \ /    \   __\  | __ \ /  _ \ /    \  / __ |/  ___/
\     \___(  <_> )   /  / __ \|  |_\  ___/|   |  \  |    | \_\ (  <_> )   |  \/ /_/ |\___ \ 
 \______  /\____/ \_/  (____  /____/\___  >___|  /__|    |___  /\____/|___|  /\____ /____  >
        \/                  \/          \/     \/            \/            \/      \/    \/ 
"""
octet_rule = ("""
               __          __                 .__          
  ____   _____/  |_  _____/  |_  _______ __ __|  |   ____  
 /  _ \_/ ___\   __\/ __ \   __\ \_  __ \  |  \  | _/ __ \ 
(  <_> )  \___|  | \  ___/|  |    |  | \/  |  /  |_\  ___/ 
 \____/ \___  >__|  \___  >__|    |__|  |____/|____/\___  >
            \/          \/                              \/
            """)
ionic_bond = """
.__              .__         ___.                      .___
|__| ____   ____ |__| ____   \_ |__   ____   ____    __| _/
|  |/  _ \ /    \|  |/ ___\   | __ \ /  _ \ /    \  / __ | 
|  (  <_> )   |  \  \  \___   | \_\ (  <_> )   |  \/ /_/ | 
|__|\____/|___|  /__|\___  >  |___  /\____/|___|  /\____ | 
               \/        \/       \/            \/      \/ 
"""
metallic_bond = """
                __         .__  .__  .__         ___.                      .___      
  _____   _____/  |______  |  | |  | |__| ____   \_ |__   ____   ____    __| _/______
 /     \_/ __ \   __\__  \ |  | |  | |  |/ ___\   | __ \ /  _ \ /    \  / __ |/  ___/
|  Y Y  \  ___/|  |  / __ \|  |_|  |_|  \  \___   | \_\ (  <_> )   |  \/ /_/ |\___ \ 
|__|_|  /\___  >__| (____  /____/____/__|\___  >  |___  /\____/|___|  /\____ /____  >
      \/     \/          \/                  \/       \/            \/      \/    \/ 
"""
electronegativity = """
       .__                 __                                            __  .__      .__  __          
  ____ |  |   ____   _____/  |________  ____   ____   ____   _________ _/  |_|__|__  _|__|/  |_ ___.__.
_/ __ \|  | _/ __ \_/ ___\   __\_  __ \/  _ \ /    \_/ __ \ / ___\__  \\   __\  \  \/ /  \   __<   |  |
\  ___/|  |_\  ___/\  \___|  |  |  | \(  <_> )   |  \  ___// /_/  > __ \|  | |  |\   /|  ||  |  \___  |
 \___  >____/\___  >\___  >__|  |__|   \____/|___|  /\___  >___  (____  /__| |__| \_/ |__||__|  / ____|
     \/          \/     \/                        \/     \/_____/     \/                        \/     
"""

formula1 = """"""

periodic_table = """|   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18 |
|                                                                          |
|1  H                                                                   He |
|                                                                          |
|2  Li  Be                                          B   C   N   O   F   Ne |
|                                                                          |
|3  Na  Mg                                          Al  Si  P   S   Cl  Ar |
|                                                                          |
|4  K   Ca  Sc  Ti  V   Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr |
|                                                                          |
|5  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I   Xe |
|                                                                          |
|6  Cs  Ba  *   Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn |
|                                                                          |
|7  Fr  Ra  **  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Nh  Fl  Mc  Lv  Ts  Og|
|__________________________________________________________________________|
|                                                                          |
|                                                                          |
| Lantanoidi*   La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu |
|                                                                          |
|  Aktinoidi**  Ac  Th  Pa  U   Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr |
|__________________________________________________________________________|"""
print("Welcome to Nikhil's chemical bonding project!")
programOn = True
while programOn == True:
    learnChoice = int(input("What would you like to learn about?  1 for Octet rule, 2 for covalent bonding, 3 for ionic bonding, 4 for metallic bonding, 5 for electronegativity, or 6 for names of formulas, or 0 to turn it off."))
    if learnChoice == 0:
        break;
    elif learnChoice == 1:
        print(octet_rule)
        print("Glad you asked! \nAtoms form bonds because it stabilizes their outer shell. In most cases, Atoms want 8 electrons in their outer shell, and that is the octet rule.\n They will try to bond with atoms that can fulfill that need.")
    elif learnChoice == 2:
        print(covalent_art)
        print("Good question! A covalent bond is a bond where the atomic particles share electron pairs and are formed between nonmetals and nonmentals\n")
        print("Valence electrons are related to covalent bonds because they are the ones getting shared in the bonding process.\n")
        print("Atomic numbers below 20 will combine because they want to have 8 electrons in their shell.\n")
    elif learnChoice == 3:
        print("The Ionic bond is a connection between two oppositely charged ions. It occurs between metals. \n \n In the shared document, you will find the images required to show a diagram of the ionic bond. \n \n Valence electrons are related to Ionic Bonds because they are about the transfer of valence electrons.")
        print("The structure of the ionic bond is a cation transferring its electrons to the anion.")
        print("Ionic bonds are electrostatic by nature.")
    elif learnChoice == 4:
        print(metallic_bond)
        print("Metallic bonds are the attraction of stationary metal cations to the surrounding electrons.")
        print("\n \n Metallic bonds are formed between two metals, hence the name.")
        print("Metals are crystalline solids, but the electrons in the outer levels are capable of drifting.")
        print("\n\nProperties of Metals: Metals can conduct heat very well, and electricity. When light is shone onto the metals, the electrons gain energy and are excited into orbitals. The electrons fall back down and emit light.")
    elif learnChoice == 5:
        print(electronegativity)
        print("Electronegativity is a measure of an atom's ability to attract shared electrons to itself, according to Khan Academy.")
        print("\n\nThe trend for electronegitivity increases from left to right on the periodic table from Francium to Fluorine.")
        print("\n See below:")
        print(periodic_table)
        print("\n\nBond polarity relates to electronegativity in that the polarity increases as the electronegativity difference increases.")
    elif learnChoice == 6:
        print("""
___________                        .__                 
\_   _____/__________  _____  __ __|  | _____    ______
 |    __)/  _ \_  __ \/     \|  |  \  | \__  \  /  ___/
 |     \(  <_> )  | \/  Y Y  \  |  /  |__/ __ \_\___ \ 
 \___  / \____/|__|  |__|_|  /____/|____(____  /____  >
     \/                    \/                \/     \/ 
""")
        print("\n\nThis is how to name Ionic formulas:")
        print("To name an Ionic comopound, the cation is named first and then the anion.")
        print("Examples:")
        print("""
                                                           
 _____   ______         _____         _____    ____        
|\    \ |\     \    ___|\    \    ___|\    \  |    |       
 \\    \| \     \  /    /\    \  /    /\    \ |    |       
  \|    \  \     ||    |  |    ||    |  |    ||    |       
   |     \  |    ||    |__|    ||    |  |____||    |  ____ 
   |      \ |    ||    .--.    ||    |   ____ |    | |    |
   |    |\ \|    ||    |  |    ||    |  |    ||    | |    |
   |____||\_____/||____|  |____||\ ___\/    /||____|/____/|
   |    |/ \|   |||    |  |    || |   /____/ ||    |     ||
   |____|   |___|/|____|  |____| \|___|    | /|____|_____|/
     \(       )/    \(      )/     \( |____|/   \(    )/   
      '       '      '      '       '   )/       '    '    
                                        '                  
""")
        print(""""
                                            
      _____            ______        _____  
  ___|\    \       ___|\     \  ____|\    \ 
 /    /\    \     |    |\     \|    | \    \
|    |  |    |    |    |/____/||    |______/
|    |  |____| ___|    \|   | ||    |----'\ 
|    |   ____ |    \    \___|/ |    |_____/ 
|    |  |    ||    |\     \    |    |       
|\ ___\/    /||\ ___\|_____|   |____|       
| |   /____/ || |    |     |   |    |       
 \|___|    | / \|____|_____|   |____|       
   \( |____|/     \(    )/       )/         
    '   )/         '    '        '          
        '                                   
""")
        print("To name Covalent compounds, Name the non-metal furthest left on the periodic table by elemental name, then name the other non-metal by elemental name and add the -ide ending.")
        print("Examples:")
        print("""
        _________  ________   ________  
        \_   ___ \ \_____  \  \_____  \ 
        /    \  \/  /   |   \  /  ____/ 
        \     \____/    |    \/       \ 
        \______  /\_______  /\_______ \
                \/         \/         \/
        """)
        print("""""
        ___________________ .____    ________  
        \______   \_   ___ \|    |   \_____  \ 
        |     ___/    \  \/|    |    /  ____/ 
        |    |   \     \___|    |___/       \ 
        |____|    \______  /_______ \_______ \
                        \/        \/       \/

        """)