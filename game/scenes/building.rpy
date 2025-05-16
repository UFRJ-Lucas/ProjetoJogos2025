label building:
    play sound "audio/music/building_ambience.mp3" loop fadein 1.5 

    # Primeira piscada (rápida visão do prédio comercial)
    scene building_day
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/building/01.wav" 
    "Artificial lights make the day resemble night."

    voice "audio/narrador/building/02.wav" 
    "At the distance you hear those royalty free music that no one really care about."

    voice "audio/narrador/building/03.wav" 
    "Rehearsed smiles, shiny corridors, and an artificial scent, like a building's perfume"

    voice "audio/narrador/building/04.wav" 
    "You feel no familiarity with this place, nor its plastic-wrapped food."

    voice "audio/narrador/building/11.wav" 
    "The time here goes by, the lure of those display window may catch your atention for a little while."
    
    window hide
    $ renpy.pause(0.3)

    scene building_night 
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/building/05.wav" 
    "Actually, it's like you seen places like this exact one several times."

    voice "audio/narrador/building/06.wav" 
    "There are other places that makes you feel like this too, in other ways..."


label performance:
    "Which place was that?"
    menu:
        "A church.":
            voice "audio/narrador/building/07.wav" 
            "The place that precedes this one."

            voice "audio/narrador/building/08.wav"
            "Once those were the highest buildings."

            voice "audio/narrador/building/09.wav" 
            "Focus on the bell and the acoustics..."
            scene black
            with fade
            jump church

        "A theather.":
            voice "audio/narrador/building/10.wav" 
            "People living other lives, pretending to be someone else."
            voice "audio/narrador/building/12.wav" 
            "There are astonishing similarities, right?"
            voice "audio/narrador/building/13.wav" 
            "When were the last time you were inside one of these?"
            scene black
            with fade
            jump theater

        "The city center." if visit_city:
            voice "audio/narrador/building/14.wav" 
            "This place is nothing special, indeed. There are countless of them throughout the city."
            voice "audio/narrador/building/15.wav" 
            "Have you ever been to the city center at night?"
            scene black
            with fade
            jump city_night

        
        
        


    