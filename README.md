# talos-puzzle

This python 3 script solves the Sigil puzzles in alos Principle game from Croteam: http://www.croteam.com/talosprinciple/

Puzzle board is made of Rows x Columns cells.
Column is the horizontal dimension.
Row is the vertical dimension.
The puzzle can use the following pieces:

- Square shape
- L right shape
- L left shape
- Bar shape
- Tee shape
- Step right shape
- Step left shape

The pieces can be flipped horizontally and vertically.

Solutions (if they exist) are output on the console and can be saved in PNG images. 

## Requirements

The script is using the `pillow (PIL fork)` library for images generation and the `numpy` library for matrix manipulation

## Performances
The script uses a brute force approach:

- Generate all possible positions of each given piece on the board, some pieces having different patterns due to possible rotations
- Combine all the generated positions together to find the solutions (tree of combinations)
- To improve performance dead branches are dropped immediately. A branch is dead when a tested position overlaps with an existing combination of positions.
- Even with the early drop of dead branches, it could take some time to solve large puzzle. To solve the red puzzle with 8 columns and 7 rows with 4 square, 4 tee, 2 bars, 1 step left, 1 step right, 1 l left and 1 l right, the script has to go through 577 289 330 256 198 172 046 386 176 combinations of pieces.
