#{
#"name": ["Cheri","Fox","Morgana","Jedoo","Brick","Shadow","Krox","Urga","Zelph"]
#,"story": ["#hero.capitalize# was a great #occupation#, and this song tells of #heroTheir# adventure. #hero.capitalize# #didStuff#, then #heroThey# #didStuff#, then #heroThey# went home to read a book."]
#,"monster": ["dragon","ogre","witch","wizard","goblin","golem","giant","sphinx","warlord"]
#,"setPronouns": ["[heroThey:they][heroThem:them][heroTheir:their][heroTheirs:theirs]","[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers]","[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his]"]
#,"setOccupation": ["[occupation:baker][didStuff:baked bread,decorated cupcakes,folded dough,made croissants,iced a cake]","[occupation:warrior][didStuff:fought #monster.a#,saved a village from #monster.a#,battled #monster.a#,defeated #monster.a#]"]
#,"origin": ["#[#setPronouns#][#setOccupation#][hero:#name#]story#"]
#}

import renpy_tracery
import random

characterNames =  {
    'setHeroNameAndPronouns': ["[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers][heroName:#femaleName.capitalize#]","[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his][heroName:#maleName.capitalize#]"],
    'designHero': ["#heroThey#", "#heroThey#", "#heroThey#", "#heroName#"],
    'maleName' : ["#nameSyllable.capitalize##maleNameEnd#", "#nameSyllable.capitalize##nameSyllable##maleNameEnd#"],
    'femaleName' : ["#nameSyllable.capitalize##femaleNameEnd#", "#nameSyllable.capitalize##nameSyllable##femaleNameEnd#"],
    'nameSyllable': ["e", "ju", "ma", "bo", "ne", "ri", "a", "syl", "val", "di", "fla"],
    'femaleNameEnd': ["va", "via", "lie", "rie", "line", "tine", "vie", "ma", "ca", "za", "ra"],
    'maleNameEnd': ["l", "gor", "co", "ro", "zo", "vio", "tin", "mo", "med", "ton", "rem", "ric"]
}

nameGenerator = renpy_tracery.Grammar(characterNames)    
nameGenerator.add_modifiers(renpy_tracery.base_english)


class StoryCharacter(renpy_tracery.TraceryCharacter):
    gender=""
    name=""
    age=0
    location=""
    text_color=""
    image=""

    
    def __init__(self, **properties):
        self.gender = random.choice(['male', 'female'])
        self.name = nameGenerator.flatten("#"+self.gender+"Name#")       
        self.text_color="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        properties['color']=self.text_color
        super(StoryCharacter, self).__init__(self.name, {}, **properties)

        characterIndex = random.randint(1,2)
        self.image="images/character/"+self.gender+str(characterIndex)+".png"


        self.age=random.randint(18, 55)
        self.location="city"


