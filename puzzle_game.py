import random
import numpy as np
import time

def generate_sequence():
    '''
    Generate an unsorted sequence of five unique numbers.

    Args:
        - None
    Returns:
        - sequence(List)
    '''
    sequence = np.unique(random.choices(range(100), k = 5))
    
    while len(sequence) != 5:
        sequence = np.unique(random.choices(range(100), k = 5)) 
        np.random.shuffle(sequence)
    
    return sequence


def generate_puzzle(sequence):

    '''
    Generate the puzzle. i.e a list of "unequal" signs.

    Args:
        - sequence(List) - generate using generate_sequence()
    Returns:
        - puzzle(List)
    '''

    puzzle = []

    for i in range(1,len(sequence)):

        if sequence[i-1] > sequence[i]:
            puzzle.append('>')
        else:
            puzzle.append('<')

    return puzzle

def solution(sequence, puzzle):

    '''
    Create a solution from the sequence and the puzzle.

    Args:
        - sequence(List) - generate using generate_sequence()
        - puzzle(List) - generate using generate_puzzle(sequence)
    Returns
        - solution(String)
    '''

    solution = ''

    for i in zip(sequence,puzzle):
        solution += str(i[0]) + ' ' + i[1] + ' '

    solution = solution + str(sequence[-1])
    
    return solution

def generate_question(solution):

    '''
    Generate the user question from the solution.

    Args:
        - solution(String) - generate using solution(sequence, puzzle)
    Returns:
        - question(List)
    '''

    solution_list = solution.split()
    question = ''

    for i in solution_list:

        if i != '>' and i != '<':
            question += ' ? '
        else:
            question += i


    question = question[1:-1]

    return question

def check_answer(answer):

    '''
    Assert that the user answer is correct.

    Args:
        - answer(String) - User Input
    Returns:
        - None
    '''
    nums = []
    chars = []

    answer = answer.replace(' ', '')

    if len(answer) < 7 :
        print('You Suck!')
        return False

    for i in answer:

        if i == '>' or i == '<':
            chars.append(i)
            answer = answer.replace(i,' ')

    nums = answer.split(' ')

    if '<' not in chars and '>' not in chars:
        print('You Suck!')
        return False

    for i in range(1, len(nums)):

        if chars[i-1] == '>':
            if nums[i-1] < nums[i]:
                return False
        else:
            if nums[i-1] > nums[i]:
                return False

    return True