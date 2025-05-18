label office:
    play sound "audio/music/office_ambience.mp3" loop fadein 1.5

    scene office_day
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/office/01.wav" 
    "You arrive at an office. A low hum fills the air and you hear the clatter of keyboards being used to write reports."

    voice "audio/narrador/office/02.wav" 
    "You see, right in front of you, a desk with nothing but a notebook and a computer. When you get closer the monitor lights up."

    voice "audio/narrador/office/03.wav" 
    "There is an email on the screen, addressed to you. It's your boss, questioning you about those reports you were meant to send."

    voice "audio/narrador/office/04.wav" 
    "You panic for a moment. It's better to just start working on these as soon as possible."

    voice "audio/narrador/office/05.wav" 
    "It shouldn't take long."

    stop sound fadeout 1.5

    scene black 
    with fade
    pause 1.0

    "A few hours later."

    scene office_night
    with fade

    voice "audio/narrador/office/06.wav"
    "That sure took longer than you expected."

    play sound "audio/sfx/ping.mp3"

    voice "audio/narrador/office/07.wav" 
    "You start to rise from your chair before you're interrupted by a sound coming from the computer. It's another email."

    voice "audio/narrador/office/08.wav" 
    "One more task to do. Something about the email feels strange, but you decide against questioning it."

    play sound "audio/sfx/ping.mp3"
    pause 1.0

    voice "audio/narrador/office/09.wav" 
    "Almost there. Just a bit more stuff to do."

    play sound "audio/sfx/ping.mp3"
    pause 1.0

    voice "audio/narrador/office/10.wav" 
    "You will move on with your life. As soon as you're done here."

    scene black 
    with fade
    pause 1.0

    play sound "audio/sfx/ping.mp3"
    pause 2.0

    play sound "audio/sfx/ping.mp3"
    pause 2.5

    play sound "audio/sfx/ping.mp3"
    pause 1.5

    play sound "audio/sfx/ping.mp3"
    pause 3.0

    play sound "audio/sfx/ping.mp3"
    pause 1.0

    voice "audio/narrador/office/11.wav"
    "Almost there..."
    
    window hide
    $ renpy.pause(1)
    play sound "audio/sfx/clue_sfx.wav"
    "{b}Ending 6 - Work to do{/b}"
    return
