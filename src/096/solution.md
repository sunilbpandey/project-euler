# Su Doku

Sudoku can, of course, be solved by hand. If we are solving it programmatically, the simplest approach is backtracking.

Start by identifying candidates for every cell. If a cell is already solved, there is only one candidate for it, otherwise all 9 digits are possible candidates.

Any cell that has a single candidate is called a "naked single". This digit can be removed as candidate from all cells in the same row, the same column or the same box. Do this until no more digits can be eliminated.

Now, find the unsolved cell which has the least number of candidates. Set the cell to one of the candidate digits and try to solve the resulting grid. If, after eliminating all the naked singles, any cell ends up with no candidates, this grid cannot be solved. If this happens, backtrack and try another candidate. If all the candidates have been exhausted, backtrack further.

Continue like this until no unsolved cells remain.
