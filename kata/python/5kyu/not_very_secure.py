def alphanumeric(password):
    return False if not password or ' ' in password or '_' in password or not all([c.isalnum() for c in password]) else True



tests = [
    ("hello world_", False),
    ("PassW0rd", True),
    ("     ", False)
]
for s, b in tests:
    print(alphanumeric(s), b)
