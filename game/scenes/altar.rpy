label altar:
    play sound "audio/music/altar_ambience.mp3" loop fadein 1.5 #achar um arquivo

    scene altar #faltando
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/altar/01.wav" # faltando
    "Alguma coisa em latim."

    #fazer o personagem do padre. Adicionar novo dublador

    menu:
        