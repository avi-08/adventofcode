import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

    with open(file_path, 'r') as f:
        grid_block = [x.strip() for x in f.readlines()]
    
    return grid_block

def traverse_grid(grid_block, right, down):
    row, col, trees = 0, 0, 0
    while row < len(grid_block):
        if grid_block[row][col] == '#':
            trees += 1
        col += right
        col %= len(grid_block[0])
        row += down
        
    return trees
  

def main():
    grid_block =    read_input('input.txt')
    print(f"Grid block size: {len(grid_block[0])} x {len(grid_block)}")      
    
    # Part one
    trees = traverse_grid(grid_block, right=3, down=1)
    print(f"Encountered {trees} trees on the slope.")
    
    # Part two
    for right, down in [(1, 1), (5, 1), (7, 1), (1, 2)]:
        trees *= traverse_grid(grid_block, right, down)
    print(f"Product of trees found on all slopes: {trees}")
        

if __name__ == '__main__':
    main() 
    