def total_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


t1 = total_seconds(int(input()), int(input()), int(input()))
t2 = total_seconds(int(input()), int(input()), int(input()))

print(t2 - t1)
