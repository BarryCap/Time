﻿define b = Character("Billy")
define o = Character("Bobby")
define r = Character("Robby")
define a = Character("Barry")
define rt = Character("Barty")
define j = Character("Jimmy")
define hn = Character("Johny")
define t = Character("Tommy")
define m = Character("Morty")
define n = Character("Norby")
#OYE
define audio.explosion = "sounds/explosion2.wav"
define audio.fire = "sounds/fire.wav"
define audio.AAAaaah = "sounds/AAAaaah.wav"
define audio.talk0 = "sounds/colonel.wav"
define audio.talk1 = "sounds/AHA.wav"
define audio.talk2 = "sounds/A-AH.wav"
define audio.talk3 = "sounds/cider.wav"
define audio.talk4 = "sounds/IAmASoulCider.wav"
define audio.talk5 = "sounds/finally.wav"
define audio.talk6 = "sounds/finalli.wav"
define audio.talk7 = "sounds/finalliHEHEHE.wav"
define audio.talk8 = "sounds/long.wav"
define audio.talk9 = "sounds/verylong.wav"
define audio.music01 = "sounds/TIMEmusic01.ogg"
define audio.music02 = "sounds/TIMEmusic02.wav"
define audio.music03 = "sounds/TIMEmusic03.wav"
define audio.music04 = "sounds/TIMEmusic04.wav"

label start:
    scene bg time
    play music music03

    menu:
        "Teleport":
            jump c1

label c1:
    scene bg blac

    play sound talk3
    b "Colonel Robson, wake up!"

    menu:
        "Se lever et ouvrir les yeux":
            jump c2
        "Ignorer":
            jump c3
        "Se retourner":
            jump c4

label c2:
    scene bg dark
    show billy content

    play sound talk5
    b "Finally!..."

    menu:
        "Dire : « Hello » à Billy":
            jump c5
        "Demander l'heure à Billy":
            jump c6
        "Tenter d'assassiner Billy":
            jump c7

label c3:
    play sound talk6
    b "Colonel Robson?"

    menu:
        "Se lever et ouvrir les yeux":
            jump c2
        "Ignorer encore":
            jump c8
        "Se retourner":
            jump c4

label c4:
    play sound talk7
    b "Colonel Robson? I know you're not asleep..."

    menu:
        "Se lever et ouvrir les yeux":
            jump c2
        "Ignorer encore":
            jump c8
        "Se retourner encore":
            jump c9

label c5:
    play sound talk5
    b "Hello Colonel!"

    menu:
        "Prendre les commandes du vaisseau et allumer la lumière":
            jump c10
        "Se préparer un café":
            jump c11
        "Demander comment ça va à Billy":
            jump c12

label c6:
    play sound talk7
    b "It is 5:00 Colonel."

    menu:
        "Why did you wake me up at this hour?":
            jump c102
        "Prendre les commandes du vaisseau et allumer la lumière":
            jump c10
        "Se préparer un café":
            jump c11
        "Demander comment va Billy":
            jump c12

label c7:
    show billy base at right

    play sound talk2
    b "Whaaa!!!"
    "Billy esquive votre attaque."

    menu:
        "Demander pardon à Billy":
            jump c13
        "L'attaquer encore":
            jump c14
        "Le menacer avec le revolver sous votre oreiller":
            jump c15

label c8:
    play sound talk6
    b "Colonel Robson!!!"

    menu:
        "Se lever et ouvrir les yeux":
            jump c2
        "Ignorer encore":
            jump c8
        "Se retourner":
            jump c9


label c9:
    play sound talk6
    b "Colonel Robson!!!"

    menu:
        "Se lever et ouvrir les yeux":
            jump c2
        "Ignorer encore":
            jump c8
        "Se retourner encore":
            jump c9

label c10:
    scene bg stam
    show cockpit base behind billy
    show billy base at right

    play sound talk8
    b "Do you need anything else?"

    menu:
        "Yes.":
            jump c16
        "No, thank you.":
            jump c17

label c11:
    scene bg coffee

    menu:
        "Remplir et boire la tasse":
            jump c18
        "Aller au cockpit":
            jump c10
        "Aller parler à Billy":
            jump c19

label c12:
    play sound talk7
    b "I'm fine, and you?"

    menu:
        "I am feeling good.":
            jump c20
        "I don't know.":
            jump c21
        "I'm not.":
            jump c22

label c13:
    play sound talk8
    b "I accept your excuses but don't try this anymore."

    menu:
        "This isn't funny."
        "You think?":
            jump c23
        "You are right.":
            jump c24

label c14:
    show billy at left

    play sound talk3
    b "Why are you doing this?"

    menu:
        "I don't know.":
            jump c26
        "Because I hate you.":
            jump c27
        "Because you're a freak.":
            jump c28
        "Because you're a fool.":
            jump c29

label c15:
    play sound talk3
    b "What's going on???"

    menu:
        "Nothing.":
            jump c30
        "Tirer dans le vide avec votre revolver":
            jump c32
        "Tirer sur Billy avec votre revolver":
            jump c33

label c16:
    play sound talk3
    b "What do you want?"

    menu:
        "A cup of tea.":
            jump c25
        "Nothing, thank you.":
            jump c31


label c17:
    hide billy

    menu:
        "Appuyer sur un bouton blanc":
            jump c36
        "Appuyer sur le bouton gris":
            jump c110
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "Ne pas appuyer sur un bouton":
            jump c45

label c18:
    "Vous avez bu la tasse de café."

    menu:
        "Aller au cockpit":
            jump c10
        "Aller parler à Billy":
            jump c19

label c19:
    show billy base at right
    show bg dark

    menu:
        "What time is it?":
            jump c43
        "Where are we?":
            jump c67

label c20:
    play sound talk9
    b "So, today we're traveling through the galaxy of Sreiin 41."
    play sound talk9
    b "At first, I'll need you at the commands to check something."

    menu:
        "Ok. (walk to the cockpit)":
            jump c65
        "What thing?":
            jump c66

label c21:
    play sound talk9
    b "Any way, we're traveling through the galaxy of Sreiin 41."
    play sound talk9
    b "At first, I'll need you at the commands to check something."

    menu:
        "Ok. (walk to the cockpit)":
            jump c65
        "What thing?":
            jump c66

label c22:
    play sound talk3
    b "You aren't ok?"

    menu:
        "Yes, I'm ok.":
            jump c46
        "No, I'm not.":
            jump c47

label c23:
    play sound talk5
    b "Yes I think."
    play sound talk8
    b "I think this is unacceptable."

    menu:
        "Ok. I won't do this anymore.":
            jump c48
        "You will die. (le tuer)":
            jump c49

label c24:
    play sound talk9
    b "Ok. Any way, we're traveling through the galaxy of Sreiin 41."
    play sound talk8
    b "We're approching a black hole, what do we do?"

    menu:
        "Nothing.":
            jump c62
        "PANIC!":
            jump c63
        "We go back.":
            jump c64
        "We go through it.":
            jump c109

label c25:
    hide billy
    "Billy prépare une tasse de thé."

    menu:
        "Appuyer sur un bouton blanc":
            jump c36
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "Ne pas appuyer sur un bouton":
            jump c45

label c26:
    play sound talk3
    b "That's all!"

    menu:
        "Yes.":
            jump c57
        "No. (tuer Billy)":
            jump c58

label c27:
    play sound talk2
    b "Why?"

    menu:
        "Because I hate you.":
            jump c27
        "Because you're a freak.":
            jump c28
        "Because you're a fool.":
            jump c29

label c28:
    play sound talk7
    b "I'm not a freak! You are a freak!"

    menu:
        "Le freak, c'est chic.":
            jump c59
        "If I were a freak, I wouldn't tell you that you were a freak!":
            jump c60
        "We aren't freaks.":
            jump c61

label c29:
    play sound talk7
    b "I'm not a fool!"

    menu:
        "Yes you are. (tirer sur Billy)":
            jump c50
        "If you say another bullshit, I shoot.":
            jump c51

label c30:
    play sound talk7
    b "Nothing??? Are you kidding???"

    menu:
        "No. (tirer sur Billy)":
            jump c50
        "Yes. (pardonner Billy)":
            jump c13

label c31:

    menu:
        "Appuyer sur un bouton blanc":
            jump c36
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "Ne pas appuyer sur un bouton":
            jump c44

label c32:
    play sound fire

    play sound talk2
    b "Aah!"
    show billy mini
    "Billy recule."

    menu:
        "Tirer encore":
            jump c32
        "S'approcher et le tuer":
            jump c68

label c33:
    play sound fire
    pause 0.5
    play music music01
    show billy mourant

    play sound talk2
    b "AAH!"

    menu:
        "L'achever":
            jump c34
        "Le laisser mourir lentement":
            jump c35

label c34:
    show billy mort

    play sound talk2
    b "Noooo!"
    hide billy
    "Billy est mort."

    menu:
        "L'envoyer par dessus bord":
            jump c83
        "Aller au cockpit":
            jump c85
        "Aller en salle de téléportation":
            jump c86


label c35:
    hide billy

    play sound AAAaaah
    b "AAAaaah..."

    menu:
        "Aller au cockpit":
            jump c41
        "Aller se faire une tasse de café":
            jump c42
        "Se suicider":
            jump c79
        "Aller en salle de téléportation":
            jump c77

label c36:
    "Rien ne se passe."

    menu:
        "Réessayer sur un autre":
            jump c57
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "N'appuyer sur aucun bouton":
            jump c45

label c37:
    show cockpit dos

    menu:
        "Appuyer sur le bouton bleu":
            jump c70
        "Appuyer sur le bouton jaune":
            jump c71
        "Appuyer sur le bouton rouge":
            jump c72
        "N'appuyer sur aucun bouton":
            jump c73

label c38:
    show cockpit graph

    menu:
        "Appuyer sur le bouton jaune":
            jump c74
        "Appuyer sur le bouton rouge":
            jump c75
        "N'appuyer sur aucun bouton":
            jump c76

label c39:
    show cockpit graph2

    menu:
        "Appuyer sur le bouton rouge":
            jump c75
        "Ne pas appuyer sur aucun bouton":
            jump c76

label c40:
    stop music
    hide billy
    play sound explosion
    show cockpit destruction1
    pause 0.5
    show cockpit destruction2
    pause 0.5
    show cockpit destruction3
    pause 0.5
    show cockpit destruction4
    pause 0.5
    show cockpit destruction5
    pause 0.5
    show cockpit destruction6
    pause 0.5
    show cockpit destruction7
    pause 0.5
    show white
    pause 1
    scene bg end1
    pause 13

    return

label c41:
    scene bg stam
    show cockpit base

    menu:
        "Détruire le vaisseau":
            jump c40
        "Aller en salle de téléportation":
            jump c77
        "Conduire le vaisseau":
            jump c84

label c42:
    scene bg coffee
    "Il n'y a plus de café."

    menu:
        "Aller chercher du café dans la calle":
            jump c94
        "Aller au cockpit.":
            jump c95
        "Aller prendre Billy":
            jump c96
        "Frapper la machine à café":
            jump c97

label c43:
    play sound talk8
    b "It is 5:05 Colonel."

    menu:
        "In the morning or in the afternoon?":
            jump c100
        "Good.":
            jump c101

label c44:
    show cockpit redb
    "Un bouton blanc s'allume en rouge."

    menu:
        "Appuyer dessus":
            jump c57
        "Appuyer sur le bouton vert":
            jump c105
        "Appuyer sur le gros bouton rouge":
            jump c106
        "Ne pas appuyer sur un bouton":
            jump c107

label c45:
    "Rien ne se passe."

    menu:
        "Appuyer sur un bouton blanc":
            jump c36
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "Ne rien toucher":
            jump c44

label c46:
    play sound talk8
    b "Ok, so it's good."

    menu:
        "No, it's not good.":
            jump c22
        "Yes. You can dispose now.":
            jump c111
        "Yes. Can you get me some coffee?":
            jump c112

label c47:

label c48:

label c49:

label c50:
    show billy mourant

    play sound talk2
    b "Why...?"

    menu:
        "Tuer Billy":
            jump c54
        "Le laisser mourir lentement":
            jump c35

label c51:
    play sound talk8
    b "Ok, ok I'll don't say anything."

    menu:
        "Good for you.":
            jump c52
        "Tuer Billy":
            jump c53

label c52:
    menu:
        "Tuer Billy":
            jump c55
        "Ouvrir la fenêtre":
            jump c56

label c53:
    show billy mort

    menu:
        "L'envoyer par dessus bord":
            jump c83
        "Lui tirer dessus":
            jump c88
        "Le manger":
            jump c89

label c54:
    "Billy est mort."
    show billy mort

    menu:
        "L'envoyer par dessus bord":
            jump c83
        "Lui tirer dessus":
            jump c88
        "Le manger":
            jump c89

    menu:
        "Envoyer Billy en sas de décompression":
            jump c83
        "S'excuser":
            jump c90
        "Le porter":
            jump c91

label c55:
    show billy mort

label c56:

label c57:
    scene bg stem
    show cockpit base

    menu:
        "Réessayer sur un autre":
            jump c58
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "Ne pas appuyer sur un bouton":
            jump c45
label c58:
    scene bg sstm
    show cockpit base

    menu:
        "Réessayer sur un autre":
            jump c58
        "Appuyer sur le bouton vert":
            jump c37
        "Appuyer sur le bouton bleu":
            jump c38
        "Appuyer sur le bouton jaune":
            jump c39
        "Appuyer sur le bouton rouge":
            jump c40
        "Ne pas appuyer sur un bouton":
            jump c45

label c59:

label c60:

label c61:

label c62:

label c63:

label c64:

label c65:
    show cockpit base behind billy

    menu:
        "Ok, so what do I have to check?":
            jump c80


label c67:
    play sound talk9
    b "So, today we're traveling through the galaxy of Sreiin 41."
    play sound talk9
    b "At first, I'll need you at the commands to check something."

    menu:
        "Ok. (walk to the cockpit)":
            jump c65
        "What thing?":
            jump c66

label c77:
    scene bg teleportation

    menu:
        "Allumer le moniteur de téléportation":
            jump c81
        "Se jeter dans le bassin de téléportation":
            jump c82
        "Retourner au cockpit":
            jump c87

label c80:
    show cockpit base behind billy

    play sound talk8
    b "There's a navigation problem."
    play sound talk8
    b "Maybe you could see what's causing it."

    menu:
        "Yeah, I'll check that.":
            jump c92
        "No that's bullshit!":
            jump c93

label c81:
    scene bg moniteur

    menu:
        "Appuyer sur le bouton xxx":
            jump c94

label c82:
    "Le liquide est froid."
    "Vous sentez votre corps progressivement vous abandoner."
    "Vous ne voyez et ne sentez plus rien, vous perdez tous vos sens un par un."
    "Vous perdez ensuite conscience."
    "..."
    jump s0

label c83:
    "Le corps de Billy est lourd."
    show bg décompression0
    "Vous arrivez néanmoins à le faire entrer dans un sas de décompression."
    pause 0.5
    show bg décompression1
    pause 0.5
    show bg décompression2
    pause 0.5
    show bg décompression3
    pause 0.5
    show bg décompression4
    pause 0.5
    show bg décompression5
    "Appareil prêt à éjecter."

    menu:
        "Éjecter Billy":
            jump c98
        "Remettre la pression":
            jump c99

label c84:

label c85:

label c86:

label c87:

label c88:

label c89:

label c90:

label c91:

label c92:

label c93:

label c94:

label c95:

label c96:

label c97:

label c98:
    "Le corps de Billy est éjecté."
    jump c108

label c99:
    "La pression remonte."
    pause 0.5
    show bg décompression4
    pause 0.5
    show bg décompression3
    pause 0.5
    show bg décompression2
    pause 0.5
    show bg décompression1
    pause 0.5
    show bg décompression0

label c100:
    play sound talk9
    b "In the morning, if it was in the afternoon, I would have said 17:05."

    menu:
        "Good.":
            jump c103

label c101:

label c102:
    play sound talk9
    b "I do it every day! And you have been telling me yesterday that I had to wake you up at 5:00."

    menu:
        "":
            jump c104

label c103:

label c104:

label c105:

label c106:

label c107:

label c108:

label c109:

label c110:

label c111:
    hide billy

label c112:

label c113:

label c114:

label c115:

label c116:

label c117:

label c118:

label c119:

label c120:

label c121:

    return