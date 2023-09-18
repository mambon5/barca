
def print_member_friends(seats):
    for row, row_seats in enumerate(seats):
        for seat, marker in enumerate(row_seats):
            if marker == "M":
                member_seat_num = (row * len(seats[0])) + seat + 1
                friends = []
                for ds in [-1, 0, 1]:
                    if 0 <= seat + ds < len(row_seats) and row_seats[seat + ds] == "F":
                        friends.append((row * len(seats[0])) + seat + ds + 1)
                print(f"Member Seat {member_seat_num}: Friends Seats {friends}")
# Example usage:
# num_rows = 5
# seats_per_row = 20
# num_members = 40
# num_friends = 60

# allocated_seats = allocate_seats(num_members, num_friends, num_rows, seats_per_row)
# print_non_member_friends(allocated_seats, num_rows, seats_per_row)
