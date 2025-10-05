# Aggressive Bull Simulation
# 0 = empty space, 1 = obstacle
field = [0, 0, 1, 0, 0, 1, 0, 0, 0]

def aggressive_bull(field):
    position = 0
    steps = 0
    n = len(field)
    
    while position < n - 1:
        # Try to jump 2 steps forward if possible
        if position + 2 < n and field[position + 2] == 0:
            position += 2
        else:
            # Otherwise, move 1 step forward if not blocked
            if field[position + 1] == 0:
                position += 1
            else:
                # Bull is blocked
                break
        steps += 1
    
    return steps, position

total_steps, final_position = aggressive_bull(field)
print(f"Aggressive Bull moved {total_steps} steps, final position: {final_position}")
