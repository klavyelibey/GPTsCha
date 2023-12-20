class CharacterForm:
    def __init__(self):
        # Create a dictionary to store all character information
        self.character = {
            "Basic Information": {
                "Name": "",          # Character's name (string)
                "Age": 0,            # Character's age (integer)
                "Gender": "",        # Character's gender (string)
                "Ethnicity": ""      # Character's ethnicity (string)
            },
            "Physical Appearance": {
                "Height": 0,         # Character's height (integer)
                "Weight": 0,         # Character's weight (integer)
                "Hair": {
                    "Color": "",     # Character's hair color (string)
                    "Style": ""      # Character's hair style (string)
                },
                "Eyes": {
                    "Color": "",     # Character's eye color (string)
                    "Shape": ""      # Character's eye shape (string)
                },
                "Facial Features": "", # Character's facial features (string)
                "Body Type": "",       # Character's body type (string)
                "Clothing Style": ""   # Character's clothing style (string)
            },
            "Personality and Behavior": {
                "Main Personality": "",  # Character's main personality trait (string)
                "Attitudes and Manners": "", # Character's attitudes and manners (string)
                "Habits": "",           # Character's habits (string)
                "Motivation Sources": "",  # Character's motivation sources (string)
                "Values": "",           # Character's values (string)
                "Beliefs": "",          # Character's beliefs (string)
                "Phobias": ""           # Character's phobias (string)
            },
            "Social Environment": {
                "Family Background": "",     # Character's family background (string)
                "Friendships": "",           # Character's friendships (string)
                "Romantic Relationships": ""  # Character's romantic relationships (string)
            },
            "Past and Experiences": {
                "Childhood": "",             # Character's childhood experiences (string)
                "School Years": "",          # Character's school years (string)
                "Adulthood": ""              # Character's adulthood experiences (string)
            },
            "Professional Career": {
                "Educational Background": {
                    "Degree": "",             # Character's educational degree (string)
                    "University": "",         # Character's university information (string)
                    "Major": "",              # Character's major (string)
                    "GPA": 0.0                # Character's GPA (float)
                },
                "Field of Work": {
                    "Sector": "",            # Character's work sector (string)
                    "Position": ""           # Character's work position (string)
                },
                "Skills": []                 # Character's skills (list)
            },
            "Hobbies and Interests": {
                "Sports": "",               # Character's interest in sports (string)
                "Art": "",                  # Character's interest in art (string)
                "Support Groups": ""        # Character's involvement in support groups (string)
            },
            "Expertise Description": "",         # Character's expertise description (string)
            "Elaboration": [],                   # Details for each expertise area (list)
            "Specialized Information": [],       # Character's specialized information (list)
            "Sub-Concepts": [],                  # Special concepts and techniques for each expertise area (list)
            "Specific Skills": [],               # Character's specific skills and projects (list)
            "Niche Areas": [],                  # Information about niche areas of expertise (list)
            "Dynamic Development": "",           # Description of the character's dynamic development (string)
            "New Trends and Technologies": [],   # Trends and technologies to keep the character updated (list)
            "Consistency": "",                   # Description of character consistency and realism (string)
            "Integration": "",                  # Description of how character's knowledge and skills integrate into the story (string)
            "Creativity": ""                    # Creative ideas to enrich the character (string)
        }

    def fill(self):
        for category in self.character:
            if isinstance(self.character[category], list):
                values = input(f"{category} (separate with commas): ").split(',')
                self.character[category] = [value.strip() for value in values]
            else:
                value = input(f"{category}: ")
                self.character[category] = value

    def display_character(self):
        import json
        print("\nCharacter Information:")
        print(json.dumps(self.character, indent=4, ensure_ascii=False))

# Create a character using the form
form = CharacterForm()
form.fill()
form.display_character()
