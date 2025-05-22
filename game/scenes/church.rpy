label church:
    play sound "audio/music/church_ambience.mp3" loop fadein 1.5
    $ renpy.pause(1)

    # Primeira piscada (rápida visão da igreja)
    scene church
    with dissolve
    $ renpy.pause(1)

    scene church_in
    with dissolve
    $ renpy.pause(1)
    
    voice "audio/narrador/church/01.wav" 
    "Steps are amplified by the old floor."

    voice "audio/narrador/church/02.wav" 
    "The echo spreads in the walls, corridors and go to the very high ceiling."

    voice "audio/narrador/church/03.wav" 
    "This gives you the impression that this sounds of steps come from all directions."

    voice "audio/narrador/church/04.wav"
    "Old wood and candles, that is the best way to describe what this place smells, the scent is intence, and also mild."

    voice "audio/narrador/church/05.wav" 
    "Silence is deep, it is so present that is affecting the mood of the place as if the silence itself was heavy."

    voice "audio/narrador/church/06.wav"
    "Sunlight shines through colorful stained glasses. This gives the place life, and makes it feel magic."

    voice "audio/narrador/church/07.wav"
    "But something is off, your chest ache."

    voice "audio/narrador/church/08.wav"
    "You are not a vampire, you won't burn, but maybe you should move."

    $ memories_visited.add("CHURCH_VISITED")

label presence:
    menu:
        "Should I go to the altar?.":
            voice "audio/narrador/church/09.wav" 
            "These altars are stunning."
            voice "audio/narrador/church/14.wav" 
            "And it is never too late to redeem yourself and do the right thing."
            scene black
            with fade
            jump altar

        "I just want to go home.":
            voice "audio/narrador/church/10.wav" 
            "Religious people call this the 'house of god'."
            voice "audio/narrador/church/13.wav" 
            "Nothing more fair than you wanting to go to your own."
            scene black
            with fade
            jump house

        "I'm not feeling very well, I want to get out from here.":
            scene church
            with dissolve
            $ renpy.pause(1)

            voice "audio/narrador/church/11.wav" 
            "Take a deep breath, it could be just anxiety."

            voice "audio/narrador/church/12.wav" 
            "And if you insist, we can go now."

            voice "audio/narrador/church/15.wav" 
            "There is a little road in the backyard of the church, you should check it out."
            scene black
            with fade
            jump cemetery
        
        
        


    