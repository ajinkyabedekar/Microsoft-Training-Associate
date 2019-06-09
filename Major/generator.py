import re
import pandas as pd
from collections import Counter


def main_generator(path):
    # loads the data from the csv file
    data = pd.read_csv(path, header=0, delimiter="\t", quoting=3)

    # trying to split the data into sent and label
    l_s = list(data['sent'])
    l_ls = list(data['label'])

    # forming a list with the obtained sentences and labels
    m_l_l = []
    for ids, label in enumerate(l_ls):
        if label == 'Not Found':
            pass
        else:
            m_l_l.append([l_s[ids], label])

    # figuring out the pattern with words on both the sides
    s_l = []
    for i in m_l_l:
        name = i[1]  # the label
        name = re.sub('[^A-Za-z0-9]+', ' ', name)  # removing any special characters
        sub = '(\w*)\W*('+name+')\W*(\w*)'  # identifying words around name
        str_rest = i[0]  # the complete sentence
        for i in re.findall(sub, str_rest, re.I):
            s_l.append([" ".join([x for x in i if x != ""]), name])  # s_l is a list of lists with a pattern

    # creating a regex bucket by removing labels from the strings
    some_pattern_list = []
    for d_list in s_l:
        if d_list[1] in d_list[0]:
            some_pattern_list.append(d_list[0].replace(d_list[1], " "))
        else:
            pass

    # converting the Counter dictionary to a list of tuples (pattern,freq)
    pattern_list_temp = ((Counter(some_pattern_list)).most_common())
    pattern_list = [tup[0] for tup in pattern_list_temp]  # creating a list of patterns from the tuples

    # figuring out the patterns with two words on the left
    s_n_l = []
    for i in m_l_l:
        name = i[1]
        name = re.sub('[^A-Za-z0-9]+', ' ', name)
        sub = '(\w*)\W*(\w*)\W*('+name+')'
        str_rest = i[0]
        for i in re.findall(sub, str_rest, re.I):
            s_n_l.append([" ".join([x for x in i if x != ""]),name])
    some_pattern_list_new = []
    for d_list in s_n_l:
        if d_list[1] in d_list[0]:
            some_pattern_list_new.append(d_list[0].replace(d_list[1], " "))
        else:
            pass

    pattern_list2 = ((Counter(some_pattern_list_new)).most_common())
    pattern_list_2 = [tup[0] for tup in pattern_list2]
    len_2_words = int((len(pattern_list_2))*.20)  # taking only the top 20% of the all the patterns created

    # Creating the matcher.py file
    new_file = open('matcher.py', 'a')
    new_file.truncate()
    new_file.write(
        '''
import re
def main_matcher(path_test):
    master_list = []
    sent_list = []
    data = open(path_test,'r')
    for text in data:
        found = 0
        small_master_list = []
        sent_list.append(text)
    ''')
    new_file.write('\n')
    new_file.close()
    for pat in pattern_list:
        bound = pat.split()
        if len(bound) == 2:
            new_file = open('matcher.py','a')
            new_file.write('        m = re.search('+"' "+bound[0]+' '+'(.+?)'+' '+bound[1]+" '"+', text)')
            new_file.write('\n')
            new_file.write('        if m:')
            new_file.write('\n')
            new_file.write('            found = m.group(1)')
            new_file.write('\n')
            new_file.write('            small_master_list.append(found)')
            new_file.write('\n')
            new_file.close()
        else:
            pass
    for pat in pattern_list_2[:len_2_words]:
        bound = pat.split()
        if len(bound) == 2:
            new_file = open('matcher.py','a')
            new_file.write('        m = re.search('+"' "+bound[0]+' '+bound[1]+' (.*)'+"'"+', text)')
            new_file.write('\n')
            new_file.write('        if m:')
            new_file.write('\n')
            new_file.write('            found = m.group(1)')
            new_file.write('\n')
            new_file.write('            small_master_list.append(found)')
            new_file.write('\n')
            new_file.close()
        else:
            pass

    new_file = open('matcher.py', 'a')
    new_file.write(
        '''
        if found==0 : # returns Not Found when the patterns do not match
            small_master_list.append('Not Found')
        master_list.append(small_master_list)

    no_no_words=['on','for','to','at','by'] # list of words which if occured in the output will be penalised while giving a score
    final_output=[]
    # selecting one from the options
    for options in master_list:
        if len(options)==1:
            final_output.append(options[0])#if only one pattern extracted use it 
        else:
            sent_score_list=[] # else score all the options to select the best one
            for option in options:
                l=option.split()
                score = 0
                score = len(l)
                for word in l:
                    if word in no_no_words:
                        score = score -3 #penalise the no_no_words
                    else:
                        pass
                sent_score_list.append(score)
            m = max(sent_score_list)
            indx=[i for i, j in enumerate(sent_score_list) if j == m] # returns a list of all the index which have max score
            index = indx[-1]#pick the last element as an index 
            final_output.append(options[index])

    tups=zip(sent_list, final_output)
    final_list = [list(l) for l in tups]

    for small_list in final_list:
        new_file = open("output.txt", "a")
        new_file.write('\\n')
        new_file.write(' '.join(small_list[0].split())+'\\t'+small_list[1])
        new_file.write('\\n')
        new_file.close()
    return(final_output)
    ''')
    new_file.write('\n')
    new_file.close()