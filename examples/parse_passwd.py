# root:*:0:0:System Administrator:/var/root:/bin/sh

users = []
with open("/etc/passwd") as f:
    for line in f:
        fields = line.split(':')
        users.append(fields[0])

with open("/tmp/users", "w") as u:
    for user in users:
        u.write("User: {}\n".format(user))
