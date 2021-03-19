# Game-of-Life
Application is designed as implementation of Conway's "Game of Life"
Here are the rules
- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    
Usage:
    Run main.py via python>=3.7. <br>Default parameters are:
        
- field_size = 50 units
- initialization = random

To change them you need to modify line #11 in main.py

### Timing test
Also timing module is avaliable. Module performs game of life until it ends using given field size and processes number.
Default values are:
- Field sizes: 5, 10, 20, 40
- Processes number: 1, 2, 4, 6, 8

To change them you need to modify lines #34 and #36 of timing-test.py respectively

Results can be plotted by plot_csv_file.py (saving data to CSV is manual, by copy-paste output from timing-test.py)
