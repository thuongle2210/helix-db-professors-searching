import random
import json
departments = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"]
universities = ["Uni A", "Uni B", "Uni C", "Uni D", "Uni E"]
research_areas = [
    ("Computer Vision", "Designing models to analyze visual data"),
    ("Natural Language Processing", "Developing algorithms for human language understanding"),
    ("Machine Learning", "Building predictive models from data"),
    ("Robotics", "Designing intelligent machines"),
    ("Quantum Computing", "Exploring computation using quantum-mechanical phenomena"),
    ("Bioinformatics", "Applying computation to biological data"),
    ("Cybersecurity", "Protecting systems from digital attacks"),
    ("Data Mining", "Extracting patterns from large datasets"),
    ("Algorithms", "Developing efficient computational procedures"),
    ("Software Engineering", "Designing and maintaining software systems"),
]
labs = [
    ("AI Lab", "Research on artificial intelligence techniques"),
    ("Robotics Lab", "Innovations in robotic systems and automation"),
    ("Bioinformatics Lab", "Computational biology and genetics projects"),
    ("Data Science Lab", "Big data analytics and visualization"),
    ("Security Lab", "Studies on computer and network security"),
]

def generate_professor_profile(idx):
    name = f"Professor {chr(65 + (idx % 26))}{idx}"
    title = random.choice(["Assistant Professor", "Associate Professor", "Professor"])
    department = random.choice(departments)
    university = random.choice(universities)
    bio = f"{name} works in the {department} department at {university}. Their research focuses on cutting-edge topics in {department.lower()}."
    
    num_areas = random.randint(1, 3)
    key_research_areas = []
    for i in range(num_areas):
        area, desc = random.choice(research_areas)
        key_research_areas.append({
            "area": area,
            "description": desc
        })
    
    num_labs = random.randint(0, 2)
    associated_labs = []
    for i in range(num_labs):
        lab_name, research_focus = random.choice(labs)
        associated_labs.append({
            "name": lab_name,
            "research_focus": research_focus
        })
    
    profile = {
        "name": name,
        "title": title,
        "department": [department],
        "university": [university],
        "bio": bio,
        "key_research_areas": key_research_areas,
        "labs": associated_labs,
        "page": f"https://{name.replace(" ","")}.com"
    }
    return profile

# Generate 100 profiles
professors = [generate_professor_profile(i) for i in range(100)]

# Example print first 2 profiles
for prof in professors[:2]:
    print(prof)

# Write to JSON file
with open("./python_code/generate_professor_profiles/professors.json", "w", encoding="utf-8") as f:
    json.dump(professors, f, indent=4, ensure_ascii=False)
print("100 professor profiles generated and saved to professors.json")