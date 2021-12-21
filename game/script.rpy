# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

############
# Characters
############

# Chet Apichart
define chet = Character("Chet Apichart")

# Sault Solper
define saul = Character("Saul Solper")

# Jory Saltman
define jory = Character("Jory Saltman")

# Riki Jespersen
define riki = Character("Riki Jespersen")

# Evelyn Sanders
define evelyn = Character("Evelyn Sanders")


return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chet

    # These display lines of dialogue.

    evelyn "You've created a new Ren'Py game."

    evelyn "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
