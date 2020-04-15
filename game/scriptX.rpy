label x0:
    "Après être passé par une phase de désintégration et de réintégration où vous voyez une lumière blanche et éblouissante, vous vous téléportez sur une planète étrange."
    scene bg xplanet
    menu:
        "Explorer":
            jump x1
        "Retourner au vaisseau":
            jump x2
        "Hurler":
            jump x3

label x1:
    "Après avoir observé la végétation étrangère et les roches diverses, et vous être rendu compte de l'air respirable, vous avez constaté que la planète était habitée."
    scene bg xplant
    "Vous remarquez une plante étrange avec une allure inofensive."
    menu:
        "Prendre des échantillons et se téléporter au vaisseau":
            jump x4
        "Toucher la plante":
            jump x5
        "Continuer d'explorer":
            jump x6
        "Attendre":
            jump x7

label x2:
    "Vous ne disposez pas d'un appareil de retéléport automatique."
    menu:
        "Wot?":
            jump x8
        "Qu'est ce qu'un appareil de retéléport automatique ?":
            jump x10
        "Explorer":
            jump x11
        "Hurler":
            jump x12

label x3:
    "Rien ne se passe."
    "En réalité, en même temps que vous avez hurlé, vous avez eu comme l'impression que quelqu'un hurlait en même temps que vous."
    menu:
        "Hurler encore":
            jump x13
        "Parler":
            jump x14
        "Explorer la planète":
            jump x17

label x4:
    "Après avoir ramassé quelques échantillons de plantes et roches, vous vous rendez compte de l'absence d'un appareil de retéléport automatique en votre possession et donc qu'il est impossible pour vous de retourner au vaisseau."
    menu:
        "Continuer d'explorer":
            jump x6
        "Toucher la plante inofensive":
            jump x9
        "Attendre":
            jump x7

label x5:
    scene bg xplantinvisible
    "La plante disparaît mais vous ne la traversez pas pour autant."
    "Elle a une texture visceuse et étrange."
    "Soudain, vous entendez un bruit juste derrière vous."
    menu:
        "Se retourner":
            jump x19
        "Rester immobile":
            jump x20

label x6:
    scene bg xplantplus
    "Vous trouvez de plus en plus de fleurs comme celle-ci."
    menu:
        "Explorer à gauche":
            jump x21
        "Explorer à droite":
            jump x22
        "Explorer devant vous":
            jump x23

label x7:
    "Au bout d'une vingtaine de seconde, la plante se met à bouger légèrement."
    scene bg xplantmove1 wait 0.5
    scene bg xplant wait 0.5
    scene bg xplantmove2 wait 0.5
    scene bg xplant
    menu:
        "Rester immobile":
            jump x24
        "Toucher la plante":
            jump x25

label x8:
    "Rien ne se passe."
    menu:
        "Wot?":
            jump x8
        "Explorer la planète":
            jump x11

label x9:
    "Lorsque vous vous retournez pour toucher la plante, vous vous appercevez quelle n'est plus là."
    scene bg xplantinvisible
    menu:
        "S'exclamer « Bah où est passée la plante ? »":
            jump x27
        "Rester immobile":
            jump x28
        "Se retourner":
            jump x29
label x10:
    show reteleportdevice
    "Un appareil de retéléport automatique est un outil permettant de retourner au derier endroit d'où vous vous êtes téléporté."
    "C'est un appareil essenciel en cas de téléportation."
    hide reteleportdevice
    menu:
        "Wot?":
            jump x8
        "Explorer":
            jump x11
        "Rester immobile":
            jump x26
        "Hurler":
            jump x12

label x11:
    scene bg xchoses
    "Après avoir observé la végétation étrangère et les roches diverses, et vous être rendu compte de l'air respirable, vous avez constaté que la planète était habitée."
    scene bg xplant
    "Vous remarquez une plante étrange avec une allure inofensive."
    menu:
        "Continuer d'explorer":
            jump x6
        "Toucher la plante inofensive":
            jump x9
        "Attendre":
            jump x7

label x13:
    "Vous avez la même impression qu'avant."
    "Vous avez d'ailleur l'impression étrange que ce cri est légèrement en avance par rapport au vôtre."
    menu:
        "Hurler encore":
            jump x15
        "Chercher l'individu hurlant en même temps que vous":
            jump x16
        "Explorer la planète":
            jump x18

    return
