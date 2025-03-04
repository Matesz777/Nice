import keyboard
import random

ammo = 0
bullets = 0
randombullet = 0

def restartgame():
    global ammo, bullets, randombullet
    bullets = 0
    ammo = int(input("Podaj liczbe naboi (Maksymalnie 6): "))
    if ammo > 6:
        print("Maksymalna pojemność magazynka to 6 naboi. Przypisuje maksymalna wartość.")
        ammo = 6
    
    randombullet = random.randint(1, ammo)

    print(f"Naciśnij klawisz '=' aby strzelić, masz {ammo} próby.")

    keyboard.on_press_key("=", lambda e: test(ammo))

def test(ammo):
    global bullets
    if bullets < ammo:
        bullets += 1
        print(f"Strzał numer {bullets}")
        if bullets == randombullet:
            print(f"ZGON!")
            print("Koniec gry! Chcesz grac dalej ? Jeśli nie to naciśnij Esc")
            keyboard.unhook_key('=')
        else:
            print(f"CYK! Jeszcze zyjesz")
    else:
        print("Koniec gry!")
        keyboard.unhook_key('=')
def NewGame(e):
    restartgame()

restartgame()

keyboard.on_press_key("r", NewGame)
print("Restart gry 'r'. Aby wyjsc z gry nacisnij 'Esc'")
keyboard.wait("esc") 