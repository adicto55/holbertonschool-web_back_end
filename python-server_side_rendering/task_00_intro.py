"""
Templating Program - Generate personalized invitation files from a template.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template with placeholders.
    
    Args:
        template (str): The template string with placeholders like {name}, {event_title}, etc.
        attendees (list): A list of dictionaries containing attendee information.
    
    Returns:
        None. Creates output files named output_1.txt, output_2.txt, etc.
    """
    
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    
    if not isinstance(attendees, list):
        print(f"Error: Invalid input type for attendees. Expected list, got {type(attendees).__name__}.")
        return
    
    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return
    
    # Check if template is empty
    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Define placeholders to replace
    placeholders = ["name", "event_title", "event_date", "event_location"]
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Start with the template
        output_content = template
        
        # Replace each placeholder with the corresponding value
        for placeholder in placeholders:
            # Get the value from the attendee dictionary, use "N/A" if missing or None
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            
            # Replace the placeholder in the template
            output_content = output_content.replace(
                "{" + placeholder + "}",
                str(value)
            )
        
        # Generate output filename
        output_filename = f"output_{index}.txt"
        
        # Write the processed template to the output file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated {output_filename}")
        except IOError as e:
            print(f"Error writing to {output_filename}: {e}")
