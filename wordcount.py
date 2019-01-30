# put your code here.

def word_counter(file):
    filename = open(file)
    counter_dict = {}
    for line in filename:
        line = line.rstrip()
        line = line.split(" ")

        for word in line:
            if word in counter_dict:
                counter_dict[word] += 1
            else:
                counter_dict[word] = 1
    for word, counter in counter_dict.items():
        print(word, ': ', counter)

word_counter('test.txt')
    