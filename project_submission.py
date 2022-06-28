import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = 'all-project-files'

class DescribeBikeShare:
    """
    We will build a class that gathers statistics for the user to view based on the input given
    """

    def __init__(self):
        """
        Initialize the names of the files we will choose to open.
        Initialize a data dictionary to interpret the user input.
        """
        self.chicago = 'chicago.csv'
        self.new_york = 'new_york_city.csv'
        self.washington = 'washinton.csv'
        self.data_dict = {'chicago' : self.chicago,
                        'new york'  : self.new_york,
                        'washington' : self.washington}
        self.num_to_city = {1 : 'chicago',
                            2 : 'new york',
                            3 : 'washington'}
        self.first_question_dict = {1 : 'bike volume',
                                    2 : 'high and low traffic times',
                                    3 : 'user statistics'}
    
    def ask(self):
        """
        Print welcome message to user and save their choice.
        """
        # print message
        self.n_stars = 50
        print('Hello! Welcome to the BikeShare Interactive EDA. Below are the possible topics you can choose from.\n')
        print('*'*self.n_stars)
        print('1. Compare bike usage by city')
        print('2. Find high and low traffic times')
        print('3. Compare User Statistics')
        print('*'*self.n_stars + '\n')

        self.user_choice = input('What topic do you want to focus on? Type "None" at any point to exit the program : ')
        self.process_first_answer()

    def describe(self):
        return
    
    def process_first_answer(self):
        """
        Figure out what the user chose.
        """
        self.formatted_input = self.user_choice.lower().strip()
        # deal with innappropriate inputs first
        if self.formatted_input not in ['none', '"none"', '1','2','3']:
            self.user_choice = input('Sorry, that\'s not an option in this program. Please choose from the list above (type 1, 2, or 3) or type "None" to exit : ')
            self.process_first_answer()
        
        # exit the code, check if user inputs none with quotes as well
        elif self.formatted_input in ['none', '"none"']:
            print("Thanks for joining us today. Hope you learned something new!")
        
        else:
            self.first_answer_choice = self.formatted_input
            self.ask_second_question()
    
    def ask_second_question(self):
        """
        Ask questions depending on what the answer to the initial question was.
        """
        print('\nTell me which cities you are most interested in')
        print('*'*self.n_stars)
        print('1. Chicago?')
        print('2. New York?')
        print('3. Washington?')
        print('*'*self.n_stars + '\n')
        self.user_choice = input('Choose two of the three options (separated by a comma. EX: 1,2 to compare Chicago and New York), or type "all" to compare all cities at once. : ')
        self.process_second_answer()
    
    def process_second_answer(self):
        """
        Parse the user's input for the second question to determine which path to take.
        """
        self.formatted_input = self.user_choice.replace(' ', '').lower().split(',')
        # deal with innappropriate inputs first
        if sum([0 if user_input in ['none', '"none"', '1','2','3'] else 1 for user_input in self.formatted_input]) > 0:
            self.user_choice = input('Sorry, that\'s not an option in this program. Please choose two of the three options (separated by a comma. EX: 1,2 to compare Chicago and New York), or type "all" to compare all cities at once : ')
            self.process_second_answer()

        # exit the code, check if user inputs none with quotes as well
        elif sum([1 if user_input in ['none', '"none"'] else 0 for user_input in self.formatted_input]) > 0:
            print("Thanks for joining us today. Hope you learned something new!")

        # compare all cities
        elif 'all' in self.formatted_input:
            self.load_files()
        
        # compare any two cities
        else:
            city1, city2 = int(self.formatted_input[0]), int(self.formatted_input[1])
            self.load_files(cities = [city1, city2])



    def load_files(self, cities = 'all'):
        if cities == 'all':
            self.chicago_df = pd.read_csv(os.path.join(DATA_PATH, self.chicago))
            self.ny_df = pd.read_csv(os.path.join(DATA_PATH, self.new_york))
            self.washington_df = pd.read_csv(os.path.join(DATA_PATH, self.washington))
            # add city names
            self.chicago_df['city'] = 'chicago'
            self.ny_df['city'] = 'new york'
            self.washington_df['city'] = 'washington'
            self.data = pd.concat([self.chicago_df, self.ny_df, self.washington_df], axis = 0)
            print('\nHere are the first 5 rows for the dataset with all cities')

        else:
            # use the dictionaries to automatically read the cities chosen
            self.city1 = self.num_to_city[cities[0]]
            self.city2 = self.num_to_city[cities[1]]
            self.df1 = pd.read_csv(os.path.join(DATA_PATH, self.data_dict[self.city1]))
            self.df2 = pd.read_csv(os.path.join(DATA_PATH, self.data_dict[self.city2]))
            # add city names
            self.df1['city'] = self.city1
            self.df2['city'] = self.city2
            self.data = pd.concat([self.df1, self.df2], axis = 0)
            print('\nHere are the first 5 rows for the dataset containing {} and {}'.format(self.city1.title(), self.city2.title()))
        print(self.data.head())

def main():
    describer = DescribeBikeShare()
    describer.ask()

if __name__ == '__main__':
    main()
