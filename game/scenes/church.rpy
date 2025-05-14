label church:
    play sound "audio/music/church_ambience.mp3" loop fadein 1.5 #achar um arquivo

    # Primeira piscada (rápida visão do parque)
    scene church #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)
    
    voice "audio/narrador/church/01.wav" #faltando
    "Steps are amplified by the old floor."

    voice "audio/narrador/church/02.wav" #faltando
    "The echo spreads in the walls, corridors and go to the very high ceiling."

    voice "audio/narrador/church/03.wav" #faltando
    "This gives you the impression that this sounds of steps come from all directions."

    voice "audio/narrador/church/04.wav" #faltando
    "Old wood and candles, that is the best way to describe what this place smells, the scent is intence, and also mild."

    voice "audio/narrador/church/05.wav" #faltando
    "Silence is deep, it is so present, affecting the mood of the place as if the silence itself was heavy."

    voice "audio/narrador/church/06.wav" #faltando
    "Sunlight shines through colorful stainede glasses. What happens to give this place live, and makes it feel magic."

    voice "audio/narrador/church/07.wav" #faltando
    "But something is off, your chest ache."

    voice "audio/narrador/church/08.wav" #faltando
    "You are not a vampire, you won't burn, but maybe you should go."

label presence:
    menu:
        "Should I go to the altar?.":
            voice "audio/narrador/church/09.wav" #faltando
            "These altars are stunning."
            voice "audio/narrador/church/14.wav" #faltando
            "And it is never too late to redeem yourself and do the right thing."
            jump altar

        "I just want to go home.":
            voice "audio/narrador/church/10.wav" #faltando
            "Religious people call this the 'house of god'."
            voice "audio/narrador/church/13.wav" #faltando
            "Nothing more fair than you wanting to go to your own."
            jump room

        "I'm not feeling very well, I want to get out from here.":
            voice "audio/narrador/church/11.wav" #faltando
            "Take a deep breath, it could be only anxiety."
            voice "audio/narrador/church/12.wav" #faltando
            "And if you insist, we can go. That is the closest door."
            jump graveyard
        
        
        


    