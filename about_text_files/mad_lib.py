# Mad lib example for functions.

def madlib(adjective_1,noun_1,verb_1,noun_2,verb_2,adjective_2,verb_3,noun_3,adjective_3):
    '''Mad lib function'''

    story =f'''
One day, a {adjective_1} bear was wandering through the {noun_1}. 
As it walked, it suddenly {verb_1} a strange noise coming from a {noun_2}
nearby. Curious, the bear decided to {verb_2} over and investigate.
To its surprise, it found a {adjective_2} creature trying to {verb_3} a 
{noun_3}. With a {adjective_3} smile, the bear helped, and they became 
fast friends.
'''
    return story

output_story = madlib('brown', 'forest', 'heard', 'cave', 'crawl', 'fuzzy', 'start', 'fire', 'silly')
print(output_story)
