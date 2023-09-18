import random

def rand_alloc_seats(num_members, num_friends, num_zones):
    num_members = num_members + num_friends
    if num_members % num_zones != 0:
        print("Error: The number of members must be divisible by the number of zones.")
        return
    
    total_seats = 100
    seats_per_zone = total_seats // num_zones
    members_per_zone = num_members // num_zones
    seats = [[] for _ in range(num_zones)]
    
    # Allocate everyone to their respective zones
    members = list(range(1, num_members + 1))
    random.shuffle(members)
    for zone in range(num_zones):
        for _ in range(members_per_zone):
            seats[zone].append(members.pop())

    return seats

import random

def allocate_seats(num_members, num_friends, num_rows, seats_per_row):
    if num_members > num_rows * seats_per_row:
        print("Error: Not enough seats available for members.")
        return None

    total_seats = num_rows * seats_per_row
    seats = [['N' for _ in range(seats_per_row)] for _ in range(num_rows)]

    # Allocate members to their seats
    member_seats = random.sample(range(total_seats), num_members)
    for member_seat in member_seats:
        row = member_seat // seats_per_row
        seat_in_row = member_seat % seats_per_row
        seats[row][seat_in_row] = "M"  # Marking member seats

    # Allocate friends next to their member friends in the same row
    for row in range(num_rows):
        row_seats = seats[row]
        member_indices = [i for i, seat in enumerate(row_seats) if seat == "M"]
        friend_indices = [i for i, seat in enumerate(row_seats) if seat == "N"]

        if member_indices and friend_indices:
            random.shuffle(friend_indices)
            for member_index in member_indices:
                if friend_indices:
                    friend_index = friend_indices.pop()
                    row_seats[friend_index] = "F"  # Marking friend seats

    return seats

# Example usage:
# num_members = 40
# num_friends = 60
# num_rows = 5
# seats_per_row = 20

# allocated_seats = allocate_seats(num_members, num_friends, num_rows, seats_per_row)
# for row, row_seats in enumerate(allocated_seats):
#     print(f"Row {row + 1}: {' '.join(row_seats)}")
