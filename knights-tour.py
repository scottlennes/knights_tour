
BOARD_DIM = (5, 6)
START = (0, 0)

def is_open(move_history, pos):
    if pos[0] >= 0 and pos[0] < BOARD_DIM[0] and pos[1] >= 0 and pos[1] < BOARD_DIM[1]:
        if pos not in move_history:
            return True
    else:
        return False

def find_open_moves(move_history):
    open_moves = []
    curr_pos = move_history[-1] 
    
    # check moves 2 in the x direction and 1 in the y direction
    for x in [-2, 2]:
        for y in [-1, 1]:
            new_pos = (curr_pos[0] + x, curr_pos[1] + y)
            if is_open(move_history, new_pos):
                open_moves += [new_pos]
                
    # check moves 1 in the x direction and 1 in the y direction
    for x in [-1, 1]:
        for y in [-2, 2]:
            new_pos = (curr_pos[0] + x, curr_pos[1] + y)
            if is_open(move_history, new_pos):
                open_moves += [new_pos]
    
    return open_moves

def find_knights_tour(move_history):
    open_moves = find_open_moves(move_history)
    
    # if there are no open moves, check if move_history is winning. otherwise return None
    if len(open_moves) == 0:
        if len(move_history) == BOARD_DIM[0] * BOARD_DIM[1]:
            return move_history
        else:
            return None

    # if there are open moves run find_knights_tour again to see if any the moves produce a winner
    for next_move in find_open_moves(move_history):
        knights_tour = find_knights_tour(move_history + [next_move])
        if knights_tour != None:
            return knights_tour
        
if __name__ == "__main__":
    print('starting...')
    print(find_knights_tour([START]))