import syllables
import poetrytools
import re

def prepare_input(file, type):
    '''
    Prepares the input from a textfile to analyze either words or meter

    Parameters
      file, string: a path to a valid textfile
      type, string: either "words" or "meter"

    Returns
      output, list: the words of the file are filtered for only for alphabetic
                     characters
      if type == "words"
        return a list of each word from the file
      if type == "meters"
        returns a pair of lists with a list of words in the first index and
        a list of corressponding meters for those words in the second index

    Pre/postconditions
      none additional
    '''
    with open(file) as f:
        file_string = f.read()

    filter_fn = lambda c: c.isalpha() or c ==" "
    filtered_string = "".join(filter(filter_fn, file_string))

    if type == "words":
        output = filtered_string.split()
    elif type == "meters":
        tokens = poetrytools.tokenize(filtered_string)
        output = [tokens[0], poetrytools.scanscion(tokens)[0]]
    return output


def get_syllable_counts(word_list):
    '''
    Takes a list of words and pairs each word with its estimated number of
     syllables

    Parameters
      word_list, list: a list of strings

    Returns
      pair_list, list: a list of pairs of words and their respective syllable
                        count
    Preconditions:
      none

    Postconditions:
      pair_list is the same length of word_list
      pairs are of the form [word, syllable count]
    '''
    pair_syllable = lambda w: [w, syllables.estimate(w)]
    return [pair_syllable(word) for word in word_list]


def make_haikus(syllable_counts):
    '''
    Takes a list of words paired with with their respective syllable counts and
     generates sequential haikus

    Parameters
      syllable_counts, list: a list of pairs of words with their respective
                              respective syllable counts

    Returns
      haikus, list: a list of lists of strings which are haikus, '$' signals the
                     end of each line in a haiku

    Preconditions
      the pairs in syllable_counts are of the form [word, syllable count]

    Postconditions
      haikus are in the order that the words appear in syllable counts
    '''
    def too_long():
        nonlocal start, check, curr_haiku, syllable_total, line
        start +=1
        check = start
        curr_haiku = []
        syllable_total = 0
        line = 0

    def new_line():
        nonlocal curr_haiku, line, syllable_total, check
        curr_haiku.append(curr_word)
        curr_haiku.append("$") # signals line break
        line += 1
        syllable_total = 0
        check += 1

    def add_word():
        nonlocal curr_haiku, check
        curr_haiku.append(curr_word)
        check += 1

    haikus = []; curr_haiku =[]
    start = 0; check = 0; line = 0; syllable_total = 0
    while start < len(syllable_counts) and check < len(syllable_counts):
        curr_pair = syllable_counts[check]
        curr_word = curr_pair[0]
        syllable_total += curr_pair[1]
        if line == 0:
            if syllable_total > 5:
                too_long()
            elif syllable_total < 5:
                add_word()
            else:
                new_line()
        elif line == 1:
            if syllable_total > 7:
                too_long()
            elif syllable_total < 7:
                add_word()
            else:
                new_line()
        else: #last line
            if syllable_total > 5:
                too_long()
            elif syllable_total < 5:
                add_word()
            else:
                new_line()
                haikus.append(curr_haiku)
                start = check
                curr_haiku = []
                line = 0
    return haikus


def process_haikus(haikus):
    '''
    Takes a list of haiku strings and replaces '$' with '\n'
    '''
    joined_haikus = [" ".join(haiku) for haiku in haikus]
    formatted_haikus = [haiku.replace(" $", "\n") for haiku in joined_haikus]
    return formatted_haikus


def find_meter(meter_list, base_meter, num_occurences):
    '''
    From a list of meter strings, finds a given meter determined by a base meter
    and a number of occurences

    Parameters
      meter_list, list: a list of strings indicating the meter of words
      base_meter, string: a string indicating a meter with "1" indicating a
                           stressed syllable and a "0" indicating an unstressed
                           syllable (e.g. an iamb is "01")
      num_occurences, int: the number of occurences of the base meter you are
                            looking for (e.g. iambic pentatmeter would have
                                         base_meter="01", num_occurences=5)

    Returns
      lines_by_index: a list of lists, where each interior list contains the
                       consectutive indices which contain the occurence of the
                       desired meter

    Pre/postconditions
      none additional
    '''
    lines_by_index = []
    meter_regex = "^(" + base_meter + "){"+ str(num_occurences)+"}$"
    line_length = num_occurences*len(base_meter)
    for i in range(len(meter_list)):
        segment = ""
        indices = []
        j = i

        while len(segment) < line_length and j < len(meter_list):
            segment += meter_list[j]
            indices.append(j)
            j += 1
        if len(segment) == line_length and re.match(meter_regex, segment):
            lines_by_index.append(indices)
    return lines_by_index
file_string.replace("\n", " ")

def process_meter(meter_occurences, token_list):
    '''
    Takes the occurences of metric content, and the list of tokens from which
    they were drawn, and produces a list of strings of words with that metric
    content
    '''
    metric_lines = []
    for occurence in meter_occurences:
        line = ""
        for index in occurence:
            line += token_list[index] + " "
        metric_lines.append(line)
    return metric_lines


if __name__ == "__main__":
    file = input("Give a path to a textfile: ")
    choice = eval(input("What would you like to find?\n" +
                        "\t1) Haikus\n" +
                        "\t2) Iambic Pentameter\n" +
                        "\t3) Trochaic Tetrameter\n" +
                        "\t4) Make Your Own Meter\n"
                        "Choice: "))
    if choice == 1:
        word_list = prepare_input(file, "words")
        syllable_counts = get_syllable_counts(word_list)
        processed_haikus = process_haikus(make_haikus(syllable_counts))
        [print(haiku) for haiku in processed_haikus]
    if choice in [2, 3, 4]:
        if choice == 2:
            base_meter = "01"
            num_occurences = 5
        elif choice == 3:
            base_meter = "10"
            num_occurences = 4
        else:
            base_meter = input("Input a base meter, using 1 for stressed and 0"+
                               "for unstressed.\n" + "For example, an iamb" +
                               "would be '01': ")
            num_occurences = eval(input("How many times would you like to see" +
                                        "if that meter occurs?\n" +
                                        "For example, the number for iambic" +
                                        "pentatmeter would be 5: "))
        tokens_meters = prepare_input(file, "meters")
        meter_list = find_meter(tokens_meters[1], base_meter, num_occurences)
        metric_lines = process_meter(meter_list, tokens_meters[0])
        print("\n")
        [print(line + "\n") for line in metric_lines]
