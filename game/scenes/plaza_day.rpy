label plaza_day:
    play sound "audio/music/plaza_ambience.mp3" loop fadein 1.5

    # Primeira piscada (rápida visão da praça)
    scene plaza_day
    with dissolve
    $ renpy.pause(0.3)

    $ memories_visited.add("PLAZA_NOTEBOOK") # memoria do caderno de rascunhos
    
    voice "audio/narrador/plaza/01.wav"
    "The sunlight is golden, almost heavy."

    voice "audio/narrador/plaza/02.wav"
    "Trees sway gently in a breeze that smells of childhood."

    voice "audio/narrador/plaza/03.wav"
    "Laughter echoes from a distance — muffled, like through water."

    voice "audio/narrador/plaza/04.wav"
    "Children run, chasing bubbles that vanish before reaching the sky."

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
            scene black
            with fade
            jump building

        "Try to draw something.":
            voice "audio/narrador/plaza/18.wav" 
            "You pick a pencil and start thinking of ideas to sketch. Maybe that could take your mind off of... everything."

            voice "audio/narrador/plaza/19.wav"
            "Soon you start tracing faint shapes in the paper, but inspiration fails to strike you. Your mind is a blank."

            voice "audio/narrador/plaza/20.wav"
            "There was a place you would go whenever you found yourself in these kinds of situation."

            voice "audio/narrador/plaza/21.wav"
            "You knew that often times a nice warm cup of coffee would be enough to get your creative juices flowing again."
            scene black
            with fade
            jump cafe

        "Close it and leave it there.":
            voice "audio/narrador/plaza/14.wav"
            "Something inside you recognizes the utter uninportance of it all."
            voice "audio/narrador/plaza/16.wav" 
            "The sun that burnt slighly, now is colder and golder. This trigger some emotions."
            voice "audio/narrador/plaza/15.wav"
            "Even the sounds of the plaza fizzle, the water in the fountain is completely still."
            voice "audio/narrador/plaza/17.wav" 
            "The water, the sun. Makes you think of that place..."
            scene black
            with fade
            jump lake
        
        
        


    