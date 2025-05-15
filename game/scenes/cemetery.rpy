label cemetery:
    play sound "audio/music/grave_ambience.mp3" loop fadein 1.5 #achar um arquivo

    # Primeira piscada (rápida visão do parque)
    scene cemetery_day #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)
    
    voice "audio/narrador/cemetery/01.wav" #faltando
    "Silence here is dense, as if this place had an aura of its own."

    voice "audio/narrador/cemetery/02.wav" #faltando
    "The only thing who dares to break it is the howl of the wind."

    play sound "audio/sfx/wind" #faltando

    $ renpy.pause(1.0)

    voice "audio/narrador/cemetery/03.wav" #faltando
    "With each step, you feel the moist soil and your feet sink gently in the ground."

    voice "audio/narrador/cemetery/04.wav" #faltando
    "The place is populated by flowers, but most of them are dead, like everything in this place."

    voice "audio/narrador/cemetery/05.wav" #faltando
    "The burial grounds bring you a wary peace, and remember you of stolen futures."


label grave:
    voice "audio/narrador/cemetery/06.wav" #faltando
    "Who is the one that rest in this place?"
    menu:
        "A close friend.":
            voice "audio/narrador/cemetery/07.wav" #faltando
            "And yet their name and face can't come to mind."

            voice "audio/narrador/cemetery/08.wav" #faltando
            "But you feel their loss, is it enough?"

            voice "audio/narrador/cemetery/09.wav" #faltando
            "Nothing was feeling right but since you arrived here it's getting worse."
            jump lost

        "A dear family member":
            voice "audio/narrador/cemetery/07.wav" #faltando
            "And yet their name and face can't come to mind."

            voice "audio/narrador/cemetery/08.wav" #faltando
            "But you feel their loss, is it enough?"

            voice "audio/narrador/cemetery/09.wav" #faltando
            "Nothing was feeling right but since you arrived here it's getting worse."
            jump lost

        "I am not really sure...":
            voice "audio/narrador/cemetery/10.wav" #faltando
            "The eerie nature of this place makes you uneasy."

            voice "audio/narrador/cemetery/11.wav" #faltando
            "But you feel a sense of loss, don't you?"

            voice "audio/narrador/cemetery/12.wav" #faltando
            "Nothing was feeling right but since you arrived here it's getting worse."
            jump lost

label lost:
    voice "audio/narrador/cemetery/13.wav" #faltando
    "Maybe is it all the stories of the lost and the damned getting to you."

    voice "audio/narrador/cemetery/14.wav" #faltando
    "Most of the media you consume depicts this place as somewhere you shouldn't be."

    voice "audio/narrador/cemetery/15.wav" #faltando
    "They are not completely wrong though, this is the place of the dead."

    voice "audio/narrador/cemetery/16.wav" #faltando
    "So why do you feel this peace being here?"

    menu:
        "The absence of noise.":
            voice "audio/narrador/cemetery/17.wav" #faltando
            "Sometimes you think that even the animals respect this space."
            voice "audio/narrador/cemetery/18.wav" #faltando
            "The legacy of those who are not here anymore, but they're missed."
            jump slumber

        "Acts of love and remembrance, even if it's too late.":
            voice "audio/narrador/cemetery/19.wav" #faltando
            "People vanish, their presence stay."
            voice "audio/narrador/cemetery/20.wav" #faltando
            "The people who was touched by their life are still somewhere out there."
            voice "audio/narrador/cemetery/21.wav" #faltando
            "Will be someone carrying your loss?"
            jump slumber

        "I just find this place has a vibe":
            voice "audio/narrador/cemetery/22.wav" #faltando
            "Sometimes you think that even the animals respect this space."
            voice "audio/narrador/cemetery/23.wav" #faltando
            "The atmosphere is unmatched, the appeal is hard to deny."
            voice "audio/narrador/cemetery/24.wav" #faltando
            "This explain why so many people believe that there is something supernatural here."
            voice "audio/narrador/cemetery/25.wav" #faltando
            "And you feel a conection to this place."
            jump slumber
        
label slumber:
    voice "audio/narrador/cemetery/26.wav" #faltando
    "The longer you stay here, more you find it conforting."
    voice "audio/narrador/cemetery/27.wav" #faltando
    "You are getting it now, this is you place."
    voice "audio/narrador/cemetery/28.wav" #faltando
    "Your home, forever and ever."
    "{b}Ending 3 - Eternal Resting Place{/b}"


    