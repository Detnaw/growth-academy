﻿##
## Notes to potential writers:
##
## I'll be leaving comments as I learn so that I can refer back to them,
## and anyone that looks as this script afterwards will be able to tell what's going on. -- SaburoX
##
## Additional notes:
##
## If any new features or custom codes (outside of the native Ren'Py library)
## are used, I'll also be leaving comments explaining as clearly as I can
## what those code-blocks are doing. -- LuckyJack020
##

#You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Images go in the Graphics folder, and so their file names are prefaced by 'Graphics/'.

# Backgrounds
image white = Solid((255, 255, 255, 255))
image Lake Road = "Graphics/Lake Road.png"
image School Front = "Graphics/School Front.png"
image School Inner = "Graphics/School Inner.png"
image Gate Front = "Graphics/Gate Front.png"
image School Planter = "Graphics/School Planter.png"
image Hallway = "Graphics/Hallway.png"
image Classroom Day = "Graphics/Classroom.png"
image Dorm Exterior = "Graphics/DormExterior.jpg"
image Dorm Interior = "Graphics/DormInterior.jpg"
image Campus Center = "Graphics/CampusCenter.jpg"
image Auditorium = "Graphics/Auditorium.jpg"
image School Exterior = "Graphics/SchoolExterior.jpg"
image F1 Hallway = "Graphics/SchoolHallway1.png"
image splash = "Graphics/SplashScreen.png"

# Charactr Portraits
image BE-1a = "Graphics/BE-1a.png" #BE Girl Neutral Portrait
image BE-1b = "Graphics/BE-1b.png" #BE Girl Happy Portrait
image BE-1c = "Graphics/BE-1c.png" #BE Girl Surprised Portrait
# image BE-1d = "Graphics/BE-1d.png" #BE Girl Angry Portrait
# image BE-1e = "Graphics/BE-1e.png" #BE Girl Sad Portrait

image BE-SC-1 = "Graphics/BE-SC-1.png" #BE Girl Scene 1
image BE-SC-2 = "Graphics/BE-SC-2.png" #BE Girl Scene 2

image GTS-1a = "Graphics/GTS-1a.png" #GTS Girl Neutral Portrait
image GTS-1b = "Graphics/GTS-1b.png" #GTS Girl Happy Portrait
image GTS-1d = "Graphics/GTS-1d.png" #GTS Girl Angry Portrait
image GTS-1e = "Graphics/GTS-1e.png" #GTS Girl Sad Portrait
image GTS-2a = "Graphics/GTS-2a.png" #GTS Girl Formal Neutral Portrait

image AE-1a = "Graphics/AE-1a.png" #AE Girl Neutral Portrait
image AE-1a flip = im.Flip("Graphics/AE-1a.png", horizontal=True)
image AE-1b = "Graphics/AE-1b.png" #AE Girl Happy Portrait
image AE-1d = "Graphics/AE-1d.png" #AE Girl Angry Portrait
image AE-1e = "Graphics/AE-1e.png" #AE Girl Sad Portrait

image FMG-1a = "Graphics/FMG-1a.png" #FMG Girl Neutral Portrait
image FMG-1b = "Graphics/FMG-1b.png" #FMG Girl Happy Portrait
image FMG-1d = "Graphics/FMG-1d.png" #FMG Girl Angry Portrait
image FMG-1e = "Graphics/FMG-1e.png" #FMG Girl Sad Portrait

image BBW-1a = "Graphics/BBW-1a.png" #BBW Girl Neutral Portrait
image BBW-1b = "Graphics/BBW-1b.png" #BBW Girl Happy Portrait
image BBW-1d = "Graphics/BBW-1d.png" #BBW Girl Angry Portrait
image BBW-1e = "Graphics/BBW-1e.png" #BBW Girl Sad Portrait

image PRG-1a = "Graphics/PRG-1a.png" #PRG Girl Neutral Portrait
image PRG-1b = "Graphics/PRG-1b.png" #PRG Girl Happy Portrait
image PRG-1d = "Graphics/PRG-1d.png" #PRG Girl Angry Portrait
image PRG-1e = "Graphics/PRG-1e.png" #PRG Girl Sad Portrait

image RM-1a = "Graphics/RM-1a.png" #Roommate Neutral Portrait
image RM-1b = "Graphics/RM-1b.png" #Roommate Angry Portrait
image RM-1c = "Graphics/RM-1c.png" #Roommate Stern/Glum Portrait
image RM-1d = "Graphics/RM-1d.png" #Roommate Flustered/Embarrassed Portrait

image HR-1a = "Graphics/HR-1a.png" #Homeroom Teacher Neutral Portrait

# Declare characters used by this game.
# Remember that character codes are case sensitive. 
define MC = Character('Keisuke', color="#0066CC") # Main Character, speaking.
define MCT = Character('Keisuke', color="#0066CC", what_prefix='(', what_suffix=')') # Main Character, Thought. Note the special prefix and suffix tags to  place his thoughts in parentheses.
define BE = Character('Honoka', color="#FCCF20")
define AE = Character('Shiori', color="#FF3300")
define FMG = Character('Akira', color="#FF9900")
define BBW = Character('Alice', color="#CC33FF")
define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
#Since Preg Girl is timid, her text is smaller by default. When she grows out of it, we can use a text tag to make her speech regular sized.
define GTS = Character('Naomi', color="#66FF33")
define RM = Character('Daichi', color="#BDB8A5")
define HR = Character('Tashi-Sensei', color="#C0C0C0")
define UNKNOWN = Character('???', color="#FFFFFF")


# Initialize imagemap for first school map. 
screen first_imagemap:
    imagemap:
        ground "Graphics/FirstMapGround.png"
        hover "Graphics/FirstMapHover.png"
        
        if not GTS_Flag_01:
            hotspot (242, 214, 150, 150) clicked Return("garden")
        if not AE_Flag_01:
            hotspot (428, 214, 150, 150) clicked Return("front")
        if not BBW_Flag_01:
            hotspot (242, 396, 150, 150) clicked Return("class")
        hotspot (428, 396, 150, 150) clicked Return("dorm")


init python:
    style.menu_choice_button.background = Frame("choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    style.menu_choice_button.hover_background = Frame("choice_bg_hover.jpg",28,9)
    style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.
    
    import math

    class Shaker(object):       #This is Python code to implement a feature to shake the screen around at random, not just in one direction like with the punch commands
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
        
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
        
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    Shake = renpy.curry(_Shake)
#End of Python custom init-coding

# The game starts here.

label splashscreen:
    scene black
    with Pause(1)
    
    show splash with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)
    
    return

label start:
    $ BE_Affection = 0
    $ GTS_Affection = 0
    $ AE_Affection = 0
    $ FMG_Affection = 0
    $ BBW_Affection = 0
    $ PRG_Affection = 0
    $ RM_Affection = 0
    
    #Initialize visit variables to have not yet been enabled.
    $ GTS_Flag_01 = False
    $ AE_Flag_01 = False
    $ BBW_Flag_01 = False
    
    # Stops the title music with a fadeout of half a second.
    stop music fadeout 0.5
    
    # Begin the character introduction scene.
    scene characterintro:
        
    
    # Without a defined character code before the dialogue, it's unattributed speech. Good for narration.
    #EX - "This is the narrator, introducing our characters."
    
    # This is what text will look like with those codes attached.
    # Line breaks are done by inserting the command \n where you want to start a new line. No spaces allowed. 
    #Italics, bold, etc are done with curly brackets
    #
    
    #EX - MC "Yo. I'm the player character, Hotsure Keisuke.\nI'm transferring to Seichou Academy this year."
    #EX - BE "I'm the BE character, Inoue Honoka!\nIt's good to see you again, Kei{i}-chan{/i}!" 

    # I'll stick new characters above so that anyone that wants to just copy those lines and replace the actual dialogue can do so without worry.
    show black
    centered "The following represents a work in progress."
    centered "Art assets are placeholders or otherwise unfinished and all general content has yet to be finalized."
    centered "For more information, visit\n https://www.expansiongames.net"
    centered "Enjoy."
    
    # Move to Lake Road screen with a fade in transition.
    scene Lake Road
    with fade

    MCT "Ahh... It's really hot today."
    "I came to a stop on a wooden bridge overlooking a lake."
    "My name is Hotsure Keisuke. My spring vacation is coming to an end,\nand I'm starting at a new school tommorrow."
    MCT "To be honest, I'm a little nervous."
    "It's supposed to be a boarding school, which is why I've got my luggage with me."
    "But..."
    MC "Where the heck am I?!\nI've been walking for an hour already!"
    "I was sure that I was lost, but as I was thinking that, I saw someone walking ahead of me."
    MCT "I guess I'd better ask for directions."
    MC "Good afternoon!"
    "At the sound of my voice, she turned around and faced me."
    
    show BE-1a
    with dissolve
    
    "It turned out to be a fairly cute girl, with brown hair."
    MC "Sorry, but can you tell me where I am? I'm a little lost."
    UNKNOWN "..."
    "She stared at me intently for a long time. Did I surprise her or something?"
    MC "See, I'm trying to find Seichou Academy."
    UNKNOWN "Seichou..."
    "Because of that, the girl seemed to realize something."
    
    show BE-1c
    
    BE "Kei{i}-chan{/i}? Hey, you're Kei{i}-chan{/i}, right?!"
    MC "Wait, How do you know my name?"
    BE "What are you talking about? It's me! Honoka!"
    MC "Eh?!"
    "Come to think of it...I guess she is a little familiar."
    "I didn't recognize her at first because it's been so long, but this girl is Inoue Honoka."
    "We used to live in the same town a long time ago, and played together all the time."
    "But then her father got transferred, and she moved away..."
    BE "I can't believe you really don't remember me!"
    MC "Ahahaha...Sorry! It's been seven years already!"
    show BE-1a
    BE "That's true, it has been that long already, hasn't it..."
    BE "...I guess I have to forgive you then. You've grown up so much, so it's unreasonable to expect you to remember me if I've changed just as much."
    MCT "Exactly! There are limits to a guy's memory, you know? Besides..."

    play sound "Audio/Boing.ogg"
    show BE-SC-1
    with vpunch
    
    MCT "I'm pretty sure I would have remembered those!"
    
    show BE-1a
    with dissolve
    
    BE "Kei{i}-chan{/i}?  You kind of spaced out there for a second."
    MC "Er...I was just thinking, have I really changed that much?"
    
    show BE-1a
    
    BE "Well, your hair is the same, but I remember when I used to be taller than you."
    
    show BE-1b
    
    extend " What about me, I've changed, right?"
    MC "...Maybe a little."
    MC "So, what are you doing out here?"
    
    show BE-1a
    
    BE "I thought that it was a nice day, so I should go for a little walk. I didn't imagine I'd run into you, Kei{i}-chan{/i}!"
    
    show BE-1c
    
    BE "Ah! You said you were looking for Seichou Academy, right?"
    BE "Could it be that you're attending there?"
    
    show BE-1b
    
    extend " That's going to be my school starting tomorrow!"
    
    show BE-1a
    
    "...Now that I think about it, it looks like she's wearing a school uniform. I guess this means I might even be in the same class as Honoka."
    BE "Come on, Kei{i}-chan{/i}!\nI'll show you the way there."
    "So with that, I picked up my luggage and followed Honoka."
    
    show BE-SC-2
    with dissolve
    
    BE "So, how have you been?\nHow about Tomo{i}-chan{/i}, her too!"
    "Tomo{i}-chan{/i} is Hotsure Tomoko, my younger sister."
    MC "She's doing fine. So am I."
    MC "Actually, she and I will be attending this school together, but her year hasn't ended yet so she's not arriving today."
    MC "But anyway, I was really surprised, Honoka."
    BE "Yeah, I was a little nervous too, moving to a new boarding school and all."
    BE "But if you're going to be here, I'm sure it'll be great!"
    BE "I guess we'll both be in your care, Kei{i}-chan{/i}, so do your best!"
    MC "Right."
    BE "Ah! We're here!"
    
    scene School Front
    with fade
    "Before I realized it, we had arrived at a huge school building. This was Seichou Academy."
    "This would be my new home for the next year.\nIt was really awe-inspiring at the time."
    "But even then, I had no idea just how much my life was going to change."
    jump Navigate
    
label Navigate:
    
    scene black
    window hide None
    call screen first_imagemap
    window show None
    
    $ result = _return

    if result == "garden":
        jump GTSScene
    elif result == "front":
        jump AEScene
    elif result == "class":
        jump BBWScene
    elif result == "dorm":
        jump RMScene
    
label GTSScene:
    
    $ GTS_Flag_01 = True
    scene black
    with dissolve
    "As we entered the school grounds, I couldn't help but notice how big everything was."
    
    scene School Planter
    with dissolve
    "What looked to be normal-sized buildings turned out to be a trick of perspective."
    "As Honoka and I walked and walked, the school seemed to grow before my eyes."
    "The doors became large and imposing, the floors far taller than normal, everything just seemed to be super-sized in Seichou Academy."
    UNKNOWN "Aaack!"
    "Honoka and I looked down to see a pair of legs flailing over the edge of one of the planters lining the building."
    "We approached the planter just as the student extracted themselves from the planter, dusting the dirt from her long skirt."
    
    show GTS-1e at Position(xpos=0.75, xanchor=0.5)
    with dissolve
    UNKNOWN "Oooh, darn it darn it darn it..."
    
    show BE-1c at Position (xpos=0.25, xanchor=0.5)
    BE "Are you okay?"
    UNKNOWN "Eeep!"
    "The pale-skinned girl turned to us, looking briefly terrified.\nShe was wearing a long skirt and long-sleeved shirt."
    UNKNOWN "Uhm, yeah, sorry, I just, uhm, fell. Just, these planters are so big." 
    UNKNOWN "I can't reach the middle of the bed without crawling on the outer ones..."
    "She gestured behind her, and we could see inside the planter were several rows of vegetables, the tops of radishes and carrots and the like poking through the soil."
    "Aside from the divot where she fell, the center row of vegetables did indeed look less well-watered than the ones closest to the edge."
    
    menu:
        "That's too bad.":
            jump Choice1a
            
        "Do you need help?":
            jump Choice1b
            
label Choice1a:
    
    MC "That's too bad, hope you can figure something out."
    UNKNOWN "Yeah...If only I was a little taller, I could reach to the middle..."
    GTS "Oh, I'm sorry, I forgot entirely! My name's Yamazaki Naomi."
    "She bowed, and we returned the gesture."
    show BE-1a at Position (xpos=0.25, xanchor=0.5)
    BE "I'm Inoue Honoka, nice to meet you. This is Kei-{i}Ahem{/i}-Hotsure Keisuke."
    MC "Nice to meet you."
    GTS "Well, I've done as much as I can today, it seems. I'll leave the rest to the groundskeepers."
    GTS "I'll see you all at orientation tomorrow."
    show BE-1b at Position (xpos=0.25, xanchor=0.5)
    BE "Goodbye! See you around!"
    hide GTS-1e
    with dissolve
    BE "..."
    show BE-1a
    BE "...Boy, that's kind of a fancy lady to be kneeling in the dirt, don't you think?"
    "I nod, and we continue on to the front doors of the school."
    jump Navigate

label Choice1b:
    MC "Do you need help?"
    show GTS-1b
    UNKNOWN "Oh, thank you, that'd be lovely. Here, let me give you the can..."
    $ GTS_Affection += 1
    "I leaned way over the planter and watered the middle row of plants having to stretch as far as I could reach but managing to get all of them."
    GTS "Thank you so much! Oh, I'm sorry, I didn't even introduce myself properly. My name's Yamazaki Naomi."
    "She bowed, and we returned the gesture."
    show BE-1a at Position (xpos=0.25, xanchor=0.5)
    MC "I'm Hotsure Keisuke, and this bundle of smiles here is Inoue Honoka. Nice to meet you."
    show BE-1b
    BE "Hi there!"
    GTS "Well, it's been a pleasure."
    GTS "Perhaps I'll see you around school?"
    MC "Yeah, sure."
    BE "Yeah! See you later!"
    hide GTS-1b
    with dissolve
    BE "..."
    show BE-1a
    BE "Well that was nice of you to help her, Kei-chan!"
    $ BE_Affection += 1
    "I nod, and we continue on to the front doors of the school."
    jump Navigate

label AEScene:
    
    $ AE_Flag_01 = True
    scene black
    with dissolve
    UNKNOWN "Mizutani!"
    "The yell made both of us jump in place, so sudden and forceful was it so soon after stepping inside."
    "When we caught our bearings{w} (And Honoka's bust stopped jiggling){w} \nwe saw the owner of the voice."
    
    scene Gate Front
    with dissolve
    "Stern and impatient-looking, the woman surveyed the front area of the school like a forewoman on a construction site, barking orders and taking notes on a clipboard."
    
    show AE-1d at Position(xpos=0.75, xanchor=0.5)
    with vpunch
    UNKNOWN "Mizutani! Quit goofing off and get over here!"
    FMG "I'm comin', I'm comin'! Geeze!"
    "Around the corner came a tanned girl somehow managing to carry a wooden bench under each arm, her short-sleeved shirt baring her defined muscles for all to see."
    
    show FMG-1a at Position (xpos=0.25, xanchor=0.5)
    with dissolve
    UNKNOWN "What took you so long?"
    FMG "I was getting two benches at once!  I thought you'd like me getting twice what ya asked!"
    UNKNOWN "Not if it takes you three times as long!"
    
    hide AE-1a
    hide FMG-1d
    show BE-1c at center
    BE "Oh boy...I feel awkward just standing here..."
    
    hide BE-1c
    show AE-1d at Position(xpos=0.75, xanchor=0.5)
    show FMG-1a at Position (xpos=0.25, xanchor=0.5)
    
    menu:
        
        "She was just trying to help...":
            jump Choice2a
            
        "You should listen to your boss, you know.":
            jump Choice2b
            
        "(Do nothing)":
            jump Choice2c

label Choice2a:
    
    MC "She was just trying to help...{w}No need to be mean."
    $ BE_Affection += 1
    $ FMG_Affection += 1
    $ AE_Affection -= 1
    UNKNOWN "Ex{i}cuse{/i} me?"
    FMG "Yeah, Matsumoto, get that stick out of your huge butt."
    "Matsumoto's face tightened and she shot daggers with her eyes."
    "It was hard not to notice the very prominent backside on her otherwise stiff and lithe frame."
    AE "My reasons for being at Seichou are not relevant to this conversation."
    show AE-1a
    AE "As class rep it's my responsibility to make sure-"
    hide AE-1a
    hide FMG-1a
    show BE-1c at center
    BE "You're class rep already? But I thought classes didn't start until tomorrow."
    show BE-1c at Position (xpos=0.25, xanchor=0.5) with dissolve
    show AE-1b at Position(xpos=0.75, xanchor=0.5) with dissolve
    AE "Well, not yet, technically, but I'm sure I will be. I always am."
    BE "(She's awfully self-assured...)"
    show AE-1a
    AE "Are you two assigned to class 3-B? Inoue and Hotsure?"
    MC "Uh, I don't know, actually..."
    AE "I do. You're on the roster. I was just being polite."
    MC "Oh, well, okay then. Yeah, I guess?"
    AE "Get up there and make sure Aida and Nikumaru have the first-day decorations put up properly."
    show AE-1d
    AE "{i}Sigh{/i} Even though I'll probably have to fix it myself."
    MC "Er, okay, sure."
    hide AE-1d with dissolve
    show BE-1c at Position (xpos=0.25, xanchor=0.5)
    "Without another word, Matsumoto turned and began barking more orders and directions to the other students arranging the decorations."
    "Honoka and I looked at each other and headed for class 3-B."
    jump Navigate
    
label Choice2b:
    
    MC "You should listen to your boss, you know."
    MC "If she's got a plan, going off on your own doesn't really help."
    $ FMG_Affection -= 1
    show FMG-1d
    FMG "My WHAT? Matsumoto's not the boss of anyone, despite what she'll tell you."
    show AE-1a
    AE "I never claimed to be anyone's \"boss\", I just had a plan to-"
    FMG "Yeah, yeah, yeah. Listen, you two in 3-B? Might as well get up there and help."
    FMG "Whatever the princess and her pet're doing can't be as bad as having lard-butt boss you around..."
    hide FMG-1d with dissolve
    "Matsumoto shot daggers at Mizutani as she left to get more benches, then turned to regard me with a glare."
    show AE-1e
    AE "I did not need your help, but she's right. Get up to 3-B and help with the decorations and cleaning."
    "Honoka and I quickly fled the scene before the temperature dropped so low as to be freezing."
    jump Navigate
    
label Choice2c:
    
    "I didn't want to get involved in the fight.{w}Especially after seeing Mizutani lift one of those big wooden benches under each arm."
    UNKNOWN "Look, it doesn't matter if you bring all the benches at once if I can't get them organized properly."
    UNKNOWN "One at a time lets us get each one in its place and ready for the next without-"
    show FMG-1e
    FMG "All right, all right, I get it, sheesh. Don't get your panties in a bunch, Matsumoto..."
    show FMG-1b
    extend "with a butt that size, you'll never fish 'em back out."
    hide FMG-1e with dissolve
    "Matsumoto shot daggers at Mizutani with her eyes until she left to get more benches, then she turned to myself in a huff."
    "My eyes snap to hers, momentarily mesmerized by just how sizable her rear was underneath the school-issue uniform."
    $ AE_Affection += 1
    show AE-1b
    AE "Hmph. Thank you for not butting in on that...{w}spectacle.{w}\nI'm Matsumoto Shiori, and you are?"
    "We introduced ourselves, and Matsumoto informed us that we were in the same class as her, class 3-B."
    "She asked us to go to our room and help two other students she'd sent earlier in the day to prepare the room, expressing some doubt as to their competence."
    hide AE-1b with dissolve
    show BE-1a at center with dissolve
    BE "You think she's ever happy with anyone? Doesn't seem the type..."
    jump Navigate

label BBWScene:
    
    $ BBW_Flag_01 = True
    scene black
    with dissolve
    "We left the arguing pair behind and entered the school proper.{w} Honoka led me through the hallways with ease, until we came to one classroom in particular.."
    
    scene Classroom Day
    with dissolve
    "So this was Classroom 3-B. I would be spending a lot of time here for the next year."
    "The first thing I noticed was that, much like the rest of the shool, the classroom seemed very big. It was much larger than any that I had been in before."
    "Whether or not this meant that there would be more students, or if this was just something that made high school different, I had no idea."
    "The next thing I noticed was that Honoka and I weren't alone in the room. Sitting across from us, at the head of the classroom, was another girl."
    show BBW-1a at Position (xpos=0.25, xanchor=0.5) with dissolve
    "She had a round face, and bright blue eyes framed by gold colored hair.{w} It seemed as though we had a foreigner in our midst."
    "She was sitting with her feet on one of the desks, but stood up and grinned when she saw us enter."
    UNKNOWN "Oh? What have we here? I guess that Shiori told you to come up here too?"
    UNKNOWN "I have everything under control here."
    BE "Who are you?"
    BBW "I'm Alice Nikumaru.{w} Charmed, I'm sure."
    "After introducing herself, Alice sat back down in her makeshift throne. Before I could open my mouth to speak, she looked past us."
    show BBW-1d
    BBW "Will you hurry up already?!"
    BBW "I want to go get something to eat and I can't do that if you're slacking off!"
    "I followed Alice's gaze. I hadn't noticed at all but there was a mousy girl in the room as well."
    hide BBW-1d with dissolve
    show PRG-1a at Position(xpos=0.75, xanchor=0.5) with dissolve
    "Her hair was tied up in a pair of tails, and she was carrying a globe."
    show PRG-1e
    UNKNOWN "{size=-6}Sorry!{/size}"
    show BE-1c at Position (xpos=0.25, xanchor=0.5)
    BE "Oh wow! Sorry about that, but I totally didn't see you there!"
    show BE-1a
    BE "I'm Inoue Honoka! Pleased to meet ya!"
    MC "Hotsure Keisuke."
    show PRG-1a
    PRG "Aida...Aida Kodama."
    hide BE-1a
    show BBW-1a at Position (xpos=0.25, xanchor=0.5)
    BBW "Great, great.{w} Now everybody knows everybody, and Aida can finish decorating. She's almost done anyway."

    menu:
        "Well, if you've got this under control...":
            jump Choice3a
            
        "Shouldn't you be doing something too?":
            jump Choice3b
            
label Choice3a:
    MC "Well, if you've got this under control, I guess I'll be going then.?"
    $ BBW_Affection += 1
    $ PRG_Affection -= 1
    $ BE_Affection -= 1
    BBW "Glad to see at least someone can follow orders."
    show BE-1c at center with dissolve
    BE "{i}Kei-chan{/i}!"
    "I winced. I might not have seen Honoka for years, but I remembered that tone well enough."
    hide BE-1c with dissolve
    MC "Okay, okay. We'll help too."
    show PRG-1e
    PRG "...I don't want to be a bother."
    BBW "Hmph. {w}Well, if you insist, I'm sure I can find something for you to do. {w}The sooner we're done here, the better."
    jump Navigate           
            
label Choice3b:
    MC "Shouldn't you be doing something too?"
    $ BBW_Affection -= 1
    $ PRG_Affection += 1
    show BBW-1a at Position (xpos=0.25, xanchor=0.5)
    BBW "I'm doing something!"
    show BBW-1b
    BBW "I'm su{w}per{w}vi{w}sing!"
    hide BBW-1b with dissolve
    PRG "It's okay...{w}I don't need any help."
    MC "It's fine. We're all supposed to be working together, right?"
    show PRG-1b
    PRG "T-thank you! Thank you very much!"
    jump Navigate            
     
label RMScene:
    scene Hallway
    with fade
     
    show BE-1a with dissolve
    BE "Alright, well, it looks like everything's ready for tomorrow...{w}(No thanks to queenie over there.){w} Time to get back to the dorms, I guess!"
    MC "They wouldn't happen to be co-ed, would they?"
    show BE-1b
    BE "Oh, Kei-chan! You're such a kidder!{w} Of course not!"
    "Honoka's laugh caused her impressive bust to shake violently, which was a small consolation prize as we parted ways."
    hide BE-1b with dissolve
    
    scene School Inner
    with fade
    
    "I headed over to the boy's dormitories, seeing they were just as enlarged as the rest of the school.{w} I felt like a child, trying the doorknob that I couldn't even get my entire hand around."
    "*Kunk-Kunk*"
    MC "Locked? I'm sure I had the right--"
    UNKNOWN "Who is it?!"
    MC "Aaah!"
    UNKNOWN "Who is it? Identify yourself!"
    
    menu:
        "Uh...Pizza delivery?":
            jump Choice4a
            
        "Keisuke Hotsure. I...think this is my room?":
            jump Choice4b
            
        "Don't worry, I'm from the government!":
            jump Choice4c
            
label Choice4a:
    MC "Uh...{w}Pizza delivery?"
    UNKNOWN "I didn't order any pizza!{w} Scram!"
    MC "Hahaha...It was just a joke, this is my dorm room.{w} I guess you're my roommate?"
    "The door opened a crack and a single narrowed eye looked out at me."
    UNKNOWN "This is your dorm?{w} Are you sure?"
    MC "Preeeetty sure...{w} Says right here on my paperwork, see?"
    "I pulled out my transfer documents from the top pocket of my luggage, but he snatched them away before I could even show them."
    "The door shut briefly, then opened again, the boy inside still glaring at me through one narrowed eye."
    UNKNOWN "Keisuke Hotsure...{w}Let's see some ID."
    MC "Haha, no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    show RM-1a with dissolve
    RM "Alright, you check out...{w}My name's Daichi Utagashi."
    $ RM_Affection -= 1
    scene Dorm Interior
    with fade
    show RM-1a
    jump RMClose
    
label Choice4b:
    MC "Keisuke Hotsure. I...{w}think this is my room?"
    "I could hear movement behind the door, like someone searching for something.{w} After a bit, the door opened a crack, a single narrowed eye looking me up and down."
    UNKNOWN "Hotsure, huh?{w} Let's see some ID"
    MC "Haha, no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    show RM-1a with dissolve
    MC "Alright, you check out...{w}My name's Daichi Utagashi.{w} Come in, I don't like leaving the door open."
    scene Dorm Interior
    with fade
    show RM-1a
    jump RMClose
    
label Choice4c:
    MC "Don't worry, I'm from the government!"
    "I thought my fake-authoritative voice would have been worth a laugh, but instead there was silence.{w} I knocked again, tried the knob, called out a few times, but there was no answer."
    "I put my ear against the door and could hear movement, so I moved over to one of the windows and took a peek in,{w} only to see the mystery occupant hurling his bags out the opposite window!"
    scene Dorm Exterior
    with fade
    "I left my luggage by the door and ran around the dorm, coming around the other side just in time to see him struggling out the window."
    show RM-1b with vpunch
    UNKNOWN "Aaah! D-Damn you!"
    RM "Daichi Utagashi isn't going without a fight!"
    "Daichi tried to go back inside, but he had already squirmed too far out to get back through the window."
    RM "Rrrgh!{w} Hrff!{w} Nnngh...{w}Dammit, I'm s-stuck!"
    MC "Will you calm down for a second and tell me what's wrong???"
    RM "Don't play coy with me!{w} You're one of them!"
    MC "\"Them\" who?"
    RM "The government! You're here to monitor me, drag me off to some secret prison!{w} Put electrodes in my brain!"
    MC "It was just a joke!{w} I'm Keisuke Hotsura, I just got here, this is supposed to be my dorm!"
    "Daichi twisted around to look at me, his eyes narrowed."
    show RM-1c
    RM "...If you really were one of them, I suppose you would have grabbed the evidence while I was helpless.{w} Help me back in and I'll open the door."
    MCT "Am I really going to have to live with this guy?"
    scene Dorm Interior
    with fade
    "After helping Daichi back through the open window and handing his bags to him {w}(He wouldn't let me carry them out of his sight){w} then checking my admission papers and ID, he finally unlocked the door and let me in."
    show RM-1d
    RM "Don't get any funny ideas, 'Keisuke Hotsure'. I've got my eye on you..."
    $ RM_Affection -= 3
    jump RMClose

label RMClose:
    "When I finally got inside, it was obvious Daichi had claimed his half of the room.{w} Half the furniture had been crammed into one corner of the room, with blankets and sheets erected into a kind of tent over his desk and dresser."
    show RM-1a
    MC "Er, so, do you want to--"
    RM "Do you know why you're here?"
    MC "Er, what?"
    RM "Why you're here, at this school?"
    MC "Well, I got the letter..."
    RM "Right after your health exam, right?"
    MC "Yeah..."
    RM "Hmph. Just as I thought."
    MCT "???"
    show RM-1d
    RM "Haven't you ever seen those people on the news?{w} The giants over ten feet tall,{w} the gravure idols with 40kg breasts,{w} all the record holders for biggest this and longest that?"
    "Thinking back on it, I had seen some reports, starting when I was a little kid."
    "It wasn't often, but every now and then there'd be some picture or other of a giant-sized man or woman, always Japanese."
    RM "If you look into the histories and records of all these people, one thing is common to all of them--{w}they {i}ALL{/i} went to school at Seichou Academy!"
    MC "So, what are you saying?"
    show RM-1c
    RM "I'm saying the government brings certain students here and--{w}and does {i}something{/i} to them!"
    show RM-1b
    RM "This kind of growth isn't natural,{w} it's statistically impossible for all of these one-in-a-million conditions to keep happening {i}just{/i} to Japanese school-age teens!"
    "I sat down on my bed, lost in thought.{w} Daichi certainly seemed to have a few screws loose, but then again,{w} why {i}had{/i} my sister and I been sent to this school with so few details?"
    "I had just accepted it as some new schooling program, like the papers had said, but now?"
    "I never paid much attention to the news, but if every one of those reports and articles over the years could be traced back to Seichou Academy,{w} that was definitely something to wonder about."
    scene black
    with dissolve
    MCT "What have my sister and I gotten ourselves into...?"
    jump Day2

label Day2:
    scene white
    with dissolve
    play sound "Audio/ClockAlarm.ogg"
    "{color=#FF0000}BREEET BREEET BREEET BREEET!{/color}"
    scene Dorm Interior
    with dissolve
    "I was startled awake by a shrill electronic alarm clock. I looked around confused for a moment, before remembering where I was."
    MCT "Hard to believe just yesterday I was in my hometown, and now I'm off on this little island..."

    "I got up and got into my uniform, doing my best to comb my shaggy hair into something approaching proper.  In the corner of my eye I saw Daichi watching me."

    if RM_Affection >= 0:
        show RM-1a
        RM "Today's the welcoming ceremony. I'm going to go get the lay of the campus."
        MC "You're going to skip the opening ceremony?"
        show RM-1b
        RM "Of course not.{w} I need to get the official story so I know where to start investigating."
        hide RM-1b with dissolve
        "I shook my head, but waved goodbye nonetheless as Daichi left.  At least he seemed in good spirits."
        $ RM_Flag_01 = True
        jump CeremonyStart

    if RM_Affection < 0:
        show RM-1c
        "As soon as he realized I'd noticed him, he spun on his heel and headed out the door."
        hide RM-1c with dissolve
        "I looked after him, puzzled, but after yesterday's oddness I figured this was the sort of behavior I could look forward to all year."
        $ RM_Flag_01 = False
        jump CeremonyStart

label CeremonyStart:
    scene Campus Center
    with fade
    "As I followed the signs to freshman welcoming, I couldn't help but notice how flat the campus seemed.  Despite the large buildings, most of them were divided into a handful of floors at most." 
    "Also, there didn't seem to be any stairs anywhere. Any dips or slopes in the elevation were all traveled with ramps."
    scene Auditorium
    with dissolve
    "When I finally reached the auditorium, I found I was still early enough to have my choice of seats."
    MCT "Where should I sit...?"

    menu:
        "I should sit in the front where the Principal can see me.":
            jump Choice5a
            
        "I should sit somewhere in the middle.":
            jump Choice5b
        
        "I should sit in the back, where no one will notice me.":
            jump Choice5c


label Choice5a:
    "I decided to sit in the front row, where the principal could see me. If I ever needed to speak with him, recognizing my face might make him better disposed toward me."
    MCT "This is a good seat...  Got spaces on either side of me."
    "{color=#FF69B4}*FLUMPH!*{/color}"
    MCT "!!"
    MCT "I... Is that..."
    show AE-1a flip at Position(xpos=0.75, xanchor=0.5) with dissolve
    MCT "Shiori-san's butt is overflowing her seat and pushing against me...{w}I can't say anything about with everyone else around..."
    MCT "I'll just quietly scoot away from her-"
    "{color=#FF69B4}*PLOMF!*{/color}"
    MCT "Oh no!"
    show BBW-1a at Position(xpos=0.25, xanchor=0.5) with dissolve
    MCT "Alice-San! She's taking up all of her seat and half of mine! What do I do??"
    MCT "I'm in the middle of a womanly butt-sandwich and it's like I'm the only one to notice! I've got to distract myself before something even more embarrassing happens!" with Shake((0, 0, 0, 0), 0.75, dist=20)
        
    menu:
        "So, Shiori-san...":
            jump Choice6a

        "Hi there, Nikumaru-san...":
            jump Choice6b

label Choice5b:
    "I decided to sit in the middle of the auditorium, where I could still hear the speeches without being so front-and-center."
    MCT "Let's see, somewhere around here should be--"
    BE "Pssst!  Kei-chan!"
    show BE-1b at Position(xpos=0.25, xanchor=0.5) with dissolve
    MC "Honoka?"
    BE "Kei chan, over here!  I've got a seat saved for you!"
    "I made my way down the row of chairs to the seat Honoka was patting next to her."
    "I noticed when I passed by Honoka, she had to lean back slightly to keep her bosoms from dragging across me, and the thought made me blush."
    "When I sat down and the the breath I'd been holding out, I realized I was sitting next to the girl we'd met gardening the evening before."
    show GTS-1a at Position(xpos=0.75, xanchor=0.5) with dissolve
    show BE-1b
    BE "Isn't this great, Kei-chan?  It's just like grade school again!"
    GTS "You two... Went to school together?"
    show BE-1a
    BE "Oh, hey there Naomi-san! Yeah, when we were kids we went to the same school. Different middle schools, though."

    menu:
        "Find your dorm okay, Honoka?":
            jump Choice6c

        "What was your grade school like, Naomi?":
            jump Choice6d

label Choice5c:
    "I decided to sit in the back, where I wouldn't have to worry about anyone seeing me."
    show FMG-1a at Position(xpos=0.75, xanchor=0.5) with dissolve
    "The back rows were sparsely filled, so much so that I saw Mizutani-san could afford to hang her toned arms of the backs of the chairs on either side of her."
    "The rest of the row was nearly empty, save for a small girl in the corner who I recognized from the night before as Aida-san."
    show PRG-1a at Position(xpos=0.25, xanchor=0.5) with dissolve
    "I also noticed she was looking at me, but as soon as our eyes met she turned away...{w}before slowly turning back to watch me from the corner of her eye."

    menu:
        "Needed the room to stretch out, Mizutani?":
            jump Choice6e

        "Seems kinda lonely back here, Aida...":
            jump Choice6f


label Choice6a:
    hide AE-1a
    hide BBW-1a
    MC "So, Shiori-san..."
    show AE-1a
    AE "Shhh! {w}They're about to start."
    MC "I know, but I was just, ah, wondering--"
    AE "You noticed too? It's weird, isn't it? Normally you have the whole faculty on-stage for these things, but it's just the principal and a few others..."
    "You nod dumbly, realizing only now that behind the principal on sage there were only a handful of faculty members."
    "It definitely seemed sparse, despite the size of the stage, but you weren't about to attribute it to anything nefarious like Daichi would."
    "You open your mouth to try and ask about the ass-squishing she's giving you, but the principal clearing his throat into the microphone snapped Shiori's attention to the stage."
    MCT "No use talking now, I suppose...  But it's nice she thought I was clever enough to notice."
    $ AE_Affection += 1
    jump CeremonyEnd

label Choice6b:
    hide AE-1a
    hide BBW-1a
    MC "Hi there, Nikumaru-san..."
    show BBW-1a
    BBW "Alice, please, no need to be so formal. *giggle* {w}But I'll accept 'Princess' if you insist..."
    MC "Ah, so, uh, Alice..."
    BBW "Hm?"
    MC "Well, your seat- ah, I mean, the seat, it's a little..."
    show BBW-1b
    BBW "Ahahaha~! Yes, the seats are a little small...{w}but you don't mind, I'm sure?"
    "The wink she gave me made me wonder how much of her pressing into me was accidental and how much was intentional."
    show BBW-1a
    BBW  "Oop, they're starting. Eyes forward."
    $ BBW_Affection += 1
    jump CeremonyEnd

label Choice6c:
    hide BE-1a
    hide GTS-1a
    MC "Find your dorm okay, Honoka?"
    show BE-1b
    BE "Yep!  It's amazing how big it is...{w}makes my bedroom at home look like a closet!"
    MC "Yeah, and for freshmen, even!"
    show BE-1a
    BE "But you know what's weird? I haven't seen a single upperclassman yet. Like, not anywhere. They're all starting today, right?  Aren't they?"
    MC "I don't know, really.  Maybe this is some kind of half-day for upperclassmen, they start later than us?"
    show BE-1c
    BE "That could be! I've never heard of a school doing that on the first day, though..."
    MC "I'm sure they'll explain it to us in homeroom. Hopefully we can get seats next to each other!"
    show BE-1b
    BE "Yeah! That'd be great, Kei-chan! Just like old times!"
    MC "Shhh, not so loud, they're starting! But yeah, just like old times..."
    $ BE_Affection += 1
    jump CeremonyEnd

label Choice6d:
    hide BE-1a
    hide GTS-1a
    MC "What was your grade school like, Naomi?"
    show GTS-1a
    GTS "Mine?"
    MC "Sure, you heard about ours..."
    show BE-1a
    BE "Yeah, what was yours like, Naomi-san?"
    show GTS-1a
    GTS "Well, ah, it was...{w}pleasant, I suppose."
    MC "\"Pleasant\"?"
    GTS "That is, ah...{w}it was rather...{w}Mm...{w}My old schools were always very well organized and regimented."
    MC "...Not very fun, then?"
    show GTS-1b
    GTS "They had a wonderful garden in the back."
    MC "Well, hopefully this school will be fun for you."
    hide GTS-1a
    show BE-1b at Position(xpos=0.25, xanchor=0.5)
    BE "Yeah! We'll do all we can to make sure you have at least one fun school!"
    show GTS-1b at Position(xpos=0.75, xanchor=0.5)
    GTS "...Thank you, both of you. Now, we musn't be speaking once the principal starts..."
    $ GTS_Affection += 1
    jump CeremonyEnd

label Choice6e:
    hide PRG-1a
    hide FMG-1a
    MC "Needed the room to streth out, Mizutani?"
    show FMG-1a
    FMG "Oh hey, it's, uh, Hotsure, right?"
    MC "Yep! So, ah, not interested in the speech?"
    FMG "Eh, whatever, I don't mind. Just like the back because I hate being squeezed between people. Gets a litle claustraphobic."
    MC "Yeah, and like, on the trains..."
    show FMG-1b
    FMG "Oh I know, those are even worse! Especially for a tall girl..."
    MC "I hope no one's ever given you trouble..."
    show FMG-1a
    FMG "Heh heh...{w}one guy tried to cop a feel, once."
    MC "What happened?"
    "Mizutani's smile tightened into a predatory, self-satisfied grin."
    show FMG-1b
    FMG "Busted his finger. Wasn't even trying to."
    MCT "Ooooo-kay, I'm suddenly very interested in what the principal has to say..."
    $ FMG_Affection += 1
    jump CeremonyEnd

label Choice6f:
    hide PRG-1a
    hide FMG-1a
    MC "Seems kinda lonely back here, Aida..."
    show PRG-1e
    PRG "Oh!  Uh, ah, well, there's three of us now, right?"
    MC "Heh, I suppose."
    show PRG-1a
    PRG "W-well, you can sit next to me...{w}if you like."
    MCT "Boy, she's acting strange...{w}like she wants to get close but is spooked of it..."
    MC "Nervous about starting at a new school?"
    PRG "A little. Could use a friend..."
    MC "Well, can't everyone?"
    PRG "Yeah...{w}Could- could you be my friend?"
    "She smiled at me, and I felt her lean over in her seat, lightly touching my side with her shoulder."
    MC "Heh, sure...{w}if you need one."
    show PRG-1b
    PRG "I do..."
    "We sat there, listening to the Principal's speech. I noticed Aida-san leaning a little closer into me as it went on."
    $ PRG_Affection += 1
    jump CeremonyEnd

label CeremonyEnd:
    hide PRG-1a
    hide BBW-1a
    hide GTS-1a
    hide FMG-1a
    hide AE-1a
    hide BE-1a
    "The ceremony continued, all dreadfully familliar and rote, but at the end there was something different. The principal settled the papers behind the podium and hesitated for a too-long moment."
    "\"The future is forever uncertain,\" he said.{w} \"But no matter what the future holds, years hence or any day now, one thing is important  above all else.\""
    "\"{i}Nosce te Ipsum{/i} {w}To thine own self be true. Remember that you are more than your station, {w}skills, {w}and especially appearance. If you need help, your teachers are always available to help you with whatever you need.\""
    MCT "What's he going on about...? I'm beginning to wonder if Daichi was on to something..."
    "Finally, the ceremony ended, and we all began to file out."
    show AE-1d
    "I saw Shiori hustle out to stand by the doors ahead of nearly everyone else, her rear wobbling side to side in a way was impossible to not draw the eye."
    MC "Shiori-san?  What's going on?"
    AE "I didn't see Utagachi in the assembly. He'd better not have skipped out on the first day or there will be hell to pay.  Hey, isn't he your roommate?"

    menu:
        "I haven't seen him...":
            jump Choice7a
        "He said he wouldn't miss the ceremony..." if RM_Flag_01: #This menu item will only appear if this variable is True
            jump Choice7b
        "He left the dorm pretty early..." if not RM_Flag_01: #Likewise, this item only appears if the variable is False
            jump Choice7c


label Choice7a:
    MC "I haven't seen him...{w}but he was acting kind of strangely this morning. No telling where he went off to."
    AE "Hmph. He'd better have a good excuse!"
    hide AE-1d with dissolve
    "I left to go to my homeroom class, worrying no excuse would be good enough for Shiori..."
    $ RM_Affection += 1
    $ RM_Flag_02 = 0
    jump HomeroomApproach

label Choice7b:
    MC "Well, he said he was going to make sure not to miss the ceremony..."
    AE "He did? Then why didn't I see him come in?"
    MC "He said he was going to walk around campus a bit this morning, get a feel for the place. Maybe he came in some different door?"
    "Shori looked back into the mostly-empty auditorium, eyes scanning the walls."
    show AE-1a
    AE "You know, I didn't consider that he could have come from a non-proscribed entrance, actually. I'll have to quiz him on the announcement's content later."
    hide AE-1a with dissolve
    "She nodded and left her post, satisfied with the answer, and we both walked to homeroom."
    $ AE_Affection += 1
    $ RM_Affection += 1
    $ RM_Flag_02 = 1
    jump HomeroomApproach

label Choice7c:
    MC "He left the dorms pretty early, don't know where he was off to..."
    AE "Hmph.  Well, he certainly wasn't here. Bah, I don't have time to waste on the likes of him.  Thank you for telling me, though, so I didn't stand there until the bell rang."
    hide AE-1d with dissolve
    "With a derisive grunt, Shiori left her post by the doors and we walked to homeroom together."
    $ AE_Affection += 1
    $ RM_Affection -= 1
    $ RM_Flag_02 = 2
    jump HomeroomApproach

label HomeroomApproach:
    scene School Exterior
    with fade
    "With the principal's strange welcome still echoing in my ears, I headed for the class building, ready to start my academic career at Seichou Academy..."
    
    scene F1 Hallway
    with fade
    "It was very strange to be in the hallways with so few people. Well, there were a normal amount of students, but in Seichou's oversized architecture we all felt miniscule.{w} I spied Honoka and some of my other classmates as we walked along, feeling like ants in a dog carrier."
    show BE-1c
    BE "Just how many students are there here, that they need such big hallways?"
    hide BE-1c
    show FMG-1a
    FMG "Beats me...{w}I feel like I should be putting up a volleyball net or something."
    
    scene Classroom Day
    with fade
    MC "Whoa!"
    show BBW-1a
    BBW "...Is this for real?{w} How come there are so few seats?"
    hide BBW-1a
    show PRG-1a
    PRG "And so far away?"
    hide PRG-1a
    show AE-1a
    AE "Some kind of anti-cheating measure...?"
    hide AE-1a
    jump SeatAssignments

label SeatAssignments:
    "Eventually we all took our seats, looking around at the sparse classroom. All the usual educational aids seemed to be on shelves or set into the wall, making the room seem even more like an empty box than it already was."
    "If not for the teacher's lectern at the front of the class, you'd be forgiven for thinking we were in a pen instead of a classroom."
    "Finally the bell rang, and at the last possible second one could enter and not be late, our homeroom teacher slid open the door and entered."
    MCT "'Dour' is the first word that comes to mind... Guy looks like he's been middle-aged his entire life."
    "The man was tall, and thin but not fit, wearing a collared shirt and dress slacks, with a jacket draped over one arm until he casually tossed it on the lectern. He swiped a piece of chalk up off the board and quickly scratched out his name on it."
    "{i}Tashi{/i}"
    "Tashi-Sensei dropped the chalk back on the tray, turned to us, and stepped forward, leaning against the lectern."
    HR "..."
    show GTS-1a
    GTS "..."
    hide GTS-1a
    HR "..."
    show RM-1a
    RM "..."
    hide RM-1a
    HR "..."
    MC "..."
    "Without a word, Tashi-Sensei opened his mouth, and the classroom gasped as a four foot long tongue flopped out, unfurling down past Sensei's belt."
    show AE-1d with vpunch
    AE "Kyaa~! What is that?!"
    hide AE-1d
    show BE-1c with vpunch
    BE "Oh, ick!"
    hide BE-1c
    show BBW-1d with vpunch
    BBW "Keep that thing away from me!"
    hide BBW-1d with dissolve
    
    "..."
    "..."
    
    HR "All right, go ahead, get it out now. But don't run away or you'll be marked tardy."
    "The non-chalance in the teacher's voice quickly turned the class' mood from panic to confusion, especially as that giant tongue continued to flop around as Tashi-Sensei got into his bag and set his papers down on the lectern."
    HR "All done? {w} Good. Here's how this works."
    HR "Welcome to Seichou Academy. You're here because you, or a sibling, have expressed a certain trait that causes unusual growth of some kind."
    show BE-1c at Position (xpos=0.25, xanchor=0.5) with dissolve
    HR "Some of your growths are already obvious..."
    hide BE-1c
    show PRG-1a at Position(xpos=0.75, xanchor=0.5) with dissolve
    HR "Others...{w}Not so much."
    hide PRG-1a
    HR "But make no mistake, unless you've got a sibling here at Seichou Acadeamy, you're {i}going{/i} to change; even if you do, you've got good odds of changing yourself."
    HR "I know the Principal likes to dance around it, but I'm not going to mince words:{w} Seichou Academy is here to help you deal with whatever you're going to become. Key word being \"Help\"."
    HR "We can get you uniforms that fit, doors you can walk through, and gym classes for any shape and size.{w} What we can't give you is resolve, self-acceptance, the courage to make a life for yourself after whatever life makes out of you." 
    "Tashi-Sensei scanned the room, taking in the fear and confusion, then shrugged."
    HR "Anyways, that's my big freshman speech. Don't expect more.{w} So, roll call. Akayama-San?"
    jump End
    
    
label End:
    show black
    with dissolve
    centered "You have reached the end of this demo of Growth Academy."
    centered "If you'd like to keep up to date with the game's development or contribute and make it a reality, please visit us at: \n https://www.expansiongames.net"
    centered "During each scene, an \"affection\" score for each of the girls were recorded based on your choices."
    centered "In the full game, they will be very important in where the story will lead; including some exclusive plot events and the chance for the girl to fall in love with you."
    centered "For now, they're just plain numbers; here's how you did!"
    centered "Inoue Honoka: [BE_Affection] \n Yamazaki Naomi: [GTS_Affection] \n Mizutani Akira: [FMG_Affection] \n Matsumoto Shiori: [AE_Affection] \n Alice Nikumaru: [BBW_Affection] \n Kodama Aida: [PRG_Affection] \n Daichi Utagashi: [RM_Affection]"
    
    centered "Thanks for playing!"

    return   # Complete Game and Return to Main Menu; End Game conditions can be taken into account for potential rewards (such as exclusive images or the ability to view full-credits for having completed the game).