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
    "Crier « Au secours ! »":
      jump s15

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
  play music music04cut1
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
  scene bg ssalle u
  pause 0.02
  scene bg ssalle d
  pause 0.02
  scene bg ssalle l
  pause 0.02
  scene bg ssalle u
  pause 0.02
  scene bg ssalle r
  pause 0.02
  scene bg ssalle d
  pause 0.02
  scene bg ssalle r
  pause 0.02
  scene bg ssalle l
  pause 0.02
  scene bg ssalle d
  pause 0.02
  scene bg ssalle u
  pause 0.02
  scene bg ssalle
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
  scene bg ssalle ani1
  "Le sol se met à trembler de manière continue."
  "Vous n'entendez cependant toujours aucun son."

  menu:
    "Crier « Au secours ! »":
      jump s15
    "Frapper dans vos mains":
      jump s16
    "Courir":
      jump s17

label s15:
  scene bg ssalle
  "Le sol s'arrête soudainement de trembler."
  "Vous sentez une présence dérrière vous."
  S "Hey!"
  S "Who are you to shout like this?"

  menu:
    "Se retourner":
      jump s18
    "Ignorer":
      jump s19

label s16:
  "Rien ne se passe."
  "Vous n'entendez pas le claquement de vos mains."

  menu:
    "Crier « Au secours ! »":
      jump s15
    "Courir":
      jump s17

label s17:
  scene bg ssalle ani2
  "Le sol se met à trembler encore plus rapidement."

  menu:
    "Continuer de courir":
      jump s20
    "S'arrêter":
      jump s21
    "Crier « Au secours ! »":
      jump s15

label s18:
  show barry base
  window hide
  pause 1
  window auto
  S "Have you been jumpin' in the teleportation pool?"
  S "Bad move."

  menu:
    "Yes, I wanted to try and see what was inside this pool.":
      jump s22
    "It was just for fun.":
      jump s23
    "I thought it would teleport me on a heavenly planet.":
      jump s24
    "Who are you?":
      jump s25

label s19:
  S "Hey!"
  S "I'm talking to you!"

  menu:
    "Se retourner":
      jump s18
    "Ignorer":
      jump s26

label s20:
  "Le tremblement est trop intense."
  scene bg w_b ani2
  "Vous vous évanouissez."
  window hide
  pause 3
  window auto
  scene c0c0c0
  "Vous  quelqu'un vous appelle."
  S "Colonel Robson?"

  menu:
    "Yes, it's me.":
      jump s27
    "Who are you?":
      jump s28
    "How do you know my name?":
      jump s29
    "Do I know you?":
      jump s30
    "Ne rien dire":
      jump s31

label s21:
  scene bg ssalle ani1
  "Le sol tremble plus lentement."

  menu:
    "Attendre plus longtemps":
      jump s32
    "Courrir":
      jump s33

label s22:
  S "See what was inside the pool?"
  S "Haven't you noticed the warning sheat ?"
  S "That's what I said. Bad move."

  menu:
    "But it's not so bad, I am not alone anymore.":
      jump s34
    "I think this is not. It might be interesting.":
      jump s35
    "In fact, yes. It is a bad move.":
      jump s36
    "Who are you?":
      jump s25

label s23:
  S "Just for fun?"
  S "Are you mad?"

  menu:
    S "“Never jump into the teleportation pool before setting a destination on the teleportation device.”"
    #OYE timed menu with « S "“Never jump into the teleportation pool before setting a destination on the teleportation device.”" » above the menu.
    "Interrompre":
      jump s37
    "Le laisser parler":
      $ True
  S "That's what Billy told me before pushing me into this fucking pool."

  menu:
    "Why Billy pushed you down the pool?":
      jump s38
    "I knew Billy was evil!":
      jump s39
    "Talk with a more appropriate language please!":
      jump s40
    "Who are you?":
      jump s41

label s24:

label s25:

label s26:

label s27:

label s28:
  a "My name's Barry."
  #OYE

label s29:

label s30:

label s31:

label s32:

label s33:
  "Le sol se met à trembler plus rapidement."
  window hide
  scene bg ssalle ani1
  pause 1
  window auto
  "Le tremblement est trop intense."
  scene bg w_b ani2
  "Vous vous évanouissez."
  window hide
  pause 3
  window auto
  scene c0c0c0
  "Vous  quelqu'un vous appelle."
  S "Colonel Robson?"

  menu:
    "Yes, it's me.":
      jump s27
    "Who are you?":
      jump s28
    "How do you know my name?":
      jump s29
    "Do I know you?":
      jump s30
    "Ne rien dire":
      jump s31

label s34:
  S "Are you?"
  hide barry
  with Fade(1)

  menu:
    "Chercher l'homme":
      jump s42
    "Hurler":
      jump s43
    "Se dire « Qu'est-ce qui se passe ? »":
      jump s44

label s35:

label s36:

label s37:

label s38:

label s39:

label s40:

label s41:

label s42:

label s43:

label s44:

  return
