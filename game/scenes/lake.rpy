label lake:
    play sound "audio/music/lake_ambience.mp3" loop fadein 1.5 

    # Primeira piscada (rápida visão do lago e a trilha)
    scene lake_day 
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/lake/01.wav" 
    "You walk through a path that doesn't seem to end."

    voice "audio/narrador/lake/02.wav"
    "Standing on top of a hill, you can see your destination."

    voice "audio/narrador/lake/03.wav"
    "Forth, the water of the lake looks still. Around, there are many trees."

    voice "audio/narrador/lake/04.wav"
    "The sun is setting, painting evetything golden, the blue of the lake, the green from vegetation."

    voice "audio/narrador/lake/05.wav"
    "It even blur those people that are in front of you."

    voice "audio/narrador/lake/06.wav" 
    "You are not alone anymore, but do you know them?"


label strangers:
    scene lake_night
    with dissolve
    $ renpy.pause(0.3)
    "Who were they?"
    menu:
        "I think they are my friends.":
            voice "audio/narrador/lake/07.wav"
            "Are they? Remeber faces? Or names?"

            voice "audio/narrador/lake/08.wav" 
            "There is something that can explain you feeling like you know them:"

            voice "audio/narrador/lake/09.wav"
            "A frail memory, that comes in waves."
            scene black
            with fade
            jump beach

        "Could they be my family?":
            voice "audio/narrador/lake/07.wav" 
            "Are they? Remeber faces? Or names?"

            voice "audio/narrador/lake/08.wav" 
            "There is something that can explain you feeling like you know them:"

            voice "audio/narrador/lake/12.wav"
            "A fleet memory, made with asphalt and covered in mist."
            scene black
            with fade
            jump road

        "I think they are just strangers.":
            voice "audio/narrador/lake/10.wav" 
            "You are familiar with people passing through you everyday, aren't you?"

            voice "audio/narrador/lake/11.wav"
            "Paying attention to this makes you think about the horn of cars."

            voice "audio/narrador/lake/13.wav"
            "And it's like you could see those tall buildings."
            scene black
            with fade
            jump city
        
        
        


    