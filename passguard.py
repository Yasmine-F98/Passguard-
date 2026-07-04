import argparse                          
import string, secrets

def evaluer_mot_de_passe(mot_de_passe):
    evaluation = {}
    
    if len(mot_de_passe) >= 8:
        evaluation["longueur"] = True
    else:
        evaluation["longueur"] = False
    
    evaluation["majuscule"] = False
    for caractere in mot_de_passe:
        if caractere.isupper():
            evaluation["majuscule"] = True
            break

    evaluation["minuscule"] = False
    for caractere in mot_de_passe:
        if caractere.islower():
            evaluation["minuscule"] = True
            break

    evaluation["chiffre"] = False 
    for caractere in mot_de_passe:     
        if caractere.isdigit():         
            evaluation["chiffre"] = True         
            break 
    
    evaluation["caractere_special"] = False 
    for caractere in mot_de_passe:     
        if not caractere.isalnum():         
            evaluation["caractere_special"] = True         
            break       
    score = list(evaluation.values()).count(True)
    message = ""
    if  0 <= score <= 2 :
        message = "Score faible"
    elif 3 <= score <= 4 :
        message = "Score moyen"
    else:
        message = "Score fort"   
    return message


def generer_mot_de_passe():
    sequence = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe_genere = []
    for i in range(8):
        mot_de_passe_genere.append(secrets.choice(sequence))
    mot_de_passe_genere = "".join(mot_de_passe_genere)
    return mot_de_passe_genere

parser = argparse.ArgumentParser()                 
parser.add_argument('--generate', action='store_true') 
parser.add_argument('--check')                        
args = parser.parse_args()   

if args.generate :
    print (generer_mot_de_passe())

elif args.check is not None : 
    print(evaluer_mot_de_passe(args.check))