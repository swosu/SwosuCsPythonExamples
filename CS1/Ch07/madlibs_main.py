import questions_for_madlib

print("hello from the main file of Mad Libs. ")
print('ADJETIVE: a word or phrase naming',\
'an attribute, added to or grammatically related',\
'to a noun to modify or describe it.'\
'The word red in "the red car" is an adjective.')

print('NOUN: a word (other than a pronoun) used to',\
'identify any of a class of people, places, or',\
'things ( common noun ), or to name a particular',\
'one of these ( proper noun ).',\
'There are common nouns and proper nouns. A common',\
'noun refers to a person, place, or thing but is not the',\
'name of a particular person, place, or thing. Examples',\
'are animal, sunlight, and happiness. A proper noun is the',\
'name of a particular person, place, or thing; it usually',\
'begins with a capital letter: Abraham Lincoln, Argentina,',\
'and World War I are all proper nouns.')

print('VERB: a word used to describe an action, state,',\
'or occurrence, and forming the main part of the predicate',\
'of a sentence, such as hear, become, happen.')

person_in_room = questions_for_madlib.question_1()
number = questions_for_madlib.question_2()
adjetive = questions_for_madlib.question_3()
color = questions_for_madlib.question_4()
noun = questions_for_madlib.question_5()
food = questions_for_madlib.question_6()
second_noun = questions_for_madlib.question_7()
ing_verb = questions_for_madlib.question_8()


print('My name is', person_in_room, ' and I am', number,\
"years old. If I were president, I'd do a whole bunch of",\
adjetive, 'things:')

print('\t1. I would drive the biggest', color, ' car in the',\
'country. And that car would go faster than any other',\
noun, 'in the world!')

print('\t2. Everyone would eat pepperoni', food, 'for dinner.')

print('\t3. I would live in the statue of', second_noun,\
' and build a', ing_verb, ' pool at her feet.')
