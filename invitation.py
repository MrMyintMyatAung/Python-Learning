# Original list of people to invite
invitees = ["Albert Einstein", "Maya Angelou", "Nelson Mandela"]

# Print the name of the guest who can't make it
guest_unable_to_attend = invitees[1]
print(f"Unfortunately, {guest_unable_to_attend} can't make it to dinner.\n")

# Replace the guest who can't make it with a new invitee
invitees[1] = "Malala Yousafzai"

# Sending new invitations using a loop
for person in invitees:
    print(f"Dear {person},\nI would be honored to invite you to dinner. Looking forward to an enlightening evening!\n")
    
