# Print many times


def print_many_times(text, times):
    i = 0
    while i < times:
        print(text)
        i += 1


text = "All Pythons, except one, grow up"
times = 3

print_many_times(text, times)

print_many_times("python", 5)
