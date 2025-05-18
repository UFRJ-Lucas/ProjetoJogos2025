# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist")
define d = Character('Priest')
image dom_visconti = "dom_visconti.png"
image dom_visconti_talking = "dom_visconti_talking.png"
# The game starts here.

default count = 0
default calling = True
default body = True
default visit_city = False
default road_peace = False
default monologue = False
default play_saw = False
default went_home = False
default dom = False
default priest_name = False

label start:

    jump prologue_awakening

    return