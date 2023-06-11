# A nonogram is also known as Paint by Numbers and Japanese Crossword. The aim in this puzzle is to color the grid into black and white squares. At the top of each column, and at the side of each row, there are sets of one or more numbers which describe the runs of black squares in that row/column in exact order. For example, if you see 10 1 along some column/row, this indicates that there will be a run of exactly ten black squares, followed by one or more white squares, followed by a single black square. The cells along the edges of the grid can also be white.

# You are given a square nonogram of size size. Its grid is given as a square matrix nonogramField of size (size + 1) / 2 + size, where the first (size + 1) / 2 cells of each row and and each column define the numbers for the corresponding row/column, and the rest size × size cells define the the grid itself.

# Determine if the given nonogram has been solved correctly.

# Note: here / means integer division.

# Example

# For size = 5 and

# nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
#                  ["-", "-", "-", "2", "2", "1", "-", "1"],
#                  ["-", "-", "-", "2", "1", "1", "3", "3"],
#                  ["-", "3", "1", "#", "#", "#", ".", "#"],
#                  ["-", "-", "2", "#", "#", ".", ".", "."],
#                  ["-", "-", "2", ".", ".", ".", "#", "#"],
#                  ["-", "1", "2", "#", ".", ".", "#", "#"],
#                  ["-", "-", "5", "#", "#", "#", "#", "#"]]
# the output should be solution(size, nonogramField) = true;

# For size = 5 and

# nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
#                  ["-", "-", "-", "-", "-", "1", "-", "-"],
#                  ["-", "-", "-", "3", "3", "2", "5", "5"],
#                  ["-", "-", "3", ".", ".", ".", "#", "#"],
#                  ["-", "2", "2", "#", "#", "#", "#", "#"],
#                  ["-", "-", "5", "#", "#", "#", "#", "#"],
#                  ["-", "-", "5", "#", "#", "#", "#", "#"],
#                  ["-", "-", "2", ".", ".", ".", "#", "#"]]
# the output should be solution(size, nonogramField) = false.

# There are three mistakes in the nonogram:

# In the 5th (1-based) row there are numbers ["-", "2", "2"], so there should be two runs of 2 black squares separated by at least one white square. However, there is only one run of 5 black squares.
# In the 6th column there are numbers ["-", "1", "2"], so there should be a run of exactly 1 black square, followed by one or more white squares, followed by another 2 black squares. However, there is a single run of 3 black squares not separated by white ones.
# Finally, in the 4th row there are numbers ["-", "-", "3"], so there should be a single run of exactly 3 black squares. However, there is just a 2-square run in that row.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] integer size

# A positive integer, the size of the grid.

# Guaranteed constraints:
# 5 ≤ size ≤ 10.

# [input] array.array.string nonogramField

# A square matrix of strings of size (size + 1) / 2 + size defining the puzzle field.
# The first (size + 1) / 2 cells of each row and each column define the numbers for this row/column. If there is no number in the cell, its value is "-".
# The remaining size × size cells define the grid, where string "#" denotes black cells and string "." denotes white ones.

# Guaranteed constraints:
# 8 ≤ nonogramField.length ≤ 15,
# nonogramField[i].length = nonogramField.length.

# [output] boolean

# true if the given nonogram is solved correctly and false otherwise.

def checkRow(size, row):
    notation_cells = (size + 1) // 2
    row = row.copy()
    row_cells = row[notation_cells:]
    
    for i, notation in enumerate(row[:notation_cells]):
        # print(i, notation, row_cells)
        if(i == 0):
            while(len(row_cells) > 0 and row_cells[0] == "."):
                row_cells.pop(0)
        if(notation == "-"):
            continue
        # otherwise, pop off the number of cells given by the notation, and they must all be black
        # and also be followed by one white cell (unless the last notation value)
        consecutive_black_cells = int(notation)
        # print(i, row_cells, consecutive_black_cells)
        for j in range(consecutive_black_cells):
            # print(i, notation, row_cells)
            if(len(row_cells) == 0):
                return False
            if(not row_cells[0] == "#"):
                return False 
            row_cells.pop(0)
        else:
            # print(i, notation, notation_cells, row_cells)
            if(i < notation_cells - 1):
                count_white_cells = 0
                while(len(row_cells) > 0 and row_cells[0] == "."):
                    count_white_cells += 1
                    row_cells.pop(0)
                else:
                    # print(i, notation, row_cells)
                    if(len(row_cells) == 0 or count_white_cells < 1):
                        return False
    # check no black cells left
    else:
        if(any([a == "#" for a in row_cells])):
            return False
        
    return True

def solution(size, nonogramField):
    # use checkRow for each row, 
    # and then for each column (transposed)
    
    notation_cells = (size + 1) // 2
    
    # add rows
    check_rows = [row for row in nonogramField[notation_cells:]]
    # add columns
    check_rows += [[row[i] for row in nonogramField] for i in range(notation_cells, len(nonogramField[0]))]
    # print(check_rows)
    # result = ([checkRow(size, row) for row in check_rows])
    # print(result)
    
    return all([checkRow(size, row) for row in check_rows])