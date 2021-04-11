# Define grammars from characters
init -1 python:
    from renpy_tracery import TraceryCharacter
    from renpy_tracery import Grammar
    import story_utils
    import random
  
    places= ['desert', 'city']
    actions =[ 'chat' , 'observe' , 'move' ]

    action1_char =''
    action2_char =''
    action1_loc =''
    action2_loc =''


    # Define Tracery grammar for narrator character.
    narrator_grammar = {
    }

    narratorGrammarObject = Grammar(narrator_grammar)


# Define Tracery characters
define e = TraceryCharacter("Eileen", grammar=narrator_grammar)
define narrator = TraceryCharacter(None, grammar=narrator_grammar)


# The game starts here.

label start:
    
    python:
        place=random.choice(places)
        startPlaceImage = "background/"+place+".jpg"
        backgroundStartImg = im.Scale(startPlaceImage, 1280, 720)

        renpy.music.play("audio/background/"+place+".ogg", loop=True)


    
    $ startPlaceImageRpy = startPlaceImage
    $ startPlace = place

    "You wake up in [startPlace]"
    scene expression backgroundStartImg


    jump choice

label choice:

    $ action1 = random.choice(actions)
    $ action2 = random.choice(actions)

    python:
        odds=random.randint(0,9)
        win = (odds==9)
        lose = (odds==0)

    $ action1_char =  story_utils.generatePerson(place)
    $ action2_char = story_utils.generatePerson(place)
    $ action1_loc = story_utils.generateLocation(place)
    $ action2_loc =  story_utils.generateLocation(place)
    $ is_win = win
    $ is_lose = lose


    $ choice1 = story_utils.generateChoice(action1, action1_loc, action1_char)
    $ choice2 = story_utils.generateChoice(action2, action2_loc, action2_char)

    menu:
        "[choice1]":
            jump choice1
        
        "[choice2]":
            jump choice2



label choice1:
    if is_win:
        $ result = story_utils.generateWinResult(action1, action1_loc, action1_char)
        "[result]"
        jump end
    elif is_lose:
         $ result = story_utils.generateLoseResult(action1, action1_loc, action1_char)
         "[result]"
         jump end
    else:
        $ result = story_utils.generateActionResult(action1, action1_loc, action1_char)
        "[result]"
        jump choice

label choice2:
    if is_win:
        $ result = story_utils.generateWinResult(action2, action2_loc, action2_char)
        "[result]"
        jump end
    elif is_lose:
         $ result = story_utils.generateLoseResult(action2, action2_loc, action2_char)
         "[result]"
         jump end
    else:
        $ result = story_utils.generateActionResult(action2, action2_loc, action2_char)
        "[result]"
        jump choice

label end:

    "The End"

    return
