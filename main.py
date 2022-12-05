from os import listdir
from os.path import splitext
import pandas as pd
import numpy as np
import random
def clean_dataframe(df):
     # replace any empty strings in the engels column with NaN value
    df['Engels'].replace('', np.nan, inplace=True)
    # drop the null values
    df.dropna(subset=['Engels'], inplace=True)
    wordlist = df.set_index('Nederlands')['Engels'].to_dict()
    return wordlist
    

def convert_file(path):
    ext = splitext(path)[-1].lower()
    if ext.endswith('.csv'):
        df = pd.read_csv(path)
    wordlist = clean_dataframe(df)
    return wordlist

def question(wordlist, number_of_question, file_loc, file_path):
    word_guessed = {}
    word_incorrect = {}
    correct = 0;
    guess_time = 1;
    continue_learning = True
    while continue_learning:
        if guess_time >= int(number_of_question):
            continue_learning = False
        word = random.choice(list(wordlist.items()))
        key = word[0]
        value = word[1]
        print(word)
        print(f"question {guess_time} {key}(input the meaning of this word:)")
        answer = input("input your answer(you could always input'q' to quit):")
        if answer == value:
            print("Correct!")
            correct += 1
            word_guessed[key] = value
            del wordlist[key]
        elif answer.lower() != 'q':
            word_incorrect[key] =answer
            print("Sorry, the answer is wrong")
        else:
            continue_learning = False
        guess_time += 1
    

def main():
    file_path = "E:\CS\project\HappyLanguage"
    print(f"worldlist path:{file_path}")
    continue_practice = True
    while continue_practice:
        for f in listdir(file_path):
            if f.endswith('.csv'):
                print(f)
        file_loc = "chapter1.csv"
        wordlist = convert_file(file_loc)
        print(f"There are {len(wordlist)} words in the lsit",end='\n')
        number_of_questions = input("how many questions do you want to be asked?")
        not_number = True
        while not_number:
            if number_of_questions.isnumeric():
                not_number = False
            else:
                number_of_questions = input('please input a number')
        print("You can quit any time during the exericise by enter 'q'")
        #main
        question(wordlist, number_of_questions, file_loc, file_path)
        
        if input("Do you want to practice again?(y/n):").lower() == 'y':
            continue_practice = True
        else:
            print("well done! See you next time!")
            continue_practice = False
if __name__ == '__main__':
    main()