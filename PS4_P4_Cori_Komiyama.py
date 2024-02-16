# Paragraph Manipulation
    #string methods, split, slice, join

paragraph = 'Python is an excellent choice as a first programming language '\
            'to learn for a multitude of reasons. Its simplicity and readability '\
            'make it approachable for beginners, with a clean and concise syntax '\
            'that minimizes the learning curve. Python\'s versatility is another key '\
            'advantage, as it can be used in various domains, from web development '\
            'and data analysis to scientific computing and aritifical intelligence.'

para_list = paragraph.split(' ')  #split paragraph into list of words
print(f'Word count: {len(para_list)}\n')  #print word count

print(f'The first word is {para_list[0]} and last word is {para_list[-1]}\n')  #first, last word

para_list[0] = para_list[0].lower()  # first word, lower
para_list[-1] = para_list[-1].upper()  # last word, upper
print(f'The first word is {para_list[0]} and last word is {para_list[-1]}\n') # reprint with changes

paragraph = ' '.join(para_list)  # join list back together

print(f'First position of "Python": {paragraph.find("Python")} \n'  # first instance
      'The reason this result is not 0 is because a string literal must be matched '\
      'exactly. Since the first word of the paragraph is actually \'python\', the first '\
      'instance of \'Python\' is not until item 233. \n')

print(f'Count of word \'and\': {paragraph.count("and")} \n') # 'and' count

paragraph = paragraph.replace("and", "&") #replace 'and' with '&'
print(f'Paragraph with \'and\' replaced by \'&\':\n{paragraph}\n') #reprint with changes

sentences = paragraph.rsplit('. ')
print(sentences)
#with_periods = '. '.join(sentences)
#print(with_periods)


print(f'Number of sentences: {len(sentences)}\n') # number of sentences

print(f'Second sentence:\n{sentences[1].lstrip()}' + '.' + '\n') # print second sentence

#with_periods = '. '.join(sentences)
#print(f'{with_periods}\n')


sentences.reverse() # reverse order of sentences

joined_paragraph = sentences[0] + ' ' +'. '.join(sentences[1:]) # join sentences
print(f'Joined paragraph:\n{joined_paragraph.strip()}' + '.') # print final paragraph







