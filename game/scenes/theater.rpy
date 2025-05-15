label theater:
    play sound "audio/music/theater_ambience.mp3" loop fadein 1.5 #achar um arquivo

    # Primeira piscada (rápida visão do teatro)
    scene theater #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/theater/01.wav" #faltando
    "Muffled sounds of whispers comes from all directions."

    voice "audio/narrador/theater/02.wav" #faltando
    "Velvet and dust make a distinct smell."

    voice "audio/narrador/theater/03.wav" #faltando
    "The place is not that bright, even with the lights turn on."

    voice "audio/narrador/theater/04.wav" #faltando
    "You hear a ring three times, the show is going to start."

    voice "audio/narrador/theater/05.wav" #faltando
    stop sound
    "All those whispers stop when the lights are turn off."

    voice "audio/narrador/theater/06.wav" #faltando
    "You hear a ring three times, the show is going to start."

    voice "audio/narrador/theater/07.wav" #faltando
    "A single flahs of light tear the darkness."

    voice "audio/narrador/theater/08.wav" #faltando
    "You have the impression that something that is equally holy and profane is going to start."


label play:

    voice "audio/narrador/theater/09.wav" #faltando
    "A single actor enters the scene."

    voice "audio/narrador/theater/10.wav" #faltando
    "They seens lost, and alone."

    voice "audio/narrador/theater/11.wav" #faltando
    "Time goes by and it looks like the play is a long monologue."

    menu:
        "How can just one actor make a whole play?" if not monologue:
            voice "audio/narrador/theater/12.wav" #faltando
            "They are performing alone, but there are the prop artists, writers..."

            voice "audio/narrador/theater/13.wav" #faltando
            "Directors, people who are in charge of the light, clothes, music, and so on."

            voice "audio/narrador/theater/14.wav" #faltando
            "They are just the star, the face of the play, but there are more unseen faces behind it."
            jump star
            

        "I wanna know more about his story.":
            voice "audio/narrador/theater/26.wav" #faltando
            "The character doesn't remember a thing, people and memories are vanishing from their mind."

            voice "audio/narrador/theater/27.wav" #faltando
            "What is causing this is uncertain, but it's made clear by the actor that their character is full of anguish."

            voice "audio/narrador/theater/28.wav" #faltando
            "They remember certain places, and what they made them feel in those moments."

            voice "audio/narrador/theater/29.wav" #faltando
            "So there is just specific places and emotions, but not people and nothing about them."

            voice "audio/narrador/theater/30.wav" #faltando
            "High concept, very subjective."

            voice "audio/narrador/theater/31.wav" #faltando
            "In the end, the character finds out who they are by finding a way home."

            voice "audio/narrador/theater/32.wav" #faltando
            "Applause, lights, and scene."

            $ play_saw = True

            jump after


        "This is not the kind of show I am familiar to.":
            voice "audio/narrador/theater/33.wav" #faltando
            "You are familiar with other genres of theater, aren't you?"

            jump genre
        
        
label star:
    voice "audio/narrador/theater/15.wav" #faltando
    "It is very common to some people to pass unoticed."

    voice "audio/narrador/theater/16.wav" #faltando
    "Don't you agree?"

    menu:
        "I thought very little about this.":
            voice "audio/narrador/theater/18.wav" #faltando
            "You do not need to worry about this, it's just a thought after all."

            voice "audio/narrador/theater/19.wav" #faltando
            "Most people don't even think about this."

            voice "audio/narrador/theater/20.wav" #faltando
            "And now your mind is gravitating around this concept. The invisibles."

            voice "audio/narrador/theater/21.wav" #faltando
            "Who are those invisible people in your life? Do you even have them?"

            voice "audio/narrador/theater/22.wav" #faltando
            "You can visualize the answer."
            jump school

        "I wanna pay attention in the story of the play.":
            voice "audio/narrador/theater/17.wav" #faltando
            "Right, let's recall what was happening."
            $ monologue = True
            jump play

        "I sometimes feel like I am one of these people.":
            voice "audio/narrador/theater/23.wav" #faltando
            "Of course you do, you indeed are."
            voice "audio/narrador/theater/24.wav" #faltando
            "When was the last time you were given credit and received proper praise?"
            voice "audio/narrador/theater/25.wav" #faltando
            "There was a place that always made you feel like this."
            jump office


label genre:
    voice "audio/narrador/theater/34.wav" #faltando
    "Comming to thing of this, which genre is you favorite?"
    menu:
        "Romance":
            voice "audio/narrador/theater/49.wav" #faltando
            "You weren't lucky with the genre, but the play can't be much longer."
            voice "audio/narrador/theater/50.wav" #faltando
            "Soon enough the lights will be turn on."
            $ renpy.pause(1)
            jump after
        "Drama":
            voice "audio/narrador/theater/49.wav" #faltando
            "You weren't lucky with the genre, but the play can't be much longer."
            voice "audio/narrador/theater/50.wav" #faltando
            "Soon enough the lights will be turn on."
            $ renpy.pause(1)
            jump after
        "Musical":
            voice "audio/narrador/theater/49.wav" #faltando
            "You weren't lucky with the genre, but the play can't be much longer."
            voice "audio/narrador/theater/50.wav" #faltando
            "Soon enough the lights will be turn on."
            $ renpy.pause(1)
            jump after
        "Comedy":
            voice "audio/narrador/theater/49.wav" #faltando
            "You weren't lucky with the genre, but the play can't be much longer."
            voice "audio/narrador/theater/50.wav" #faltando
            "Soon enough the lights will be turn on."
            $ renpy.pause(1)
            jump after
        "Based on a real person's life":
            voice "audio/narrador/theater/49.wav" #faltando
            "You weren't lucky with the genre, but the play can't be much longer."
            voice "audio/narrador/theater/50.wav" #faltando
            "Soon enough the lights will be turn on."
            $ renpy.pause(1)
            jump after
        "I prefer going to the movies":
            voice "audio/narrador/theater/49.wav" #faltando
            "You weren't lucky with the genre, but the play can't be much longer."
            voice "audio/narrador/theater/50.wav" #faltando
            "Soon enough the lights will be turn on."
            $ renpy.pause(1)
            jump after


label after:
    voice "audio/narrador/theater/35.wav" #faltando
    "The show ended, people are already getting up."
    voice "audio/narrador/theater/36.wav" #faltando
    "You can't stay here, you need to do what everyone is doing, leaving."
    voice "audio/narrador/theater/37.wav" #faltando
    "But where are you going? Did you come to the theater alone?"

    menu:
        "I like doing this alone sometimes.":
            voice "audio/narrador/theater/38.wav" #faltando
            "Being at truce with yourself is great, you are the company that you have all of the time."
            voice "audio/narrador/theater/39.wav" #faltando
            "And there is nothing wrong with solitude, it even makes you think of..."
            jump rooftops

        "I should go home." if play_saw:
            voice "audio/narrador/theater/40.wav" #faltando
            "The meaning of the play stuck with you."
            voice "audio/narrador/theater/41.wav" #faltando
            "Is there something in your home?"
            if went_home:
                voice "audio/narrador/theater/42.wav" #faltando
                "Is it double-checking if your eyes are now others?"
            jump room

        "Why does the fun have to end?":
            voice "audio/narrador/theater/43.wav" #faltando
            "That is right, don't stop dancing till the curtains fall."
            voice "audio/narrador/theater/44.wav" #faltando
            "There must be another thing to do, other places to see."
            voice "audio/narrador/theater/45.wav" #faltando
            "To find them, you need to go through a place that conects all places."
            jump streets

        "Where this theater is located again?" if visit_city:
            voice "audio/narrador/theater/46.wav" #faltando
            "You don't remember coming in, right?"
            voice "audio/narrador/theater/47.wav" #faltando
            "So there is only one way of knowing it."
            voice "audio/narrador/theater/48.wav" #faltando
            "You open the doors of the entrance, and..."
            jump city_night