define BBW = Character('Alice', color="#CC33FF")
define Lunch = Character('Lunchlady', color="#CC33FF")
define Francois = Character('Francois', color="#CC33FF")
define BBWCell = Character('Alice', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')

image BBW neutral = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-neutral.png",
    "True", "Graphics/BBW-1-neutral.png")
image BBW happy = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-happy.png",
    "True", "Graphics/BBW-1-happy.png")
image BBW sad = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-sad.png",
    "True", "Graphics/BBW-1-sad.png")
image BBW surprised = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-surprised.png",
    "True", "Graphics/BBW-1-surprised.png")
image BBW angry = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-angry.png",
    "True", "Graphics/BBW-1-angry.png")
image BBW aroused = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-aroused.png",
    "True", "Graphics/BBW-1-aroused.png")
image BBW haughty = ConditionSwitch(
    "gametime > datelibrary['BBW_size_2']", "Graphics/BBW-2-haughty.png",
    "True", "Graphics/BBW-1-haughty.png")

image cg BBW001 = "Graphics/BBW-SC-1.png"

init 2 python:
    datelibrary['BBW_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_2'] = datetime.date(2005, 4, 10)
    
    eventlibrary['BBW001'] = {"name": "Human Resources", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME]], "priority": False}
    eventlibrary['BBW002'] = {"name": "Concerning a Missing Right Arm", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME]], "priority": False}
    eventlibrary['BBW003'] = {"name": "Necessity is the Mother of Employment", "girls": ["BBW", "PRG"], "location": "cookingclassroom", "conditions": [[ConditionEnum.ISDAYTIME]], "priority": False}
    eventlibrary['BBW004'] = {"name": "As Long as the Job Gets Done, Right?", "girls": ["BBW", "PRG"], "location": "classroom", "conditions": [[ConditionEnum.ISNIGHTTIME]], "priority": False}
    eventlibrary['BBW005'] = {"name": "What to Expect When You're Growing", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.PRESET]], "priority": False}
    eventlibrary['BBW005A'] = {"name": "You Ate, You Drank, and You Were Merry, For Today You Diet", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.FLAG, "BBW005_ondiet"]], "priority": False}
    eventlibrary['BBW005B'] = {"name": "Pump You Up, Not Plump You Up", "girls": ["BBW", "PRG", "FMG"], "location": "gym", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.FLAG, "BBW005_workout"]], "priority": False}
    eventlibrary['BBW006'] = {"name": "A Proud Patron of the Arts", "girls": ["BBW"], "location": "hallway", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    eventlibrary['BBW007'] = {"name": "Her Other Fluent Language", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    eventlibrary['BBW008'] = {"name": "How to Train Your Diva", "girls": ["BBW", "PRG"], "location": "musicclassroom", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.EVENT, "BBW006"]], "priority": False}
    eventlibrary['BBW008A'] = {"name": "The Fat Lady Won't Sing", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.FLAG, "BBW008_extrascene"]], "priority": False}
    eventlibrary['BBW009'] = {"name": "Between a Soft and a Hard Place", "girls": ["BBW", "PRG", "FMG"], "location": "pool", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.EVENT, "BBW008"]], "priority": False}
    eventlibrary['BBW010'] = {"name": "ABC: Always Be Clothing", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.EVENT, "BBW007"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW011'] = {"name": "True Romance", "girls": ["BBW", "PRG"], "location": "hallway", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW012'] = {"name": "Business Business Business Numbers", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.EVENT, "BBW010"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW013'] = {"name": "The Elephant In The Room", "girls": ["BBW"], "location": "hallway", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW015'] = {"name": "This is the Stealth Section", "girls": ["BBW", "AE"], "location": "dormexterior", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.EVENT, "BBW012"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW016'] = {"name": "BBW016", "girls": ["BBW"], "location": "dormexterior", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.EVENT, "BBW012"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW017'] = {"name": "What's She Got That I Haven't Got More Of?", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]]], "priority": False}
    eventlibrary['BBW020'] = {"name": "I Like Big...?", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BBW_size_2"]], [ConditionEnum.FLAG, "BBW017_testpass"], [ConditionEnum.NOFLAG, "BBW008A_fail"]], "priority": False}
    
label BBW001:
    scene Cafeteria with fade
    MC "Well! That was... a first day. I didn't expect the school to be exactly like my old one, but on a list of unexpected surprises I didn't think..."
    MC "OK, I guess I couldn't have expected it for it to be a surprise."
    extend " But still, if the teacher had ripped off his face to reveal an alien underneath I wouldn't have been more surprised."
    MC "At least food is familiar enough. A nice snack after class is normal, right?"
    UNKNOWN "I'm sorry, you must not realize who you're talking to."
    MC "I wonder who that is."
    "Standing near the doors leading to the kitchen itself was the heavyset girl from my class. There was a man in a chef's outfit standing behind her, and she was arguing with an old woman in an apron and hairnet."
    show BBW angry with dissolve
    BBW "The name is Alice Nikumaru."
    BBW "I am sure there was some kind of memorandum circulated among the staff announcing my arrival at this school."
    extend " A missive to let you all know that I am here and that special accommodations to satisfy me would be instituted."
    Lunch "If you have an allergy or other dietary need, I would have been told."
    BBW "You there. Tell... Madame Hairnet here who I am."
    MC "She's a student. She's in my class."
    show BBW haughty
    BBW "I am THE student, as far as you are concerned. You may see hundreds of others passing down your line as you ladle warmed over spaghetti sauce onto rubber pasta, but I am not just another stomach to fill."
    MCT "You didn't hear the part about me being in your class, did you?"
    BBW "The meals you mass-produce for the student body may be satisfactory given the level of culinary talent you possess, but I have greater needs."
    BBW "Francois here studied at the finest institutes in France, Italy and Japan, all for the sake of honing his skills to a level suitable for me."
    Lunch "We make enough food for even the fat kids. Don't worry, you'll get your share."
    show BBW angry
    BBW "I am NOT some 'fat kid'. I am not even obese."
    show BBW neutral
    BBW "And it is not a matter of quantity, but quality. My palate is a delicate instrument that needs to be handled with care. I have certain expectations that you – as qualified for this job as you may be – can not meet."
    BBW "Now, I've already gone to the trouble of ordering the equipment you probably don't have – wood-fire pizza oven, rotisserie, espresso machine, meat smoker; just a few odds and ends..."
    BBW "But he will need, say, 20%% of your workspace emptied out and handed over to him."
    Francois "And deliveries."
    show BBW happy
    BBW "Of course. And he needs to have deliveries made every day, so if you could give him the address and directions to this building, that would be wonderful."
    MCT "Oh, is that all? Your own private chef and special deliveries every day? Just how loaded is this girl?"
    Lunch "Students don't get to bring private chefs with them, princess. Outsiders don't get access to our kitchen or any other facilities on campus. Either you can take what we offer you, or you can make your own meals in the Home Ec classes."
    show BBW angry
    BBW "What? Francois can not perform at his best in a classroom kitchen. He needs a full assemblage of utensils and appliances-"
    Lunch "I said you can make your meals."
    extend " Yourself."
    show BBW haughty
    BBW "Do you really expect me to subject my dainty hands and creamy skin to the raw ingredients that come with making a three-star meal?"
    BBW "Do you have any idea how much this manicure costs? What would handling an ox tongue or a raw Cornish game hen do to it?"
    Lunch "If you don't get out of my kitchen in the next five seconds, you'll be dunking that expensive manicure in cold, greasy dishwater as I have you scrubbing every pot and pan we have."
    show BBW angry
    BBW "You... You wouldn't."
    Lunch "You wouldn't be the first student punished with kitchen duty."
    BBW "Very well, but this is not the end. A Nikumaru does not give up."
    show BBW neutral
    BBW "Did you see that?"
    MCT "Did you forget that you talked to me not two minutes ago?"
    menu:
        "Yeah. Typical hard-ass school employee, being cruel for the sake of it.":
            jump BBW001_c1_1
        "That was kind of harsh. She could at least have tried to work something out with you.":
            jump BBW001_c1_2
        "I've heard of spoiled little girls, but your own private chef? That's a whole new level.":
            MC "I've heard of spoiled little girls, but your own private chef? That's a whole new level."
            BBW "Is it 'spoiled' to have the best that money can buy? I am Alice Nikumaru."
            jump BBW001_c1_after

label BBW001_c1_1:
    MC "Yeah. Typical hard-ass school employee, being cruel for the sake of it."
    show BBW haughty
    BBW "Maybe this is how they do it at lesser institutions, but in my experience schools exist for the betterment of the students."
    extend " If this is a taste of how this place operates, perhaps transferring is the sensible thing. There must be other schools that can handle my needs."
    MC "I guess if you can have a private chef, you can also have a private tutor."
    jump daymenu

label BBW001_c1_2:
    MC "That was kind of harsh. She could at least have tried to work something out with you."
    BBW "Absolutely. Life is filled with give and take, and she wouldn't even come to the negotiating table. How is it that so many people can not understand the basics of business deals?"
    MC "Fancy yourself something of a business-woman, eh?"
    show BBW happy
    BBW "I know a lot about how the world works. It's an inherited trait."
    jump BBW001_c1_after

label BBW001_c1_after:
    show BBW neutral
    BBW "Perhaps you've heard of my father, Daitaro Nikumaru?"
    menu:
        "Daitaro... Isn't he some sort of businessman?":
            jump BBW001_c2_1
        "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?":
            jump BBW001_c2_2

label BBW001_c2_1:
    MC "Daitaro... Isn't he some sort of businessman?"
    show BBW happy
    BBW "Not just 'some sort' of businessman. He is the leader of the heavy manufacturing and seafood industries in Japan. He is ranked on the list of the richest people in the world."
    MC "Consider me impressed. But if he's so rich, couldn't he just buy this school and install Francois as head chef?"
    show BBW neutral with dissolve
    BBW "Francois is not a garden-variety chef you can put in charge of just any mess of underlings. His talent is best utilized when he can focus on a single diner's menu."
    extend " But you do raise a good point. Perhaps I should have a chat with Father."
    hide BBW
    MC "I- Is she really going to ask her father to buy this school? Just because she doesn't want to eat the cafeteria food?"
    jump daymenu
    
label BBW001_c2_2:
    MC "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?"
    show BBW angry
    BBW "* scoff * Is there not a single ounce of class or breeding in this place?"
    hide BBW
    MC "I'd settle for an ounce of humor."
    jump daymenu
    
label BBW002:
    scene Cafeteria with fade
    MCT "This place seems kind of quiet for a high school cafeteria. Everyone's so subdued, it's like someone died. Guess I'm not the only one who was thrown for a loop by yesterday's news."
    MCT "We're all probably wondering the same thing: what's going to happen to me? How... big am I going to get? Am I going to end up like one of those people who can't live in normal society?"
    MCT "Ugh, this is too heavy for first thing in the morning. Let's just get something to eat and take the day as it goes."
    MCT "..."
    MCT "Now to find a table. Oh! There's Alice, eating by herself. I don't think she'd mind if I joined her."
    "I found Alice sitting at a table, a few plates and bowls of food in front of her. She looked unimpressed by the spread."
    show BBW neutral with dissolve
    MC "Mind if I join you?"
    BBW "Be my guest. Perhaps you could help me with something."
    MC "Uh, sure! What's on your mind?"
    "Alice held up a fork with a piece of fish on it."
    BBW "This fish. There's something familiar about it."
    MC "It's mackerel. Fish is a common part of Japanese breakfasts."
    show BBW haughty
    BBW "I know that. I've lived here for most of my life. And 'common' may be the best word for what I am eating. I would never have known what this uninspired morsel was if you hadn't told me."
    "She ate the forkful of fish, her face displaying bland disgust."
    BBW "So tell me this: why, when there are literally hundreds of ways of turning even as pedestrian a choice as mackerel into an appetizing entree, did the staff in this kitchen decide to approach their job like they were vulcanizing a piece of rubber?"
    BBW "Is it because they are just that incompetent? What sort of 'cook' treats their ingredients so disdainfully?"
    MC "I don't know. Grilled mackerel's pretty good."
    BBW "I wouldn't mind having mackerel if it was properly prepared. Poach it, bake it in a honey chipotle glaze, something. But I guess that's too much to ask. Just slap it on a grill, turn it after a minute, job's done, right?"
    show BBW neutral
    BBW "Perhaps I should find out who is supplying seafood to this school and have Father undercut them. We could get some decent food in here without profits being too razor thin."
    MCT "Please don't talk about your father influencing the school with his wealth. I don't know if you're joking or if you actually will try it. Or if you even can."
    jump BBW002_prechoice
    
label BBW002_prechoice:
    menu:
        "What do you normally have, if not mackerel?" if not getFlag("BBW002_c1_1"):
            jump BBW002_c1_1
        "What do you normally have, if not mackerel? (disabled)" if getFlag("BBW002_c1_1"):
            pass
        "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once.":
            jump BBW002_c1_2
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1

label BBW002_c1_1:
    $setFlag("BBW002_c1_1")
    MC "What do you normally have, if not mackerel?"
    BBW "Tuna, usually. Though for breakfast I prefer something more like a French menu with coffee, berries in cream, and a croissant. Maybe a poached egg. I'm very particular about my breakfast; a heavy meal to start the day can leave me feeling lethargic for hours."
    "She picked up her mug and drank from it, showing the same mild disgust."
    show BBW angry
    BBW "And this is not coffee. I'll have to call Mother later, have her send my French press here."
    BBW "I suppose it was foolish of me to think this place would have proper coffee, but I was told this was an exclusive institution. So far the only thing 'exclusive' is the most uninspired menu I have ever encountered. Is this what you eat every day?"
    jump BBW002_prechoice

label BBW002_c1_2:
    MC "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once."
    show BBW neutral
    BBW "All the more reason to let me have Francois on hand. It's unnecessary to force every student here to subsist on this food, and to have someone like me – someone accustomed to a certain standard – suffer this it becomes downright cruel."
    MC "It's not that bad. I've had better, but I've definitely had worse."
    MCT "Besides, you managed to clear your plates."
    show BBW haughty
    BBW "You must not have had much better than this, but trust me when I say that offering this to my refined palate is like substituting Mascagni with... think of the name of some vulgar pop diva."
    MCT "I don't know who Mascagni is."
    menu:
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1
        "Other than the food, what do you think of this place?":
            jump BBW002_c2_2

label BBW002_c2_1:
    MC "So, how about that news about why we're here? How are you taking that?"
    show BBW neutral
    BBW "I have never encountered a problem I could not deal with. Whatever sort of... mutation I am about to experience, I will handle it with grace and composure. You will not see me sobbing or wailing my misfortune."
    MC "Hmm-mmm. You have any idea what it might be? Or if they even know?"
    BBW "I haven't the slightest."
    show BBW neutral:
        zoom 2.0
    MC "Yeah, it's a puzzle. Anyway..."
    show BBW neutral:
        zoom 1.0
    jump BBW002_c2_2

label BBW002_c2_2:
    MC "Other than the food, what do you think of this place?"
    show BBW neutral
    BBW "I haven't formed an opinion yet, but my expectations are dropping rapidly. First the unwelcome surprise of this school's true purpose, then the matter of the food. And, of course, being denied the privilege of my servants."
    show BBW angry
    BBW "The term has begun with me being hobbled, almost as if they want me to flounder."
    menu:
        "Do you really need someone to carry your books? Is even that beneath you?":
            jump BBW002_c3_1
        "I'm sure you can get by without a butler or whatever.":
            jump BBW002_c3_2

label BBW002_c3_1:
    MC "Do you really need someone to carry your books? Is even that beneath you?"
    show BBW haughty
    $setAffection("BBW", -1)
    BBW "Your jealousy is so transparent. Go ahead and mock my situation, as children always make light of what they don't understand. If you had even the basic conception of culture and breeding you would understand how this all degrades me."
    hide BBW
    MCT "I was just teasing..."
    jump daymenu

label BBW002_c3_2:
    MC "I'm sure you can get by without a butler or whatever. I get that you're used to having... help. I'm going to guess that you've gone to private academies, right? Elite places that take care of fewer students."
    show BBW haughty
    BBW "I have attended only the best schools in America and Japan. Yes, this place is... different from them. There are a lot more people, for one."
    MC "But you're not the only one adjusting. I mean, we've all been thrown into it without warning, and none of us know what the future holds."
    MC "Maybe you should reach out to some of the other students. Someone in our class might help you deal with this upheaval. Listen to your problems, help you navigate the school culture. You don't have to deal with this on your own."
    show BBW neutral
    BBW "You do have a point. The uncertainty we are all experiencing is a common ground I can exploit."
    MCT "Exploit?"
    BBW "Thank you, Hotsure-san. You've given me something to think about."
    hide BBW
    MC "Well that ended abruptly. Maybe if I'd been more direct... Wait, did she actually remember my name?"
    jump daymenu
    
label BBW003:
    scene Hallway with fade
    MC "I think the library is this way? Maybe? Wait, that bulletin board doesn't look familiar... Ah! I was supposed to turn left back there."
    UNKNOWN "Amazing!"
    MC "Oh? I know that voice."
    scene Cooking Classroom with fade
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "Simply superb. Where did you study?"
    PRG "I didn't. I just sort of... taught myself."
    BBW "Don't be so modest. These are fantastic."
    show PRG happy
    PRG "Oh! K-Keisuke!"
    show BBW neutral
    BBW "Hmm? Hotsure-san, what brings you here?"
    MC "I was walking by and overheard you two. What's supposed to be so awesome?"
    show BBW happy
    show PRG neutral
    BBW "This souffle Kodoma-san has prepared. I've seen enough of Japan's attempts to mimic French cuisine to know to lower my expectations, but this is surprising."
    menu:
        "Oh, is it really that good?":
            jump BBW003_c1_1
        "Can I try one?":
            jump BBW003_c1_2
        "Aida, I didn't know you were a cook.":
            MC "Aida, I didn't know you were a cook."
            jump BBW003_c1_3

label BBW003_c1_1:
    MC "Oh, is it really that good?"
    show BBW neutral
    BBW "It's all relative. I wouldn't tell her to open up a bakery, but for a high school student working with the ingredients and facilities on hand, these are almost revelatory. I can see my judgment was sound as ever to invite her into service."
    MC "Invite who?"
    BBW "Kodoma-san, of course. It almost seems destined that my roommate would turn out to be perfectly suited to act as my right-hand woman during my time at this school."
    MC "I think I missed something."
    BBW "What do you mean? It was your own idea that I should seek help among our classmates. And Kodoma-san is all too eager to fill the role of my servants while I'm left to fend for myself here."
    MC "I wasn't really suggesting you find a maid..."
    show BBW happy
    BBW "Nonsense, Kodoma-san is more than qualified to act as my chef, secretary, personal trainer, accountant, media relations manager, bodyguard, chauffeur and interpreter. And she's eager to start right away. Aren't you, Kodoma-san?"
    PRG "Y-yes, ma'am."
    menu:
        "Is she? I guess that's fortunate for you.":
            jump BBW003_c2_1
        "So are you paying her, or... ?":
            jump BBW003_c2_2
        "Aida, do you really just want to be her maid?":
            jump BBW003_c2_3

label BBW003_c2_1:
    MC "Is she? I guess that's fortunate for you."
    show BBW haughty
    BBW "It is. I would have survived had I been left to my own devices, but people like me – those of us who are always looking at the big picture and have so many things to worry about – we benefit from having dedicated subordinates. Having someone to cook for me frees up time and energy I can devote to other things."
    MC "Like what?"
    BBW "Anything. My studies, my hobbies, being the glamorous trendsetter that I am."
    MC "I guess if she's OK helping you, there's nothing wrong with that."
    BBW "Why wouldn't she be okay? I'm giving her focus and direction, at a time when she needs it most. All of us have been blindsided by the news of this school, and I think the best way to deal with it is to carry on as always. It's what I'm doing."
    MC "I can't say you're letting all this get to you. Maybe you have something there."
    show BBW neutral
    BBW "Of course, I could use more help. It's a full-time job being me, and I'm always looking for people I can count on to help me. Would you be interested in a job?"
    MC "I'll... get back to you on that. I need to be somewhere else right now."
    BBW "Very well, but don't complain if I find someone else to fill the position."
    MCT "It'd be nice to make some new friends here, but I'm not looking to be anyone's butler..."
    jump daymenu

label BBW003_c2_2:
    MC "So are you paying her, or... ?"
    show BBW haughty
    BBW "It's not polite to talk about money so plainly. But to answer your question, I have offered Kodoma-san compensation for her services. And let us leave it at that."
    MC "Didn't mean to offend."
    show BBW neutral
    BBW "I'm sure you didn't, but do be careful in the future. Now, Kodoma-san and I have more to discuss, so is there something you need or...?"
    MC "Don't mind me. I have somewhere else to be right now."
    jump daymenu

label BBW003_c2_3:
    show BBW neutral
    MC "Aida, do you really just want to be her maid?"
    PRG "O-Oh no, it's not like that. Alice- M-Madame Nikumaru is very nice, and I enjoy helping others. I'm just happy to have found a f-friend!"
    MC "Okay... I guess that's one way of looking at it."
    BBW "Kodoma-san is happy with her position, as you can see."
    MC "Yeah. Sure. Happy. Well, I need to get going..."
    jump daymenu

label BBW003_c1_2:
    MC "Can I try one?"
    BBW "I suppose. There are more than enough here. Take one, and tell me my assessment was wrong."
    menu:
        "Hey, you're right. These are pretty good.":
            jump BBW003_c3
        "Aida, these are pretty good.":
            MC "Aida, these are pretty good."
            jump BBW003_c1_3

label BBW003_c3:
    MC "Hey, you're right. These are pretty good."
    show BBW haughty
    $setAffection("BBW", 1)
    BBW "Did you think I was being hyperbolic? I don't hand out praise unless it's earned, and even then I'm careful with my words."
    BBW "I have found in Kodoma-san a rare talent, waiting to be nurtured and cultivated. And who better to guide her than someone with a palette as refined as mine? No one else at this school can help her like I can."
    MC "That's pretty generous of you."
    BBW "I know, but it's the least I can do. It's one of the burdens of the wealthy seldom talked about: the need to foster talent wherever it is found. With my help Kodoma-san will become an excellent chef, someone capable of pleasing even my tastes."
    MCT "And now I'm wondering just how altruistic you are. Still, Aida seems happy with herself, so who am I to butt in?"
    jump daymenu


label BBW003_c1_3:
    $setAffection("PRG", 1)
    PRG "Ohnoit'snothingspecial. I-I-I just like to make treats and share them with people."
    MCT "Cripes, is she that unfamiliar with compliments?"
    BBW "Kodoma-san had mentioned that she was thinking of making treats for our classmates, though I think directing her energy to one person, such as myself, is better than any scattershot approach."
    MCT "Better for who?"
    BBW "I'm afraid we can't stop and chat. Kodoma-san has more training to do if I'm to bring her on as my assistant."
    MC "Your assistant?"
    BBW "Naturally I'll need to find someone to help me now that my personal retinue has been barred from the school. And Kodoma-san practically begged me for the position."
    MCT "Why do I believe things played out a little differently outside your head?"
    jump daymenu
    
label BBW004:
    scene Classroom with fade
    MCT "After class clean-up. That's normal. Mind-numbingly boring, but right now I'll take dull over surprising."
    MCT "..."
    MCT "?"
    MC "Um, are you planning to help out?"
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "I have Aida taking care of my share of the work."
    MC "Aida? Where is she- Why are you down there?"
    show PRG neutral at Position (xpos=0.75, xanchor=0.5, ypos=0.9, yanchor=0.5) with dissolve
    PRG "Oh! H-hello Hotsure-san. I'm just doing what Nikumaru-san said."
    MC "Did she say to scrub the floor? I'm pretty sure we just need to sweep it."
    PRG "I- I know. I just wanted to do a good job."
    MC "But it's not your job. Alice's name was on the roster."
    show BBW haughty
    BBW "And I got Aida to do it for me. It's called delegating. As long as the work gets done, nothing else matters."
    menu:
        "I... guess I can't argue with that.":
            jump BBW004_c1
        "It's not just about getting the work done.":
            jump BBW004_c2
        "Do I have to tell on you? Because that seems like a really childish thing for all of us.":
            jump BBW004_c3

label BBW004_c1:
    MC "I... guess I can't argue with that."
    show BBW neutral
    BBW "Of course not. Aida isn't complaining, so there should be no issue here."
    MC "I'm not saying I agree. I just can't think of a counterargument."
    jump daymenu

label BBW004_c2:
    MC "It's not just about getting the work done. It's about being part of a team."
    show BBW neutral
    BBW "I am part of the team. I'm supplying leadership and direction to Aida. If she's not complaining, is it really any of your business?"
    MC "...You might not want to make a habit of this. That's all I'm saying."
    jump daymenu

label BBW004_c3:
    MC "Do I have to tell on you? Because that seems like a really childish thing for all of us."
    show BBW angry
    $setAffection("BBW", -2)
    BBW "You're threatening to report me? At what point did any of this become your concern, anyway?"
    MC "When I saw someone not doing their share. This is a collective assignment, we all have to carry our weight. You don't get to sit back and take it easy just because you managed to rope someone else in."
    BBW "Are you a figure of authority in this class? No? Then you do not get to tell me that I do not get to do something."
    show BBW haughty
    BBW "As for alerting someone with actual power, go ahead. Play the sniffling toddler, tattle on me. My conscience is clear."
    MC "Guess that's what I'll be doing..."
    jump daymenu

label BBW005:
#INT: Cafeteria
#Keisuke (internal): Things seem a little livelier today. Not as much moping. And at least one person is very happy.
#BBW_Happy: Tres bien! Aida, dear, this is divine.
#Keisuke: Enjoying Kodoma-san's food again, I see.
#BBW_Happy: If you could taste this for yourself you would understand this is less about enjoying and more about experiencing.
#Keisuke: Are you offering to share some with me?
#BBW_Neutral: I... No. We are not on such familiar terms.
#Keisuke: Guess I can't argue with that, though it does look like she went all out. An omelet, fried potatoes, bacon, sausage... and doughnuts? Isn't that a bit heavy for a breakfast? Especially considering how much there is?
#BBW_Neutral: Are you implying something?
#Keisuke: No. I'm just saying that if I ate all that I'd be feeling sleepy by second period.
#BBW_Haughty: Breakfast is the most important meal. All your energy and drive for the day comes from it, so it's better to pack in as many nutrients as possible.
#Keisuke: That's one way of looking at it, I guess.
#BBW_Haughty: Plus, the more dishes I sample the better I can guide Kodoma-san in her job. For instance, this omelet could do with a bit less onions, and maybe more ham.
#PRG_Neutral: Y-Yes, Nikumara-sama.
#Keisuke (internal): That's some nice rationalization there.
#END SCENE

    scene Cafeteria with fade
    MC "Hair? What kind of mutation is hair growth? This almost seems like a joke. ... Hmm, no open tables. Oh! There's a spot."
    show BBW sad at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG sad at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "..."
    PRG "I-Is something wrong, Nikumaru-sama? Did I use too much coriander, or..."
    show BBW neutral
    BBW "No. The dish is exemplary. It's just..."
    MC "Stewing over the test results? Is it something bad?"
    show BBW haughty
    show PRG neutral
    BBW "A Nikumaru does not 'stew.' We take action, we confront problems. Destiny does not come to us, we make things happen."
    MC "So what was it? Or is it too personal to tell?"
    show BBW angry
    BBW "(You might have thought of that before you asked.) To answer your question, yes, I am thinking about the test results. I am questioning what can be done to curtail my... expansion."
    MC "If anything can be done."
    show BBW haughty
    BBW "There is always a way, even if it might be extreme. But the lengths you are willing to go to achieve something demonstrate how much you deserve it. Right, Kodoma-san?"
    show PRG neutral
    PRG "Ah! Y-yes, Nikumaru-sama!"
    MC "So what is your 'factor?'"
    show BBW neutral
    BBW "They say, and you might have trouble believing this just as I did, that I am inclined to grow... stout."
    MC "Stout?"
    BBW "..."
    extend " Obese."
    extend " Fat."
    MC "Oh. Yeah, that's, um, hard to swallow. But maybe it won't be too bad. They can't tell how 'stout' you'll end up being, right?"
    show BBW angry
    BBW "No, they can not predict that. But any excessive weight is unbecoming, which brings me to my quandary. Do I restrict my diet even further than the modest regiment I already have, or do I allow the growth to happen and fix things later?"
    MC "You think you can lose the weight after you're done growing? Isn't this supposed to be permanent?"
    show BBW neutral
    BBW "Failure only comes when you give up. Liposuction and similar weight loss treatments have helped others, so why not me?"
    BBW "But I am interested in your thoughts. Which sounds like a better approach, tackling the growth now or dealing with it at a later date?"
    menu:
        "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier.":
            jump BBW005_c1
        "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get.":
            jump BBW005_c2
        "What if you worked out? Burn those calories before they turn into fat.":
            jump BBW005_c3


label BBW005_c1:
    $setFlag("BBW005_ondiet")
    MC "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier."
    BBW "That does seem the best tactic. If I don't give my body the means to get fat..."
    MC "Just don't starve yourself or anything."
    BBW "Of course not. I know exactly what my body needs. Kodoma-san!"
    PRG "Yes, Nikumarua-sama!"
    BBW "Going forward I want my meals to have a maximum of 650 calories. Adjust my menu accordingly, but be sure to include an appetizer, entree, side dish and dessert."
    MC "So now she's your dietician?"
    BBW "All part of her job description. Did you get all that?"
    PRG "Yes, Nikumaru-sama."
    MCT "Seems a bit much to ask of anyone, even if they're as eager to please as Aida is. But what do I know about cooking?"
    jump daymenu

label BBW005_c2:
    MC "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get."
    BBW "I agree, this is the idea most likely to succeed. I don't know enough right now, so how am I supposed to proceed? What if my growth is miniscule? Would I end up starving myself for nothing? Or what if it is extreme, and denying myself a proper diet is for naught?"
    PRG "N-Nikumaru-sama? The quail is ready."
    show BBW happy
    BBW "Then bring it out! And excellent choice to include the spicy mustard greens in this salad. It was exactly what it needed."
    show PRG happy
    PRG "T-thank you!" 
    MCT "Whether this will work or not, it is the path of least resistance. Maybe that's why she's eager to go along with it."
    jump daymenu

label BBW005_c3:
    $setFlag("BBW005_workout")
    MC "What if you worked out? Burn those calories before they turn into fat."
    BBW "Now that is sensible. I admit, the thought of denying myself proper meals is distressing, more so after discovering Kodoma-san's talents."
    show BBW haughty
    BBW "I mean, who else at this school is prepared to give her ability the recognition it deserves? And if I can support her while taking care of myself at the same time, so much the better."
    MC "Have your cake and eat it too, you mean?"
    show BBW neutral
    BBW "Quite. You do have a good mind, Hotsure-san, but perhaps humor is outside your reach."
    MCT "I wasn't trying to make a joke."
    jump daymenu

label BBW005A:
    scene Cafeteria with fade
    MCT "Why do I always have trouble finding an open seat? I wonder how much harder this will be once some of the people start growing..."
    MC "Mind if I sit here?"
    show BBW sad at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    PRG "Oh! G-Good morning, Hotsure-san."
    BBW "... By all means."
    MC "Thanks. Say, did you two get the Lit reading done? I kind of spaced out last night."
    PRG "I did it. How far along did you get?"
    MC "About... two pages in."
    BBW "Kodoma-san."
    PRG "Yes, Nikumaru-san?"
    BBW "Can you get the other half of the grapefruit? The first half was not adequate alone."
    PRG "Certainly, ma'am. And would you like some more toast?"
    BBW "... Two slices."
    PRG "With jam or butter?"
    BBW "No. Plain."
    PRG "All right. I'll be right back."
    hide PRG with dissolve
    MCT "Someone's in a bad mood. I wonder if I should say something or not."
    MC "Light breakfast today?"
    MCT "Mouth, you're not helping."
    BBW "Light breakfast today, and every day. Light lunch every day. Light dinner every day."
    MC "Oh? ... Oh! Yeah. Your factor. I guess you're doing the diet thing, huh?"
    BBW "If I am to maintain authority over my own body and not be controlled by the whims of fate, then yes, I am doing 'the diet thing.' Every day, at every meal, I will be watching my intake, limiting the calories, sugars, and fats I take in. I will limit it all to what I need and no more."
    MC "You don't seem too happy about it."
    show BBW angry
    BBW "Is there something here I should be happy about? I have a palate more refined than people twice my age. My appreciation of the arts – culinary or otherwise – exceeds that of professional critics. And now I must cut out my tongue, surviving on simple fruits and steamed vegetables and whatever other staples a Neanderthal wandering the plains of famine would call a meal."
    MCT "That's a bit melodramatic. Better think of some positive way to look at this."
    MC "At least it will help in the long run! That'll be good, right?"
    show BBW neutral
    BBW "I am already beginning to question that. I can endure an existence marked by suffering and lacking. I am strong enough to bear up in the face of abject want, unlike many others."
    show BBW angry
    BBW "But is that a life worth living? Is the path of self-denial, of self-inflicted misery, beneficial to anyone? How can one grow as a person if they have committed their life to depriving themselves of opportunity and experience? Every bowl of plain rice, every plate of salad, is another act of self-flagellation. Shall my days be marked by anguish, my life's story a tale of torment? Who would live such a life by choice? Who would be inspired by that?"
    MC "But... you just started the diet. This is your first meal."
    BBW "Is my suffering any less brutal for being so brief? Shall I remain silent until I have carried my burden for a certain number of days? No! Pain is pain. It is not to be dismissed for failing to meet some arbitrary metric. You were the one to suggest this trial of deprivation, and now you mock me for not embracing my torture?"
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    PRG "Miss Nikumaru? I brought you your food."
    show BBW neutral
    BBW "Thank you, Aida, but now I want you to go prepare me a real breakfast. Crepes Florentine and smoked salmon to start, along with some coffee and fresh-squeezed orange juice."
    PRG "Y-Yes, ma'am. ... I'll just leave the toast and grapefruit."
    show BBW angry
    BBW "Or does this not meet your approval, Hotsure-san?"
    MC "Whoa! I'm not judging you. I'm just..."
    BBW "You're just... what?"
    MC "I'm just saying a diet might not be easy, but in the end you might be glad you did it."
    BBW "Is my mood a concern of yours? Is it your business to tell me how I deal with my factor? I assume you have your own condition to deal with, no?"
    MC "Yeah. My hair grows really fast."
    BBW "... That is your condition? That is why you're here?"
    MC "Yep. That's it."
    show BBW neutral
    $setAffection("BBW", -2)    
    BBW "I would suggest you withhold any attempts to guide others through their own crises until you have experience with actual problems yourself. Some people seem to just float through life without a care in the world, never understanding how hard and unyielding life can be."
    MC "Uh huh... Consider me properly scolded."
    MCT "I was just trying to help."
    jump daymenu
    
label BBW005B:
    scene Classroom with fade
    "The last bell of the day rang and everyone got ready to get up and go. I had nothing in particular I wanted to do this afternoon, but like most everyone else I wanted to get out as quickly as I could."
    "I made it halfway to the door before I was stopped by a hand on my shoulder. Turning around, I saw Alice standing there with Aida hovering behind."
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "It's time we begin our journey."
    MC "Journey?"
    BBW "Our journey towards health and well-being for myself. In order to stave off the effects of my growth factor I will be taking up an exercise routine. An intense calorie-burning regimen to keep myself fit and sleek."
    MC "Where do I come in?"
    BBW "It was your idea, after all. And I can't tackle such a daunting task myself. I remember reading that new habits undertaken with others have a better success rate, and let's be frank, some exercise wouldn't do you much harm."
    MC "I'd be insulted, but... Yeah. What about Kodoma-san, though? I thought you said she would be your personal fitness trainer."
    BBW "And she is, but she can't be both working out and coaching me. Plus, she wouldn't do as a spotter. Too frail."
    MC "I think she should be insulted, but..."
    show PRG sad
    PRG "..."
    MC "Yeah. Well, I have nothing better to do right now, so why not? Let's hit the gym."
    show BBW happy
    BBW "That's the spirit. Go change, and we'll meet you at the weight room."
    
    scene Gym with fade #weight room?
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "OK! Where do we start?"
    MC "Um..."
    BBW "I was asking Kodoma-san. She's the official expert here."
    PRG "Uh... Maybe if we did some stretches?"
    show BBW happy
    BBW "Excellent. We'll ease into the workout."
    "We went to a set of mats set up in a corner, away from the weights and machines, and Kodoma-san led us in some light stretches and calisthenics that took me back to grade school. I can't say it did anything to burn calories, but it did loosen me up."
    "Eventually she stopped (or she ran out of exercises)."
    PRG "Now how about we... do push-ups?"
    show BBW neutral
    BBW "You're the boss. Come on, Keisuke."
    hide BBW with dissolve
    "Alice and I got down on the mat and started doing push-ups. That is, we tried. I knocked out a couple before I was struggling to keep my form, but Alice was having trouble doing just one."
    BBW "Nnnnnhg... Gggggrrrr... One!"
    BBW "Aaaaannnn... Two!"
    show PRG happy
    PRG "Come on, Nikumaru-san! Push it! Unleash the beast! Own your power!"
    "Kodoma-san tried encouraging Alice with some slogans I'm sure she got off fitness clothing commercials, and ever so slowly she managed to do a full set."
    BBW "Ggggggggnnnnnnnn... Ten!"
    PRG "You did it, ma'am! Well done!"
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "Thank you, thank you. If you'll excuse me, I need to take a quick water break. Hydration is important, after all."
    hide BBW with dissolve
    show PRG neutral
    PRG "OK. We'll wait for you."
    "I wasn't going to say anything; after all, it's not like I'm effortlessly knocking out the push-ups one-handed or anything. And Alice was sweating by the end, so she was putting in some effort."
    "She came back five minutes later, no longer sweating and looking like she had straightened up her hair in the bathroom."
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "What shall we do next?"
    "Kodoma-san looked around, a little bit lost among the machines she clearly had no experience with."
    PRG "Maybe we can start here? And then work our way around?"
    "She was looking at a pulldown bar, the kind where you stay standing and pull the bar in front of your chest."
    BBW "Very well. Keisuke, you go first."
    MC "Why me- No, never mind. I'll go."
    "As I was looking at the weights in increments of ten pounds, trying to guess what my limit was, another person came over and joined us."
    show PRG neutral at Position (xpos=0.9, xanchor=0.5) with dissolve
    show FMG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    FMG "Hey sorry to bother but how much longer are you...Oh hey guys. What brings you here?"
    MC "Hi, Akira. We're just working out, trying to help Alice lose weight."
    show BBW angry
    BBW "I don't need to lose weight. I just need to keep myself from getting fat. There is a world of difference there."
    MC "Right. Anyway, we'll try not to take too long."
    FMG "Nah it's cool, I could use the breather anyways."
    show BBW neutral
    "She stayed standing a bit to the side, watching as I decided how to adjust the weight and making me self-conscious. If it was just me and Alice I could get away with something easy, but with Akira looking over my shoulder I was afraid she would say something if I wasn't going all out."
    "In the end I decided to add 50%% more what I was originally going to lift. To my surprise it weighed more than what I expected. Before I could lift it up, Akira came and grabbed the bar."
    FMG "Sorry but I have a quick question, just how much did you put on the bar?"
    MC "About 150 pounds. Why?"
    show FMG sad
    FMG "Because it looked like it was too much for you. You gotta know your limits and take it one step at a time."
    BBW "You look like you know what you're talking about. Maybe you have some tips you can share."
    show FMG neutral
    FMG "Sure. First off, did you take a protein shake before exercising?"
    BBW "Uh, no? Is that necessary?"
    FMG "Not really but it helps. Here, I have an extra."
    MC "I don't think we need it. We're not trying to build up muscle, are we?"
    FMG "Fair enough I guess."
    "Akira puts the shake away before whispering to me."
    show FMG happy
    FMG "{i}Between you and me, I just wanted to see Alice's reaction to drinking this sludge.{/i}"
    FMG "All right, tips. The first thing you want to do is, like I said, know your limits and pace yourself. Take short breaks when you need it. Keep consistent and follow a routine. And the most importantly, be patient, don't expect results overnight. As long as you keep it up and actively enjoy it, you won't have any problems."
    show BBW happy
    BBW "Sounds good. Let's get to it."
    show BBW neutral
    BBW "..."
    MC "..."
    BBW "You were about to begin."
    MC "Right."
    "I reset the weight to what I thought was a manageable amount. Akira was still standing by, watching, but I put her out of my mind as I did ten reps with what felt like too little weight in her eyes."
    "When I was done I stepped aside for Alice."
    BBW "My turn."
    "She left the weight where it was, but turned out to be too much for her."
    show BBW angry
    BBW "Nnnnggg! Grrrrr!"
    "She reduced the weight and tried again, then reduced it a third time."
    BBW "Gggnnnn!"
    "She probably would have reduced it again if she wasn't already at the bare minimum. I looked over at Akira as Alice struggled to get to ten reps."
    show FMG sad
    FMG "...Um, you ok Alice? Need anything?"
    BBW "Ggnnnooo, thank you. Just doing what you said and taking it slow."
    FMG "...I didn't mean to the point where you're not even pulling the damn bar. For god's sake, you have it at the lowest level!"
    BBW "Did you not just tell us to know our limits? Are you now reversing yourself and telling me to risk injury by going beyond my limitations? What is it you want me to do?"
    show FMG angry
    FMG "No I...ugh screw it, I'm getting ice cream before I really get mad!"
    hide FMG with dissolve
    "And she stormed off. For a second I thought about going after her, trying to cool things off so at least she wouldn't leave mad, but then I decided it'd be better this way."
    "Plus, turning back to Alice, I saw that if I did want to play mediator I had another opportunity."
    show BBW neutral
    BBW "Well that was uncalled for. It was certainly arrogant of her."
    MC "Arrogant?"
    BBW "Not everyone is gifted with physical prowess, and for her to carry on as if anyone should be able to do what she can... That's arrogant."
    MC "I'm not sure that was her problem, but I agree she could have been a bit more patient... How about I talk to her later, once she's cooled off? She probably could help you with this better than I or Aida could."
    show BBW happy
    $setAffection("BBW", 1)
    BBW "That's thoughtful, but you don't need to put yourself out. This was a worthwhile experiment, but I've reached the conclusion that I'm not cut out to be a gym rat. I don't think this stress of trying to constantly outdo myself would be good for my temperament, if Mizutani-san is any indication. Still, thank you for your assistance."
    MC "You're welcome. (I guess.)"
    BBW "Now, Aida, let's go back to the dorms. I feel a hot bath and massage is the best way to unwind after a workout like this."
    PRG "Y-Yes, ma'am! I'll get the oils."
    jump daymenu

label BBW006:
    scene Hallway with fade
    MCT "Classes are done, so what now? Don't want to go back to my room, I've got enough weirdness going on without someone trying to find more lurking around every corner. Maybe I can see if any of the clubs are recruiting yet."
    "..."
    MCT "Sounds like the music club is rehearsing. Not my thing... Oh!"
    show BBW neutral with dissolve
    MC "Niku- Alice. Thinking of joining the music club?"
    show BBW haughty
    BBW "Offering my services to the ensemble is one reason I'm here, though I'm disheartened to find out freshmen are not considered for seated positions. Waiting a year just to take my rightful place on the stage..."
    BBW "I'm more sorry for the club, having to endure without my contribution."
    MC "How thoughtful. So what instrument do you play?"
    BBW "I have my own natural instrument: my voice."
    MC "You're a singer?"
    BBW "A soprano. And a gifted one, I should say. I've been coached since I was five."
    MC "I didn't know the music club did operas."
    show BBW neutral
    BBW "According to the club adviser, they do not. Put more accurately, they never have."
    show BBW haughty
    BBW "But the higher arts are not more difficult by nature. With sufficient commitment and practice I'm sure they could put on a fair performance. And with me as the star..."
    show BBW neutral
    BBW "I'd also hoped to find a talent or two I could nurture during my time here."
    MC "Nurture?"
    BBW "The Nikumarus have a long history of patronage of the arts, one I hope to continue. I would like to get a start on it by finding a budding talent to encourage. Pushing them to refine their art and attain what greatness they were born for."
    BBW "Privilege, after all, comes with the responsibility of helping others."
    MCT "You sound both selfless and selfish as you say that."
    BBW "On that note, do you play any instruments, Hotsure-san?"
    MC "Me? Uh..."
    menu:
        "No, I don't.":
            jump BBW006_c1
        "I've practiced a little, but I'm not really talented.":        #maybe these should be skill checks?
            jump BBW006_c2
        "I don't mean to brag, but I'm a pretty skilled musician.":     #maybe these should be skill checks?
            jump BBW006_c3


label BBW006_c1:
    MC "No, I don't."
    BBW "Hmm. An honest answer, but a shame."
    MC "Does anybody here catch your eye? Or ear, I should say?"
    BBW "It's too soon to say. None of them are masters, so finding the seed of potential requires a deeper look. I'll need to sit in on a few more meetings."
    MC "I take it you'll be the joining the club, even as a benchwarmer?"
    BBW "...I am unfamiliar with that term. But yes. With my gift it would only be appropriate that I join. And I cannot convince the club president of their folly in keeping me in reserve if I am not here."
    MC "You don't take 'No' for an answer, do you?"
    show BBW haughty
    BBW "I'm a Nikumaru. A 'No' to me is just another obstacle to overcome."
    jump daymenu

label BBW006_c2:
    MC "I've practiced a little, but I'm not really talented."
    BBW "Oh? What instrument?"
    MCT "Immediate regret setting in. What's an impressive instrument?"
    MC "Uh... Violin. I've had a few lessons, but I'm no, you know, virtuoso."
    BBW "None of the students here are, if the music club is any indicator. But talent can blossom anywhere when given a guiding hand. Show me what you can do."
    MC "Here? Now? Are you sure it's OK to use the club's instruments?"
    BBW "Of course. The instruments belong to the school, and we're students."
    MC "All right."
    "I squeaked out a few sharp chords that sounded like someone stroking a balloon. Alice's thoughts were too easy to read as she grimaced in pain."
    show BBW angry
    BBW "Enough!"
    MC "Sorry. It's been a while since I've practiced."
    show BBW neutral
    $setAffection("BBW", -1)
    BBW "Maybe I shouldn't have expected much. You... You might have some skill. Some day."
    "She wasn't disappointed, but as she turned away I could tell she was let down."
    jump daymenu

label BBW006_c3:
    MC "I don't mean to brag, but I'm a pretty skilled musician."
    MCT "Oh dear god, why did I say that? I can't even play the triangle."
    BBW "Really? Which instruments do you favor?"
    MCT "Instruments? Plural? Oh, jeez..."
    MC "I mostly play... violin. But I also toy with the oboe."
    MCT "Sure, let's keep lying."
    BBW "The violin? It wouldn't take much to outshine the other students here, but how experienced are you? Have you had many public performances?"
    MCT "Fix this, you dolt. Now!"
    MC "I've never performed in front of an audience. I don't have the nerves for it. Just a lot of practice in private."
    BBW "All that practice must have been worth something. Show me what you can do."
    "And before I could say anything she was thrusting one of the club's violins into my hands. This was too fast for me to deal with, I couldn't think of anything to say to get out of it. So, nervously, I put the violin under my chin like I had seen people do in movies and I tried stroking the bow back and forth."
    "The disgust on Alice's face was immediate, and I couldn't blame her. If the violin was a living being I would have been arrested for animal cruelty. But I still thought I could fake it if I could, I don't know, figure out how to stroke the chords right."
    show BBW angry
    BBW "Stop! Stop!"
    MC "Sorry. It's been a while since I-"
    $setAffection("BBW", -3)
    BBW "Learned how to tune it properly? I don't know what kind of goofing off you think constitutes 'practice,' but you should keep this musical torture private."
    hide BBW with dissolve
    "And she stormed off. Which, considering her mood, may have been preferred."
    jump daymenu

label BBW007:
    scene Cafeteria with fade
    MCT "First time I haven't had trouble finding a spot. I guess other people are spending lunch up on the roof or in their classrooms, like at a normal school. Looking around, it does seem like a lot of people are drifting into cliques or avoiding certain people."
    MCT "And I'm off by myself, which is par for the course."
    "No sooner had I thought that than someone sat down across from me."
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    MC "Oh, Alice. Didn't know you'd be having lunch here."
    BBW "Why wouldn't I? It is a pleasant day outside, but it seems improper to eat in some random place. Or maybe it is simply proper to eat where the food is served. Structure is an oft-overlooked virtue, in life and in business."
    MC "If you say so."
    "It took me a second to realize Alice wasn't alone. Right behind her was Aida, holding a few packages."
    show PRG sad at Position (xpos=0.75, xanchor=0.5) with dissolve
    MC "Hi, Aida. How did you get so much mail already? It's still the first week of the year."
    PRG "Oh, it's not mine. I was carrying it for Nikumaru-sama. We just came from the mail room."
    extend " ... There was nothing for me."
    MCT "She seems a bit sad. Is there something about mail that bothers her? Better change the conversation."
    BBW "Interested in what I got?"
    MC "Uh..."
    BBW "A lot of it is the usual care package stuff. Hand lotion, chewable candies, perfume, a new phone -"
    MCT "That left 'usual' territory pretty quickly."
    BBW "But I also ordered myself some things. White knee-high stockings seem to be 'in' among the other students, and I was not aware how cold winters in this part of the country can get, so I needed a new coat."
    BBW "And Aida confided in me that she only has one pair of shoes and barely any clothing besides her school uniforms. So I ordered some stuff for her."
    MC "That was considerate."
    BBW "Well, she doesn't have a credit card or bank account of her own, so ordering things online are beyond her means. But it was the least I could do to facilitate her shopping."
    MC "Facilitate... You mean she still paid for the stuff herself?"
    BBW "But of course. I'm not running a charity. And I would like to point out that with my connections I was able to buy directly from the manufacturer, saving her money."
    MC "What do you mean by connections?"
    show BBW haughty
    BBW "I know the sons and daughters of many business owners and CEOs. We always turn up at the same hotels in Monaco or ski lodges in Switzerland. You don't think the owner of a factory that makes dresses or suits has to buy off the rack, do you?"
    MC "I guess not. So if I needed to buy a new laptop could you get me one at a discount?"
    show BBW neutral
    BBW "I suppose I could. Hitomi and I – that's Hitomi Ogawa, daughter of the president of Ogawa Electronics – aren't on the closest of terms, but she could get me one for... 90,000 yen. Plus 10%% commission for myself would be 99,000."
    MC "An Ogawa laptop for under a hundred thousand yen? That's pretty steep for some old model being unloaded-"
    BBW "That's for an Ogawa D2300. 22” monitor, if I remember correctly."
    MC "... For 99,000?! Are you serious?"
    BBW "Completely."
    MCT "Unbelievable. That's a 170,000-yen machine, and she says she can get one for under 100K?"
    BBW "Don't be surprised. I'd be buying direct from the company, so there's no middle-man mark-up. Except for my commission, of course."
    MC "O-Of course."
    BBW "Or would you prefer the Essence 4K? I could probably get that for, let me see..."
    "And she checked her smartphone. Was she checking the manufacturing cost online, or did she know what the mark-up from retailers was?"
    BBW "How does 115,000 yen sound?"
    MC "I think I might faint."
    BBW "Shall I order one? You don't have to pay me now, you can take care of that when it gets here."
    MC "No, no. I don't need a new laptop. I mean, I could use one, but I don't have that kind of money."
    BBW "Well you should have said so."
    show PRG neutral
    extend " ... Idea. Aida, take a note: I am going to start a business here at school. Direct retail, goods offered at a discount."
    MC "There's already a store on campus, you know."
    BBW "I know, I've seen it. But it lacks many of the essentials of modern living, and the mark-up is scandalous. 300 yen for a soda? I can beat those prices and still make a worthwhile profit."
    PRG "What do you need me to do, Nikumaru-sama?"
    BBW "Our first step will be to get the word out. We'll need some sort of ad campaign, make the people aware of my service. Then we'll need a system of taking orders and fulfilling them. Dorm-room delivery would be an enticing service; convenient for the customer."
    BBW "But the guys' dorm... Keisuke! How would you like a job?"
    MC "Me? Doing what?"
    BBW "Haven't you been listening? I'll need runners, people to deliver packages as they come in. I can offer you 1,000 yen an hour."
    MC "I... will think about it."
    MCT "She's actually serious about this. I wouldn't have guessed she was this sort of vigorous go-getter. I guess business runs in her blood."
    jump daymenu
    
label BBW008:
    scene Hallway with fade
    "After another day of classes I found myself not in my dorm and not in my classroom. I wasn't heading anywhere special, I was just wandering around."
    "After some time I found myself at the music room."
    scene Music Classroom with fade
    MCT "Maybe I can listen in on them practicing."
    "But the club wasn't meeting right now. Instead there were two people, Aida and another student. It's not like I wanted to spy on them, but I was curious and they were talking loud enough to overhear them."
    Student "-alented or not, I have no patience for someone trying to undermine my authority."
    show PRG sad with dissolve
    PRG "Y-yes, ma'am. But I don't think she means to be-"
    Student "You seem to be the closest thing she has to a friend, so maybe she'll listen to you. Tell her she can either be happy in the chorus or she can look for another club to join."
    PRG "Y-yes, ma'am."
    "The other girl (is she the music club president?) turned away, the conversation over. Head bowed, Aida made for the door. I stepped back, but not fast enough to not get caught."
    show PRG surprised
    PRG "Oh! H-Hotsure-san."
    MC "Hey, Aida."
    MCT "Should I ask what that was about? Aida looks pretty bummed."
    MC "Is something wrong? It looked like you were being given the third degree."
    show PRG neutral
    PRG "N-no. I wasn't in trouble. It's Nikumaru-san. She doesn't like being in the chorus, but Mizawa-san won't make her lead vocalist."
    MC "Is that the club president? Is Alice butting heads with her or something?"
    PRG "Yes. They keep getting into arguments, and now Mizawa-san is threatening to kick Nikumaru-san out if she doesn't behave."
    MC "I haven't known her too long, but Alice doesn't seem like much of a team player. Guess I'm not surprised she's already getting into trouble like this."
    show PRG sad
    PRG "I-I'm supposed to t-tell her to mind herself, b-but I don't think Nikumaru will listen to me. She's kind of head strong."
    MCT "And you're kind of a pushover."
    MCT "Oh, that's mean. But it's not wrong."
    menu:
        "Well, good luck with that.":
            show PRG surprised
            $setAffection("PRG", -2)
            PRG "..."
            MCT "I could go for a soda now."
            jump daymenu
        "Maybe I could help.":
            jump BBW008_prechoice

label BBW008_prechoice:
    MC "Maybe I could help."
    MC "I wouldn't say Alice listens to me so much as she hears what I say. I can pass the word along for you."
    show PRG happy
    PRG "C-could you?"
    show PRG sad
    $setAffection("PRG", 1)
    PRG "I-I don't want to trouble you, but it would be so sad if she got kicked out of the club. She's a stranger here, you know. She doesn't fit in."
    MC "We're all strangers, but I get what you mean. She kind of fits that whole 'pushy American' stereotype, doesn't she?"
    show PRG angry
    PRG "Oh, no! Nikumaru-san is just very determined."
    MCT "Determined. Sure."
    MC "Do you know where Alice is now?"
    show PRG neutral
    PRG "She should be in the cafeteria. I made some snacks for her to sample while she works on setting up her business."
    MC "Might as well deliver the news now, then."

    scene Cafeteria with fade
    "We found Alice sitting at her usual table, one hand typing on a laptop and the other picking up tea room pastries from a tray next to her."
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "Hotsure-san, good afternoon. Thank you for bringing Aida back. I've been waiting for her for...five and a half minutes now."
    MC "Actually she brought me here. There's something I need... Something you should know."
    show BBW neutral
    BBW "Oh?"
    MC "Yeah, um... How's the music club? You're still doing that, right?"
    BBW "Despite my feelings on how it is being managed, yes, I am still a member."
    MC "Right, right. So I was told- That is, Aida was told..."
    show BBW angry
    BBW "..."
    "I stammered a few words, and Alice became irritated quickly."
    MC "We were told to tell you to, you know... Maybe ease up on the prima donna thing."
    BBW "Excuse me?"
    MC "It's not that you're... You can be a little... "
    MC "You're going to get kicked out if you don't stop fighting with the president."
    BBW "Oh, really? Aida, is this true?"
    show PRG sad
    PRG "Y-yes, Nikumaru-san."
    BBW "You go back and tell her..."
    MCT "She didn't understand anything I just said, did she?"
    show PRG neutral
    menu:
        "Say nothing. Let Alice do what she wants.":
            jump BBW008_c1
        "Suggest Alice not make things worse.":
            jump BBW008_c2
        "Tell Alice she's in the wrong.":
            jump BBW008_c3

label BBW008_c1:
    $setFlag("BBW008_extrascene")
    MCT "Well, if she wants to pick a fight, let her. Whatever happens is on her head."
    show BBW haughty
    BBW "Thank you for bringing this to my attention, Hotsure-san. My esteem for Mizawa-san was already low, but to use an intermediary like this is pathetic."
    MC "No problem."
    "I decided to excuse myself then. Didn't want to get caught up in this drama."
    jump daymenu

label BBW008_c2:
    MCT "Oh man, this is going to get out of hand quickly if I don't do something."
    MC "Maybe you shouldn't push back right away."
    show BBW neutral
    BBW "What do you mean? Should I let this stand-?"
    MC "Some people just don't get the message right away, do they? Clearly the club president - this Mizawa girl - hasn't recognized your talent yet."
    show BBW haughty
    BBW "No, she hasn't-"
    MC "So getting her face again won't do any good. This seems like one of those times where the person needs to realize their failure on their own."
    BBW "And what do I do in the meanwhile? Resign myself to the chorus until Mizawa-san decides to admit she was wrong?"
    MC "I don't think there's much you can do at the moment."
    BBW "Are you not familiar with the phrase 'The squeaky wheel gets the grease'? If I'm supposed to wait for that tone-deaf girl to realize my talent, I will be stuck in the chorus all year."
    MC "And have you ever heard the phrase 'The upturned nail gets hammered down'? If you keep fighting her you won't even be on the chorus."
    show BBW angry
    BBW "..."
    BBW "Hmm..."
    show BBW neutral
    $setAffection("BBW", 1)
    BBW "Is it just me, or are Japanese people excessively non-confrontational?"
    BBW "Very well. Aida, forget my last order. I'll toe the line, for now."
    BBW "But not forever, Hotsure-san. I don't intend to let my genius go ignored indefinitely."
    MC "Wait, why are you making it sound like it's my job to get you out of the chorus?"
    jump daymenu

label BBW008_c3:
    MC "Can't you just admit that you're in the wrong here?"
    show BBW angry
    BBW "I beg your pardon?"
    MC "You're not the leader of the music club, are you?"
    BBW "I'm the best singer-"
    MC "That's a no, then. Well, the actual leader has made a decision, and it doesn't matter if you like it or not."
    MC "Maybe you are the best singer, but there's more to an ensemble, a group of people, than any one person getting what they want."
    MC "You're going to have a hard time getting along here if you don't understand that. We're all dealing with some pretty major stuff right now, not just you."
    $setAffection("BBW", -1)
    BBW "How dare you..."
    "She didn't have to say anything, I knew what she was thinking. All the better, as I wasn't looking for a fight or anything."
    MC "Just something to think about."
    "And I turned and walked away. Maybe a bit quicker than I intended, but I didn't want to stay and get chewed out or anything."
    jump daymenu

label BBW008A:
    scene Cafeteria with fade
    show BBW angry
    BBW "That impudent egotist!"
    "I was sitting in the cafeteria, not so much enjoying my lunch as eating it without gagging-"
    BBW "How could such a woman be put in a position of authority? Bribery? Blackmail? Nepotism?"
    "-when Alice came up to my table and started complaining to me about someone."
    "There was no way to know how long she had already been ranting before reaching me..."
    BBW "A leader who thinks their job is to simply dictate to others does not understand leadership. A captain who does not know her destination might as well run the boat aground."
    MC "Problem with authority? Is this about the music club thing?"
    BBW "What does it say about a club leader who is more concerned with maintaining a cordial environment where mediocrity can rule than challenging everyone to deliver their best?"
    MC "That... this is more about having some fun than anything else?"
    show BBW neutral
    BBW "And how is it 'fun' to rehearse the same pieces of music without striving for improvement?"
    show BBW angry
    BBW "This Mizawa-san is only wasting everyone's time if she refuses to demand anything of her members."
    MC "It's only the start of the year. I'm sure there must be some period of adjustment for a musical group to come together."
    MC "Maybe if you tell her - politely - that you think she can ask a little more of everyone she'll agree. Maybe she already wants more of them, but she doesn't want to be overbearing."
    show BBW haughty
    BBW "I have already addressed my concerns with Mizawa-san. Just now, when she suspended me from the club."
    MC "What?! She kicked you out?"
    show BBW neutral
    BBW "Not permanently, but I am on forced sabbatical until I have 'adjusted to the upheaval in my life,' as she put it."
    show BBW haughty
    BBW "She thinks I am, what were her words, 'behaving out of turn' because I am in an unfamiliar environment, with the news of my condition hanging over me."
    show BBW angry
    BBW "Projection. That's what it is. Mizawa-san is uncomfortable being here, and so she is pretending I am the one with the problem."
    show BBW neutral
    BBW "Perhaps that is easier to believe than acknowledging I am in the right."
    MC "So... This isn't about the other students in the club? This is just about you still butting heads with her?"
    show BBW haughty
    BBW "This is only about the club, and how I know what is best for it."
    show BBW angry
    BBW "Mizawa-san may try to pull rank, but shoving me aside does not win her the argument. I am still of half a mind to press the issue."
    menu:
        "I don't see what good that would do. If she's as headstrong as you say, arguing will only make her dig her heels in.":
            jump BBW008A_c1 #(Neutral outcome)
        "If you feel this strongly, go for it. You're the one talking about squeaky wheels, right?":
            jump BBW008A_c2 #(Moderate loss of affection with Alice)
        "Arguing with Mizawa-san obviously isn't doing any good. Maybe try a different tack.":
            jump BBW008A_c3 #(-10 points of affection with Alice)

label BBW008A_c1:
    MC "I don't see what good that would do. If she's as headstrong as you say, arguing will only make her dig her heels in."
    show BBW angry
    BBW "Mmmf!"
    BBW "..."
    show BBW neutral
    BBW "She probably would, wouldn't she?"
    BBW "I suppose this is a situation that calls for patience rather than the firm hand of guidance."
    BBW "Very well. I shall endure my sabbatical with my natural grace, and when I return to the music club even Mizawa-san will not be able to deny what a difference my presence makes."
    hide BBW with dissolve
    "And she trotted off. I don't think she was any less angry, but at least things hadn't gotten worse."
    jump daymenu

label BBW008A_c2: 
    MC "If you feel this strongly, go for it. You're the one talking about squeaky wheels, right?"
    show BBW neutral
    BBW "You are not wrong. There may still be time to find Mizawa-san before lunch ends, and we can settle this matter before the club meeting this afternoon."
    hide BBW with dissolve
    "And she walked off."
    scene black with fade
    "Ten minutes later, she came back."
    scene Cafeteria with fade
    show BBW angry
    $setAffection("BBW", -2)
    BBW "There is no word for 'foolishness' in your language that is strong enough for that girl."
    MC "She didn't listen to you-"
    BBW "She says that I am a hair's breadth from being cut entirely, and she makes it sound as if she is being reasonable by giving me a 'second chance.'"
    BBW "That my talent, which I have clearly demonstrated by this point, could be dismissed so flippantly..."
    BBW "Argh!"
    BBW "I almost want to leave of my own accord. Being hobbled by this enabler of mediocrity may not be worth it."
    MC "I-"
    hide BBW with dissolve
    "But she was already storming away, as if she wanted to get away from the entire school."
    jump daymenu

label BBW008A_c3:
    $setFlag("BBW008A_fail")
    MC "Arguing with Mizawa-san obviously isn't doing any good. Maybe try a different tack."
    MC "Instead of taking up this fight yourself, why don't you get some others on your side?"
    MC "Talk to the other members of the music club, see if they'll back you up. Then you can all go up to the club prez and try to reason with her."
    show BBW happy
    BBW "That is not a bad idea, Hotsure-san. Strength in numbers."
    show BBW haughty
    BBW "Or if I can convince enough members to see it my way, I could simply try to oust Mizawa-san as president."
    MCT "OK, that is not what I'm suggesting."
    show BBW neutral
    BBW "There's still time before lunch ends. I need to speak with some of the other members."
    hide BBW
    "And she walked off, holding her chin up as if she had already won a victory."
    scene Hallway with fade
    "As I left the cafeteria and started to make my way back to class, I ran into Alice coming in the opposite direction."
    show BBW angry
    $setAffection("BBW", -10)
    BBW "Hotsure-san! How could you possibly suggest such a terrible idea?"
    MC "Me? What did-"
    MCT "Oh, this must be about the music club thing."
    BBW "I've been kicked out of the music club! Mizawa-san claims I was attempting to mutiny-"
    MCT "Well, you did suggest-"
    BBW "And now I have been expelled entirely."
    "By her expression I had no doubt who she blamed for this, and while there were a number of ways I could have responded, I ultimately decided on staying silent and not making things worse."
    "Alice continued glowering at me, perhaps waiting for me to answer, but after a while she huffed and muttered"
    BBW "What is wrong with this place?"
    "And then she walked away."
    "Which was awkward, because we were headed in the same direction, so I had to hang back a couple feet and try to look anywhere besides directly at her."
    scene Classroom with fade
    "And when we got to class and took our seats she adamantly refused to look in my direction."
    show BBW angry with dissolve
    BBW "Harumph!"
    hide BBW with dissolve
    "At least I knew where I stood at the moment."
    jump daymenu
    
label BBW009:
    scene Hallway with fade
    "It was only the second week of the year and I was already getting cabin fever being stuck at the school 24/7."
    "There was a town not far from the gates, but I hadn't gotten a chance to check it out yet. Hadn't even checked out much of the school, for that matter."
    "That's probably why I found myself at the locker rooms after class. Going back to my dorm room didn't appeal to me; just two weeks in and I was getting tired of that place."
    "And I still didn't belong to a club, so I had no specific place to be..."
    "I was thinking of maybe changing into my gym clothes and doing a little cardio when I was surprised to see Nikumaru-san, of all people, coming out of the women's locker room."
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    MC "Oh, Ni- Alice! How's it going?"
    show PRG sad at Position (xpos=0.75, xanchor=0.5) with dissolve
    PRG "..."
    MC "A-and you, Kodoma-san! What were you two up to?"
    BBW "I was doing a light workout."
    MC "I thought you weren't going to try to lose weight just yet."
    show BBW neutral
    BBW "I'm not, but exercise has other benefits besides weight loss."
    show BBW haughty
    BBW "A strong mind in a strong body, as they say."
    BBW "So I was making use of the school's swimming pool. 20 laps, back and forth. A fair workout to get my heartrate up."
    MC "20 laps!? That's... That's actually impressive."
    BBW "I understand how it can seem like that to most people, but I have a natural affinity for the water. I've been an accomplished swimmer since I was a young girl."
    if isEventCleared("BBW008"):
        MC "Maybe you should have joined the swim team instead of the music club."
        BBW "I did consider it, actually, but the school would allow me to join only one club. I find the limitation frustrating but bearable."
        show BBW angry
        BBW "And who knows. If the matter between me and the music club president is not resolved satisfactorily I may take my talents to more appreciative grounds."
    MC "How fast can you swim? Have you ever timed yourself?"
    show BBW neutral
    BBW "Quite fast, actually. I should have had Kodoma-san timing me, upon reflection. An accurate chart of my ability would help measure my fitness levels."
    PRG "I'm sorry, Alice. I'll remember next time, I promise!"
    show BBW haughty
    BBW "I don't have a specific number, but I feel confident that I am the best swimmer in our class. Probably in the top percentile of the school."
    MC "Even better than Mizutani-san? She's pretty athletic, you know."
    BBW "There's more to it than just physical strength. Stamina, hydrodynamics, breathing control."
    MC "!"
    "Alice didn't see her, but standing behind her was-"
    BBW "Sheer muscle may be good for lugging heavy weights around, but swimming is a much more graceful art than lugging something around."
    show FMG angry behind BBW at Position(xpos=0.15, xanchor=0.5) with dissolve
    "-was Akira. And judging by her expression she had heard enough of the conversation to get the gist of it."
    BBW "It's the difference between composing poetry and punching a sack of meat. Elegance versus brute force."
    "I was just about to interrupt Alice - even though she already seemed to be wrapping up - when Akira beat me to it."
    FMG "Hello Alice What's-your-last-name! Interesting theory you have there!"
    "Alice blanched at the sound of Akira's voice, but she recovered swiftly."
    hide PRG with dissolve
    show BBW surprised at Position(xpos=0.75, xanchor=0.5)
    show FMG angry at Position(xpos=0.25, xanchor=0.5)
    BBW "!"
    show BBW happy
    BBW "It's not so much a theory as good common sense."
    BBW "One isn't pushing against the water but rather propelling oneself through it. It's a complete different act, an interplay of body and water rather than a conflict between muscle and weight."
    FMG "Oh yeah! Well how about we test your little 'act of pushing water by being something something BS' by seeing who's the fastest swimmer! Or are you too full of yourself to do it!?"
    "Alice let out a single 'Ha' while brushing one of her curls over her shoulder."
    show BBW haughty
    BBW "I would never make a claim I could never back up. If you wish to see the truth of my words in action, then certainly. Let us race."
    FMG "God, are all Americans as snobby as you? Let's do this!"
    "Alice turned to me, her self-satisfied look still there."
    show BBW happy
    BBW "Any objections to Hotsure-san acting as judge? I'm sure he'll be impartial."
    show PRG neutral
    PRG "I... I could, maybe..."
    show FMG neutral
    FMG "Yeah, sure. But Keisuke, don't you think this is a forgone conclusion?"
    MC "Well..."
    menu:
        "You do seem the obvious choice, Mizutani-san.":
            $setAffection("FMG", 1)
            FMG "Heh, well whatever happens, happens I guess!"
            show BBW neutral
            BBW "Indeed..."
        "Alice seems pretty confident. I think this might be an upset.":
            $setAffection("BBW", 2)
            show BBW haughty
            BBW "Not an upset. As Mizutani-san said, it's a foregone conclusion."
            show FMG angry
            FMG "Whatever, 'princess'!"
        "I really don't know.":
            show BBW neutral
            BBW "Well, you shall know soon enough."
    scene Pool with fade
    "I went out to the pool as the two ladies got changed. Aida came out and stood next to me, and then the swimmers showed up."
    show FMG angry at Position(xpos=0.25, xanchor=0.5) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5) with dissolve
    BBW "Three full laps should be adequate, I think. Any objections?"
    FMG "Just don't forget your pool cap thingy! Don't want to get your expensive mullet to get ruined by chlorine!"
    "They took their positions, I counted down from three, and they were off."
    hide FMG with dissolve
    hide BBW with dissolve
    "It was neck and neck for most of the first lap, but when the two reached the far end and pushed off the wall to return Alice began to pull ahead."
    "By the time she completed her first lap Alice was a full length ahead of Akira, and that lead grew for the rest of the race."
    "When she completed her third lap Alice almost leapt out of the pool, springing to her feet and looking down to watch Akira reach the end."
    show FMG sad at Position(xpos=0.25, xanchor=0.5) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5) with dissolve
    FMG "...Son of a bitch... Good job I guess... I'm going to bed, later."
    hide FMG with dissolve
    show BBW happy at Position(xpos=0.5, xanchor=0.5)
    BBW "At least she's magnanimous in defeat."
    MC "Nice job. That was quite the blowout."
    show BBW haughty
    BBW "Was there ever a doubt? But as much as I enjoyed this contest, I have to get going."
    show BBW neutral
    BBW "Aida, what's next on my agenda?"
    hide BBW with dissolve
    "She was already walking away as Aida answered. Something about 'contacting her distributor.'"
    jump daymenu
    
label BBW010:
    scene Cafeteria with fade
    "It was a quiet morning. Reminded me of the first day, after we all learned why we were here."
    "Looking around at the faces in the cafeteria when I arrived, I got the same vibe as before. The embarrassment everyone was probably feeling because of their second puberty issue."
    show BBW happy with dissolve
    "Standing out in the mildly dark gloom of the other students, one face was unexpectedly shining."
    MC "Good morning, Alice."
    BBW "It is a good morning, isn't it?"
    "I took another quick scan of the room, at the subdued expressions and lack of light-hearted chatting you would normally find."
    MC "It's subjective, I guess."
    MC "Is there a particular reason you're happy? Did Aida make some really nice treats or something?"
    BBW "Business, my dear Hotsure-san. Business is doing well, and it's set to do even better soon."
    MC "Oh, your, what would you call it... Your..."
    show BBW neutral
    BBW "My requisition agency."
    MC "Yeah... That. Are people coming to you for stuff?"
    show BBW happy
    BBW "Word is beginning to spread of my services, with strong customer satisfaction driving an increase of my market share."
    show BBW haughty
    BBW "And I have set my flag on a particular shore with tremendous growth potential, based on both necessity and a consistent need for replacements."
    MC "What... Cell phones?"
    show BBW happy
    BBW "Clothing, my dear boy."
    show BBW haughty
    BBW "It may have escaped your notice, being a guy and all - one apparently not particularly concerned with your own appearance, at that - but the changes we are experiencing are already making the clothing and other accessories we arrived with obsolete."
    show BBW happy
    BBW "The school does supply new uniforms in larger sizes as we need them, but their system does not have the motivating factor of free market capitalism to push their productivity."
    BBW "And such aid only extends to the clothing we need as students. Personal expression and comfort is left to the individual to provide, a tiresome chore when the only stores are outside the school, all the way in town."
    show BBW angry
    BBW "And are we supposed to make that trip while wearing ill-fitting, potentially scandalous clothing?"
    MC "Hey..."
    show BBW happy
    BBW "Now there's a better choice. I, through my personal contacts with the biggest and best names in clothing retail, can offer you-"
    MC "Hey!"
    show BBW surprised
    BBW "!"
    MC "I don't need a sales pitch. I know what you're doing. You offered to get a computer for me, remember?"
    show BBW neutral
    BBW "Yes, yes. Got carried away there for a second."
    show BBW happy
    BBW "But the fact that you're familiar with this is perfect, because I have a proposition for you."
    BBW "I have more potential customers than I have time and energy to corral myself. I need subordinates out there spreading the word and taking orders."
    BBW "How'd you like the job?"
    MC "What, like a salesman?"
    show BBW neutral
    BBW "Not 'like' a salesman. Actually be one."
    show BBW happy
    BBW "It's child's play. All you have to do is distribute these catalogues I've made-"
    "She handed me a box of tri-folded papers - more like brochures than catalogues - that she must have made on her computer."
    "While they lacked the polish an experienced graphic designer would bring, they did get right to the point, emphasizing the low prices and breadth of available sizes for every body type."
    BBW "-and talk up what a bargain this is. Be sure to emphasize the more prestigious name brands, and that other designer labels will be available in the future."
    show BBW neutral
    BBW "Still have a few more deals to finalize. This school is so remote, bulk shipping out here is a logistical nightmare."
    show BBW happy
    BBW "But we already have most of our selection here at the school, ready to distribute to any interested buyer."
    BBW "And if anyone wants to see our products in real life, you can tell them that I'm already wearing my first new set of clothing."
    BBW "The school told me it would take as much as a week to get me a larger set of uniforms, but I - going directly to the company that has the contract with this school - was able to get this comfortable and properly-fitting outfit before my old set became restrictive."
    "She did a quick modeling job, turning around to show how her top didn't pinch or roll up on her now-wider torso and rounder belly."
    show BBW happy:
        zoom 2.0
    "I actually hadn't noticed that she had gotten plumper. It hadn't been two weeks yet, and I wasn't expecting to see such changes so quickly."
    "But apparently she had, because unless she had told me I wouldn't have noticed that this was a larger outfit, and it fit her as well as her old set. I could see how she thought this would be a good advertisement for her business."
    show BBW haughty:
        zoom 1.0
    BBW "No muffin top, no pinching in the sleeves."
    "I was still looking over her plump middle, my eyes lingering on the soft curves of her belly, when she snapped me out of my reverie."
    show BBW happy
    BBW "Sound good?"
    menu:
        "I could use a little spending money.":
            MC "I could use a little spending money."
            BBW "Can't we all?"
            MCT "I don't think you're hurting..."
        "(Might as well agree. I don't think she'd take 'No' for an answer.)":
            MC "Sure, I can do it."
            show BBW neutral
            BBW "I was hoping you'd be a little more fired up, but..."
            BBW "As long as you bring the thunder when you're engaging the customers, it's fine."
            MCT "Bring the thunder?"
        "You can count on me!":
            MC "You can count on me!"
            BBW "Excellent! That enthusiasm is exactly what I'm looking for."
    show BBW happy
    BBW "We can discuss your salary and bonuses later. Right now I want you to take advantage of the period before classes."
    BBW "Get out there and distribute those catalogues. I want to see that box at least half-empty before the bell for first period rings."
    "Caught up in her energy and enthusiasm, I sped away to start hawking her services."
    "I tried to think of who would need new clothes. Like Alice, I hadn't noticed any real growth in anybody yet."
    "But maybe necessity wasn't the best avenue to take yet. Maybe there was someone who just wanted something nice and flattering for after school."
    menu:
        "Shiori. She tends to dress conservatively, but doesn't every woman want to look nice?": # (-1 affection point with Alice)
            jump BBW010_c1
        "Aida. Alice had mentioned she doesn't have an extensive wardrobe.": #(No change in affection points with Alice)
            jump BBW010_c2
        "Honoka. Even if she hasn't grown, her needs already stretch most clothing shops.": #(+1 affection point with Alice)
            jump BBW010_c3

label BBW010_c1:
    $setScenecount("AE", 1)
    $setFlag("BBW010_shiori")
    scene Hallway with fade
    show AE neutral with dissolve
    "I found Shiori prowling the halls, eyes jumping around from student to student, as if she was looking for violations of the school dress code or something."
    "For a second I thought this would be a good lean-in to my sales pitch, but when I saw her expression I scratched that idea."
    "Something a little more subtle would be needed."
    MC "Hey, Matsumoto-san. You sleep well?"
    AE "Hotsure-san. Well, I'd say about four hours at this point, however that's neither here nor there. Anything you need?"
    MCT "I could respond with 'Actually, it's about what you need.' Except she looks more serious than usual."
    MC "Just making conversation. We are classmates, after all. We should be friendly with one another."
    AE "Ah, I see. Yes, well, while I'm all for interaction, I'm preoccupied at the moment. Begging your pardon."
    "She started to turn away, but I at least had to give her a 'catalogue' to say I did my job."
    "Gracelessly, I almost shoved one of them at her arm."
    MC " Here. Something to check out at your leisure, when you have some free time."
    AE "Hm? What is...The Nikumaru Outlet Direct? Keisuke...is this what I think it is?"
    "Something in her tone told me to tread carefully. But I, not exactly a cat burglar, couldn't do much except flail around."
    MC "Well, it's... I'm not sure what you think it is. What do you..."
    "She's glaring at me, and I see that playing coy wouldn't work even if I could do so properly."
    MC "Alice... Nikumaru-san has created a direct-market business. She orders stuff from manufacturers and can sell them at a discount. Clothes, school supplies, stuff like that."
    show AE angry
    AE "Hotsure-san...you can't just...ngh...where is Nikumaru-san? I swear if she thinks she can just undermine the administration with this-this tripe!"
    MC "She should be in the cafeteria..."
    "Only now did I realize what a blunder this was. Of course the school would have some rule about not running a business out of your dorm or something like that, and of course Shiori would memorize it and expect it to be followed to the letter."
    hide AE with dissolve
    "Shiori was already brushing past me, making a direct line for the cafeteria."
    $setAffection("BBW", -1)    
    "I looked down at the box of 'catalogues' I was holding, wondering if I should keep handing them out or consider myself fired."
    jump daymenu

label BBW010_c2:
    $setScenecount("PRG", 1)
    scene Cooking Classroom with fade
    "My first guess was that Aida would be at the cooking classroom, preparing Alice's breakfast. I wasn't wrong."
    "When I saw the baggy state of her clothes I thought this was probably a dead end. But then I wondered if she had any casual clothing that fit her and pushed on."
    show PRG neutral with dissolve
    MC "Good morning, Kodoma-san. Making breakfast?"
    PRG "Oh!  Uh, hello Hotsure-san. Is Nikumaru-sama ready for her food?  I-I can hurry it up..."
    MC "Oh no, it's not that. I was just walking by and thought I'd say hi."
    MC "Is that a new uniform? It looks a bit baggier than your old one."
    PRG "Um, d-do you not like it?"
    "For a split-second I thought about suggesting she buy something in her own size, but her doe-eyed expression made her look like she was on the brink of tears and I shot that idea down."
    MC "No, it's... it's cute."
    MC "But when you're cooking you don't really want anything that can get stained or burnt, right?"
    "I took out one of the 'catalogues' and held it out."
    MC "If you're interested in something a bit more form-fitting - for safety purposes - there's..."
    show PRG sad
    "I trailed off, because her expression had turned ashamed, lip bit and eyes downcast."
    MC "What?"
    PRG "I, I'm sorry Hotsure-sama, but... W-well, I already got these from Nikumaru-sama. I was her first customer."
    "I suppressed a groan as I realized that of course Aida would already be in on Alice's plans. It was her need for more clothing that had first put the idea of doing this in Alice's head."
    MC "Right, right. Forgot. Well, sorry to bother you."
    show PRG neutral
    PRG "No, no! I'm sorry for, um, wasting your time...  I'll, uh, still take one of the pamphlets, if you like..."
    "Hesitantly, I handed her one. I think not doing so would have made her more embarrassed."
    MC "If you'd like to place an order... Well, you know where to find me."
    if getAffection("PRG") >= 3:
        PRG "Yes, th-thank you, Keisuke-san... I-I'll see you later."
    else:
        PRG "Yes, th-thank you, Keisuke-san..."
    "As I walked away I wondered who was more embarrassed, me or her. She was doing a better job of putting a happy face on it, at least."
    "My first stab at a sale and I whiffed it. But I still had time before class started, so the morning wasn't a complete waste. Yet."
    jump daymenu

label BBW010_c3:
    $setScenecount("BE", 1)
    scene Hallway with fade
    "I was trying to think of where I could find Honoka when I was tackled from behind, collapsing to the ground."
    "A heavy, squishy weight on my back told me my search was over."
    show BE happy with dissolve
    BE "Hey, Kei-chan. You're looking a bit more spaced out than usual. You hit your head on something? I mean, besides me, of course."
    "Climbing to my feet, the sales pitch I had been rehearsing in my mind was pushed aside as I tried to think of something sarcastic and/or witty to say in response."
    MC "You ask me that after you run into me? Project much?"
    "But even as I said it I found myself distracted by Honoka's chest. After Alice's modeling routine I had curves on the brain, and Honoka was looking particularly big today."
    BE "Hehe, yeah, clearly it looks like you took a hit to the noggin, considering you can't lift your neck above chest level."
    MC "I was just... Um..."
    "And then, as if struck by inspiration, I realized this was actually perfect."
    MC "I was just noticing that your shirt looks a bit tight. That can't be comfortable, can it?"
    show BE neutral
    BE "Oh yeah! Definitely tighter. Been noticing it get tighter every day recently. Was pretty fun at first, definitely proof that I'm growing where they said I would. But, heh, yeah, it's not exactly comfortable. You have no idea how much bras pinch when they aren't made to fit you right."
    MC "Bras... Yeah. Those things."
    "Black lace bras with the cups almost transparent, frilly edges rising from her cleavage like dolphins jumping out of the sea. White cotton cups pulled taut by two great mounds of flesh, the straps digging into her shoulders..."
    BE "..."
    MC "Ah!"
    "I snapped my head downward to escape eye contact with her. Only then did I remember the box I was holding in my hands. I took out one of the 'catalogues.'"
    MC "If you're looking for new clothing, there's a new service that just opened up. Really affordable clothes, some custom-made, direct from the manufacturer."
    "Quizzical, she looked the 'catalogue' over."
    BE "Huh. Wow, there's a lot of stuff in here. Pretty neat, actually. Most of the time once you get past a certain size, you can only get bras in boring colors or things without patterns. It really takes the fun out of it. But, they're saying here they can do more custom patterns? Prices seem okay too, all things considered. How'd you get your hands on this?"
    MC "Ali- Nikumaru-san hired me. She knows people in high places at all these companies, so she has an 'in,' so to speak."
    MC "She's also selling school supplies and other stuff, but I guess she's focusing on clothing right now because... Well."
    "I gestured at her chest, wrapped up in a too-tight shirt and bra."
    show BE happy
    BE "Because it's like starting up an ice cream stand in the middle of a heat wave. She'll make a killing here if she can get everything authorized! You better be getting a cut of all of this if you're going to be helping her out. Don't let her take advantage of you."
    show BE surprised
    BE "Unless you're into that kind of thing. A big girl like Alice? Yeah,  I could definitely see that. Was there a dominatrix getup in this catalogue? That'd be something to see on her..."
    "Man, my imagination was getting a workout today."
    "I shook my head to clear my mind."
    MC "I am being compensated (though the specifics haven't been hammered out yet). I believe she even mentioned something about a commission."
    MC "So can I put you down for a sale? I can run your order back to her before class starts, but I'm not sure how long it will be until everything arrives. She did say she already has a lot of stuff here..."
    show BE happy
    BE "Oh absolutely! Here, let me take a look again real quick. ... Yeah, I think I can spring for three bras and, maybe two shirts. No I'll just stick with this one for now. Luckily I've been looking up how to properly measure busts so I can figure out my own size. Well, as long as I'm capable of getting my arms around them that is!"
    MC "Even if you have trouble measuring yourself, we can find clothing big enough..."
    "My voice trailed off as I was hit with the mental image of Honoka carrying a pair of breasts bigger than she was, carting them around in a wheelbarrow..."
    "...and running me over with them."
    "Like I said, my imagination was running on all cylinders today. Salesman-mode had delayed the image conjured by her blithe comments about her growth, but the idea that she would grow so big she couldn't wrap her arms around herself... That was impossible to ignore."
    "I cleared my throat, blushing as I saw her smile mischievously at me, and sputtered."
    MC "I'll get back to you on how soon we can deliver these. Do you just want the plain model for the bras?"
    show BE surprised
    BE "Oh god no. I want one with the heart design, one with the joystick design, and, hm, I dunno, probably one with just some nice color. What do you think would be best; blue, pink, or black?"
    MCT "Black! Black!"
    MC "I think... black might be best. Bold, but not garish."
    show BE neutral
    BE "Sounds good to me. We'll go with the black then. And I circled the shirt I wanted too. Thanks Kei-chan. This is pretty cool, I appreciate it."
    MC "Well, I am being paid. But you're welcome, all the same."
    "She winked playfully and then spun around, jogging away."
    "Even from the back I could see the extra bounce... in her step. I admired it for a moment, and then turned back to the matter at hand."
    $setAffection("BBW", 1)
    "Landing a sale five minutes into my job was great, but I suspected Alice wouldn't ignore a still-full box of 'catalogues' because of it."
    jump daymenu
    
label BBW011:
    scene Hallway with fade
    "Another day done, and I find myself with no idea of what I want to do."
    "The afternoon's a blank page, but when you can start in a million different ways it's impossible to pick just one."
    MCT "It's not like I'm hoping to find something to do if I wander around the school long enough, but... Maybe I will?"
    scene Classroom with fade
    pause 2
    scene Gym with fade
    pause 2
    scene Pool with fade
    pause 2
    scene School Exterior with fade
    "Half an hour passed. I walked from the classrooms to the gym to the pool to behind the campus. Nothing."
    scene Roof with fade
    pause 2
    scene School Planter with fade
    "Another half hour. I went to the rooftop, the garden. Nothing."
    "At one point I thought I saw a person sneaking behind the cafeteria, but they were gone when I got there."
    scene School Exterior with fade
    "Another fifteen minutes of walking, and I started to think maybe I should have gone to the gym and gotten a real workout in."
    scene Dorm Exterior with fade
    "I had finally decided to go back to my dorm and take care of my homework when I was saved from my boredom as I almost ran into Aida."
    show PRG sad at Position(xpos=0.75, xanchor=0.5) with dissolve
    M "Whoops. Pardon me."
    "O-oh! I'm sorry."
    "Standing right behind her was Alice."
    show BBW neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    BBW "Don't mind her. She's too excited for her own good."
    BBW "Watch where you're going, Kodoma-san."
    PRG "Y-yes, ma'am."
    MC "What's going on that has you in such a rush?"
    BBW "Kodoma-san wants to join the film club meeting today. Apparently they're screening one of her favorite movies."
    show PRG happy
    PRG "It's called Waiting for the Wrong Bus. It's a romantic-comedy from a couple years ago."
    MC "Yeah, I've heard of that. Typical chick flick, right?"
    PRG "Oh, it's more than that. It's a beautiful and tender tale of two destined souls overcoming circumstances working to keep them apart-"
    MC "Isn't it because they don't like each other at first, but then they do?"
    show PRG angry
    PRG "No! It's not just that. Come watch the movie with us and you'll see."
    BBW "It does sound like every other rom-com I've seen."
    PRG "You're both wrong."
    menu:
        "Sorry, but I've got homework to do. And chick flicks aren't my thing, you know?":
            jump BBW011_fail
        "OK, OK. I'll come with and see for myself.":
            jump BBW011_prechoice
            
label BBW011_fail:
    MC "Sorry, but I've got homework to do. And chick flicks aren't my thing, you know?"
    show PRG sad
    PRG "Oh... All right."
    show PRG happy
    PRG "Maybe some other time?"
    MC "Uh, maybe."
    jump daymenu

label BBW011_prechoice:
    MC "OK, OK. I'll come with and see for myself."
    show PRG happy
    PRG "!"
    "Aida's face lit up, clearly happy to have another person accompanying her."
    scene black with fade
    "We three went to the film club meeting. The club had about a dozen people, which left plenty of seats for guests."
    "100 minutes later we were back out in the hallway."
    scene Hallway with fade
    show PRG happy at Position(xpos=0.75, xanchor=0.5)
    show BBW neutral at Position(xpos=0.25, xanchor=0.5)
    PRG "What did you think? Wasn't it beautiful?"
    "Aida had her hands clasped in front of her heart, her cheeks so rosy and her eyes closed. She looked like she might swoon at a moment's notice."
    BBW "..."
    "Alice, meanwhile, looked like she was listening to elevator music playing at one-half speed."
    menu:
        "It was... sweet?":
            jump BBW011_c1
        "They didn't like each other at first, and then they did. I called it.": #(-1 Affection with Aida)
            jump BBW011_c2
        "Well... Alice? What did you think?":
            jump BBW011_c3

label BBW011_c1:
    MC "It was... sweet?"
    PRG "Wasn't it? When Kenji ran into the burning building to get her teddy bear it was so touching."
    PRG "What was your favorite part?"
    MCT "Guess I've got to make a bluff check."
    MC "When Kenji... was complaining about Ayami and then suddenly he was talking about how much he loved her?"
    "That actually had to have been my least favorite scene, but that's why it was the only one I could think off."
    "And the way Alice fought back a snort, it didn't look like the movie had worked on her, either."
    "But this was an opportunity to free myself from the conversation."
    jump BBW011_c3

label BBW011_c2:
    MC "They didn't like each other at first, and then they did. I called it."
    show PRG angry
    $setAffection("PRG", -1)
    PRG "But it's more than that. It's about them realizing what the other means to them, and how happy they are together."
    MC "I have to say, I didn't see that. They spent, like, 75%% of the movie sniping at each other, and then suddenly they want to be together?"
    PRG "It's not sudden. Don't you remember the scene where Kenji warns Ayami not to eat the shrimp that made everyone else sick?"
    PRG "It's because deep down he cared about her."
    MC "That only makes sense if you can believe that neither would come out and say what they were feeling."
    MC "But that seems to be every movie like this. All their problems would be solved if they were just honest for five seconds."
    show PRG happy
    PRG "But then they wouldn't get to show their love. What about when Kenji ran into the burning building to get Ayami's teddy bear? Wasn't that dashing?"
    MC "And then he realizes he could have gone around the building to get to Ayami's room, because the fire hadn't touched that place yet. And then he trips and knocks himself out. It was amusing."
    MC "But running into the building in the first place? I'm really not a fan of the big, showy demonstrations of love. They always come across as manufactured."
    show PRG angry
    MC "That climax in particular... Probably the only realistic thing in the movie was the firefighters berating him for that stupid stunt."
    PRG "But he got the bear!"
    MC "The bear was never in danger."
    PRG "That's not the point!"
    "I could see how quickly this was falling apart, and I didn't want to keep digging myself deeper."
    "Fortunately, I had an out."
    jump BBW011_c3

label BBW011_c3:
    show PRG neutral
    MC "Well... Alice? What did you think?"
    "Alice looked down at Aida, still blushing deeply."
    BBW "I think it was exactly like every other rom-com I've seen."
    MC "Is that a good thing?"
    BBW "If it's what you're looking for, yes. The familiar has its own appeal."
    show PRG sad
    PRG "But you didn't like it?"
    "Alice hesitated again before responding. Despite her bored expression, her quick glances at Aida told me she was being careful with her words."
    "Concern for Aida's feelings, I would assume."
    BBW "I don't find it realistic. Not that movies need to be realistic all the time, but when it comes to romance I, personally, don't like games."
    show PRG neutral
    PRG "Games?"
    BBW "If there is something you want and you do not make every effort to claim it, what are you doing? You are playing around, wasting time and effort."
    MC "That's a pretty harsh view of romance, don't you think? You make it sound like a guy going after a girl sees her as nothing but a prize."
    BBW "Her heart is the prize."
    BBW "Courtship is a challenge, the man is tested and tries to prove himself. And, if he is successful, he is rewarded with her love."
    MC "But the woman doesn't have to do anything? Doesn't have to prove herself?"
    BBW "Women have their own trials in any relationship, but how often are we the pursuer?"
    MC "Not big on women's lib, I take it."
    show BBW haughty
    BBW "Au contraire. I've never met a woman in our generation more dedicated to conquering the world of business and smashing the glass ceiling than I am."
    BBW "I'm simply a realist. Even with advances in women's equality it's considered custom for the man to initiate, to pursue, to 'win.'"
    BBW "But this set-up gives us ladies our own power, as long as we recognize it and use it."
    MC "So you don't mind being considered an object, a trophy?"
    MC "You wouldn't be insulted if, say, I asked you out, dated you, and then 'won' you? Made you my wife?"
    "She chuckled, brushing one of her locks behind her shoulder."
    BBW "Hotsure-san... Do you know what a woman wants?"
    MC "Eh?"
    MC "You mean like flowers and chocolates?"
    show PRG happy
    PRG "Or stuffed animals!"
    show BBW neutral
    BBW "No, I'm not talking about simple gifts."
    BBW "I'm talking about romance. Do you know how to woo a lady?"
    MC "Yeah! I mean... I've dated before. I understand romantic... stuff."
    MCT "I just lost when I called it 'stuff,' didn't I?"
    show BBW haughty
    BBW "Romantic 'stuff.' Heh."
    BBW "I don't think I need to worry about becoming merely your wife."
    BBW "Thinking it is your job to win means you are destined to lose."
    show BBW neutral
    BBW "Fun talk, though. We should do this again."
    BBW "Hopefully with a better movie."
    show PRG sad
    PRG "But *I* liked it."
    jump daymenu
    
label BBW012:
    scene Classroom with fade
    "When the classes ended for the day, I was more than ready to shut my brain off."
    "The whammy of the news of our condition didn't mean we got to stop learning. Tashi-sensei ran the class like a herd of pack mules, just instead of piling loads of goods onto our backs we were packing our brains full of facts and figures."
    "I had several chapters of reading to get through later that day, but first I needed to decompress before my grey matter started to overheat."
    "But as I gathered up my things and made to leave, I felt a hand on my shoulder."
    show BBW neutral with dissolve
    BBW "Keisuke, do you have a moment?"
    MC "Uh... Yes?"
    show BBW happy
    BBW "Excellent. We need to have a meeting to discuss the future of The Nikumaru Outlet Direct."
    BBW "I'm calling all employees in, so come along."
    scene Cafeteria with fade
    "I followed Alice to the cafeteria, where Aida had already laid out tea and crumpets at Alice's usual table."
    show BBW happy with fade
    BBW "Good. We're all here."
    MC "All three of us?"
    show BBW neutral
    BBW "Both of us. Kodoma-san is still operating in her capacity as my personal assistant, so for now this is still a two-person operation."
    show BBW happy
    BBW "There's me in the CEO/CFO/President chair, and you pounding the pavement to get orders and make deliveries."
    BBW "It's exactly the type of humble beginnings that all great corporate empires are born from."
    show BBW angry
    BBW "But we're in the midst of a crisis right now. Our very existence as this school's premiere clothing retailer is under attack."
    show BBW neutral
    BBW "Hence this meeting. We need to address this attack on free enterprise: Matsumoto-san asserts that it violates the school's rules and regulations for a student to run a business on campus."
    if not getFlag("BBW010_shiori"):
        MC "Wait, we're not allowed to be doing this? Then why are we having this meeting?"
        show BBW haughty
        BBW "Don't be so hasty to accept defeat, Keisuke. As in any competition, to win in business is not just to strive for success, but to reject failure."
        BBW "If you allow others to set the terms you're handicapping yourself. It is only when you seize control of the playing field and the rules of the game that ultimate victory becomes possible."
    MC "So you think there's some sort of loophole to exploit?"
    show BBW haughty
    BBW "Over, under or through. There's always a way to get past a mountain."
    BBW "The Nikumaru Outlet Direct will not shutter its doors just because one nosey bureaucrat seeks to hobble us. I've already found a way forward."
    jump BBW012_c1
    
label BBW012_c1:
    menu:
        "About that name..." if not getFlag("BBW012_c1_1"):
            jump BBW012_c1_1
        "About that name... (disabled)" if getFlag("BBW012_c1_1"):
            pass
        "Maybe we should just stop before we get into real trouble." if not getFlag("BBW012_c1_2"):
            jump BBW012_c1_2
        "Maybe we should just stop before we get into real trouble. (disabled)" if getFlag("BBW012_c1_2"):
            pass
        "I'm all ears.":
            jump BBW012_c1_3
        

label BBW012_c1_1:
    $setFlag("BBW012_c1_1")
    MC "About that name... It's a bit long, isn't it? And kind of bland."
    show BBW neutral
    BBW "That is one thing addressed in my plans. I admit, marketing is not my strongest suit."
    BBW "But if you have a suggestion, by all means. Share."
    MC "How about... Niku-Knacks!"
    show BBW angry
    BBW "..."
    show BBW neutral
    BBW "OK. Marketing is a weak point for both of us."
    BBW "I'll keep that in mind."
    jump BBW012_c1

label BBW012_c1_2:
    $setFlag("BBW012_c1_2")
    MC "Maybe we should just stop before we get into real trouble."
    show BBW angry
    "Alice scoffed-"
    BBW "Scoff."
    "-and gave me a withering look, but I pushed on."
    MC "Maybe Matsumoto-san's a bit strict, but she's not being a hard-ass-"
    MC "Um, she's not some sort of killjoy that has it out for you personally."
    MC "The school has rules for a reason, even if we don't always like them. It's lame, but true."
    MC "And with everything on our plates right now anyway, with school work and dealing with our conditions, do you really want more drama in your life by starting something with the class president?"
    MC "Or maybe the teachers and administrators?"
    "She didn't respond immediately, but I simply waited. She looked irritated enough already and I knew better than to poke her."
    "After a moment she exhaled and said"
    show BBW neutral
    BBW "This is how I'm dealing with it."
    MC "I'm... sorry?"
    BBW "The schoolwork isn't too much for me. If anything it's a bit easier than at my old school."
    BBW "But the news about our condition? I've already tried to stop it by dieting and working out. It wasn't successful, and I've come to accept that - for now, at least - my weight gain will run its inevitable course."
    show BBW angry
    BBW "But that doesn't mean I will allow it to change my life."
    BBW "I was already on the path to a life of success and prestige in the world of business before I came here. My size will not be a roadblock, or even an obstacle."
    show BBW haughty
    BBW "I will proceed as I was before, as if nothing has changed."
    BBW "I am not ignoring what is happening, but neither will I allow it to control me or my actions. That is not the Nikumaru way."
    menu:
        "Oh... I think I understand.": #(+1 affection point with Alice)
            jump BBW012_c2_1
        "I still think you're making trouble for yourself down the line.": #(-1 affection point with Alice)
            jump BBW012_c2_2

label BBW012_c2_1:
    MC "Oh... I think I understand. You're pretty serious about this, huh?"
    $setAffection("BBW", 1)
    BBW "I am always serious about business, Hotsure-san."
    MC "I can respect that, even if I'm not entirely convinced it won't come back to bite you."
    MC "But if you're sure you want to do this, I can help."
    jump BBW012_c1

label BBW012_c2_2:
    $setFlag("BBW012_c1_1")
    MC "I still think you're making trouble for yourself down the line."
    MC "And I've gotta be blunt, I don't fancy getting Matsumoto-san or any of the teachers getting on my case because you're trying to make a few extra dollars."
    show BBW angry
    $setAffection("BBW", -1)
    BBW "If you're that concerned, don't be."
    BBW "You're simply a hired hand. If any hammer is dropped it will be on my head."
    MC "I'm not asking you to take all the blame-"
    show BBW haughty
    BBW "Whatever your objections, you'll be protected. This is my business, after all."
    BBW "You worry about making your deliveries, and I'll handle everything else."
    jump BBW012_c1

label BBW012_c1_3:
    show BBW happy
    BBW "Earlier today I contacted a clerk at a law firm that does occasional out-of-house work for my father's business."
    BBW "As we speak she's filing the paperwork to create the Alice's Wishes Granted LLC."
    BBW "Its official address will be a PO box I've secured in town, with all correspondence coming or going through it. Legally speaking, no business will be conducted on school grounds."
    MC "That's your solution? Won't that be inconvenient for people who want to place orders, having to mail a letter to a PO box?"
    MC "And who's going to collect the mail? I don't think-"
    "Alice held up a hand to stop me."
    show BBW neutral
    BBW "We won't be taking orders through snail mail. That's far too inefficient."
    BBW "If you hadn't interrupted, I would have explained that I also have a software engineer developing a website and business email account."
    BBW "Everything involved in placing the order and paying for it will be handled online. The PO box is merely a formality."
    BBW "Understand?"
    MC "I guess. Is it really necessary?"
    BBW "Yes. As I said, by establishing a storefront off school grounds I am no longer in violation of any rules."
    MC "And what about filling the orders? Will the packages be delivered to you here?"
    show BBW happy
    BBW "Got it in one. While there are prohibitions on what items can be mailed to students here, our selection of products does not include weapons, drugs, or other such items."
    BBW "Everything to be mailed to me is in keeping with permissible personal effects."
    MC "You're still exchanging goods for money."
    BBW "No, I am accepting gifts purchased by my fellow students and then graciously returning them when it turns out they do not suit my needs."
    MC "You're... what?"
    "She grinned deviously, like a smug cat meme."
    show BBW haughty
    BBW "Once the website is up and running you'll see. Or perhaps I should tell you now."
    BBW "The website and order form will be constructed so as to appear as if our customers are buying items on my personal wish list."
    BBW "All orders will be mailed to me, with the customer's information included as a special message so I know who the thoughtful party is."
    MC "And once you have a new skirt or set of underwear you'll say 'Oh, this doesn't fit me' or 'Oh, it's not my style' and you 'give it back' to the person who bought it."
    "Her smile didn't grow wider, but it somehow grew more smug."
    MC "One question: What's the difference between bending the rules and breaking them?"
    BBW "Breaking gets you punished. Bending increases your profit margin."
    jump daymenu

label BBW013:
    scene Hallway with fade
    "My name had come up on the class clean-up schedule again, so when I got out for the day the hallways were mostly empty. Everyone else was back at their dorm or enjoying the pleasant afternoon."
    "It made it easy to recognize the two figures over by the stairs, even if one wasn't the only blonde woman on campus and the other wasn't..."
    show BBW angry at Position(xpos=0.75, xanchor=0.5) with dissolve
    MCT "Oh no..."
    "If the other wasn't my roommate."
    show RM angry at Position(xpos=0.25, xanchor=0.5) with dissolve
    "I couldn't hear what they were talking about, but I could see Alice standing rigid, her expression stony cold as Daichi held up one of those measuring device clamp things."
    "What were they called? Shiori would probably know..."
    "Anyway, I started walking slower, not wanting to eavesdrop on the two but also fearing I had some idea of what they were talking about."
    RM "Taking these measurements now is vital if we're going to chart your future expansion. We need to know how much you weigh and where your body distributes your fat-"
    BBW "Grrrr!"
    RM "-to compare with how big you - and specific parts of you - will become later."
    show RM neutral
    RM "I also need you to answer some questions about your eating habits, your exercise routine. If you have one."
    RM "Are you eating more than you did before you came here? More often? Are you hungrier than before?"
    RM "Do you find it harder to carry your weight? Do you get tired more quickly?"
    RM "This will all tell us what 'they' are doing to you, which will give us a clue as to their ultimate plans."
    MCT "Yeah, this is exactly what I feared."
    BBW "'They?' 'They' who?"
    show RM angry
    RM "The govern-"
    BBW "Clearly I was being facetious. I don't actually want to know what paranoid fantasy you're harboring."
    MCT "I should probably step in and get Daichi out of there before she really tears into him."
    MCT "Then again, I don't want to bring her wrath upon myself..."
    menu:
        "Stay back. Daichi got himself into this.": #(-1 affection point with Alice)
            jump BBW013_c1
        "Rescue Daichi.": #(+1 affection point with Alice)
            jump BBW013_c2

label BBW013_c1:
    "I backed away slowly, not drawing either's attention, and hid inside a classroom door."
    BBW "Do you think I have nothing better to do than be accosted by some conspiracy theorist?"
    BBW "What are you, a 'growth truther?' Do you think they're slipping us hormones in our food?"
    show RM neutral
    RM "That might actually be-"
    BBW "I DON'T HAVE TIME FOR YOUR GAMES, BOY!"
    BBW "I am stuck here on an isolated rock, shoved away with a bunch of other... people with a condition like mine, dealing with the news that my own body is going to blimp out of its own accord."
    BBW "And you want to get in my face about some secret cabal making me fat?"
    RM "To be honest, I don't know who exactly is doing this."
    BBW "SHUT! IT!"
    BBW "And answer me this: if there was an insidious conspiracy bent on performing experiments on random people, do you really think that I, Alice Nikumaru, daughter of Daitaro Nikumaru, would be one of those guinea pigs?"
    BBW "My father has connections reaching through every corner of the world's industrial and political. No one would dare subject me to something like this without invoking his wrath."
    RM "There might have been-"
    BBW "I TOLD YOU TO SHUT IT!"
    BBW "And get out of my sight. Don't ever even think of planting your grimy little paws on me, and don't ever talk to me about my body again."
    show RM sad
    RM "OK. OK."
    hide RM with dissolve
    show BBW angry at Position(xpos=0.5, xanchor=0.5)
    "Daichi didn't quite run from her, but he didn't drag his feet."
    "Alice stayed standing there and watched him leave. After a while she exhaled, but she didn't look any less tense."
    "I didn't want to take the long way back to the dorms, so I'd have to walk past her. Hopefully she wouldn't-"
    BBW "Hotsure-san."
    MCT "Uh-oh."
    MC "Ali- Nikumaru-san. You look... tense."
    BBW "Did you hear any of that buffon's rambling?"
    MC "Uh, yeah. I got the gist."
    MC "Daichi's kind of like that-"
    BBW "Daichi? Is that his name?"
    MC "Yep. He's my roommate..."
    "The next words shriveled in my mouth as Alice turned the full intensity of her glare upon me. Too late, I realized my mistake."
    BBW "Your roommate?"
    $setAffection("BBW", -1)
    BBW "So is it a coincidence that out of all the students on campus, he came to me, your classmate, to harass?"
    BBW "Who put it in his mind to come to Alice, the soon-to-be portly girl?"
    MC "Actually he's in our class-"
    MC "Never mind that. I didn't tell him to bother you. I want nothing to do with his ramblings, and I would never put him up to coming after you."
    BBW "(tsk)"
    BBW "You didn't stop him, either."
    MC "No, but... What was I supposed to do?"
    "Alice held up a dismissive hand and turned away."
    BBW "Teach him to have more class. He's in the same boat we all are, isn't he?"
    MC "Yeeeeahhh... He is."
    BBW "Then he should have some empathy, if not basic social grace."
    "She walked off in a huff, and I wasn't too eager to chase her and explain my uninvolvement."
    "Better to take the hit and let her be angry with me for a while."
    jump daymenu

label BBW013_c2:
    "Daichi was opening his mouth to retort. I couldn't predict his exact words, but I knew they would be some form of doubling down, trying harder to get her to listen to him."
    "I couldn't let that happen. Alice didn't deserve to listen to his ramblings, and Daichi needed to be pulled out of the hole he was digging for himself."
    MC "Daichi! There you are."
    show RM neutral
    RM "Huh? Keisuke?"
    MC "Shiori is looking for you. She said something about a sample the nurse needs to get from you?"
    show RM embarassed
    RM "Crap! Where was she?"
    MC "Back that way."
    hide RM with dissolve
    "I hooked a thumb over my shoulder, and Daichi immediately pelted in the opposite direction. He was gone before I even finished walking up to Alice."
    BBW "..."
    BBW "Matsumoto-san wasn't in the classroom, was she?"
    MC "No."
    "Alice let out a gust of air, relaxing in body, but not quite spirit. A feeling of tension hung around her, like an aura."
    show BBW neutral
    BBW "No. At this time she should be in the library, taking care of her paperwork."
    MC "I can see that."
    BBW "She is predictable, if nothing else."
    show BBW happy
    $setAffection("BBW", 1)
    BBW "I owe you my thanks, Hotsure-san. If that fool had continued, I'm not sure I could have been held responsible for my actions."
    MC "I wouldn't be surprised. At least you don't have to share a room with him."
    show BBW neutral
    BBW "He's your roommate? Then you must know if he's always like that."
    MC "Yes and no. He's got no shortage of ideas about what's 'really happening' here, but this is the first time I've seen him going that far."
    BBW "Trying to put his hands on someone else?"
    MC "I really don't think he was trying to be grabby or anything. He just... forgot about personal boundaries."
    MC "He is very serious about all this."
    BBW "I suppose some of us are having a harder time dealing with this than others."
    BBW "Assigning blame for this may be more accommodating than accepting it's pure chance. It's easier when you can be angry at someone."
    BBW "What is his growth factor? It must be severe to set him off like that."
    MC "He... It's rather personal."
    "What? It's not like I could tell her Daichi wasn't supposed to be here."
    BBW "I understand."
    BBW "Still, one would think that someone in his position would have more empathy for the rest of us. We have all been blindsided by this. None of us should be making it harder for anyone else when it comes to our conditions."
    MC "Yeah. I'll tell him to ease up when I see him later."
    MC "Say, Alice..."
    "I hesitated a moment, but she looked at me, waiting."
    MC "Don't take this the wrong way, but I'm curious. Are you upset about your weight?"
    BBW "No."
    "She answered pretty quickly, in that way that makes it hard to believe someone. But I didn't say anything."
    BBW "I accepted what was happening once I learned the news, and I know I can address my weight gain once it fully happens."
    BBW "In the meantime, I am still Alice Nikumaru. I am not defined by my size or my appetite."
    BBW "Character is revealed in how they deal with tribulation, not what form those trials take."
    MC "You sound like you're dealing with it pretty OK."
    "I was about to walk away, but then I decided..."
    MC "Hey, Alice. I was about to get a snack at the cafeteria. You hungry?"
    BBW "... Hmm..."
    show BBW happy
    BBW "I could go for some cake."
    jump daymenu

label BBW015:
    scene Hallway with fade
    show BBW happy
    BBW "Keisuke! A mission!"
    "I was headed to... breakfast..."
    show BBW neutral
    MCT "There goes my train of thought. How am I supposed to manage if I can’t supply a running commentary of my day?"
    BBW "Keisuke."
    MC "Yes? Good morning."
    show BBW happy
    BBW "Good morning. Are you ready to work?"
    MC "I’m ready for breakfast. It’s not work, but it’s-"
    show BBW neutral
    BBW "Breakfast is important, but so is fulfilling one’s obligations."
    BBW "The wheels of business never stop turning, and thus we ourselves can never cease."
    MC "It’s a little early to go looking for sales."
    BBW "That’s not what I need you for. Do you remember the restructuring of our company?"
    MC "Hmm? Oh! Right."
    MC "That wish list thing."
    "Only now did I notice the thick mailing envelope in Alice’s hand."
    MC "Did we already get an order?"
    show BBW happy
    BBW "First of the company’s new era."
    BBW "And you have the singular privilege of making this first delivery. The first delivery of any kind for the company."
    "She handed me the brown, bubble interior envelope, already open."
    "Inside was a folded sheet of paper and a small green and white garment wrapped in plastic."
    "The paper was an order form. Turned out the garment was a pair of panties, ordered by one Moriko Fukushi."
    MC "Where can I find this woman?"
    BBW "She’s in room 306 of the women’s dorm. You’ll find it on the sales slip. If you hurry you can probably find her there now."
    show BBW angry
    BBW "But exercise caution."
    BBW "Mastumoto-san is already keeping one eye on me, and I suspect her myopic adherence to the rules blinds her to such things as the spirit of the law."
    BBW "Which I am fully in line with, as you know."
    show BBW neutral
    BBW "The most efficient solution is to avoid contact with her. I have no quarrel with her personally, after all."
    MCT "It would only be antagonistic to point out the simplest solution is to drop this whole venture."
    MCT "And hypocritical. It’s not as if I’m turning down the promise of money."
    MC "I got it. Stealth."
    "Alice nodded and let me go."
    "The question now was, how to get to the dorm? Guys weren’t forbidden from going into the women’s dorm building, but it stood to reason it was the place I’d most likely run into Shiori."
    menu:
        "Take the direct approach. Get in, get out.":
            jump BBW015_c1_1
        "Go around and come in from the rear. Less chance of getting caught.":
            jump BBW015_c1_2
        "Think outside the box. Go through the vents.": #(-1 affection point with Shiori)
            jump BBW015_c1_3

label BBW015_c1_1:
    "I tucked the mailing envelope into my backpack and headed for the women’s dorm with deliberate speed."
    scene Dorm Exterior with fade #this may need new graphics
    "I ignored the ladies I passed in increasing numbers the closer I got to the building. If anyone asked I had an excuse at the ready-"
    UNKNOWN "Hotsure-san."
    MCT "Eep!"
    show AE neutral with dissolve
    AE "What are you doing here?"
    "I had made it to the lobby of the women’s dorm, mere feet from the elevator and relative safety."
    "Of course I would get stopped here."
    "Worse, I had the sales slip in my hand as I was double-checking the room number."
    menu:
        "Answer.": #(+1 alice affection)
            jump BBW015_c2_1
        "Hide the sales slip.":
            jump BBW015_c2_2

label BBW015_c2_1:
    "Folding the slip one-handed, I casually tucked it into my pocket while answering."
    MC "I was trying to find Mizutani-san. I had a manga I had borrowed from her, and I wanted to give it back."
    AE "And you couldn’t wait until class?"
    MC "I suppose I could have, but I wanted to do it before I forgot."
    MC "I’m sure you can appreciate the importance of promptness."
    AE "I do…"
    "Her eyes narrowed. I could feel beads of sweat start to appear at the top of my forehead."
    AE "Very well. Go return the book."
    AE "But don’t dawdle. Access to the women’s dorm is a privilege, not a right."
    MC "Yes, ma’am."
    scene black with fade
    "After that brief scare the rest of the delivery went off without a hitch."
    "I found the right room, found Fukushi still there, and gave her the package."
    "Later..."
    scene Classroom with fade
    show BBW happy
    $setAffection("BBW", 1)
    BBW "Excellent work!"
    BBW "Dependable and resourceful. Keisuke, you have the makings of a great Nikumaru delivery agent."
    "Alice seemed more impressed with my job than I felt I deserved, but it wasn’t that odd for her to overreact."
    BBW "Be on standby for the next delivery. Business will start slow, but before you know it be flooded with orders."
    MCT "Just so long as they’re not all a close call like this one..."
    jump daymenu

label BBW015_c2_2:
    "Before I said anything I needed to hide that sales slip."
    MC "Well..."
    "I folded the slip in two, and then again, and was just about to put the telltale paper into my pocket when Shiori noticed my fumbling."
    AE "What is that?"
    "Her tone made me shiver. It wasn’t an idle question, something I could pass off as ‘just a piece of paper.’"
    $ timer_count = 2
    $ timer_jump = "BBW015_c2_2_menu2"
    show screen choicetimer
    menu:
        "EAT THE SLIP!":
            jump BBW015_c3_1

label BBW015_c2_2_menu2:
    menu:
        "Lie.":
            jump BBW015_c3_2
        "Hand the note over.":
            jump BBW015_c3_3
        "EAT THE SLIP!":
            jump BBW015_c3_1

label BBW015_c3_1:
    "I did the first thing that came to mind."
    show AE surprised
    AE "Ah-"
    "I shoved the paper into my mouth and began chewing."
    "It was hard to chew at first, because the paper was folded twice over. I had to work up some spit to get it soft, first."
    show AE angry
    AE "Hotsure-san..."
    MC "Yesh?"
    $setAffection("AE", -1)
    AE "Did… did you just destroy evidence in front of me? What was that?"
    "I forced myself to swallow. My throat ached as I struggled to get the wet mass of paper down."
    MC "Gasp!"
    MC "It was... nothing. It was private."
    AE "…"
    MC "There was no mistaking her mood, but the exact thoughts running through her head were harder to figure."
    AE "You are in the women’s dorm, with a ‘private’ note you clearly do not want others to see. Any chance you had of clearing your name of suspicion went down your gullet with the paper."
    AE "But since the note is gone, you no longer have any reason to be here, correct?"
    MC "I-"
    show AE neutral
    AE "Rhetorical question."
    AE "I’m afraid I must ask you to leave, and I will keep note of this."
    scene black with fade
    "I turned around and left, not wanting to give her a chance to change her mind."
    "Alice was surprisingly chill about the news of my failure."
    scene Classroom with fade
    show BBW neutral
    BBW "This is not the desired outcome, Hotsure-san, but you did mitigate any potentially worse results."
    BBW "I compliment you on your unorthodox solution."
    show BBW happy
    BBW "You still have the package, yes?"
    MC "It’s in my backpack."
    BBW "Then all is not lost. After classes today you can try again."
    show BBW neutral
    BBW "I don’t know if Fukushi-san belongs to any teams or clubs, but I would suggest waiting until after the dinner hour."
    BBW "You are more likely to find her in her dorm then."
    scene black with fade
    "She wasn’t wrong. After dinner I went back to the women’s dorm and found Fukushi there."
    "The delivery was made, and I apologized for the less-than-prompt service."
    "Not the smoothest operation, but I avoided complete disaster."
    "Still, it was an instructive taste of what I could expect going forward."
    jump daymenu

label BBW015_c3_2:
    "I couldn’t hide the slip, but I didn’t have to just hand it over."
    MC "This is a private note, meant for one particular individual."
    AE "Which individual? Perhaps I can pass it on for you?"
    MC "Sorry, but that’s private."
    AE "…"
    "I could sense she wanted to ask more questions. Maybe some sixth sense was telling her I was up to no good."
    "But as nosy as she was, there was no rule (as far as I knew) granting the student council search and seizure rights."
    "That is what I was gambling on, and sure enough..."
    AE "Very well. But keep your visit here brief."
    AE "I wouldn’t to hear of any infractions on your behalf... understand?"
    MC "Yes, ma’am."
    scene black with fade
    "I found Fukushi’s room, with her still in it. I gave her the package, thanked her for using our service, and left."
    "Alice was more than pleased with how I handled myself."
    scene Classroom with fade
    show BBW happy
    $setAffection("BBW", 1)
    BBW "Brilliantly done, Keisuke."
    "Maybe more pleased than was justified, but I wasn’t going to complain. It felt good to have done a job well."
    show BBW neutral
    BBW "You will have to be more cautious going forward, though. Spending too much time at the women’s dorm will draw attention."
    BBW "That’s a problem to consider before our business grows too much. But we can deal with it tomorrow."
    show BBW happy
    BBW "In the meantime, you’ve earned yourself a snack."
    BBW "Go enjoy the rest of your day."
    "I hung around for a moment, wondering if she was going to give me a couple yen to get myself a treat."
    "But no. She just kept smiling, then jerked her head to dismiss me."
    jump daymenu

label BBW015_c3_3:
    "I couldn’t think of a lie that Shiori wouldn’t see right through, so I pulled the slip back out of my pocket and held it out."
    MC "Here."
    MC "It’s a sales slip. I have a delivery to make for Alice…"
    AE "...Well, I’d like to commend you for your honesty. I’m glad you have the sense for basic decency."
    MC "O-oh?"
    show AE angry
    AE "Unfortunately, the fact that you went behind my back to do this makes that wholly irrelevant!"
    "Of course."
    scene black with fade
    "I mostly tuned out Shiori’s mini-tirade, already fearing what Alice was going to say."
    "At least Shiori could direct her anger elsewhere. Alice..."
    scene Hallway with fade
    show BBW angry
    BBW "Hotsure-san! Explain yourself!"
    MC "I got caught."
    BBW "You laid down and died! You didn’t even try to avoid discovery."
    MC "I’m not a natural liar. I’m sorry."
    BBW "Who said anything about lying?"
    BBW "Don’t you know how to massage the truth? When she asked what the slip was, you should have said ‘It is a private matter between me and someone else.’"
    BBW "Being student council president does not entitle her to intrude on our private affairs."
    MC "It’s still lying by omission, isn’t it?"
    BBW "Grrrrrrr!"
    BBW "Do you even want this job?"
    "I thought about it for a few seconds, weighing the promise of spending money against the idea of getting in trouble."
    MC "I’m not sure."
    BBW "You think on it. And I’ll be thinking of whether you deserve this opportunity."
    "She didn’t so much as look in my direction for the rest of the day."
    jump daymenu

label BBW015_c1_2:
    scene Dorm Exterior with fade
    "It would mean taking more time, but this seemed like a good time for the less obvious path."
    "After all, everyone leaving the dorms was heading to the cafeteria, going out the front entrance. Nobody would notice me coming in from the back door and heading right for the stairs."
    "I took the stairs two at a time, doublechecking the room number."
    "When I got to the third floor I peeked through the door. The coast looked clear."
    "It wasn’t."
    show AE neutral with dissolve
    AE "Hotsure-san? What are you doing here?"
    "Her eyes flicked down to the mailing envelope. I had to think of something, quick."
    if getAffection("AE") >= 10:
        jump BBW015_test_pass 
    if getAffection("AE") >= 4:
        jump BBW015_test_semipass
    jump BBW015_test_fail

label BBW015_test_pass:
    MC "There was a mailing mix-up. Somebody’s order got sent to my room."
    MC "They must have put ‘Men’s dorm’ on the address, not ‘Women’s.’"
    AE "A mailing mix-up?"
    "Shiori-san looked back at the envelope, but then back at me; her eyes showing confusion and possible disappointment. Closing her eyes and exhaling deeply, she looked back to me."
    AE "I understand. I’ll have to rectify that from happening again. I...won’t keep you."
    show AE happy
    AE "But be sure to be quick. You need to make sure to get breakfast before class."
    hide AE with dissolve
    scene black with fade
    "I nodded and walked past her, only mildly guilty about lying like that."
    "Later, Alice complimented me about the job."
    scene Classroom with fade
    show BBW happy
    BBW "A satisfying first mission. And you even managed to give Matsumoto-san the slip."
    BBW "Well done. Just be sure to stay on your toes next time as well."
    "The quiet reservations I still had about this entire technically illicit affair were further quieted when Alice smiled at me and gave that encouraging note."
    "I knew this was strictly a business arrangement, but there was still something nice about having her approval."
    jump daymenu

label BBW015_test_semipass:
    MC "There was a mailing mix-up. Somebody’s order got sent to my room."
    MC "They must have put ‘Men’s dorm’ on the address, not ‘Women’s.’"
    AE "That makes no sense. There’s not a single female student with the name “Keisuke Hotsure”."
    MC "Y-yeah, well…"
    "Busted."
    "Shiori-san crossed her arms expectantly, showing deep frustration."
    show AE angry
    AE "Look, I’m willing to trust that you’re doing as you say."
    AE "Do *not* make that trust ill-founded."
    show AE neutral
    AE "Go ahead and take the item to the rightful owner. And then please leave."
    AE "The residents here need to prepare for the day, and I don’t want your presence to be distracting."
    MC "Got it."
    scene black with fade
    "I nodded and walked past her, not really feeling guilty about lying like that."
    "Later, Alice complimented me about the job."
    scene Classroom with fade
    show BBW happy
    BBW "A satisfying first mission. And you even managed to give Matsumoto-san the slip."
    BBW "Well done. Just be sure to stay on your toes next time as well."
    "The quiet reservations I still had about this entire technically illicit affair were further quieted when Alice smiled at me and gave that encouraging note."
    "Her approval was nice, but at the same time I had Shiori’s disapproving expression stuck in the back of my mind."
    "I couldn’t see a way to keep both ladies happy, but maybe there was a way to not let one down?"
    jump daymenu

label BBW015_test_fail:
    "I tried to think of a plausible lie, but Shiori’s gaze was practically stabbing me. So intense, I almost wanted to confess right then and there."
    MC "I... was coming to return a manga I borrowed from Mizutani-san."
    AE "I see. And what is in that envelope?"
    MC "It’s just..."
    "She held out a hand."
    AE "Let me see it."
    "I did as instructed. She pulled the panties out, an eyebrow arching as she realized what they were."
    "Fortunately I had the sales slip in my hand, and she didn’t look at the label on the envelope. Either of those could have given up the game."
    AE "These are... yours?"
    MC "Don’t judge."
    "She stared at me for a bit, then silently put the panties back in the envelope and handed it back."
    AE "Mizutani-san does not live on this floor. She’s one floor down."
    AE "Return her manga and please leave the dorm. The ladies here need to get ready for the day."
    MC "Roger."
    scene black with fade
    "I went to the staircase and went down one flight, but I stayed in the stairwell."
    "After a few minutes I went back up to the third and checked the hall again. Shiori was gone."
    "And I hadn’t missed Fukushi. I made the delivery and got out of the building."
    "Alice was amused at my cover story, but she was more taken with my commitment to getting the job done."
    scene Classroom with fade
    show BBW happy
    $setAffection("BBW", 1)
    BBW "It’s not the most airtight story you could have come up with, but you did good, Keisuke."
    MC "Yeah, I’ve already thought of how I could have handled that in a much less embarrassing way."
    MC "At least I can trust Matsumoto-san to be one of the most tight-lipped people here. Anyone else..."
    "I had a sudden flash of Honoka seeing me with a pair of women’s underwear. My blood ran icy."
    BBW "Don’t be too hard on yourself. Most others would have crumbled under her stare."
    BBW "Just be more careful next time. Better to not find yourself in that position at all."
    jump daymenu

label BBW015_c1_3:
    scene Nurse Office with fade
    "It took all of five seconds to realize this was the wrong decision."
    "To avoid detection I had gone into the men’s room, waited until it was empty, and then tried to crawl into the ventilation system."
    "Thus when I got stuck nobody was around to see me, or hear me."
    "Almost an hour passed, me half in and half out of the vent, before someone came in to pee. Another twenty minutes were gone before I pulled out."
    "I got banged up and scraped. My clothes took most of the damage, but I still had plenty of scratches to get treated."
    show AE angry with dissolve
    $setAffection("AE", -1)
    "And of course the student council president had heard of my little escapade. In trying to avoid running into her I had ended up alone in the nurse’s office as she chewed me out."
    "As she chewed me out and I ‘Uh-huh’ed every now and then I thought to myself ‘I have to learn how Daichi does this.’"
    hide AE with dissolve
    "Surprisingly, things got a little better when Alice showed up."
    show BBW neutral with dissolve
    BBW "Were you hurt too bad?"
    MC "I’ll live."
    BBW "Good."
    show BBW angry
    BBW "Idiot! What kind of stunt was that?"
    MC "I thought it would be the easiest way to avoid detection."
    show BBW neutral
    BBW "You might as well have climbed to the roof and rappelled down to her room."
    BBW "Do you still have the package?"
    MC "It’s in my backpack still."
    BBW "Very well. When you are able you can still finish the job."
    BBW "This is not an auspicious start to your career, but I suppose I cannot fault you for your enthusiasm."
    BBW "Just learn to balance it with some common sense."
    jump daymenu
    
label BBW016:
    scene Dorm Interior with fade
    "Classes were done, my homework was done, and even though I had wandered around the school for over an hour, I hadn’t found anything to do."
    "No one to talk to, nobody that needed help with anything. I was left to myself."
    "So I came back to the dorm. Daichi was out - fortunately - so I had a nice quiet room to relax in."
    "I had broken out my laptop and was refamiliarizing myself with Titans of Eververse when my phone buzzed."
    MC "?"
    "It wasn’t a call, though. It was a text."
    "I couldn’t remember the last time someone had ever texted me, much less the last time I had sent one."
    BBWCell "<Hello, Keisuke. This is Alice. How are you?>"
    "I spent a few seconds staring at the message, confused. What did she want? Why was she texting me?"
    "Then I realized she might not want anything. Didn’t Americans text each other all the time?"
    "But was Alice the sort to make small talk just because? She usually had something on her mind."
    "And here I had gotten comfortable and was having fun with my game."
    menu:
        "Text back you’re up to nothing special.":
            jump BBW016_c1_1
        "Text back asking if she wants something.":
            jump BBW016_c1_2
        "Text back you’re in the middle of something and can’t talk.": #(-1 affection point)
            jump BBW016_c1_3

label BBW016_c1_1:
    Cell "<I’m good. Just having a quiet afternoon to myself.>"
    "I unpaused the game - good thing I was between fights - when I heard another beep from my phone."
    MCT "That was fast."
    MCT "Or direct, I should say. Fitting."
    BBWCell "<I am currently idle as well. Kodoma-san is working on a new recipe for me to try, and at my insistence she is taking her time to make sure it is perfect. Thus, I am waiting later than usual for my afternoon tea and as I have completed my homework and studies I am looking for something else to occupy my time.>"
    "I wasn’t sure how to feel that she hoping I could keep her entertained, but this did imply she wasn’t contacting me with a new delivery assignment."
    "Right?"
    jump BBW016_c1_after

label BBW016_c1_2:
    Cell "<Was there something specific you wanted to talk to me about?>"
    "Her response was immediate."
    BBWCell "<No, no. This is just friendly small talk.>"
    BBWCell "<I find myself idle as I wait for Kodoma-san to finish working on a new recipe.>"
    jump BBW016_c1_after

label BBW016_c1_after:
    Cell "<Oh. I thought you had another delivery for me to make or something.>"
    "Again, she responded right away."
    "Looked like I wasn’t going to make it to the next dungeon anytime soon…"
    BBWCell "<Again, no. Our company is still in its infancy, building a customer base and waiting for word of mouth and customer satisfaction to rise.>"
    BBWCell "<I am not interrupting anything, am I?>"
    menu:
        "Not really.":
            jump BBW016_c2_1
        "Well, actually...":
            jump BBW016_c1_3

label BBW016_c2_1:
    Cell "<Not really. I was just doing some level-grinding.>"
    "I turned my player character back around and headed back to the village."
    "When my phone beeped again I kept one hand on my mouse and used the other read her response."
    BBWCell "<I am not familiar with that term. What does it mean?>"
    Cell "<Video game speak. I’m trying to make my character more powerful.>"
    BBWCell "<That explains my ignorance. I have never been one for frivolities such as that.>"
    Cell "<There’s nothing wrong with video games.>"
    BBWCell "<Perhaps not, but there are always better uses of your time.>"
    Cell "<That’s subjective. If I’m having fun, if it helps me relax, that’s good enough for me.>"
    Cell "<I’m thinking of maybe joining the computer club. I hear they spend most of their time playing MMORPGs.>"
    BBWCell "<Tsk.-"
    "Yes, she actually wrote out ‘Tsk’ in a text."
    BBWCell "<Tsk. When there are other, more enriching art forms available to you, you choose to wallow in crude power fantasies.>"
    "I didn’t want to get into an argument over the merits of video games, but when I saw a flaw in her argument I felt I had to press."
    Cell "<If you’ve never played video games, then you can’t really criticize them, can you?>"
    "That bought me all of a couple seconds. Maybe I had stunned her."
    BBWCell "<I have seen what those games are like.>"
    BBWCell "<Either a cartoonish mascot jumping from one cliff to another, hopping onto creatures that get in his way.>"
    BBWCell "<Or an orgy of ultraviolence that allows the disturbed to play out their grotesque fantasies.>"
    "Now I was getting a little peeved."
    Cell "<I wouldn’t have pegged you as a moral prude, Alice.>"
    Cell "<Not that I want to start an argument, but there are far more types of videos than just platformers and shoot ‘em ups.>"
    jump BBW016_c3
    
label BBW016_c3:
    menu:
        "Like fighting games." if not getFlag("BBW016_c3_1"):
            jump BBW016_c3_1
        "Like fighting games. (disabled)" if getFlag("BBW016_c3_1"):
            pass
        "Like dating sims." if not getFlag("BBW016_c3_2"):
            jump BBW016_c3_2
        "Like dating sims. (disabled)" if getFlag("BBW016_c3_2"):
            pass
        "Like simulator games.": #(opens up BBW018)
            jump BBW016_c3_3

label BBW016_c3_1:
    $setFlag("BBW016_c3_1")
    "I started to write ‘Like fighting games,’ before realizing I wasn’t doing myself any favors with that."
    if getFlag("BBW016_c3_2"):
        BBWCell "<Such as…?>"
        "I gritted my teeth, trying to think of an example that would blow away her contempt in one move."
    jump BBW016_c3

label BBW016_c3_2:
    $setFlag("BBW016_c3_2")
    "I started to write ‘Like dating sims,’ and stopped right before I sent it off."
    "If she didn’t know what dating sims are, I’d have to explain it. And if she did know, I’d have to explain why that was the genre I went to."
    "I didn’t relish the thought of having to defend dating sims to a female classmate."
    if getFlag("BBW016_c3_1"):
        BBWCell "<Such as…?>"
        "I gritted my teeth, trying to think of an example that would blow away her contempt in one move."
    jump BBW016_c3

label BBW016_c3_3:
    $setFlag("BBW016_unlock")
    Cell "<Like simulator games.>"
    "Another pause of a couple seconds followed."
    BBWCell "<Explain. Please.>"
    Cell "<It’s right there in the name. They’re games that simulate something, like farming or flying an airplane.>"
    Cell "<A lot of them are simple by design, a way to unwind by doing something repetitive.>"
    "I started typing ‘I’m not really into them,’ but then inspiration hit."
    "My lips curling up in a smile, I deleted what I had typed and then wrote"
    Cell "<The more complex ones have you running a city or a business.>"
    "I hit send, and waited."
    "This time it took almost ten seconds for her to respond. I had enough time to enter the inn and save my game."
    BBWCell "<There are business video games?>"
    Cell "<Yep.>"
    Cell "<Though not like regular businesses where you create a product and sell it.>"
    Cell "<The bigger titles revolve around more exciting things like amusement parks or zoos.>"
    BBWCell "<How do they work?>"
    "Cue victory fanfare."
    play sound "Audio/Victory.ogg"
    pause 3
    Cell "<You’re put in charge of a business that’s starting out or is struggling, and your job is to make it profitable.>"
    Cell "<You create rides or buy animals, set ticket prices, add concession stands or whatever.>"
    "Another pause."
    BBWCell "<Do you have any of those types of games?>"
    Cell "<I don’t, but I can find one or two.>"
    Cell "<Interested in trying them?>"
    BBWCell "<I suppose I owe it to myself to sample all forms of art, so that I may make a more discerning judgement.>"
    BBWCell "<It is more impressive to appreciate the interplay of light and shadow in a Raphael than to master some violent spectacle.>"
    BBWCell "<But you were right: I cannot judge unless I have experienced it for myself.>"
    Cell "<I’ll look into finding some business management simulators.>"
    BBWCell "<Money is no object. I can reimburse you.>"
    BBWCell "<It looks like Kodoma-san is ready to serve the dish, so I will take my leave.>"
    "I sent a final message - Enjoy - and put my phone down."
    "I was free to return to Titans of Eververse, but the thought of getting Alice into gaming, even if it was the ‘Zoo Manager’ variety I’m not interested in."
    "So I went to my usual PC gaming storepage and started looking through the business management titles."
    jump daymenu

label BBW016_c1_3:
    Cell "<Well actually, I was in the middle of a dungeon crawl. Can I talk to you later?>"
    "This time she actually took a moment to respond."
    $setAffection("BBW", -1)
    BBWCell "<Oh. Well I would not want to interrupt whatever childish game you’re engaged in.>"
    BBWCell "<Your time is too precious to spend engaged in actual human interaction, I see.>"
    "And that was the last text she sent me."
    "For my part I tried to diplomatically explain I could talk later, but all I got was silence in return."
    "I had a pretty good feeling she wouldn’t hide her irritation the next time we met. I just hoped she didn’t carry it too long."
    jump daymenu
    
label BBW017:
    "I was feeling peckish after class, so I went to the cafeteria looking for something a bit more filling than a candy bar."
    "A bowl of ice cream called out to me, but it did mean I had to stay in the cafeteria as I ate it."
    "No sooner had I gotten comfortable than Alice huffed her way into the dining area."
    "Her anger was almost palpable. Not in her expression so much as this aura emanating off her."
    "Not a hornet’s nest I would want to smack, but the cafeteria was mostly empty and so she noticed me almost instantly."
    show BBW angry with dissolve
    BBW "Hotsure-san! What do you know of this?"
    "She thrust a piece of paper at me. It was a list of some sort. I took it and read it over."
    MC "It looks like all the girls in our class."
    BBW "Ranked by preference."
    BBW "Some boy or boys have judged all the women in our class and ranked them according to order of attractiveness."
    MC "Is that what this is?"
    MCT "(That’s pretty skeevy, but I can’t say I’m surprised. Stuff like that happened at my old school, too.)"
    MCT "(I can see why she’s upset. We’re all here because of some physical abnormality, and now here’s some jerk objectifying all the girls-)"
    BBW "Why am I number 13?"
    MC "Th-That’s what you’re angry about?"
    BBW "Of course."
    show BBW neutral
    BBW "I have no reason to fear being judged for my beauty, but I have not decided if placing me so low is malicious or ignorant."
    MC "Wait, how are you at 13? There’s less than 10 girls in our class."
    show BBW angry
    BBW "They included women from other classes."
    BBW "But that is not the worst part. Look at the top of the list."
    MC "Matsumoto… Shiori’s number one?"
    BBW "Madame President herself is at the top of the rankings. I want you to explain that to me."
    MC "You think I had something to do with this? Because I didn’t."
    show BBW neutral
    BBW "But you are a man, yes? You should have some insight into the thought process."
    BBW "Do you think Matsumoto-san is more attractive than me?"
    MCT "So I’m being put on the spot. Because I’m the one who was here? This is not the first time you’ve betrayed me, ice cream."
    menu:
        "Yes.": #-2 aff
            jump BBW017_c1
        "No.": #
            jump BBW017_c2
        "Square the circle.": #-1 aff
            jump BBW017_c3

label BBW017_c1:
    MC "If you must ask… Yes."
    show BBW angry
    BBW "…"
    MC "It’s all subjective, right?"
    $setAffection("BBW", -2)
    BBW "You’re honest, at least."
    BBW "That will serve you well. Stupidity and deception are a terrible combination."
    "And that was her final word."
    jump daymenu

label BBW017_c2:
    if getAffection("BBW") >= getAffection("AE"):
        $setFlag("BBW017_testpass")
        MC "If you must ask… No."
        BBW "Go on…"
        MC "Go on? It’s all subjective, isn’t it?"
        BBW "Yes and no. Any culture has an established ideal of beauty. You’re right to say I’m more attractive than Matsumoto-san, but this list indicates you’re the exception."
        BBW "Why is that?"
        "I considered sweet-talking her, but something told me she wasn’t going to have any of that."
        MC "Well, it might not be physical."
        MC "Personality-wise, you are kind of abrasive."
        "She didn’t say anything for a moment, but I could see her thinking over what I just said."
        BBW "Let’s say you’re right (though I’m not admitting to being unduly proud). How does that explain Matsumoto’s popularity?"
        BBW "She goes out of her way to push people away. It’s as if she wants to be despised."
        MC "I think you might be overstating it, but you’re not entirely wrong. She has the ‘tsun’ part of the tsundere type going for her."
        MC "It’s a paradox. The more you can’t have something, the more you want it."
        MC "And with someone like Matsumoto-san there’s the fantasy that if you can pierce her icy exterior you can find the sweet center and she’ll reciprocate your feelings."
        MC "You… You’re seen more as a stuck-up rich girl. People aren’t going to be interested in getting to know you if they think that’s all there is."
        "She stayed silent a while, her irritated mood melting."
        BBW "And do you think that’s all I am? A stuck-up rich girl?"
        MC "I think there’s more to you than your money. You have an interest in music, right?"
        show BBW haughty
        BBW "I am cultured, yes."
        MC "Right. Just don’t be so elitist about it and you can probably find some other people with the same interest."
        show BBW neutral
        BBW "Elitist? Whatever do you mean?"
        MC "You were butting heads with the music club president after just a couple days, remember?"
        show BBW haughty
        BBW "Is it elitist to let others know when their standards are below acceptable?"
        MC "Yes! Yes, that’s the very definition of ‘elitist!’"
        show BBW angry
        BBW "!"
        "She looked like she was about to snap, but then quickly relaxed, exhaling slowly."
        show BBW neutral
        BBW "Boys like it when someone like Matsumoto-san orders them around, because they harbor this fantasy that they can win her over. But they don’t like it when someone like me chastises them for their shortcomings."
        BBW "It’s all about having this illusion of control, isn’t it? Some people just can’t accept not being in charge of everything."
        BBW "Boys like to play pretend, after all."
        "A response so obvious, but it had to be held back."
        MC "Not all guys are like that, you know."
        show BBW happy
        BBW "Oh, I know. I’m not lumping you in with the children who concocted this list."
        BBW "You are man enough to admit your own feelings, and reasonable in your tastes."
        show BBW neutral
        BBW "I’m not sure if you’re mature enough to follow your own path, but we shall see…"
        show BBW happy
        BBW "Enjoy your ice cream."
        hide BBW with dissolve
        "She walked off in a much better mood than when she had shown up, but I didn’t think it was so simple as her being complimented by my saying I found her more attractive than Shiori."
        "Something else was on her mind, but I didn’t stop to consider what it might have been."
        "You can say she was right about me not being mature enough, if you want, but when the conversation was over my impulse was to get on with my life as if nothing had happened."
        jump daymenu
    else:
        MC "If you must ask… No."
        BBW "..."
        show BBW angry
        BBW "You’re a terrible liar."
        MC "I- Wha?"
        show BBW neutral
        BBW "I’ve seen you and Matsumoto-san. You’re rather close, the two of you."
        MC "No, we’re… We’re friendly, but it’s not like we’re dating."
        show BBW haughty
        BBW "I understand human behavior, Hotsure-san. It’s a necessary trait for anyone looking to enter the jungle of free enterprise."
        BBW "You can’t hide what you’re feeling whenever you’re chatting with the Ice Queen. Maybe she can’t figure it out, maybe you’re too timid to take the leap, but I know."
        show BBW angry
        BBW "So don’t EVER try to sweet talk me like that again."
        MC "Okay. Okay. I guess I do find Shi- Matsumoto-san a bit more attractive than you. A bit."
        MC "But it’s not like I would put you at 13 or anything that low."
        "Alice’s expression softened a bit, her stony exterior melting into something a little less severe."
        show BBW neutral
        BBW "Of course you wouldn’t. Nobody with sense would."
        show BBW angry
        BBW "But I still need to find whatever cretin made this list."
        show BBW neutral
        BBW "Hotsure-san."
        hide BBW with dissolve
        "And she walked off."
        jump daymenu

label BBW017_c3:
    MC "Well... it’s all relative. Beauty is in the eye of the beholder and all that."
    MC "I mean, when you say ‘attractive’ are you talking about pure physical beauty, and do we then go off of classical standards of what a given culture considered ideal?"
    MC "For that matter, how do you compare two different objects that are both, in their own ways, beautiful? A landscape and a portrait differ in their subject matter, but they each have their own criteria for what is beautiful or not."
    show BBW angry
    MC "So while you have your own unique air and… gravitas, someone like Shiori has an equally distinct but undeniably different bearing. Who is to say which is ‘right’ or ‘more attractive?’"
    "As I rambled I could see Alice’s expression darkening. This wasn’t working."
    $setAffection("BBW", -1)
    BBW "Stop. Just stop."
    MC "..."
    BBW "I don’t know what’s going on inside your head, but I have no tolerance for weakness."
    BBW "And however I may feel about Madame President, I don’t think she’s the sort to take pity on a wishy-washy… toad."
    BBW "Figure out what you want and grow the requisite spine to go after it. Playing the middle isn’t going to get you anywhere."
    "And our conversation ended there."
    jump daymenu
    
label BBW020:
    scene Cafeteria with fade
    "I had gotten to the cafeteria earlier than most of the other students, but after the rush had come and gone I was still there."
    "See, I’d brought a book with me to read while I ate, and it turned out to be more engrossing than I expected. ‘I’ll just finish this chapter,’ I told myself, even after my plate was clean."
    "When I found a good place to stop I looked up to find most of the cafeteria empty. Just a few stragglers or members of sports teams coming off practice."
    UNKNOWN "Hotsure-san."
    "I was initially annoyed to have the quiet of the place broken, but when I realized who it was I relaxed a little."
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "Enjoying your dinner? Or it looks like you’ve already finished."
    MC "Yeah. I was just reading."
    BBW "That’s good. Feed the mind as well as the body."
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    "As Aida arrived, pushing a cart with a covered tray on top, Alice took the seat opposite me. She let Aida set her place for her, eager to see what she would be having."
    BBW "Stir-fried vegetables and beef, with mushroom soup. It looks delicious, Kodoma-san."
    PRG "Th-Thank you."
    BBW "We should see about going into town this weekend, pick up some seasonal fruits. Summer will be here soon, and I do so enjoy watermelon and strawberries."
    "She was surprisingly happy, considering the last time we had talked had been about that list."
    MC "You’re in a good mood. Did something happen?"
    BBW "My probation with the music club has come to an end."
    show BBW neutral
    BBW "I am still not satisfied with the club’s guiding hand, but I recognize that further instigation will only take me further from my desires."
    BBW "So I will hold my tongue and restrict myself to the role given to me."
    BBW "It is to the club’s detriment, but sometimes a flawed leader needs to be given the rope to hang themselves."
    MC "That’s a bit heavy."
    MCT "Wrong choice of words, man."
    "But Alice didn’t seem to care, she was already enjoying her meal."
    MC "Is that why you’re having a late dinner? Club meeting?"
    show BBW happy
    BBW "That, and I found resolution to the… matter we were talking about yesterday."
    MC "Oh? Did you find out who it was?"
    show BBW neutral
    BBW "Found and confronted them."
    MC "What… What did you do?"
    "She shrugged, as if the entire matter was behind her."
    BBW "I didn’t have to do much of anything. The child behind the list is even more pathetic than I expected."
    BBW "So pathetic I didn’t have it in me to bring my full wrath down on him."
    BBW "I will simply say that his presence at this school is possibly more tragic than anyone else’s. To tear him down more than he must already be would be cruel."
    show BBW angry
    BBW "However, he does understand - in no uncertain terms - that if he continues with this behavior I will identify him to every other woman on the list."
    BBW "Let those less forgiving than me punish him."
    MCT "Yikes. It says something she thinks threatening to out someone is ‘forgiving.’"
    MCT "Can’t blame her for being angry, though."
    MC "Did he explain why he ranked you so low, or did you not ask?"
    show BBW neutral
    BBW "He said I am too ‘plump’ for his tastes."
    BBW "He specifically cited my belly fat, after I asked him about Matsumoto-san’s ‘plump’ rear."
    BBW "I understand that certain body parts are more appealing to men than others, but this did confirm my assumption that this was a purely superficial exercise."
    BBW "Were I in Matsumoto-san’s place I would be deeply offended if I was seen as a rear with a woman attached."
    MC "I’m not surprised it was about looks, but he didn’t say anything about her ‘strong’ bearing?"
    BBW "By ‘strong’ do you mean ‘stiff?’"
    BBW "No, he didn’t say anything about personality. I got no sense he has looked past any of our bodies."
    MC "So he just doesn’t like ‘plump’ women."
    menu:
        "His loss. Beauty can come in all sizes.":
            jump BBW020_c1
        "To each his own, I guess.":
            jump BBW020_c2

label BBW020_c1:
    MC "His loss. Beauty can come in all sizes."
    "Alice smiled wryly, almost rolling her eyes."
    BBW "That’s a bit platitudinal for my tastes, Hotsure-san."
    BBW "And while I appreciate the gesture, I do not need the affirmation."
    MC "I’m just saying there is no single definition of attractiveness. Different people look good in different ways."
    BBW "That is all subjective. ‘Beauty’ is a label given by the observer, not claimed by the subject."
    BBW "Some men may find a stout woman pleasing to the eye and the touch, but it is a niche taste."
    MC "So you’re worried about your weight. You think you won’t look good anymore if you get fatter?"
    show BBW angry
    BBW "!"
    show BBW neutral
    BBW "(Sigh)"
    BBW "I have already accepted my condition, and I’m prepared to deal with it if it becomes a genuine issue."
    BBW "Whatever fears may have been planted by my diagnosis will not be acknowledged. We don’t deal with what might be wrong, but what can go wrong or is going wrong."
    BBW "I am not worried about my weight."
    "I didn’t really believe her."
    "Maybe she wasn’t concerned about her weight in a vacuous ‘Oh no, I gained a couple pounds’ sense, but there was something bothering her."
    BBW "Question."
    MC "Yes?"
    BBW "You said ‘anymore.’ That I ‘won’t look good anymore’ if I get fat."
    MC "Yeah… You are pretty."
    show BBW haughty
    BBW "I know I am."
    MCT "That was fast."
    show BBW neutral
    BBW "But would I still be pretty if I was fat?"
    MC "You want to know if I like fat women?"
    BBW "I just want to know what your agenda is."
    show BBW haughty
    BBW "Obviously our current relationship as employer/employee would make dating problematic, but I am curious."
    "There was something confrontational about how she asked this. But also something… vulnerable? Like she was a little too eager."
    "I don’t know why I felt like I had to hide anything here. Maybe it was just how Alice was so bold that I had to go in the opposite direction."
    MC "You said you are not bothered by your weight. So I take it that you’re not looking for a compliment."
    show BBW neutral
    BBW "It’s not about me. It’s all about you, and your preferences."
    MC "Yes."
    MC "So speaking of what I like in general terms, with no comments about certain individuals, I will say that…"
    MC "I do, in fact, find something… enticing about larger women."
    BBW "Go on…"
    MC "Soft things are inviting. Pillows, sofas, plush jackets. They feel nice, they’re relaxing."
    show BBW happy
    BBW "You want to lie down on a fat woman?"
    "I coughed, my mind going straight to the lewdest possible vision, and the way Alice chuckled after a beat I could tell she had surprised herself."
    BBW "That tells me more than you just said, actually."
    "It was more than I wanted to say, definitely."
    "But it was also more than I expected. I’ve never thought about being with a… a fat woman, but thinking about it now I could see the attraction."
    "I quickly got things back on track."
    MC "There are beautiful women who are larger than normal, to answer your original question."
    MC "As for physical desire…"
    show BBW neutral
    BBW "You do not need to paint any pictures."
    show BBW happy
    BBW "I could simply invoke the stereotype that men are never discerning about where they… Ahem …"
    MC "Hang the bird feeder in the garden?"
    show BBW neutral
    BBW "… What?"
    MC "I don’t know. I couldn’t think of a euphemism that didn’t sound dirty."
    show BBW happy
    BBW "I think they’re supposed to. Just not too dirty."
    "She ate the last bit of stir fry, daintily wiped her mouth, and pushed her chair back from the table."
    BBW "That was an excellent meal, and the conversation was… interesting."
    BBW "Hotsure-san, I’ll leave you to your book."
    BBW "See you in class tomorrow."
    MC "Yeah. See you."
    hide BBW with dissolve
    "Even after she was gone and Aida had cleaned up the dishes and silverware, my thoughts kept coming back to Alice."
    "I had been invited to consider her body, so it’s not like I was a pervert or anything. But now that the idea of being with a large woman was in my mind, I didn’t find myself trying to get it out."
    jump daymenu

label BBW020_c2:
    MC "To each his own, I guess."
    "Alice chewed a mouthful of stir fry, thinking."
    show BBW neutral
    BBW "Overweight women aren’t that common in Japan, in my experience."
    BBW "America is different. Too much bad junk food, restaurants giving bigger and bigger portions for better value."
    BBW "It’s not that being overweight is seen as attractive, but it is unremarkable to see a heavyset man or woman in a relationship."
    MC "I suppose. I’ve never been outside the country."
    BBW "…"
    "Something was on her mind, and I thought I knew what it was, but I didn’t want to press things."
    "After the business with the list she must have been sensitive about her appearance, and I wasn’t the one who could build her up without sounding like a bad self-help guru."
    "The longer the silence went on the more pressure I felt. Alice was eating, so she had an excuse not to say anything. And besides, it just felt like she was waiting for me to break through whatever wall was being set up."
    MC "Well… I should probably get back to my room. I’ve still got that history reading to do."
    "Alice nodded, not looking up at me, and I felt tense every step of the way out of the cafeteria."
    scene black with fade
    "Something was supposed to have happened there. I could feel it."
    "And I’d blown it."
    jump daymenu