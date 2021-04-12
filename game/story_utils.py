
import renpy_tracery

characters = {
        'city': ["merchant", "barmaid", "priest", "musician"],
        'desert': ["hermit", "nomad", "merchant"]
        }
charactersGrammar =  renpy_tracery.Grammar(characters)

locations = {
        'city': ["church", "bar"],
        'desert': ["oasis", "great dune"]
        }
locationsGrammar =  renpy_tracery.Grammar(locations)

misc = {
        'timeUnit': ["minute", "hour", "day"],
        'movement': ["stroll", "wander around"],
        'chatSubject': ["the weather", "the local #localKnowledge#", "the whereabouts"],
        'localKnowledge': ["religion", "traditions", "cuisine", "legends"],
        'animal': ["rat", "elephant", "bird", "cat", "dog", "#ferociousAnimal#"],
        'ferociousAnimal': ["bear", "rabid dog", "eagle"],
        'fatigue': ["exhaustion", "hunger", "thirst", "despair"],
        'enemy': ["bandit", "#ferociousAnimal#", "soldier"],
        'lookFor': ["find", "look for", "try to find"],
		'discover': ["find", "encounter", "stumble upon", "discover"],
        'discuss': ["discuss", "chat", "have a chat", "converse"],
		'greetings': ["hi there", "hello", "hi", "hey"],
		'doYouKnow': ["do you know about", "have you heard about"],
		'interesting': ["interesting", "nice", "exciting", "pleasant"]
    }

def generateLocation(place):
    return locationsGrammar.flatten("#"+place+"#")

def generatePerson(place):
    return charactersGrammar.flatten("#"+place+"#")
    
def generateInitialDescription(place):
    init_grammar = {
        'origin': ["#<loc:"+place+">init#"],
        'init': ["You wake up in a #loc# you don't know.", "You've just arrived in this #loc#...|Time to explore!"]
    }
    init_grammar.update(misc)
    
    initGrammarObject = renpy_tracery.Grammar(init_grammar)
    initGrammarObject.add_modifiers(renpy_tracery.base_english)
    return initGrammarObject.flatten("#origin#").split("|")

def generateChoice(action,action_loc,action_char):
    choice_grammar = {
    'origin': ["#<char:"+action_char+"><loc:"+action_loc+">"+action+".capitalize#"],
            'move': ["#lookFor# a #loc#", "wander around"],
            'chat': ["#discuss# with random person", "#discuss# with #char.a#"],
            'observe' : ["look around", "take a look", "observe your surroundings"]
            }
    choice_grammar.update(misc)
       
    choiceGrammarObject = renpy_tracery.Grammar(choice_grammar)
    choiceGrammarObject.add_modifiers(renpy_tracery.base_english)
    return choiceGrammarObject.flatten("#origin#")

def generateActionResult(action,action_loc,action_char):
    action_result_grammar = {
        'origin': ["#<char:"+action_char+"><loc:"+action_loc+">"+action+"#"],
            'move': ["You #movement# for a few #timeUnit.s# before you #discover# a #loc#.", "After a few #timeUnit.s#, you encounter #char.a# who kindly shows you the way to the #loc#."],  
            'chat': ["@CHAR1 #greetings.capitalize#!|@PLAYER I'm new here... Do you know about anything #interesting# to do here?|@CHAR1 Hmm... #doYouKnow.capitalize# the #loc#? It's pretty #interesting# to visit.","You #discuss# with the #char# who teaches you about #chatSubject#.","You #discuss# with the #char# who tell you about #interesting.a# place to visit : the #loc#."],
            'observe' : ["You look around you and spot a few #animal.s#."]
            }
    action_result_grammar.update(misc)
       
    action_result_grammar_object = renpy_tracery.Grammar(action_result_grammar)
    action_result_grammar_object.add_modifiers(renpy_tracery.base_english)
    return action_result_grammar_object.flatten("#origin#").split("|")

def generateWinResult(action,action_loc,action_char):
    action_result_grammar = {
        'origin': ["#<char:"+action_char+"><loc:"+action_loc+">"+action+"#"],
            'move': ["You #discover# a #loc#. Finally a good place to rest!", "On the way to the #loc#, you encounter #char.a# who kindly show you the way. You instantly fall in love and marry a month after."],
            'chat': ["You are so entranced with your conversation with the #char# that you decide to join them in their adventure."],
            'observe' : ["You look around you and spot something special...|It's a treasure! You're in luck!"]
            }
    action_result_grammar.update(misc)
    
       
    action_result_grammar_object = renpy_tracery.Grammar(action_result_grammar)
    action_result_grammar_object.add_modifiers(renpy_tracery.base_english)
    return action_result_grammar_object.flatten("#origin#").split("|")

def generateLoseResult(action,action_loc,action_char):
    action_result_grammar = {
        'origin': ["#<char:"+action_char+"><loc:"+action_loc+">"+action+"#"],
            'move': ["You wander endlessy before you die of #fatigue#.", "On the way, you get attacked by #enemy.s# and die."],
            'chat': ["You don't know what you said wrong, but the #char# seems offended and stabs you to death."],
            'observe' : ["You look around you and spot a few #enemy.s#. They charge at you and you are soon dismembered."]
            }
    action_result_grammar.update(misc)
    
    action_result_grammar_object = renpy_tracery.Grammar(action_result_grammar)
    action_result_grammar_object.add_modifiers(renpy_tracery.base_english)
    return action_result_grammar_object.flatten("#origin#").split("|")


