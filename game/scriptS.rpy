label s0:
    window hide
    scene bg ssalle
    play music music04
    pause 1
    window auto
    "Lorsque vous vous reveillez, vous êtes debout, au milieu d'une immense salle dont vous ne voyez pas les murs ni le plafond."
    "La seule lumière visible de la pièce semble venir de vous-même, de l'intérieur de votre corps."
    "Vous n'arrivez pas à identifier le temps pendant lequel vous avez été inconscient, cela à pu être quelques minutes comme quelques années."

    menu:
        "Marcher tout droit":
            jump s1
        "Aller derrière vous":
            jump s2
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5

label s1:
    "Comme le sol est extrêmement rectiligne, vous ne pouvez donc compter que sur votre mémoire pour savoir si vous avez avancé ou si vous êtes juste resté sur place."

    menu:
        "Marcher tout droit":
            jump s6
        "Aller derrière vous":
            jump s2
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5

label s2:

    "Comme le sol est extrêmement régulier, vous ne pouvez donc compter que sur votre mémoire pour savoir si vous avez reculé, avancé ou si vous êtes juste resté sur place."

    menu:
        "Marcher tout droit":
            jump s6
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5

label s3:
    "Vous ne voyez autour de vous rien que le néan."
    "Derrière, devant, à gauche, à droite, rien."

    menu:
        "Marcher":
            jump s6
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5

label s4:
    "La lumière semble réelement venir de l'intérieur de vous-même, votre corps est comme baigné de lumière, si bien que cela vous ébloui, et cela procure une sensation très étrange."

    menu:
        "Marcher":
            jump s6
        "Rester immobile":
            jump s8

label s5:
    "Rien ne se passe."

    menu:
        "Marcher tout droit":
            jump s6
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5

label s6:
    "Vous ne pouvez compter que sur votre mémoire pour savoir si vous avez réelement avancé."
    "Vous n'arriverez probablement à rien en marchant ainsi."

    menu:
        "Marcher":
            jump s7
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5

label s7:
    "Vous n'arriverez probablement à rien en marchant ainsi."

    menu:
        "Marcher":
            jump s7
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Rester immobile":
            jump s5
        "Dormir":
            jump s9

label s8:
    "Rien ne se passe."

    menu:
        "Marcher tout droit":
            jump s6
        "Regarder autour de vous":
            jump s3
        "Chercher plus précisément l'origine de la lumière":
            jump s4
        "Appeler à l'aide":
            jump s10

label s9:
    show bg black
    play music music05
    "Vous vous endormez immédiatement et d'un sommeil profond."
    window hide
    pause 3
    window auto
    "Lorsque vous vous réveillez, vous ne voyez plus rien."

label s10:
    "Aucun son ne sort de votre bouche."

    menu:
        "Hurler":
            jump s11
        "Frapper le sol":
            jump s12
        "Frapper dans vos mains":
            jump s13

label s11:
    "Aucun son ne sort de votre bouche."
    "Rien ne semble avoir bougé."

    menu:
        "Hurler encore":
            jump s11
        "Frapper le sol":
            jump s12
        "Frapper dans vos mains":
            jump s13

label s12:
    "Vous n'entendez rien mais vous sentez le sol trembler."

    menu:
        "Frapper plus fort":
            jump s14
        "Hurler":
            jump s11
        "Frapper dans vos mains":
            jump s13

label s13:
    "Vos mains ne produisent aucun son."

    menu:
        "Hurler":
            jump s11
        "Frapper encore dans vos mains":
            jump s13

label s14:

label s15:

    return
