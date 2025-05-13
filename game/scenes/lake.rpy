label park:
    play lake "audio/music/lake_ambience.mp3" loop fadein 1.5

    # Primeira piscada (rápida visão do parque)
    scene lake_day
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/lake/01.wav" #faltando
    "You walk through a path that doesn't seem to end."

    voice "audio/narrador/lake/02.wav" #faltando
    "Standing on top of a hill, you can see your destination."

    voice "audio/narrador/lake/03.wav" #faltando
    "Below, the water of the lake looks still, there are many trees."

    voice "audio/narrador/lake/04.wav" #faltando
    "The sun is setting, painting evetything golden, the blue of the lake, the green from vegetation."

    voice "audio/narrador/lake/05.wav" #faltando
    "It even blur those people that are in front of you."

    voice "audio/narrador/lake/06.wav" #faltando
    "You are not alone anymore, but do you know them?"


label strangers:
    "Who are they?"
    menu:
        "I think they are my friends.":
            voice "audio/narrador/lake/07.wav" #faltando
            "Are they? Remeber faces? Or names?"

            voice "audio/narrador/building/08.wav" #faltando
            "There is something that can explain you feeling like you know them:"

            voice "audio/narrador/building/09.wav" #faltando
            "A frail memory, that comes in waves."
            jump breach

        "Could they be my family?.":
            voice "audio/narrador/lake/10.wav" #faltando
            "Are they? Remeber faces? Or names?"

            voice "audio/narrador/building/11.wav" #faltando
            "There is something that can explain you feeling like you know them:"

            voice "audio/narrador/building/12.wav" #faltando
            "A fleet memory, made with asphalt and covered in mist."
            jump road

        "I think they are just strangers.":
            voice "audio/narrador/building/13.wav" #faltando
            "You are familiar with people passing through you everyday, aren't you?"

            voice "audio/narrador/building/14.wav" #faltando
            "Paying atention to this makes you think about the horn of cars."

            voice "audio/narrador/building/15.wav" #faltando
            "And it's like you could see those tall buildings."
        
        
        


    