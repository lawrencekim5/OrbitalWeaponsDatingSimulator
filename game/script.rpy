# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

############
# Actual Nice OOP Code. It's been a long time coming
############

# Classes for characers. Still not sure what attributes should be implemented. Affection seems pretty straightforward, but what else? Trust plays with suspcicion,

# How the main game will play out: Orbital Weapons has fallen on som hard times after the Desolator misfire. Legal fees sapped away all of their profits, and are stsill causing them to bleed. However, Riki still believes in the company and is pushing for growth despite the company hemmorhaging money. As such, she instructs Chet Apichart to high some (unpaid) interns so that she can continue to grow the company.

# Riki is pretty crazy and wants to cut costs so because she gets extremely infuriated at all the "legal bs" she has to do with. So what if the desolator cannon annihalated 3/4 of Los Angeles? She didnt cause the misfire, why does she have to deal with it? While Riki's main goal is to expand Orbital Weapons, she also has a secondary goal of creating a scapegoat to take the fault, and along with it, all the legal and monetary responsibilities, for the desolator misfire. She will then replace the scapegoat with the intern (player).
# This is the main game mechanic, while you are getting to know the characters, Riki will make moves behind the scenes to paint the story.
# THe sufrace-level plot has the player join the orbital weapons crew and attempt to discover the truth of the desolator misfire. Riki will imply that there is a traitor in the Orbital Weapons team,so the player will be under the impression that they need to discover who among the team caused the misfire. This is all a fabrication by Riki, the truth is that someone (Dylan Tran? some other dude) caused the misfire. For the first playthrough, the player will essentially be gaslighted into believing that someon from orbital weapons did the misfire.

# Timeframe: Game takes place over the course of 30 days.

# Endings:
    # Endings will be different based on how successful Riki is in framing someone. Riki will target random characters or the first 15 days at great speed. For the next 15 days, Riki will begin to target whoever had the most suspcion points, if the otehr characters become suspicious of them too, that causes a suspcion ending. 
    # Endigns are composed of two parts, suspicion and romance. 
        # Suspicion: For each character that gets framed, there are two variations, normal suspicion ending, and romanced suspicion ending. Normal suspicion ending is when a characyer is framed. Romanced suspcion ending is when you're romancing the character that was framed. (Total of 6 that we have to write).
        # Romance: For each character, there are 2 romance endings, non suspicion and suspicion. For non-suspicion, you continue to work with them at Orbital Weapons after absorbing the old person's job. For suspicion romance ending, you take the job of the person you're romancing. Ther are some branches to this ending, 1) you can betray the character by admiting you used romance to get their job (this occurs if you point them out as the traitor), 2) you can keep in touch with them but still work at orbital weapons (this is pretty depressing, the character will live in debt), 3) you can quit orbital weapons and choose to run away with them. Total of 6 endings that we need to write, with some deviations. 
        # Riki endings. These endings are a bit special. Riki is manipulative, so there is no way of knowing if she really is affectionate for the player. She has a hidden stat that essential goes up if the player does malicious and manipualtive actions. If Real affection reaches a certain point, get the Devastation ending, romance RIki and join her in devastating landscapes for fun. If Real affection is not high enough but fake affection is, romance RIki, but she uses the opportunity to frame the player for the desolator misfire. 

# Characters: 
    # Riki Jespersen - CEO Chief Executive Officer
        # riki: psychotic and aggressive. sees fault in everyone and never in herself. malicious and probably has multiple personalities
    # Saul Solper - CTO Chief Technology Officer
        # saul: sleazy and greedy. puts his own gain over everyone else. not self-aware or perceptive enough to be ashamed of what he does. not necessarily evil
    # Chet Apichart - CFO Chief Finnancial Officer
        # chet: laid back, chill, supportive individual. all about living life and being happy. probably smokes a lot of weed
    # Jory Saltman - CPO Chief Product Officer
        # jory: very incompetent at his job, but is scared of people finding out. wants to be left alone. quiet and reserved



# Stats needed. Trust - how likely a character is to listen to you. Suspicion - how likely other characters think that person is suspicious. Affection - how much the character likes the player. Real affection - Riki only stat, how much Riki actually likes the player

# This class initializes the Character objects
init python:
    class Person:
        def __init__(self, fullname, firstname, lastname, job, trust = 0, affection = 0, suspicion = 0, realaffection = 0):
            self.fullname = fullname
            self.firstname = firstname
            self.lastname = lastname
            self.job = job
            self.trust = trust
            self.affection = affection
            self.suspicion = suspicion
            self.realaffecion = realaffection


# Character stat change functions
        def trust_change(self, change):
            self.trust += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "'s trust has increased by " + str(abs(change)))
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "'s trust has decreased by " + str(abs(change)))

        def affection_change(self, change):
            self.affection += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "'s affection has increased by " + str(abs(change)))
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "'s affection has decreased by " + str(abs(change)))

        def realaffection_change(self, change):
            self.realaffection += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "'s real affection has increased by " + str(abs(change)))
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "'s real affection has decreased by " + str(abs(change)))

        def suspicion_change(self, change):
            self.suspicion += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "looks to be a little more suspicious.")
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify(str(self.fullname) + "is less suspicious now.")



    class Player:
        def __init__(self, fullname, job, money, karma, positivekarma, negativekarma, fitness, intelligence, charisma):
            self.fullname = fullname
            self.firstname = player_firstname
            self.lastname = player_lastname
            self.job = job
            self.money = money
            self.karma = karma
            self.positivekarma = positivekarma
            self.negativekarma = negativekarma
            self.fitness = fitness
            self.intelligence = intelligence
            self.charisma = charisma

# player stat change functions

        def money_change(self, change):
            self.money += change
            if (change > 0):
                renpy.notify("You got $" + str(abs(change)) + " dollars.")

            else:
                renpy.notify("You lost $" + str(abs(change)) + " dollars.")


        def karma_change(self, change):
            self.karma += change
            if (change > 0):

                self.positivekarma += change
                renpy.play("audio/sfx/interface.mp3", channel=None)
                # replace notification message with justice scale, suddent tilt to the right
                # add bar indicating total morality. this is identified by the karma value. poskarma and negkarm are separete values for dialouge branches
                renpy.notify("Your karma has increased by " + str(abs(change)))
            else:
                
                self.negativekarma += abs(change)
                renpy.play("audio/sfx/interface.mp3", channel=None)
                # replace notification message with justice scale, suddent tilt to the left
                renpy.notify("Your karma has decreased by " + str(abs(change)))


        def fitness_change(self, change):
            self.fitness += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify("Your fitness has increased by " + str(abs(change)))
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify("Your fitness has decreased by " + str(abs(change)))

        def intelligence_change(self, change):
            self.intelligence += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify("Your intelligence has increased by " + str(abs(change)))
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify("Your intelligence has decreased by " + str(abs(change)))


        def charisma_change(self, change):
            self.charisma += change
            if (change > 0):
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify("Your charisma has increased by " + str(abs(change)))
            else:
                renpy.play("audio/sfx/interface.mp3", channel=None)
                renpy.notify("Your charisma has decreased by " + str(abs(change)))

###################################
# Effects and Other Implementations
###################################


################
# Variables
###############
default positivekarma = 0
default negativekarma = 0
default player_firstname = "Jacob"
default player_lastname = "Jayme"
default loop1 = False
default confidential1 = False
############
# Flags
#########

default flag_solicitorbeatdown = False
default questionasked1 = False
############
# Characters
############



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

    # <Class>(Character("<Name>")) is proper syntax when creating character names. This makes it possible for renpy to easily create dialouge.

    $ chet = Person(Character("Chet Apichart"), "Chet", "Apichart", "Chief Technology Officer", 0, 0, 0, 0)
    $ saul = Person(Character("Saul Solper"), "Saul", "Solper", "Chief Financial Officer", 0, 0, 0, 0)
    $ jory = Person(Character("Jory Saltman"), "Jory", "Saltman", "PLACEHOLDER", 0, 0, 0, 0)
    $ riko = Person(Character("Riki Jespersen"), "Riki", "Jespersen", "Chief Executive Officer", 0, 0, 0, 0)

    $ player = Player(Character("Jacob Jayme"), "Unemployed", 20, 0, 0, 0, 0, 0, 0)


##############
# Story Start#
##############

# PROLOUGE
    
    scene library with dissolve:

    "It's a beautiful day at the Cal Poly Pomona Campus!"
    scene library with dissolve:
        xpos 0.7 ypos 1.0 xanchor 0.80 yanchor 0.60 zoom 2.0
        linear 2 yanchor 0.53
    "The sky is an unblemished shade of blue, with nary a cloud in the sky!"
    
    scene library with dissolve:
        xpos 0.7 ypos .03 xanchor 0.80 yanchor 0.60 zoom 3.0
        linear 2 yanchor .67


    "The grass is a vibrant verdant green, which is surprising given the current state of California's water supply."
    
    scene library with dissolve:
    "But these are all sights you've seen before, so you pass on by without a second thought."
    "After all, the source of this day's beauty has 0 relation to this random picture of the University Library."
    "Today's beauty lies within the intangible..."
    "The prospect of landing an internship with a top cybersecurity company!"

    scene careerfair with dissolve:
        zoom 1.9
    play music orbitalwalking if_changed loop
    "That's right, today is the CPP Cybersecurity Career Fair!"

    menu:
        "But tell me, what are you looking forward to the most at the career fair?"
            

        "I just really need a job.":
            "Obviously it's a job! What else would you be looking for at a career fair?"
            $ player.intelligence_change(1)
            "{i}Your ability for basic self-reflection increases your intelligence to [player.intelligence]!"
            
        "It's always fun to meet new people!":
            "Meeting new faces, talking to people with similar interests, building up your professional network... all of this encompasses the joy that is social interaction!"
            "Plus, who knows? Every social gathering is an opporunity to meet that special someone!~"
            $ player.charisma_change(1)
            "{i}You blush at your own thoughts. You're such a silly romantic! Your rizz increases to [player.charisma]."

        "I'd rather be at the gym!":
            "Actually, it turns out you weren't that excited about the career fair."
            "You'd rather be working out at the gym right now. Who cares about finding a job, you just want gains!"
            "Plus, having a healthy appearance helps a lot with job interviews by making you seem assiduous, attentive, and attractive. Being fit has a surprising amount of practical applications!"
            "But then again, you need to be considered for a job interview first before you can use your appearance for social leverage. You should probably head to the career fair."
            "BUT... what if you meet a recruiter at the gym? Maybe heading over to the gym is actually the right option!"

            $ player.fitness_change(1)
            "{i}Your mental gymnastics increases your fitness to [player.fitness]. You end up deciding to go to the career fair.{i}"

            # mental gymnastics
    
    

    define solicitor = Character("Solicitor", image="solicitor")
    define unknown = Character("???")


    unknown "Excuse me, can I have a moment of your time?"

    show unknownsolicitor_normal:
        zoom 0.5
        xpos 0.5  # Center the image horizontally
        ypos 0.5  # Center the image vertically
        xanchor 0.5  # Set the anchor point to the center horizontally
        yanchor 0.5 

    "You turn your head to see a man calling out to you."

    show unknownsolicitor_normal:
        zoom 0.5
        xpos 0.5  
        ypos 0.5 
        xanchor 0.5  
        yanchor 0.5 
        linear .1 zoom 1.5

    "He briskly approaches with the speed of an 8-year old child and the audacity of a 9-year old child, all while maintaining a gleaming smile that's betrayed by his souless eyes."

    show unknownsolicitor_normal:
        zoom 1.5
        xpos 0.5  
        ypos 0.5 
        xanchor 0.5  
        yanchor 0.5 
        linear .1 zoom 1
    "You step back."
    "A cursory glance at his clipboard and pen tells you everything you need to know. After all, you've seen his kind many times before."

    hide unknownsolicitor_normal
    show solicitor_normal
    "It's a solicitor."

    hide solicitor_normal with dissolve
    "You ignore him and turn away. While you do feel slightly guilty about not hearing him out, you really don't want to be late to the- {nw}"
 
    show solicitor_normal with vpunch
    
    solicitor "Woah hey there buddy, wait up a minute! I just want to talk to you about our cause for a second. It'll only take a second, I promise!"

    menu:
        "What do you want to do?"

        "Hear him out.":
            "You're afraid that the career fair might be ending soon, but you decide to listen to the solicitor anyways."
        
        "Run away.":
            
            if player.fitness < 2:
                "You attempt to run away, but you need a fitness level of 2 to be able to run away from solicitors. Too bad your fitness is at [player.fitness]! I guess you're forced to listen to him."

            else:
                hide solicitor_normal
                show solicitor_angry:
                    xpos 0.5  
                    ypos 0.5 
                    xanchor 0.5  
                    yanchor 0.5 
                    linear .1 zoom 2
                solicitor "You fucking cheater."


    

    solicitor "Thanks for stopping! Nice to meet you! I'm Blaine. What's your name?"

    $ player_firstname = renpy.input("What's your first name?")
    $ player_firstname = player_firstname.strip()
    if player_firstname == "":
        $ player_firstname = "Jacob"

    $ player_lastname = renpy.input("What's your last name?")
    $ player_lastname = player_lastname.strip()
    if player_lastname == "":
        $ player_lastname = "Jayme"

    $ player.fullname = player_firstname + " " + player_lastname

    $ socialsecuritynumber = renpy.input("And... what's your social security number?")
    $ socialsecuritynumber = socialsecuritynumber.strip()

    player.fullname "Hello solicitor. I'm [player_firstname]."

    solicitor "Hey [player_firstname], nice to meet you! My name is Blaine, not solicitor by the way... hahaha..."

    "You stare blankly at him. It's strange how your experience in ignoring so many solicitors has made them all indistinguishable to you. All of this solicitor's details seem poorly rendered. You can hardly tell if he even has any human features."
    
    
    if len(socialsecuritynumber) == 9 and socialsecuritynumber.isdigit():
        solicitor "Anyways.... Thanks for giving me your social security number! I wasn't expecting that at all! I was just joking about wanting it though, so I don't care if you gave me a legit number or not."
        hide solicitor_normal
        show solicitor_happy
        "You watch as the solicitor scribbles [socialsecuritynumber] into his clipboard."
        show solicitor_normal
        hide solicitor_happy

    else:
        solicitor "Anyways.... I noticed that you didn't give me a social security number. That was just a joke so I'm not disappointed at all. Hahaha! I hope you found it as funny as I did!"

    
    solicitor "Thanks for stopping though, I really appreciate it. Could I take a moment of your time to tell you about this charity I'm running? We're working towards saving the coral reefs in Florida."
    solicitor "With climate change increasing ocean acidification, we're at major risk of unprecedented loss of biodiversity within our ocean's ecosystems! The coral reefs are a huge provider of food, medicine... they're just important for life in general!"

    menu:
        solicitor "If you are willing to be genererous and provide a small donation, it would go a long way towards helping our cause. How about it?"

        "Donate $10":
            $ renpy.notify("The solicitor WON'T remember this.")
            
            "It sounds like its for a good cause and its not like you're in desperate need of money. Cal Poly Pomona is notoriously affordable. You can spare $10 to help the less fortunate."
            $ player.karma_change(1)
            "{i}You feel like the epitome of generosity! Your karma increases to [player.karma]!{i}"
            $ player.money_change(-10)
            player.fullname "Sure, I can donate. Here's $10."
            
            menu:
                solicitor "...That's it? C'mon, you can do better than that! I can easily see that you have at least $10 in your wallet right now."

                "Donate $10 more":
                    $ player.money_change(-10)
                    "You fork over an additional $10."
                    solicitor "Wow thanks. Now I can afford to feed a homeless shelter for two days instead of one."
                    player.fullname "I thought your charity was about saving the Florida coral reefs?"
                    solicitor "Huh? Oh... yeah, we are. W-what did I just say?"

                    menu: 
                        solicitor "Actually don't answer that. Could you donate some more though? I have a daily quota of $500 and I only need $480 more to reach it."

                        "Donate more":
                            
                            "You try to donate $10 more dollars, but you realize you've run out of cash! Even though CPP may be affordable, that doesn't change the fact that you're a broke college student."
                            $ player.intelligence_change(-1)
                            "{i} Your fiscal irresponsibility permanently damaged your mental state. You have lost some of your brain cells and are no longer able to think as clearly. Your intellegence decreased to [player.intelligence]!"
                            solicitor "Oh? Looks like you're out of money. Welp, no point in talking to you anymore. Thanks for your generosity! See you later!"
                            hide solicitor_normal with dissolve
                            "Having fulfilled your ethical obligations, you continue to head over to the career fair. You make it to your destination 0.01\% faster due to your lighter wallet."

                        "Leave":
                            "You decide that you fulfilled your ethical obligations. Time to head over to the career fair!"
                            solicitor "Thank you for your generosity! See you later!"
                            hide solicitor_normal with dissolve
    

                "Leave":
                    hide solicitor_normal with dissolve
                    "You feel as though you donated a fair amount. The solicitor's attitude killed your generous spirit. You start to head over to the career fair."
                    "You hear no objections to your depature. No doubt a new target for solicitation has already been found."


        "Make an excuse and leave":
            player.fullname "I'm sorry, I'm a bit busy right now. Maybe next time."
            solicitor "..."
            $ renpy.music.set_pause(True, channel="music") # pause music
            hide solicitor_normal
            show solicitor_neutral:
                xpos 0.5  
                ypos 0.5 
                xanchor 0.5  
                yanchor 0.5 
                linear .1 zoom 1.55
            $ renpy.pause (5.0, hard=True) # hard pause
            solicitor "Mhm, that's what they all say. Go away you heartless piece of trash."

            hide solicitor_neutral with dissolve
            $ renpy.music.set_pause(False, channel="music") # unpause music
            "The solicitor's words sting deep even though you know his comments aren't indicative of your morality."
            "{i}You feel a bit sad. At least there's no stats for depression in this game! Make sure YOU take care of YOURself though. Mental health is important!{i}"

        "Teach him a lesson he won't forget":
            "You've had it with these solicitors. While you're normally able to tolerate them, this one is currently the main impediment towards you and your future cybersecurity career. Unfortunately for him, you won't let anything stand between you and success."
            "You ready your fists."
            solicitor "Wait... what are you- {nw}"
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.5, hard=True)
            play audio punch
            show solicitor_normal with hpunch
            $ renpy.pause (0.5, hard=True)
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.3, hard=True)
            play audio chop
            show solicitor_normal with hpunch
            $ renpy.pause (0.3, hard=True)
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.1, hard=True)
            play audio chop
            show solicitor_normal with hpunch
            $ renpy.pause (0.1, hard=True)
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.01, hard=True)
            $ renpy.notify("The solicitor WON'T remember this.")
            play audio chop
            show solicitor_normal with hpunch
            $ renpy.pause (0.01, hard=True)
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.01, hard=True)
            play audio punch
            show solicitor_normal with hpunch
            $ renpy.pause (0.01, hard=True)
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.001, hard=True)
            play audio chop
            show solicitor_normal with hpunch
            $ renpy.pause (0.001, hard=True)
            play audio punch
            show solicitor_normal with vpunch
            $ renpy.pause (0.001, hard=True)
            play audio punch
            show solicitor_normal with hpunch
            $ renpy.pause (0.001, hard=True)
            play audio chop
            show solicitor_normal with vpunch
            solicitor "{cps=1}...{/cps}{nw}" # slow text speed
            hide solicitor_normal with dissolve
            
            ""
            $ player.fitness_change(1)
            "{i}You got a pretty good workout! Your fitness increased to [player.fitness]!{i}"
            $ flag_solicitorbeatdown = True

            unknown "Holy moly."
            unknown "Is he okay?"
            unknown "WHAT THE HELL [player_firstname]!"
            unknown "Someone call campus police!"

            "Uh oh. Looks like the passing strangers witnessed your unjustifiable act of aggression. It probably wasn't the best idea to beat someone up in public, especially when the victim wasn't even harming anyone."
            "You think it may be best to get therapy to sort out your anger issues."
            $ player.karma_change(-1)
            "{i}You feel like a worse person. No, you ARE a worse person than you were a minute ago. Your karma decreased to [player.karma]!{i}"
            

            
    "Anyways, now that the solicitator is taken care of, it's time to attend the career fair!"      
    scene black with dissolve
    # play walking noise
    scene careerfairempty with dissolve:
        xpos 0.5  
        ypos 0.5 
        xanchor 0.5  
        yanchor 0.5 
        zoom 1.99

    "Oh no! Where are all the booths? The recruiters? The keys to your future?"
    "Did the career fair end already? There's no way that the solicitator took that much of your time!"
    "Tears start to stream from your eyes."
    "You wallow in despair."
    "You curse Daylight Savings Time. Not for any particular reason, you're just very upset right now."

    unknown "Excuse me, are you here for the career fair? Do you know if it ended already?"
    "A smooth angelic voice with the consistency and sweetness of marmalade rings out in the distance. Dripping with warmth and care, the timbre relaxes you instantly."
    "{i}You become a little happier! There's no stat for this though. Maybe it's because it's impossible to assign happiness with a quantitative value?{i}"
    "{i}Or maybe it's because happiness is often so fleeting that it's not worth tracking.{i}"

    show chet with dissolve:
        zoom 0.7
        xpos 0.5  
        ypos 0.45 
        xanchor 0.5  
        yanchor 0.5 
    "A cheery man with a bright smile appears in front of you."
    "All is right in the world."

    chet.fullname "Hi there! I'm Chet Apichart, Chief Financial Officer at Orbital Weapons. What's your name?"
    player.fullname "Hi Chet. My name is [player_firstname]."

    menu:
        chet.fullname "Nice to meet you [player_firstname]! You seemed very upset earlier. Is everything alright?"

        "I'm fine now that you're here~":
            player.fullname "I was feeling pretty down earlier, but everything's alright now that you're here. Your million dollar smile just wiped away all my worries."
            chet.fullname "That's such a nice thing to say, thank you!"
            "Chet continues to smile at you. You feel slightly disconcerted."
            chet.fullname "Were you late to the career fair as well?"
            player.fullname "Yeah I was. I'm really disappointed, this was one of my only opportunites for a decent internship."

            menu:
                chet.fullname "Well, I was looking to hire some people for Orbital Weapons, but it seems like you're the only one here now. So why don't I tell you a little bit about our company and you can see if you're interested?"
                
                "Really? That'd be great!":
                    player.fullname "Yes please! Thank you very much!"
                    jump prologue2

                "Actually, I'm just here for the CTF flag. Gimme.":
                    player.fullname "That sounds nice, but I'm actually just here for the CTF flag. Do you know what it is?"
                    jump ctf

        "I hate you Chet! I don't want to play this stupid dating simulator anymore. Just give me the flag!":
            player.fullname "Get me out of this game already! I just want to finish the CTF, hurry up and give me the flag!"
            label ctf:
                menu:
                    chet.fullname "I'm sorry, I have no idea what you're referring to [player_firstname]. Are you talking about the banners that we bring for our booths? I was running late so I wasn't able to bring anything for Orbital Weapons, but I can tell you about our company if you're interested!"
                    "That sounds great!":
                        player.fullname "That'd be perfect!"
                        jump prologue2
                    "NO! I'm talking about the Terrestrial Weapons CTF flag! Where is it!?":
                        player.fullname "I'm supposed to find a flag for a Terrestrial Weapons CTF challenge in this game. It's supposed to be some specific string that's encased in the curly braces of 'tw\{\}'. Have you seen anything like it?"
                        
                        menu:
                            chet.fullname "Hmmm, I HAVE heard of Terrestrial Weapons before. I'm not a huge fan of that company, but I still don't know what you're talking about. What game are you talking about?"

                            "Nevermind, ignore what I was talking about. I want to go back to playing the dating simulator.":

                                player.fullname "Actually, forget what I said just now. I'm not sure what came over me."
                                player.fullname "Did you mention that you worked at Orbital Weapons? Can you tell me more?"
                                chet.fullname "Absolutely! I thought you'd never ask!"
                                jump prologue2

                            "I'm talking about this game! CTFd said that this dating simulator would have a flag!":
                                player.fullname "I'm talking about this game! CTFd said that this dating simulator would have a flag!"
                                chet.fullname "...Isn't CTFd a CTF platform? I'm still having a hard time understanding you."
                                "You think you see a confused expression flash across Chet's face, but he still has that cheery smile plastered on his face."
                                "It's probably because the developers ran out of budget before they were able to create different expressions for their characters."
                                "It also explains why Chet Apichart only ever appears as a disembodied head."
                            
                                "{i}Guilty as charged :(. It's hard to photoshop so many characters! We do have a couple in work though.{i}"
                                show chet_sakaning_on_des with dissolve:
                                    zoom 2
                                    xpos 0.5  
                                    ypos 0.45 
                                    xanchor 0.5  
                                    yanchor 0.5 
                                
                                "{i}Look, check this one out! Support the game and you'll get to see more epic creations like this one!{i}"
                                hide chet_sakaning_on_des
                                "What the hell was that!? Who's thoughts were those!?"
                                chet.fullname "Are you okay? You have a strange expression on your face."

                                player.fullname "I am so confused. All I wanted was to do was get more points in the CTF. What did I get myself into?"
                                "You start crying."
                                
                                unknown "What's going on here?"
                                hide chet with dissolve
                                show pike with dissolve:
                                    zoom 1.6
                                    xpos 0.45  
                                    ypos 0.5 
                                    xanchor 0.5  
                                    yanchor 0.5 
                                "HOLY MOLY! IT'S DR. PIKE!"
                                define pike = Character("Dr. Pike")
                                player.fullname "Hello Dr. Pike. I'm trying to find a CTF flag in this dating simulator but I'm having some issues."
                                player.fullname "Chet Apichart isn't being very cooperative."
                                pike "*sigh* Is this for the SWIFT OSINT CTF? This sounds like something Jacob would do. Give me a moment, I'll figure something out."

                                hide pike with dissolve

                                "Dr. Pike heads over to the Student Data Center."
                                show chet with dissolve:
                                    zoom 0.7
                                    xpos 0.5  
                                    ypos 0.45 
                                    xanchor 0.5  
                                    yanchor 0.5 
                                chet.fullname "I'm sorry for not being of much help."
                                player.fullname "It's okay. I think Dr. Pike is going to be able to find that flag, so no harm done!"
                                menu:
                                    chet.fullname "I still feel very bad about it though. Let me make it up to you! There's a great sushi place near Diamond Bar, how about it?"

                                    "No.":
                                        player.fullname "No."
                                        chet.fullname "I see.... That's okay, I'll just treat you next time!"
                                        chet.fullname "It was nice to meet you [player_firstname]. You're a very interesting person! I feel like you would fit right in at Orbital Weapons. See you around!"
                                        hide chet with dissolve
                                        "Chet smiles at you and leaves. Not that he ever stopped smiling in the first place."
                                        "It was slightly disconcerting."
                                        $ player.charisma_change(-1)
                                        "{i}That wasn't very smooth of you! Your charisma decreases to [player.charisma]!{i}"
            
                                show pike with dissolve:
                                    zoom 1.6
                                    xpos 0.45  
                                    ypos 0.5 
                                    xanchor 0.5  
                                    yanchor 0.5 
                                pike "Hi [player_firstname], I'm back! I found Jacob in the SDC and I was able to get the flag from him. Here it is!"
                                pike "tw\{starCr0ss3dL0v3rs\}"
                                pike "Have fun completing the rest of the CTF!"
                                player.fullname "Thank you Dr. Pike!"
                                hide pike with dissolve
                                player.fullname "...I love you."
                                "Dr. Pike isn't here to here your final words. But don't worry! He knows that all his students love him."
                                "{i}Have fun completing the CTF!{i}"
                                jump ending

    
label prologue2:
    menu:
        chet.fullname "Alright! So essentially, Orbital Weapons offers a crowdsourced alternative for city-wide annihalation. You can think of it as Uber Eats, but instead of being hungry for food, you're hungry for armageddon."
        "That sounds highly unethical.":
            player.fullname "That sounds highly unethical. Why would you choose to work in an industry like that?"
            $ player.karma_change(1)
            "{i}Your sense of basic morality makes you feel like a better person. Your karma increases to [player.karma]!"
            chet.fullname "You bring up a good point! Orbital bombardment is inherently unethical, absolutely! But, the issue is that while devastation at this scale exists, it exists as a viable option only for the elite few with deep enough pockets."
            chet.fullname "What we do is level the playing field, allowing the less fiscally fortunate to pool their money together to have the same destructive options available to them."
            chet.fullname "In this sense, I see our work as something profoundly noble! I hope you will come to see it that way too."
        "Nuking cities? Sign me up!":
            player.fullname "Nuking cities? SIGN ME UP!"
            "You try your best to sound as enthusiastic as possible. You don't want to offend the person who's capable of blowing up you and your entire family."
            $ player.intelligence_change(1)
            "{i}That's actually a really smart move! You feel your brain enlarge as your intelligence increases to [player.intelligence]!"
            "Or maybe you DO like the idea of ruining the lives millions of people? It's hard to tell when you haven't had that many karma checks yet."
            chet.fullname "Haha! That's the spirit! Most people shy away from our company after hearing about the gigantic scale of our services, but I think you're a perfect fit!"

    chet.fullname "Now that you know a little about the company, do you have any questions that you would like to ask?"
    $ loop1 = True
    while loop1 == True:
        menu:
            chet.fullname "Feel free to ask anything! I can answer anything that's not confidential."

            
            "How many people work at Orbital Weapons?":
                $ questionasked1 = True
                player.fullname "How many people work at Orbital Weapons?"
                chet.fullname "We're actually a very small company! We currently have four members of our team, including me! Let me tell you a little bit about each one."
                hide chet with dissolve
                show rikihead with dissolve:
                    zoom 0.7
                    xpos 0.5  
                    ypos 0.45 
                    xanchor 0.5  
                    yanchor 0.5
                chet.fullname "First up we have Riki Jespersen! She is our Chief Executive Officer. She started Orbital Weapons back in 2021 all by herself! She undoubtedly possesses a very bight mind, and just might have what it takes to make Orbital Weapons a Fortune 10 company."
                chet.fullname "She does have some strange moments where she lashes out at our team though. I guess one of the downsides of being a genius is being forced to deal with people who can't keep up with your brilliance."
                hide rikihead with dissolve
                show saulhead with dissolve:
                    zoom 0.7
                    xpos 0.5  
                    ypos 0.45 
                    xanchor 0.5  
                    yanchor 0.5
                chet.fullname "Next is Saul Solper! He is our Chief Technology Officer. Computers, networks, the blockchain, he's a master of it all! He is a very capable person that is able to fulfill Orbital Weapons's technolgy needs all by himself!"
                chet.fullname "I would advise you not to get too close to him though. Not that he's a bad guy!"
                chet.fullname "It's just that he's not the biggest team player. You'll see for yourself once you meet him."
                hide saulhead with dissolve
                show joryhead with dissolve:
                    zoom 0.7
                    xpos 0.5  
                    ypos 0.45 
                    xanchor 0.5  
                    yanchor 0.5
                chet.fullname "And then we have Jory Saltman! He is our Chief Product Officer. He's responsible for the design, manufacturing, and marketing of our orbital ion cannons and annihalation services."
                chet.fullname "To be honest, I don't know too much about the details of his work. Jory is a very introverted individual and prefers to keep to himself. I wish he would open up to us a bit more, I'm sure he's a nice person!"
                hide joryhead with dissolve
                show chet with dissolve:
                    zoom 0.7
                    xpos 0.5  
                    ypos 0.45 
                    xanchor 0.5  
                    yanchor 0.5                
                chet.fullname "Lastly, we have me, the Chief Financial Officer! I'm in charge of budgets, cost predictions, and making sure we're compliant with any financial regulations."
                chet.fullname "My job entails a magnitude of strategic decision making, which I love! Being responsible for managing the company's cash flows provides me with a unique vantage point to witness our company's growth firsthand. It's a very fulfilling job!"

            "What would I do as an intern?":
                $ questionasked1 = True
                player.fullname "What responsibilities will I have as an intern?"
                chet.fullname "Admittedly, our team is very small and we could all use your assistance. So for your internship, you'll likely find yourself helping out here and there across the four of us."
                chet.fullname "And if you find yourself to be more interested in certain roles, feel free to focus your efforts there! We want you to do what you enjoy!"

            "Where is the company located?":
                $ questionasked1 = True
                player.fullname "Where is Orbital Weapons located?"
                chet.fullname "We're located right here in California! We had plans to move headquarters a while back, but they never went through."
                chet.fullname "If you're interested in that, Riki may be able to explain more about that decision."

            "Do you offer remote work options?":
                $ questionasked1 = True
                player.fullname "Do your employees have the option to work remotely?"
                chet.fullname "Unfortunately, we do not. It's a strict requirement that we work at our company headquarters. Sometimes we'll spend an entire week at the office!"
                chet.fullname "In fact, if you decide to intern here, you'll be living at the Orbital Weapons company headquarters for the full duration of the month-long internship."
                chet.fullname "Don't worry though! The office is very comfortable and offers a lot of amenities. I bet you won't want to return home after staying there for a month!"

            "What's the turnover rate?" if not confidential1:
                $ questionasked1 = True
                player.fullname "What's the turnover rate for your employees?"
                chet.fullname "That's confidential."
                $ confidential1 = True

            "What would my starting salary be?":
                $ questionasked1 = True
                player.fullname "What is the starting salary for your interns?"
                chet.fullname "To be honest, Orbital Weapons is going through some difficult financial times due to an accident that occured several years ago. We're still trying to recoup costs, so our hiring budget is severely limited."
                chet.fullname "We don't even have an HR department, so I was put in charge of recruiting! Can you believe that!?"
                chet.fullname "Unfortunately, I believe that this will be an unpaid internship. I can try to negotiate a living stipend for you, but don't expect too much."
                chet.fullname "Although, I am confident that having Orbital Weapons on your resume will make any internship experience with us more than worthwhile."

            "I don't have any other questions.":
                player.fullname "I don't have any other questions."
                $ loop1 = False


    

    if questionasked1 == True:
        chet.fullname "Alright then! Thanks for asking such good questions and being so interactive, I had a great time!"
        menu:
            chet.fullname "Well... what do you think? Do you want to work for Orbital Weapons?"
            "Yes":
                player.fullname "Absolutely! When can I start?"
                $ chet.affection_change(1)
                "{i}Chet becomes visibly happy. The fact that this is even possible given his perpetual smile is indicative of just how happy you made him. Your affection with Chet Apichart increases to [chet.affection]!{i}"
                
            "No":
                player.fullname "Not really."
                chet.fullname "I see.... Either way, I appreciate you taking the time to talk to me. If you ever change your mind in the future, let me know!"
                hide chet with dissolve
                "Chet leaves, and so does your opportunity for an internship. Why did you turn him down again?"
                "Probably due to the lack of pay, the forced 30-day isolation, and incredibly miniscule size of the business. In hindsight, you've avoided a huge red flag."
                $ player.intelligence_change(3)
                "{i}The results of your cost-benefit analysis impresses you. Your intelligence increases to [player.intelligence]! You still don't have an internship though, so are you really a winner?{i}"
                jump ending


    else:
        chet.fullname "Really? You don't have any questions?"
        menu:
            chet.fullname "Oh well, I thought you would have been interested in our work, but I must have guessed wrong. I'm a little upset, but if you ever change your mind let me know."

            "I'm sorry, but I'm not interested.":
                player.fullname "I'm sorry. Orbital Weapons just seems a little lame. I hope you find someone else that's more interested in wasting their life at your company."
                # show chet angry
                "Chet's smile disappears. He looks a little strange without his signature grin."
                hide chet with dissolve
                "He leaves without a response."
                # jump to terrestrial weapons arc
                # temporary jump to ending
                jump ending

            "I don't need to ask questions to know I want to work for you.":
                player.fullname "I didn't ask any questions because I already know that I want to work at Orbital Weapons. Truthfully, I was sold the second you said \"Weapons\". Count me in!"
                "Chet's face of disappointment quickly brightens up."
                $ player.charisma_change(1)
                "{i}Wow! What a save! Kind of a risky move, but it seems to have had a good effect. Your charisma increased to [player.charisma]!{i}"
            

    chet.fullname "That's awesome! I'll get the paperwork started! You should be able to start as soon as you begin your Summer break, I'll keep you updated!"
    "Chet is beaming with cheerfullness. You're pretty happy too, you just landed an internship without so much an interview! Who knew it could be so easy?"
    if flag_solicitorbeatdown == True:
        chet.fullname "But just to make sure, you don't have any impulsive tendencies, right?"
        chet.fullname "Our work involves large-scale bombardment, so it's important that we only hire those that aren't overly violent and uninhibited."
        player.fullname "I've never hurt a soul in my life."
        "Solicitors don't have souls."
        "{i}They're not all bad! Shame on you for being so violent!{i}"
        chet.fullname "Perfect! I can tell by the look in your eyes that you aren't lying!"
    chet.fullname "I'm going to head back to HQ to tell everyone! It was very nice to meet you [player_firstname], I'll see you soon!"
    hide chet with dissolve
    "And so begins your story at Orbital Weapons, as well as the flood of unanswered questions that always accompany the start of a new chapter in your life."
    "Will you reach financial stability?"
    "Will you find love?"
    "Will you accelerate the Earth's unsustainable rate of global warming by nuking California's major cities?"
    "The answer to these questions can be only found if you continue on in your celestial journey..."
    "Across time and space..."
    "In Orbital Weapons: Star Crossed Lovers!"

    
label ending:
    scene bluesky
    "That's all the content we have for now! Thanks for playing!"
    "A lot of things in this demo are WIP, especially the sprites and the music. Did I mention that Lawrence made the music!!! :o He's so talented!"
    "If you want to follow the development of the game, or play the dating sim on your own computer, you can download it at https://github.com/lawrencekim5/OrbitalWeaponsDatingSimulator! Don't read the script files unless you want to be spoiled though! I promise the plot is going to be very good."
    "It's best experienced blind, please trust me! >:("
    "If you have any suggestions, feedback, encountered any bugs or typos, please let me know! You can message 'terrance5' and 'chetapichart' on Discord if you liked the game and want it to continue! Also remember to thank Jacob for his awesome CTF."
    "Please give feedback, I sustain myself solely through positive reinforcement and have no motivation otherwise - Lawrence."
    "Thanks for enjoying this Jacob and Lawrence production. Also big shout out to Alex Tselevich for being the creator of the Orbital Weapons universe! Check out nosecurity.blog!"
    "Bye bye!"
    return

################################################
# OLD CODE and some examples
label OLDCODE:
    # $ player.fullname("I'm a pserson now") <- this does not work for some reason
    chet.fullname "here's my current trust level [chet.trust] and poskarma is [player.positivekarma] neg is [player.negativekarma]"

    $ chet.fullname("Here is my current trust level [chet.trust]")


    $ chet.trust_change(1)

    evelyn "Hello dear! \nI'm Evelyn Sanders, a senior accountant and HR representative at Orbital Weapons. It's very nice to meet you!"


    chet.fullname "testing"




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
