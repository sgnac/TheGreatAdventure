
import renpy_tracery

characters = {
        'city': ["merchant", "barmaid"],
        'desert': ['hermit']
        }
charactersGrammar =  renpy_tracery.Grammar(characters)

locations = {
        'city': ["church"],
        'desert': ['oasis']
        }
locationsGrammar =  renpy_tracery.Grammar(locations)

misc = {
        'timeUnit': ["minute", "hour", "day"],
        'movement': ["stroll", "wander around"],
        'subject': ["the weather", "the local religion", "the whereabouts"],
        'animal': ["rat", "elephant", "bird"],
        'fatigue': ["exhaustion", "hunger", "thirst"],
        'enemy': ["bandit", "bear", "soldier"]
        }

def generateLocation(place):
    return locationsGrammar.flatten("#"+place+"#")

def generatePerson(place):
    return charactersGrammar.flatten("#"+place+"#")

def generateChoice(action,action_loc,action_char):
    choice_grammar = {
            'move': ["<loc:"+action_loc+">find a #loc#", 'wander around'],
            'chat': ['chat with random person', "<char:"+action_char+">chat with #char#"],
            'observe' : ["look around"]
            }
    choice_grammar.update(misc)
    
       
    choiceGrammarObject = renpy_tracery.Grammar(choice_grammar)
    choiceGrammarObject.add_modifiers(renpy_tracery.base_english)
    return choiceGrammarObject.flatten("#"+action+"#")

def generateActionResult(action,action_loc,action_char):
    action_result_grammar = {
        'origin': ["#<char:"+action_char+"><loc:"+action_loc+">"+action+"#"],
            'move': ["You #movement# for a few #timeUnit.s# before you encounter a #loc#.", "after a few #timeUnit.s#, you encounter #char.a# who kindly show you the way to the #loc#."],
            'chat': ["@CHAR1 Hi there!|@PLAYER I'm new here... Do you known about anything interesting?|@CHAR1 Hmm... Do you know about the #loc#? It's pretty nice to visit.","You converse with the #char# who teaches you about #subject#.","You have a nice chat with #char# who tell you about a nice place to visit : the #loc#."],
            'observe' : ["You look around you and spot a few #animal.s#."]
            }
    action_result_grammar.update(misc)
       
    action_result_grammar_object = renpy_tracery.Grammar(action_result_grammar)
    action_result_grammar_object.add_modifiers(renpy_tracery.base_english)
    return action_result_grammar_object.flatten("#origin#").split("|")

def generateWinResult(action,action_loc,action_char):
    action_result_grammar = {
        'origin': ["#<char:"+action_char+"><loc:"+action_loc+">"+action+"#"],
            'move': ["You finally find a #loc#. Finally a good place to rest!", "On the way to the #loc#, you encounter #char.a# who kindly show you the way. You instantly fall in love and marry a month after."],
            'chat': ["You are so entranced with your conversation with the #char# that you decide to join them in their adventure."],
            'observe' : ["You look around you and spot a nice treasure."]
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


