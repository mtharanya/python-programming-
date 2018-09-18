start = 0
end = 0

while start < 2 or end <= start:
    start = int(raw_input("Enter start -> "))
    end = int(raw_input("Enter end -> "))

print sum([x for x in range(start, end+1) if x % 2 == 0])
