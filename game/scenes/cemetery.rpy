label cemetery:
    play sound "audio/music/grave_ambience.mp3" loop fadein 1.5

    # Primeira piscada (rápida visão do parque)
    scene cemetery_day
    with dissolve
    $ renpy.pause(0.3)
    
    voice "audio/narrador/cemetery/01.wav" 
    "Silence here is dense, as if this place had an aura of its own."

    voice "audio/narrador/cemetery/02.wav" 
    "The only thing who dares to break it is the howl of the wind."


    $ renpy.pause(1.0)

    voice "audio/narrador/cemetery/03.wav" 
    "With each step, you feel the moist soil and your feet sink gently in the ground."

    voice "audio/narrador/cemetery/04.wav" 
    "The place is populated by flowers, but most of them are dead, like everything in this place."

    voice "audio/narrador/cemetery/05.wav" 
    "The burial grounds bring you a wary peace, and remember you of stolen futures."

    voice "audio/narrador/cemetery/06.wav"
    "Who is the one that rest in this place?"

    menu:
        "A close friend.":
            voice "audio/narrador/cemetery/07.wav"
            "And yet, neither their name nor face can come to mind."

            voice "audio/narrador/cemetery/08.wav" 
            "You feel their loss, but is it enough?"

            voice "audio/narrador/cemetery/09.wav" 
            "Nothing was feeling right since you arrived here, and it's getting worse."
            jump lost

        "A dear family member":
            voice "audio/narrador/cemetery/07.wav" 
            "And yet their name and face can't come to mind."

            voice "audio/narrador/cemetery/08.wav" 
            "But you feel their loss, is it enough?"

            voice "audio/narrador/cemetery/09.wav" 
            "Nothing was feeling right since you arrived here, and it's getting worse"
            jump lost

        "I am not really sure...":
            voice "audio/narrador/cemetery/10.wav" 
            "The eerie nature of this place makes you uneasy."

            voice "audio/narrador/cemetery/11.wav" 
            "But you feel a sense of loss, don't you?"

            voice "audio/narrador/cemetery/12.wav"
            "Nothing was feeling right, but since you arrived here, it's getting worse."
            jump lost

label lost:
    
    scene cemetery_night
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/cemetery/13.wav"
    "Maybe it is all the stories of the lost and the damned getting to you."

    voice "audio/narrador/cemetery/14.wav" 
    "Most of the media you consume depicts this place as somewhere you shouldn't be."

    voice "audio/narrador/cemetery/15.wav"
    "They are not completely wrong though, this is the place of the dead."

    voice "audio/narrador/cemetery/16.wav" 
    "So why do you feel this wary peace being here?"

    menu:
        "The absence of noise.":
            voice "audio/narrador/cemetery/17.wav" 
            "Sometimes you think that even the animals respect this space."
            voice "audio/narrador/cemetery/18.wav"
            "The legacy of those who are not here anymore, but they're missed."
            jump slumber

        "Acts of love and remembrance, even if it's too late.":
            voice "audio/narrador/cemetery/19.wav"
            "People vanish, their presence stay."
            voice "audio/narrador/cemetery/20.wav"
            "Those who were touched by their lives are still somewhere out there."
            voice "audio/narrador/cemetery/21.wav"
            "Will be someone carrying your loss?"
            jump slumber

        "I just find this place has a vibe":
            voice "audio/narrador/cemetery/17.wav" 
            "Sometimes you think that even the animals respect this space."
            voice "audio/narrador/cemetery/23.wav"
            "The atmosphere is unmatched, the appeal is hard to deny."
            voice "audio/narrador/cemetery/24.wav" 
            "This explain why so many people believe that there is something supernatural here."
            voice "audio/narrador/cemetery/25.wav" 
            "And you feel a conection to this place."
            jump slumber
        
label slumber:
    voice "audio/narrador/cemetery/26.wav"
    "The longer you stay here, more you find it conforting."
    voice "audio/narrador/cemetery/27.wav" 
    "You are getting it now, this is your place."
    voice "audio/narrador/cemetery/28.wav"
    "Your home, forever and ever."
    window hide
    $ renpy.pause(1)
    play sound "audio/sfx/clue_sfx.wav"
    "{b}Ending 4 - Eternal Resting Place{/b}"
    return


    