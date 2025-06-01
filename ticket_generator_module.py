
import random

def generate_full_strip():
    def generate_ticket():
        ticket = [[None for _ in range(9)] for _ in range(3)]
        nums = [random.sample(range(i*10 + 1, i*10 + 11), 3) if i != 0 else random.sample(range(1, 10), 3) for i in range(9)]
        for col in range(9):
            col_nums = sorted(nums[col])
            for row in range(3):
                ticket[row][col] = col_nums[row] if row < len(col_nums) else None
        return ticket
    return [generate_ticket() for _ in range(6)]
