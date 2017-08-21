define FMG = Character('Akira', color="#FF9900")
define Rin = Character('Rin', color="#CC33FF")

image FMG neutral = DynamicImage("Graphics/FMG-[globalsize]-neutral.png")
image FMG happy = DynamicImage("Graphics/FMG-[globalsize]-happy.png")
image FMG sad = DynamicImage("Graphics/FMG-[globalsize]-sad.png")
image FMG surprised = DynamicImage("Graphics/FMG-[globalsize]-surprised.png")
image FMG angry = DynamicImage("Graphics/FMG-[globalsize]-angry.png")
image FMG aroused = DynamicImage("Graphics/FMG-[globalsize]-aroused.png")

init 2 python:
    datelibrary['FMG_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['FMG_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['FMG_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['FMG_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['FMG_size_2'] = datetime.date(2005, 4, 10)
    
    eventlibrary['FMG001'] = {"name": "FMG001", "girls": ["FMG"], "location": "gym", "conditions": [], "priority": False}
    eventlibrary['FMG002'] = {"name": "FMG002", "girls": ["FMG"], "location": "gym", "conditions": [[ConditionEnum.EVENT, "FMG001"]], "priority": False}
    eventlibrary['FMG003'] = {"name": "FMG003", "girls": ["FMG"], "location": "hallway", "conditions": [[ConditionEnum.EVENT, "FMG002"]], "priority": False}
    eventlibrary['FMG004'] = {"name": "FMG004", "girls": ["FMG"], "location": "track", "conditions": [[ConditionEnum.EVENT, "FMG003"]], "priority": False}
    eventlibrary['FMG005'] = {"name": "FMG005", "girls": ["FMG"], "location": "hallway", "conditions": [[ConditionEnum.PRESET]], "priority": False}
    eventlibrary['FMG006'] = {"name": "FMG006", "girls": ["FMG"], "location": "track", "conditions": [[ConditionEnum.EVENT, "FMG004"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    eventlibrary['FMG007'] = {"name": "FMG007", "girls": ["FMG"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "FMG006"]], "priority": False}
    eventlibrary['FMG008'] = {"name": "FMG008", "girls": ["FMG"], "location": "dormexterior", "conditions": [[ConditionEnum.EVENT, "FMG007"]], "priority": False}
    eventlibrary['FMG009'] = {"name": "FMG009", "girls": ["FMG"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "FMG008"]], "priority": False}
    
label FMG001:
    scene Track with fade #track might not be the right background?
    "After thinking it over, I decided to check out the Athletics Area, so when I have P.E. I would know where it is."
    "Compared to the rest of the academy, the building itself was not only taller, but almost as wide as the rest of the school."
    "From how tall the windows were made the the building looked least two or three stories tall."
    "Wondering if the inside really was big as it looked on the outside, I found myself walking in to satisfy my curiosity."
    scene Gym with fade
    "The inside was was not what I thought it would look like, what I imagined to be a normal three story building turned out to be just one room that was three stories high."
    "The exercise equipment was unique, to say the least; while some did look normal, most of them came in extreme shapes and sizes."
    "One thing I also noticed was that the building was so empty that there was a lone echo coming from the far end of the building and once again curiosity drove me to follow where the source of the echo was coming from."
    "As I got closer to the source, I began to hear someone counting."
    UNKNOWN "...87...88..."
    "From where I was I could tell it was female, but I couldn't make out who it was just yet."
    UNKNOWN "...92...93..."
    "After a minute of looking, I found that the source of noise was coming from a bench-pressing Akira."
    "From what I could guess, she was too focused on her workout to notice me walking towards her, or that she assumed it was just someone who was working out as well."
    show FMG angry with dissolve
    FMG "98...99...100!"
    "Akira then proceeded to put the weights back on the bar and move off the bench press; it was only when she looked up she saw me watching her."
    show FMG neutral
    FMG "Well hey there..."
    extend "Um, your name was Keisuke, right?"
    MC "Indeed it is."
    FMG "All right, Keisuke, got it...So as I was saying...what brings you to these parts?"
    MC "Curiosity mostly, I wanted to checked out the Athletics Area to get a better layout of the school and when I got here I heard an echo that lead me to you."
    show FMG happy with dissolve
    FMG "And here I was thinking you were here to check me out."
    "The way she said that sounded she was joking, but I just found it kinda awkward, still it would be a bit rude not to give some sort of reply."
    "My only response was a light chuckle and then silence. We stood there for about 30 seconds till I spoke up."
    MC "So Akira...how are you holding up?"
    show FMG neutral
    FMG "Huh, what do you mean?"
    MC "Well, I mean that we're going have these 'growths' affect the rest of our lives, so what I'm asking is how you're taking this?"
    show FMG happy
    FMG "Oh, in that case, I'm fine with it."
    MC "Huh, really?"
    show FMG neutral
    FMG "Yeah, I don't know if I will grow or not but if I do, I accept it with open arms."
    MC "You don't know you're going to grow?"
    FMG "Well I mean compared to people like your boob friend or Shiori Buttsumoto, I'd think I look normal enough."
    MC "Well, you are a bit muscular."
    FMG "Yeah. But not overly."
    "She proceed to put her hand under her chin and push her head to left side, causing a series of loud cracking from her neck. She repeated this process with the right before continuing."
    show FMG happy with dissolve
    FMG "I may work out almost every day, but it's not my entire life, Just 80%%."
    show FMG neutral with dissolve
    FMG "So yeah, just call it a hunch. What about you?"
    MC "Well, I don't feel any different but I am kinda worried about my sis-"
    "I didn't get to finish my sentence when Akira looked at a nearby clock and interrupted me."
    show FMG sad
    FMG "Ah crap! It's 5:35! I'm five minutes late for my routine!"
    hide FMG with dissolve
    "She said while running past me to the door."
    MC "Wait, huh?"
    "Was all I could say in flustered state. Akira then turned around, jogging in one spot for a brief moment."
    show FMG sad with dissolve
    FMG "Sorry! I have to go now, if you want to talk you can find me here whenever theres no classes or at the local gym, later!"
    hide FMG with dissolve
    "And in a flash, Akira proceeded to sprint out the door, leaving me in the same spot, still a bit confused."
    MC "Well that happened."
    "With that I left the building."
    jump daymenu
    
label FMG002:
    scene Gym with fade
    "With class over I decided to take a shortcut through the Athletics Area."
    "I'd expected to see Akira coming out of the building, what I didn't expect to see was her looking very tired."
    "I figured she must need some cheering up so went to go talk to her."
    MC "Hey Akira, what's up?"
    "Her facial response was of that of slight confusion and following that annoyance."
    show FMG angry with dissolve
    FMG "Ugh, what do you want Keisuke?!"
    "I was honestly taken aback by Akira's response, but in hindsight with how tired she looked, I probably should have expected this."
    "Her face slowly softened from a face of annoyance to one of regret."
    show FMG sad
    FMG "*Sigh*...Look, I'm sorry, I just get frustrated sometimes."
    "She apologized, for the most part she did look apologetic but she still looked physically tired, if not mentaily."
    MC "Um, is everything all right?"
    "She took a deep breath before answering."
    FMG "Not really, I went too hard on the treadmill and now I'm too tired to do the rest of my routine."
    MC "Really, how?"
    FMG "I thought if I did twice the speed I normally go I'd get it done in half the time."
    "She paused before continuing."
    FMG "For the most part it worked, but I forgot about the side effect of going past your limit."
    MC "I mean, isn't that the goal to push yourself?"
    FMG "Yeah, but the point of it is to PUSH your limit, not fricking PASS it to the point of exhaustion."
    FMG "Trust me, it's not healthy to do that, the body can only take so much exercise before needing to repair muscle. If you keep doing it with no breaks, you're doing more harm than good."
    MC "Well that sucks, what are you going to do now?"
    FMG "I'm going to bed, I need to let my muscles heal. So if it's all the same, I'll be leaving."
    MC "Ok then, bye."
    FMG "...yeah, later."
    hide FMG with dissolve
    "I was about to make my leave, when I heard Akira call out my name."
    show FMG neutral with dissolve
    FMG "Um...thanks for caring enough to ask."
    MC "You're welcome Akira."
    "With that we went our separate ways."
    jump daymenu
    
label FMG003:
    scene Hallway with fade
    "Finally finished with my morning class, I went to get a quick snack from the vending machines before I had to repeat the process with my next class."
    "At least for the most part it was business as usual..."
    FMG "HEY KEISUKE!!!"
    "...That is until I saw Akira sprinting down the hall."
    "I braced for impact,but Akira came to a screeching halt just before colliding into me."
    show FMG neutral with dissolve
    FMG "Yo, how're you?"
    "Akira asked that almost too casually for someone who just came sprinting down a hallway at 32 kph."
    MC "Um...fine?"
    show FMG sad
    FMG "Great, hey look about the other day..."
    MC "Oh you don't have to apologize, you were just having a bad day is all."
    show FMG neutral
    FMG "Yeah I know, but I feel like I should make it up to you. I thought about it and, well, do you want to join me in my work out sessions?"
    MC "Wait, what?"
    FMG "Well I figured I could make it up to you by becoming like your personal trainer."
    MC "My personal trainer? Why?"
    FMG "Well I know that you're not chubby like 'Princess' Alice Whatever-her-last-name-is, but that doesn't mean you're not out of shape either."
    FMG "Plus, it could help having some muscle when in the middle of a fight, or just wanting to look good."
    FMG "But if you don't want to, that's fine, I'm not gonna force you to do something you don't want to do."
    FMG "So, you game?"
    menu:
        "Eagerly agree":
            jump FMG003_c1
        "Agree but at your own pace":
            jump FMG003_c2
        "Refuse":
            jump FMG003_c3

label FMG003_c1:
    $setAffection("FMG", 2)
    MC "Sure, why not? Let's do it!"
    "I honestly have no idea why I came off so excited, maybe some of akira's energy had rubbed off on me."
    show FMG happy
    FMG "Heck yeah! That's the spirit, Keisuke. I expect you at your top fitness..."
    show FMG sad
    FMG "...Wait is it top fitness?"
    show FMG happy
    FMG "Ah screw it, just be ready okey?"
    MC "All right, when do get started?"
    show FMG neutral
    FMG "When the time comes, you'll know..."
    MC "Um... no I don't, t-that's why I-"
    FMG "Oh Crap the bell's gonna to ring in 30 seconds! LATER!"
    hide FMG with dissolve
    "She yelled out before sprinting down the hall... leaving me bewildered."
    MC "...Asked...Wait, 30 seconds!?"
    jump daymenu

label FMG003_c2:
    $setAffection("FMG", 1)
    MC "...All right, I guess..."
    FMG "Yes! We ca-"
    MC "BUT!"
    "I spoke up, catching her off guard."
    MC "I will only do it at my own pace, I don't want to feel like i'm dying after the first session."
    show FMG sad
    FMG "...Oh well...yeah that makes sense."
    show FMG neutral
    FMG "I'll admit I'm a little disappointed, but I'm more glad you're willing to give it a shot."
    MC "Well I am willing as long as-"
    FMG "Oh Crap the bell's gonna to ring in 10 seconds! LATER!"
    hide FMG with dissolve
    "She yelled out before sprinting down the hall... leaving me bewildered."
    MC "...You don't go overboard...Wait, 10 seconds!?"
    jump daymenu

label FMG003_c3:
    $setAffection("FMG", -1)
    MC "Um look it's nice of you to offer but I got too much to worry about with school and everything else."
    "Upon me saying this her facial expressions turned from hopeful to disappointed."
    show FMG sad
    FMG "Oh...ok."
    MC "I'm sorry about this, but thanks for the offer."
    FMG "No it's fine, I'm not made of glass. If you change your mind you know where to find me..."
    MC "...So see you later?"
    FMG "Yeah Later."
    hide FMG with dissolve
    "I honestly felt kinda bad for her but i got too much on my plate to worry about exercise."
    "..Like the fact I'm going to be late for class if I don't move!"
    jump daymenu
    
label FMG004:
    #Should probably acknowledge if it was refused in scene 003
    scene Hallway with fade
    "Another day, another class over...and for once I have nothing to do..."
    "...That is, until a paper ball (that Akira threw before running out of class) hit me on the head."
    MC "Ow."
    "I said more out of reflex than pain, and decided to uncrumple the piece of paper out of boredom."
    "\n{i}The time has come! Meet me at the school's track in 5\n~Akira{/i}"
    "I guess she must have been excited, as she hadn't even put a period at the end of her note."
    "Well, I promised I'd join her, so might as well see what she's up to."
    scene Track with fade
    "By the time I arrived, Akira was already there as expected, doing stretches as I approached."
    "As I got closer she stopped doing her stretches and walked up to me."
    show FMG happy with dissolve
    FMG "Welcome partner, to the beginning of your training!"
    MC "Well I'm ready for whatever, what will we be doing today?"
    show FMG neutral
    FMG "Today we shall do something simple and easy."
    "She's going to make me run, isn't she..."
    FMG "Running this whole track."
    "I hate being right sometimes."
    show FMG sad
    FMG "*sigh*... But we have to do something, first..."
    "She reached for her bag, pulling out two cups with lids on it."
    FMG "...We have to drink...*gag*... these protein shakes."
    MC "Oh that's it, you made it sound like something bad."
    FMG "Well the thing is, I HATE protein shakes. Like a lot."
    MC "Really? I thought protein shakes were important for exercise."
    FMG "Well it is, doesn't mean I have to like them though. Now as much as I want to delay drinking this sludge, it has to be done."
    "She took it in one go, eyes shut tight the entire time. When she finished it she looked like she was about to vomit."
    "I knew I had to drink it as well, but I figured Akira might just be over exaggerating , I mean can't be that-"
    MC "*GAG*"
    "Oh god, why didn't she add fruit or something..."
    "Well I've already agreed to this, might as well finish it."
    FMG "Ugh... God, I feel like I'm gonna die every time I drink those things."
    MC "Yeah I don't blame you...just what was is in that?"
    show FMG neutral
    FMG "It's just water and protein powder, why?"
    MC "Ever thought of using a liquid that has flavor, like milk or Berry tea?"
    "She just looked at me with no expression, but I swear I could hear her screaming internally."
    FMG "..."
    extend " Oh well, there's always next time."
    show FMG happy
    FMG "Now that the hard part is over, now we get to the actual exercise! Don't worry, I'm not asking for you to run a mile, just a quarter of one!"
    FMG "Today we're going to just make one lap around this track."
    "I followed her to the starting point."
    show FMG neutral
    FMG "All right, ready..."
    FMG "GO!"
    hide FMG with dissolve
    if getSkill("Athletics") < 5:
        jump FMG004_testfail
    else:
        jump FMG004_testpass

label FMG004_testfail:
    $setAffection("FMG", -1)
    MCT "Ok, Akira's got the lead, but if I can keep a good pace I can do this!"
    MCT "I can do this!"
    MCT "...I can do this..."
    MCT "...I...can...do...this..."
    "I realized Akira had already finished, and she was walking towards me... and I wasn't even near halfway done."
    show FMG sad with dissolve
    FMG "Um...are you okay?"
    "Her concern was clearly shown."
    MC "I... can't *wheeze* do this..."
    FMG "But... dude you're not even half way."
    "Her concern turned to slight annoyance."
    MC "Don't...care *heavy breathing* must... rest..."
    show FMG angry
    FMG "Dude, you're really not making a good first impression, you're worse off than I thought."
    "Now she looked REALLY annoyed."
    MC "...Tell... Daichi...I took his last chocolate...b-bar..."
    FMG "You're not even dying you big baby!"
    hide FMG
    "The last thing I saw before my world was swallowed in darkness was a angry Akira."
    "When I woke up it was an hour later, Akira was nowhere to be found,but there was a piece of paper on my chest."
    "\n{i}Dear Kei, WORK ON GETTING IN FRICKING SHAPE!\n~Akira{/i}"
    "...Yeah I get the feeling Akira is not going to let me live this down..."
    jump daymenu

label FMG004_testpass:
    $setAffection("FMG", 1)
    "Despite Akira already in the lead, I managed to keep a good pace."
    "I started to feel a bit winded half way but I pushed myself to go farther."
    "It was about to the end when I was starting to get too tired, luckily I've managed to run the whole lap before stopping completely."
    show FMG happy with dissolve
    FMG "WOO!"
    "Akira fist pumped before walking towards me."
    FMG "Great job there dude, you sure got potential!"
    MC "But I lost, you won by a landslide."
    FMG "It's not about competing, it's about giving all you got and you stuck with it all the way to the end!"
    FMG "Stay right there, need to go get something from the vending machines."
    hide FMG
    "She run to where the vending machines were. When she came back, in each of her hands was ice cream, one cherry blossom and one vanilla."
    show FMG happy
    FMG "Here, A congratulation prize, didn't know what flavor you liked so I got you vanilla."
    MC "Ice cream? But isn't that like the worst thing you could have during a workout?"
    show FMG neutral
    FMG "True, but i'd probably burned half the calories of this ice cream pop in this run, and that's not including the rest of my workout today."
    "I don't think that's how it works..."
    FMG "Besides, I'll take eating a ice cream pop and workout the entire day then drink a fricking protein shake and workout just for only an hour any day of the week."
    MC "At least you got your priorities straight."
    show FMG happy
    FMG "Hell yeah I do!"
    "We stayed there for a while till both ice cream's were finished. Akira tossed her popsicle in the trash before turning to me."
    show FMG neutral
    FMG "Well this has been fun, lets call it a day shall we."
    MC "Sure, but I got a question."
    FMG "Shoot."
    MC "Why vanilla?"
    FMG "I don't know, you seem like a vanilla kinda guy."
    "I don't know why but I got a chuckle out of that."
    "I waved good bye before heading back to my room."
    jump daymenu

label FMG005:
    scene Hallway with fade
    "As much as I didn’t like the shot, I am glad this is all over. Well I have nothing better to-"
    FMG "*sniff*"
    "That’s odd, it sounds like there’s someone crying near the corner."
    FMG "*sob*...Why did I have to get a shot...*sob*"
    "As I walked closer to the corner, I saw the one person I did not expect to be crying ...Akira Mizutani."
    show FMG sad
    FMG "...Hey..."
    "She looked slightly annoyed and she had her left hand on her right upper arm...but I could tell there was some moisture still under her eyes."
    menu:
        "Are you okay?":
            jump FMG005_c1
        "Man shots suck.":
            jump FMG005_c2

label FMG005_c1:
    $setAffection("FMG", -1)
    FMG "No, I just had a stupid needle jammed into my arm to find out my growth factor, which by the way was a waste of time."
    MC "Okay...Well what was it?"
    "I did my best to try and act dumb for her sake but instead she took it the wrong way."
    show FMG angry
    FMG "MY MUSCLES!"
    "I was taken back from her outburst, to which she grudgingly looked away."
    show FMG sad
    FMG "Look, I'm not in the best of moods so just leave me alone for now, ok?"
    "She preceded to walk away from me, I figured it was best to leave her alone."
    jump daymenu

label FMG005_c2:
    $setAffection("FMG", 1)
    MC "Man, shots suck, am I right?"
    "I felt that it was best to try to lighten her up, and it seems I was rewarded."
    show FMG neutral
    FMG "Heh, yeah they do, i'm guessing you heard all of that?"
    MC "Um..."
    FMG "It's fine, just don't go spreading what just happened, I kinda have an image to uphold."
    MC "Fair enough then."
    MC "...so will you be all right?"
    FMG "Well it's not the growth that's affected me the most...it's the needles."
    MC "Um, if I may, why do you hate needles so much?"
    FMG "When I was 3 I was playing in the backyard when a rabid raccoon bit me on my leg...hard."
    "She emphasized this by pulling down her right sock, revealing a scar in the shape of a bite on her calf."
    FMG "If you were wondering why I wear my socks so high, that's why."
    "She pulled up her sock before continuing."
    FMG "My parents rushed me to the hospital where they injected me with all kinds of needles."
    show FMG sad
    FMG "I think it's a combination of the bite and the needles that kinda f'd me up."
    FMG "Just the sight alone makes me hyperventilate...but when it goes under is when I start getting pissed."
    MC "Wow...I don't know what to say."
    show FMG neutral
    FMG "Don't worry about it, I mean it's not something I care for, but I usually feel better when talking about it...well when I calm down at least..."
    FMG "Otherwise I'd just get mad for no good reason."
    FMG "All right, if it's all the same to you I'd rather be alone right now."
    FMG "But for what it's worth, thanks for the talk...I REALLY needed it. Oh and in case you were wondering, my factor is my muscles, kinda obvious in retrospect. See Ya."
    hide FMG
    "With that she left, leaving me alone next to the door to the nurse's office."
    jump daymenu
    
label FMG006:
    #evening only?
    scene Classroom Day with fade
    "Another day of classes ended, and for once I actually felt like working out today. I walked to Akira’s desk just as she got up, once she saw me walking towards her she put a paper ball behind her back... like I hadn't noticed."
    show FMG neutral with dissolve
    FMG "Um, hey Kei, I was about to head your way, got anything planned for the next hour?"
    MC "Not really, did you want to exercise more? Because I feel like it today."
    FMG "Oh! Yeah, I got time for you today. I got to get my workout stuff so meet me to the athletics area in five, OK?"
    MC "All right, sounds good."
    "She walked out the door... But not before not before throwing that ball at my head."
    hide FMG with dissolve
    FMG "Sorry, can't waste a good paper ball!"
    MC "...Why does she keep doing that..."
    scene Track with fade
    "By the time I got to the athletics area, Akira was already doing her warm up stretches."
    show FMG neutral with dissolve
    FMG "Hey there, you know I’m kinda surprised that you came to me today. But anyways, first order of business is the shakes."
    MC "You look more happy about that than last time."
    FMG "Thing is, you know I hate protein shakes, right?"
    MC "Right."
    show FMG happy
    FMG "Well, I've been experimenting with different drinks, and I found one that doesn't make me want to vomit to death."
    "She pulled out her shake cup from her bag in triumph."
    FMG "Behold and be amazed!"
    MC "Isn't that the same thing?"
    show FMG neutral
    FMG "Shut up and let me have this moment."
    show FMG happy
    FMG "Milk protein coffee ice cream shake!"
    FMG "Basically I mixed coffee flavored ice cream with a bit of milk with the protein powder and the final result was this."
    MC "Huh, you really like ice cream don't you?"
    FMG "Yep, it's my third or fourth favorite thing ever!"
    "She drank it in one go, with a little still inside."
    show FMG neutral
    FMG "Ahh, that tasted almost drinkable!"
    "Akira slammed the drink on a nearby table; however, she didn't realize until it was too late that she slammed it on the edge, causing it to fall down on the carpet and leave a stain."
    show FMG angry
    FMG "...Oh come on!"
    FMG "Great, now we gotta clean this before it stains..."
    MC "Oh well, all right."
    "Much to Akira's dismay, we spent about the next hour cleaning the carpet. By the time we finished, Akira looked...upset?"
    FMG "Man this blows...cleaning that carpet took over an hour, we don't even have time to work out."
    "I don't think I've seen her like this, the question is why though."
    MC "Don't worry, we can exercise some other time."
    show FMG sad
    FMG "{i}Sigh{/i} Kei, that's not what I'm mostly bummed about, I wasted your time by cleaning a mess I made when you could have done something more fun..."
    "Oh, she feels guilty for making me help her out..."
    menu:
        "Buy her ice cream":
            jump FMG006_c1
        "Try to make her feel better":
            jump FMG006_c2
        "Make your leave":
            jump FMG006_c3
            
label FMG006_c1:
    $setAffection("FMG", 1)
    MCT "Geez, I don't want her to feel bad just because I helped her, there's gotta be something I could... That's it!"
    MC "You know what? Wait right there for a minute, okay?"
    show FMG neutral
    FMG "Huh, what are you doing?"
    MC "Just a minute!"
    MC "Here, I know you feel bad but I figured I could cheer you up with -"
    show FMG happy
    FMG "{i}GASP{/i} FREE ICE CREAM!? GIMME GIMME GIMME!"
    "In a flash, Akira grabbed the ice cream and proceeded to consume it as quick as a five-year-old who just discovered ice cream."
    "It only took her thirty seconds for her to eat the entire ice cream bar...how did she not get a brain free- ECK!"
    "And wrapped me in a VERY tight hug."
    FMG "Thank you so much! "
    MC "Yo-u're... wel-come... bu-t c-can’t breathe."
    show FMG neutral
    FMG "Oh!"
    "She let go before fully crushing my body."
    show FMG happy
    FMG "Sorry about that, I’m just a bit happy is all."
    MC "It's fine, I just wanted to let you know I’m not upset about it at all."
    FMG "Well, thanks for that, I really appreciate it."
    "I looked at the time and it was almost 7 pm."
    MC "I think it’s time we head out."
    show FMG neutral
    FMG "Yeah, it’s getting late, thanks again for everything."
    jump daymenu
    
label FMG006_c2:
    MC "Um...Hey don't worry about it, It had to be cleaned up so..."
    "...Yeah I have no idea what I'm doing, at least she stopped looking sad."
    show FMG neutral
    FMG "Yeah I know, I’ll find a way to make it up to you."
    MC "Um...you don-"
    FMG "I swear, I will make up for my mistake and wasting your time!"
    MC "Please-"
    show FMG angry
    FMG "THIS I SWEAR!!!"
    hide FMG with dissolve
    MCT "...Aaannnd she is out of here..."
    MCT "Well it's out of my hands now, might as well go back to the dorms."
    jump daymenu

label FMG006_c3:
    $setAffection("FMG", -1)
    "Um this is awkward so..."
    MC "Look it's late, how about we do this later?"
    FMG "{i}Sigh{/i} Fine, whatever..."
    MC "So...we good?"
    FMG "Sure, whatever."
    "I think it's best just to leave her alone for now..."
    jump daymenu
    
label FMG007:
    scene Cafeteria with fade
    "Lunch hour. The cafeteria was bustling with the sounds of infinite conversations from students blending together into different shapes and sizes, making it hard to differentiate one from another."
    "I walked past table after table of students eating, talking, even one student was passed out, besides that there was nothing out of the norm."
    "At the far end, near the windows, was an all too familiar bodybuilder.  Akira was resting her head on her hand, taking slow but big bites from what was left of her stir-fried beef and rice, and while she didn’t look tired, she was staring into space."
    show FMG neutral with dissolve
    MC "Hey, is it all right if I eat with you?"
    FMG "Sure, I'm almost done but take a seat."
    MC "Hey, do you want to work out after class?"
    show FMG sad
    FMG "Yeah, sorry, but I'm not feeling it today. I got a knot the size of a baseball in my thigh and it’s a pain to walk, let alone work out. All I want to do is eat my lunch."
    MC "Oh, sorry."
    show FMG neutral
    FMG "Don't worry about it."
    "For the next few minutes we ate in silence. By the time Akira was finished, she decided to start a conversation."
    FMG "So what do you do in your spare time?"
    MC "Nothing really, just whatever I feel like at the time. What about you, besides the obvious?"
    FMG "I play arcade games."
    "Considering Akira's lifestyle choices, arcade games kinda came out of left field."
    FMG "Oh come on, don't look so surprised. Just because I work out doesn't mean I don't have other hobbies."
    menu:
        "Encourage":
            jump FMG007_c1
        "Apologize":
            jump FMG007_c2
        "Rationalize":
            jump FMG007_c3

label FMG007_c1:
    $setAffection("FMG", 1)
    MC "So...what’s your favorite arcade game?"
    FMG "...Rage of the Waste."
    MC "Isn’t that the rail shooter set in a 80’s vision of the future?"
    FMG "No, you’re thinking of Cyber Revolution: Crimson Beam. Which by the way is my second fav."
    FMG "RotW is a fighting game that takes place in a post apocalyptic Los Angeles, U.S.A. Where an angry defence engineer single handedly caused the apocalypse by launching nukes at Russia."
    MC "Sounds interesting."
    show FMG happy
    FMG "Yeah, if we ever get the chance, let’s play some okay?"
    MC "Sure, love to."
    "Akira smiled at the prospect before making her leave."
    jump daymenu
    
label FMG007_c2:
    MC "Sorry, it's just I never pictured you the gamer type."
    FMG "Blame my dad, his hobby rubbed off on me."
    "She explained half heartedly, before getting up to leave."
    FMG "Later."
    MC "Bye."
    jump daymenu

label FMG007_c3:
    MC "I mean, the only times I see strong people around the arcade are usually jerks who'd take smaller kids' yen..."
    show FMG angry
    extend "Wait, I didn't mean it like that!"
    FMG "Wow dude, way to judge a book by its cover!"
    MC "Wait, I'm-"
    FMG "Ugh, why do I even try..."
    hide FMG dissolve
    "She left before I could explain...though to be fair I don't think I could have salvaged that."
    jump daymenu

label FMG008:
    scene Dorm Exterior with fade
    "I wasn't really going anywhere today, just felt like going for a walk and taking in the sights."
    "Days're a bit hotter, students are hanging out, Mizutani-san is trying to get something under a vending machine, wind's a bit- ...wait, what?!"
    "My mind wasn't playing tricks; Akira Mizutani was on her knees trying to get something from under the machine."
    show FMG angry
    FMG "Oh come on, you stupid pencil!"
    "She groaned in frustration before getting up, once she did she saw me watching her."
    show FMG sad
    FMG "*Sigh* Hey."
    MC "Um... What's wrong?"
    FMG "Ugh. My only pencil fell behind the vending machine and my arm's too big to fit. I'd move the stupid machine if I wasn't afraid I might break something!"
    "She went to grab a fallen stick from one of the trees, and went back down to the vending machine to try to poke the pencil out. Alas, the stick only pushed the pencil further back."
    show FMG angry
    FMG "A-Are you for real!? Ugh!"
    MC "Sorry to hear that, do you want to borrow a pencil?"
    "She calmed down before answering."
    show FMG neutral
    FMG "Nah. I'd feel like I owed you a new one, and I barely got enough cash for myself."
    MC "Well, is there anything else I could do?"
    FMG "Actually... Hey, you got smaller hands than I do, think you could grab it for me?"
    MC "Oh, sure, I'll try."
    MCT "Wait, what did she say about my hands? Nevermind..."
    "It was hard to reach, but I got it."
    show FMG happy
    FMG "All right, thanks dude!"
    FMG "..."
    show FMG sad
    FMG "Huh... You know something... That's one thing I'm not looking forward to..."
    MC "Excuse me?"
    FMG "My muscles. Well, the whole growth thing in general. With how things are going, I'm gonna grow so big, it's going to be hard to fit in small places."
    show FMG neutral
    FMG "Don't get me wrong, I'm looking forward to see how big I might get, I just hope I'm not sacrificing my mobility in the process."
    FMG "It's worrying, but like I said before; whatever happens, I accept it with open arms."
    show FMG happy
    FMG "Anywho, it's been fun but I gotta jet! Thanks again!"
    "Huh. now I'm beginning to wonder if I got lucky or not with my growth..."
    jump daymenu

label FMG009:
    scene Dorm Exterior with fade
    "The day went by as normal, the sun was setting, people were talking and hanging out, and I find myself craving a Rocco-Choco Bar from the vending machines. To my surprise, Akira was waiting near the vending machine; for the most part she seemed a little annoyed, but calm."
    show FMG neutral with dissolve
    FMG "Hey Kei, what's up?"
    MC "Nothing much, just getting something from the vending machine. What's up with you?"
    show FMG sad
    FMG "*Sigh* I'm waiting for someone because I need to talk to her. Speak of the devil..."
    "Just like she said, there really was someone walking towards us. A redhead with a small scar on her right eyebrow, wearing what I could describe as an punkish version of the school uniform, which gave her this aura of disobedience and defiance."
    "There were two big things that really made her stand out. One: her eyes were as blue, if not bluer than Alice’s, which could mean she's a foreign exchange student. And two..."
    "...Her nipples were easily seen bulging through the fabric of her shirt."
    UNKNOWN "Yo Akira, I'm here so what did you... wait, are you trying to hook me up with this guy?!"
    show FMG neutral
    FMG "What?! No! God Rin, this is something different."
    UNKNOWN "Well sorry then but, who and why is he here?"
    FMG "Well since you asked, this is Keisuke. He was just saying hi before you got here."
    UNKNOWN "Oh, this is that Keisuke kid you've been spending your time exercising with? Well then, allow me to introduce myself."
    Rin "The name’s Rin Blackbourne, pronounced Black-burn; weird last name in these parts, I know, but I was born and raised in Manchester, England after me mum moved from Japan."
    MC "Nice to meet you. So, how do you know Akira?"
    FMG "She’s my roommate,"
    show FMG angry
    extend " who by the way STILL has yet to get her dirty clothes off the bathroom floor!"
    Rin "*sigh*, really Mizutani, that's why I'm here? Would it kill you not to bring it up every day?"
    FMG "Let's not forget that you leave half-empty bags of potato chips all over the floor; I wouldn't care if our room didn't smell like sour cream and onions! I swear, you sure are a slob!"
    Rin "In my defense, that Butts-in-moto brat has been watching me like an ex-girlfriend, plus I’m the president of the art club! I gotta be there or else it will come crashing down like the Berlin Wall!"
    FMG "Ugh! Why do you feel the need to push the blame on others?! Admit it, You're just lazy Rin!"
    Rin "Akira, just because you're my roommate and stronger than me, doesn’t mean I ain't gonna knock ya bloody teeth in if ya don’t knock it off!"
    "It looked like the both of them were going to fight it right here..."
    MC "Um, hey gu-"
    FMG "Ugh! I'm not dealing with this now!"
    "Akira lashed out before walking away, all the while angry."
    hide FMG
    extend " Rin, for her part, just looked back at me defeated."
    Rin "*sigh* sorry you had to be part of that, she can be a little hot-headed."
    "She apologized, before walking to the vending machine to buy chips, it's only when she grabbed the first chip she said more."
    Rin "Heh, she is right about one thing, I really am lazy."
    "She emphasized this by eating the chip. I honestly didn't really know how to take this, so maybe an apology was in order."
    MC "Well, sorry if I made you uncomfortable in any way."
    Rin "Oh no, far's I can tell, you did nothing wrong. Akira's just having some issues of her own."
    Rin "In any case, if you really want to get along better with her, try to take her boisterous attitude with a grain of salt."
    MC "What do you mean by that?"
    Rin "My gut is telling me that she's hiding something, but I ain't gotta clue as to what."
    Rin "As for me, I suppose I'll still help her when you're not around. Later Kei."
    jump daymenu