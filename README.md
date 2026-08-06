# Sudoku generator (Python)

Generates a complete Sudoku board and removes cells to produce a puzzle.
Coursework, forked from the course template.

`sudoku_generator.py` fills the diagonal boxes with `fill_box`, completes the
rest recursively with `fill_remaining`, and then `remove_cells` blanks out the
requested number of cells. Validity during filling is checked by
`valid_in_row`, `valid_in_col`, and `valid_in_box`.

```bash
./main.sh
```
