#conessione al database redis
import redis
import sys
r = redis.Redis(
  host='redis-11245.c135.eu-central-1-1.ec2.cloud.redislabs.com',
  port=11245,
  password='YcEyrqZS3LNXpAwfbFJltUWW6OuRMZzu')

is_connected = r.ping()
if not is_connected:
    print("REDIS NON CONNESSO")
    sys.exit(-1)
    
    
# nel caso si vogliono settare i punti a 0 
# r.set('team1',0)
# r.set('team2',0)

while True:
    try:
        scelta_team = int(input("Inserisci il team 1 o 2 || (3) per uscire: \n"))
        if scelta_team == 1:
            try:
                print("Inserisci il tipo di tiro \n")
                scelta = int(input("(1) tiro libero | (2) tiro in area | (3) tiro fuori dall'area \n"))
                if scelta == 1:
                    r.incr('team1') #qui lo crea da solo
                elif scelta == 2:
                    r.incrby('team1',2)
                elif scelta == 3:
                    r.incrby('team1',3)
                elif scelta == 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Valore inserito non valido")
                
        elif scelta_team == 2:
            print("Inserisci il tipo di tiro \n")
            scelta = int(input("(1) tiro libero | (2) tiro in area | (3) tiro fuori dall'area \n"))
            try:
                if scelta == 1:
                    r.incr('team2')
                elif scelta == 2:
                    r.incrby('team2',2)
                elif scelta == 3:
                    r.incrby('team2',3)
                elif scelta == 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Valore inserito non valido")
        elif scelta_team == 3:
            break
        else:
            raise ValueError
        
    except ValueError:
        print("Valore inserito non valido")


punteggio_team1 = int(r.get('team1'))
print(f'Punteggio totti team 1: {punteggio_team1}')
punteggio_team2 = int(r.get('team2'))
print(f'Punteggio totti team 2: {punteggio_team2}')
