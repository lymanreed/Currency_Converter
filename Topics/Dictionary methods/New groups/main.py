# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
groups_n_kids = {}

n_groups = int(input())
c = 0
for group in groups:
    if c < n_groups:
        groups_n_kids[group] = int(input())
        c += 1
    else:
        groups_n_kids[group] = None

print(groups_n_kids)
