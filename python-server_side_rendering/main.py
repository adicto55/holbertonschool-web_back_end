"""
Main file to test the invitation generation program.
"""

from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

print("=" * 50)
print("Generating invitations from template...")
print("=" * 50)

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)

print("\n" + "=" * 50)
print("Testing error handling cases...")
print("=" * 50)

# Test Case 1: Empty template
print("\nTest 1: Empty template")
generate_invitations("", attendees)

# Test Case 2: Empty attendees list
print("\nTest 2: Empty attendees list")
generate_invitations(template_content, [])

# Test Case 3: Invalid template type
print("\nTest 3: Invalid template type (integer)")
generate_invitations(123, attendees)

# Test Case 4: Invalid attendees type
print("\nTest 4: Invalid attendees type (string)")
generate_invitations(template_content, "not a list")

# Test Case 5: Attendees list with non-dict elements
print("\nTest 5: Attendees list with non-dict elements")
generate_invitations(template_content, [{"name": "Alice"}, "not a dict"])
