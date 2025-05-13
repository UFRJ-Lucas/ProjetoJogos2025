default count = 0
default calling = True
default body = True

label park:
    play sound "audio/music/plaza_ambience.mp3" loop fadein 1.5

    # Primeira piscada (rápida visão do parque)
    scene plaza_day
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/plaza/01.wav"
    "The sunlight is golden, almost heavy."

    voice "audio/narrador/plaza/02.wav"
    "Trees sway gently in a breeze that smells of childhood."

    voice "audio/narrador/plaza/03.wav"
    "Laughter echoes from a distance — muffled, like through water."

    voice "audio/narrador/plaza/04.wav"
    "Children run, chasing soap bubbles that vanish before reaching the sky."

    voice "audio/narrador/plaza/05.wav"
    "You sit on a worn bench, wood splintered by time, and something aches in your chest."

    voice "audio/narrador/plaza/06.wav"
    "A sketchbook lies beside you."

    voice "audio/narrador/plaza/07.wav"
    "A sketchbook lies beside you."

    voice "audio/narrador/plaza/09.wav"
    "You open it."

    voice "audio/narrador/plaza/10.wav"
    "The pages are filled with blurry lines, half finished-drawings, colors that seem to melt."

label book:
    "What do you do with the sketchbook?"
    menu:
        "Try to remember who I was drawing.":
            voice "audio/narrador/plaza/11.wav"
            "You can't remember their face, nor their name"

            voice "audio/narrador/plaza/12.wav"
            "But you can remember where you know them."

            voice "audio/narrador/plaza/13.wav"
            "You saw them almost everyday..."
            jump office

        "Close it and leave it there.":
            voice "audio/narrador/plaza/14.wav"
            "Something inside you recognizes the utter uninportance of it all."
            voice "audio/narrador/plaza/16.wav" #faltando
            "The sun that burnt slighly, now is colder and golder. This trigger some emotions."
            voice "audio/narrador/plaza/15.wav"
            "Even the sounds of the plaza fizzle, the water in the fountain is completely still."
            voice "audio/narrador/plaza/17.wav" #faltando
            "The water, the sun. Makes you think of that place..."
            jump lake
        
        
        


    