# Define grammars from characters
init -1 python:
    from renpy_tracery import TraceryCharacter
    from renpy_tracery import Grammar
    import story_utils
    import random
    from story_character import StoryCharacter
  
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

    characterList = []


# Define Tracery characters
define player = TraceryCharacter("You", grammar=narrator_grammar)
define narrator = TraceryCharacter(None, grammar=narrator_grammar)



# The game starts here.

label start:
    
    python:
        place=random.choice(places)
        startPlaceImage = "background/"+place+".jpg"
        backgroundStartImg = im.Scale(startPlaceImage, 1280, 720)
        renpy.music.play("audio/background/"+place+".ogg", loop=True)

    
    $ startPlaceImageRpy = startPlaceImage
    $ results = story_utils.generateInitialDescription(place)
    
    scene expression backgroundStartImg
    while results:
        $ result = results.pop(0)
        "[result]"

    jump choice 

label choice:

    $ action1 = random.choice(actions)
    $ action2 = random.choice(actions)

    python:
        odds=random.randint(0,9)
        win = (odds==9)
        lose = (odds==0)

    $ action1_char =  story_utils.generatePerson(place)
    $ action1_loc = story_utils.generateLocation(place)
    $ action2_char = story_utils.generatePerson(place)
    while action2_char == action1_char:
        $ action2_char = story_utils.generatePerson(place)
    $ action2_loc = story_utils.generateLocation(place)
    while action2_loc == action1_loc:
        $ action2_loc = story_utils.generateLocation(place)

    $ is_win = win
    $ is_lose = lose

    $ choice1 = story_utils.generateChoice(action1, action1_loc, action1_char)
    $ choice2 = story_utils.generateChoice(action2, action2_loc, action2_char)
    while choice2 == choice1:
        $ choice2 = story_utils.generateChoice(action2, action2_loc, action2_char)

    menu:
        "[choice1]":
            jump choice1
        
        "[choice2]":
            jump choice2



label choice1:
    if is_win:
        $ results = story_utils.generateWinResult(action1, action1_loc, action1_char)
    elif is_lose:
        $ results = story_utils.generateLoseResult(action1, action1_loc, action1_char)
    else:
        $ results = story_utils.generateActionResult(action1, action1_loc, action1_char)
    
    jump display_result


label choice2:
    if is_win:
        $ results = story_utils.generateWinResult(action2, action2_loc, action2_char)
    elif is_lose:
        $ results = story_utils.generateLoseResult(action2, action2_loc, action2_char)
    else:
        $ results = story_utils.generateActionResult(action2, action2_loc, action2_char)

    jump display_result
        

label display_result:
    
    python:
        characterList.append(StoryCharacter())

    while results:
        $ result = results.pop(0)
        if result.startswith("@PLAYER "):
            $ result = result.replace("@PLAYER ", "")
            player "[result]"
        elif result.startswith("@CHAR1 "):
            $ result = result.replace("@CHAR1 ", "")
            show expression characterList[-1].image 
            characterList[-1] "[result]"
        else:
            "[result]"

    hide expression characterList[-1].image 
    if is_win or is_lose:
        jump end
    else:
        jump choice


label end:

    "The End"
    return
