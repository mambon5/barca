
import assignaSeientsFans as asei
import printingFriends as prif


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def draw_oval_stadium(seats, num_zones, zone_colors):
    # Define the oval stadium
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Load and set the background image
    background_img = mpimg.imread('estadi.jpg')  # Replace 'background_image.jpg' with your image file
    ax.imshow(background_img, extent=[0, 60, 3, 40], alpha=0.5)

    # Define stadium parameters
    stadium_width = 40.0
    stadium_length = 60.0
    center_x = stadium_length / 2
    center_y = stadium_width / 2
    radius_x = stadium_length / 2
    radius_y = stadium_width / 2

    # Draw the oval stadium
    ellipse = plt.matplotlib.patches.Ellipse(
        (center_x, center_y), width=stadium_length, height=stadium_width, fill=False, color='black', lw=2
    )
    ax.add_patch(ellipse)

    # Calculate seat positions in oval stadium
    num_rows = len(seats)
    seats_per_row = len(seats[0])
    zone_size = seats_per_row // num_zones
    total_seats = num_rows * seats_per_row

    seat_numbers = list(range(1, total_seats + 1))
    np.random.shuffle(seat_numbers)

    for row in range(num_rows):
        for seat in range(seats_per_row):
            zone_index = min(seat // zone_size, num_zones - 1)
            zone_color = zone_colors[zone_index]
            angle = (seat / seats_per_row) * np.pi * 2
            x = center_x + (radius_x - row * stadium_width / (2 * num_rows)) * np.cos(angle)
            y = center_y + (radius_y - row * stadium_width / (2 * num_rows)) * np.sin(angle)
            seat_num = seat_numbers.pop(0)
            circle = plt.Circle((x, y), 0.2, color=zone_color, alpha=0.7)
            ax.add_patch(circle)
            plt.text(x, y - 0.5, str(seat_num), ha='center', va='center', fontsize=8)

    plt.xlim(0, stadium_length)
    plt.ylim(0, stadium_width)
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage:
num_zones = 4
seats_per_row = 20
num_rows = 5
num_members = 40
num_friends = 60


# allocated_seats = asei.rand_alloc_seats(num_members, num_friends, num_zones)
allocated_seats = asei.allocate_seats(num_members, num_friends, num_rows, seats_per_row)
print("allocated seats:")
print(allocated_seats)
zone_colors = ['blue', 'green', 'red', 'yellow']  # Color for each zone
prif.print_member_friends(allocated_seats)
draw_oval_stadium(allocated_seats, num_zones, zone_colors)
