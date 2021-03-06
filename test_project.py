import pytest
import project

def test_zeros():
    assert project.zeros([
        [8, 3, 9, 0, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]]) == \
        [(0, 3), (0, 4), (1, 3), (1, 4), (3, 3), (3, 4), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (8, 3), (8, 4)]
    assert project.zeros([
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1]]) == \
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]

def test_row_check():
    assert project.row_check([
        [8, 3, 9, 1, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == True
    assert project.row_check([
        [8, 3, 9, 1, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 1, 2, 0, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 1, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == True
    assert project.row_check([
        [8, 3, 9, 2, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == False

def test_column_check():
    assert project.column_check([
        [8, 3, 9, 1, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == True
    assert project.column_check([
        [8, 3, 9, 1, 1, 4, 2, 5, 7],
        [6, 7, 4, 0, 1, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == True
    assert project.column_check([
        [8, 3, 9, 3, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == False

def test_square_check():
    assert project.square_check([
        [8, 3, 9, 1, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == True
    assert project.square_check([
        [8, 3, 9, 1, 2, 3, 2, 5, 7],
        [6, 7, 4, 4, 5, 6, 1, 8, 3],
        [2, 5, 1, 7, 8, 9, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == True
    assert project.square_check([
        [8, 3, 9, 1, 2, 3, 2, 5, 7],
        [6, 7, 4, 4, 5, 6, 1, 8, 3],
        [2, 5, 1, 7, 8, 9, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (2, 3)) == True
    assert project.square_check([
        [8, 3, 9, 7, 0, 4, 2, 5, 7],
        [6, 7, 4, 0, 0, 2, 1, 8, 3],
        [2, 5, 1, 8, 3, 7, 6, 9, 4],
        [9, 6, 3, 0, 0, 5, 4, 2, 8],
        [7, 2, 8, 3, 4, 9, 5, 1, 6],
        [4, 1, 5, 2, 8, 6, 3, 7, 9],
        [0, 0, 0, 0, 0, 0, 7, 4, 1],
        [1, 8, 2, 0, 0, 3, 9, 6, 5],
        [5, 4, 7, 0, 0, 1, 8, 3, 2]], (0, 3)) == False
