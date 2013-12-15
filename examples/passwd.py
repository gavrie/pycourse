with open("/etc/passwd") as f:
    for line in f:
        fields = line.strip().split(':')
        print fields[0]
