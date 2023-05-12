# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

############
# Actual Nice OOP Code. It's been a long time coming
############

init python:
    class Person:
        def __init__(self, name, trust = 0, affection = 0):
            self.c = name
            self.trust = trust
            self.affection = affection














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
define evelyn = Character("Evelyn Sanders", image="evelyn")

image evelyn normal handinpocket = "images/char/evelyn/evelyn_normal_handinpocket.png"
image evelyn normal handraised = "images/char/evelyn/evelyn_normal_handraised.png"
image evelyn angry handinpocket = "images/char/evelyn/evelyn_angry_handinpocket.png"
#image evelyn angry handraised = "images/char/evelyn/evelyn_angry_handraised.png"
image evelyn happy handinpocket = "images/char/evelyn/evelyn_happy_handinpocket.png"
image evelyn happy handraised = "images/char/evelyn/evelyn_happy_handraised.png"



return

# The game starts here.

label start:

# Character Initializations

    $ chet = Person(Character("Chet"), 0, 1)


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show evelyn normal handraised

    # These display lines of dialogue.

    evelyn "Hello dear! \nI'm Evelyn Sanders, a senior accountant and HR representative at Orbital Weapons. It's very nice to meet you!"


    chet.c "testing"




    show evelyn normal handinpocket
    evelyn "I'll be conducting your interview for the internship position that you recently applied for. Don't get nervous dear, this will be very casual as the entire Orbital Weapons team was already very impressed with your resume."
    evelyn "Specifically, your involvement with SWIFT was something that we noticed. Members of that club have been known to be bound for greatness."

    show evelyn happy handinpocket
    evelyn "So this interview is pretty much a formality, but it serves an important function as a way to get to know you better! \nDon't worry dear, I know you will do great."

    show evelyn normal handinpocket

    evelyn "Before we start the interview, please write your first and last name on this form. It will be proof that you completed your interview and will also let the rest of the Orbital Weapons team know what to call you!"


label player_naming:

    default papers_used = 0
    default interview_points = 0

    if papers_used == 1:
        evelyn "I'll get you another form then. Keep in mind we don't have too many of these forms, so please make sure to write your name correctly this time"
    elif papers_used == 2:
        evelyn "Is something the matter my dear? If your nerves are making you write your name incorrectly, please relax! Like I said, this is an informal interview so there's no need to be anxious."
    elif papers_used == 3:
        evelyn "Please take a deep breath and write your name correctly this time. We only have so many forms to spare."
    elif papers_used == 4:
        show evelyn angry handinpocket
        evelyn "...Dear. Are you playing some kind of practical joke? These forms are printed on matte card stock. I've paid for them out of my own pocket and they're not cheap, sweetie."
        evelyn "I've been patient so far but I am running out of forms. Please write your name correctly this time."
    elif papers_used == 5:
        show evelyn angry handinpocket
        evelyn "I'll give you one more chance dear."
    elif papers_used == 6:
        show evelyn angry handinpocket
        evelyn "I'll give you ONE more chance dear."
    elif papers_used == 7:
        show evelyn angry handinpocket
        evelyn "You messed with the wrong lady, honey. I'll have you know I grew up in the streets and I'm always strapped. You've cost me over $90 in card stock, but I'm not accepting cash for payback."
        evelyn "No, you'll be paying with your life."
        # show evelyn gun
        evelyn "See you later, you son of a gun."
        jump evelyn_shoots_player

    $ player_fname = renpy.input("Please write your first name here.")
    $ player_lname = renpy.input("Please write your last name here.")

    define player = Character("[player_fname] [player_lname]")

    show evelyn normal handinpocket
    menu:
        evelyn "So your full name is [player_fname] [player_lname], is that correct?"

        "Yes":
            show evelyn happy handraised
            evelyn "Pleased to meet you [player_fname]! We're now all set to begin the interview."

        "No":
            $ papers_used += 1
            jump player_naming

    menu:
        evelyn "Let's start with an easy question. What made you want to work for Orbital Weapons?"

        "The prestige":
            player "It's a very prestigious company. Not many organizations can say they offer crowdfunded, large-scale annihalation services."
            player "Working for such a company would let me be proud of what I do, as well as impress others."
            jump interview_q1_a

        "The company's mission":
            player "I really vibe with Orbital Weapons' goal as a company. I'm sick of how only the economically blessed members of our society get to devastate countries at their whims."
            player "The ability to destroy large swaths of civilization should available to all, which is why I want to help make that vision come to fruition."
            jump interview_q1_b

        "Chet Apichart":
            player "I really, really, really, really, like Chet Apichart. His looks, his apitude for singing, his rocking dad bod. Forgive me if you think I said too much, but it needed to be said."
            player "Chet Apichart is one hell of a specimen, and I would do anything to get closer to him."
            jump interview_q1_c

        "Lack of other opportunities":
            player "It's somewhat embarassing to admit this, but I haven't had much luck with my other applications. I'm desperate at this point and am taking every opportunity I can get."
            jump interview_q1_d

label interview_q1_a:
    show evelyn normal handinpocket
    evelyn "That is true! Orbital Weapons is a very famous and prestigious company. Working here will be a solid resume boost that will be sure to open up a lot of opportunities for you in the future!"
    show evelyn happy handraised
    evelyn "Of course, we would very much like for you to stay and use your talents for our company."
    jump interview_q2

label interview_q1_b:
    show evelyn happy handinpocket
    evelyn "That's an excellent answer! I very much detest the inequality in our society that is inherent to wealth imbalances."
    evelyn "I am very pleased to hear that you share similar thoughts. Perhaps we can chat more about this topic after the interview!"
    jump interview_q2

label interview_q1_c:
    # show evelyn_confused
    evelyn "That's an interesting answer dear, I am slightly concerned. I'm not quite sure if that should be the main criteria for your job hunt, but I have seen more extreme deviations in my time."
    show evelyn happy handinpocket
    evelyn "However, as long as if you do not let your obsession disrupt your work or cause any Title 9 violations, I think that we can look past this!"
    jump interview_q2

label interview_q1_d:
    show evelyn normal handinpocket
    evelyn "No need to worry dear. I was the same as you a long time ago. It was only by chance that Orbital Weapons hired me as an accountant, and I've stayed here every since!"
    show evelyn happy handraised
    evelyn "I'm sure you won't regret taking this opportunity!"
    jump interview_q2

label interview_q2:
    show evelyn normal handinpocket
    evelyn "Let's move on to the second question."
    menu:
        evelyn "I'm very interested in your involvement with SWIFT and would love to hear more about it! \nWhat role did you have in the club?"

        "I am an eboard member":
            if (player_fname == "Taylor" and player_lname == "Nyugen"):
                player "I am the president of SWIFT! Apart from inspiring the rest of the club with my swoleness, I perform administrative outreach, handle dele"
            else:
                player "Yeah, I'm definitely an eboard member of SWIFT. I do a bit of eboard stuff, no biggie."


        "I am a SWIFTern":
            player "i lied"
        "I am a paid member":
            player "i lied"
        "I am a regular memeber":
            player "i lied"
        "I am not part of SWIFT":
            player "i lied"
    # This ends the game.

    return
