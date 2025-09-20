import helix
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
db = helix.Client(local=True, port=6973, verbose=True)


research_areas = {
    "Computer Vision for Basketball": "Designing CNN and Transformer architectures that track player pose, ball trajectory, and court zones to quantify defensive pressure and shooting mechanics.",
    "Predictive Modelling & Simulation": "Building Monte-Carlo and sequence models that forecast possession outcomes and season performance using play-by-play and spatial data.",
    "Sports Analytics with Large Language Models": "Leveraging LLMs to explain model outputs, auto-generate commentary, and mine historical game archives for strategic patterns.",
    "Wearable Sensor Data Mining": "Applying time-series and graph learning techniques to inertial-measurement signals for fatigue monitoring and injury prevention.",
    "Fairness & Ethics in Sports AI": "Studying algorithmic bias and ensuring equitable analytics across different leagues, genders, and play styles."
}

research_area_ids = {}
for research_area in research_areas:
    print("research_area:", research_area)
    research_area_node = db.query("create_research_area", {"name": research_area})
    print("research_area_node:", research_area_node)
    research_area_ids[research_area] = research_area_node[0]['research_area']['id']

departments = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"]
department_ids = {}
for department in departments:
    department_node = db.query("create_department", {"name": department})
    department_ids[department] = department_node[0]['department']['id']

universities = ["Uni X", "Uni Y", "Uni Z"]
university_ids = {}
for university in universities:
    university_node = db.query("create_university", {"name": university})
    university_ids[university] = university_node[0]['university']['id']

labs = {"Basketball Data Science Lab": "An interdisciplinary group combining data science, biomechanics, and sport psychology to create next-generation analytics tools for basketball."}
lab_ids = {}
for lab in labs:
    lab_node = db.query("create_lab", {"name": lab, "research_focus": labs[lab]})
    lab_ids[lab] = lab_node[0]['lab']['id']



professors = [
    {
        "name": "James",
        "title": "Assistant Professor",
        "page": "https://james.com",
        "department": ["Computer Science"],
        "university": ["Uni X"],
        "bio": "James is an Assistant Professor whose work sits at the intersection of basketball analytics, computer vision, and large-scale machine learning. His research focuses on turning raw player-tracking video, wearable-sensor streams, and play-by-play logs into actionable insights for teams, coaches, and broadcasters. Signature projects include ShotNet— a deep learning model that predicts shot success probability in real time— and DunkGPT, a language model fine-tuned on millions of play descriptions to generate advanced scouting reports.",
        "key_research_areas": [
            {
                "area": "Computer Vision for Basketball",
                "description": "Designing CNN and Transformer architectures that track player pose, ball trajectory, and court zones to quantify defensive pressure and shooting mechanics."
            },
            {
                "area": "Predictive Modelling & Simulation",
                "description": "Building Monte-Carlo and sequence models that forecast possession outcomes and season performance using play-by-play and spatial data."
            },
            {
                "area": "Sports Analytics with Large Language Models",
                "description": "Leveraging LLMs to explain model outputs, auto-generate commentary, and mine historical game archives for strategic patterns."
            }
        ],
        "labs": [
            {
                "name": "Basketball Data Science Lab",
                "research_focus": "An interdisciplinary group combining data science, biomechanics, and sport psychology to create next-generation analytics tools for basketball."
            }
        ]
    },
    {
        "name": "Thuong Le",
        "title": "Database Engineer",
        "page": "https://james.com",
        "department": ["Computer Science"],
        "university": ["Uni X"],
        "bio": "Thuong Le is an Assistant Professor whose work sits at the intersection of basketball analytics, computer vision, and large-scale machine learning. His research focuses on turning raw player-tracking video, wearable-sensor streams, and play-by-play logs into actionable insights for teams, coaches, and broadcasters. Signature projects include ShotNet— a deep learning model that predicts shot success probability in real time— and DunkGPT, a language model fine-tuned on millions of play descriptions to generate advanced scouting reports.",
        "key_research_areas": [
            {
                "area": "Fairness & Ethics in Sports AI",
                "description": "Studying method bias and acomplishing equitable analytics across different games, appearance"
            }
        ],
        "labs": [
            {
                "name": "Basketball Data Science Lab",
                "research_focus": "An interdisciplinary group combining data science, biomechanics, and sport psychology to create next-generation analytics tools for basketball."
            }
        ]
    }
]

for professor in professors:
    # Create Professor Node
    professor_node =db.query("create_professor", {"name": professor["name"], "title": professor["title"], "page": professor["page"], "bio": professor["bio"]})

    professor_id = professor_node[0]['professor']['id']

    # Link Professor to Research Area
    for research_area in professor["key_research_areas"]:
        if research_area['area'] in research_areas:
            research_area_id = research_area_ids[research_area['area']]
            db.query("link_professor_to_research_area", {"professor_id": professor_id, "research_area_id": research_area_id})

    # Link Professor to Department
    for department in professor["department"]:
        if department in department_ids:
            department_id = department_ids[department]
            db.query("link_professor_to_department", {"professor_id": professor_id, "department_id": department_id})

    # Link Professor to University
    for university in professor["university"]:
        if university in university_ids:
            university_id = university_ids[university]
            db.query("link_professor_to_university", {"professor_id": professor_id, "university_id": university_id})

    # Link Professor to Lab
    for lab in professor["labs"]:
        if lab['name'] in lab_ids:
            lab_id = lab_ids[lab['name']]
            db.query("link_professor_to_lab", {"professor_id": professor_id, "lab_id": lab_id})

    # Create Research Area Embedding
    research_area_and_description = "\n".join([research_area['area'] + ": " + research_area['description'] for research_area in professor['key_research_areas']])
    research_area_and_description_embedding = model.encode(research_area_and_description).astype(float).tolist()
    db.query("create_research_area_embedding", {"professor_id": professor_id, "areas_and_descriptions": research_area_and_description, "vector": research_area_and_description_embedding})




# ask and answer:

## num1:
# query = "Find me a professor who does computer vision for basketball"
# embedded_query_vector = model.encode(query).astype(float).tolist()
    
# results = db.query("search_similar_professors_by_research_area_and_description", 
# {"query_vector": embedded_query_vector, "k": 1})

# print(results)


## num2:
query = "Find me a professor who ensure the equality"
embedded_query_vector = model.encode(query).astype(float).tolist()
    
results = db.query("search_similar_professors_by_research_area_and_description", 
{"query_vector": embedded_query_vector, "k": 1})

print(results)

## 1.“What professors does X research area?”

# professors_by_research_area_name = db.query("get_professor_by_research_area_name", {"research_area_name": "X"})
# print(professors_by_research_area_name)

# ## 2.“What professors are working in X University?”
# professors_by_university_name = db.query("get_professors_by_university_name", {"university_name": "X"})
# print(professors_by_university_name)

# ## 3.“What professors are working in X Department?”
# professors_by_department_name = db.query("get_professors_by_department_name", {"department_name": "X"})
# print(professors_by_department_name)

# ## 4.“What professors are working in the X University and are working in X department?”
# professors_by_university_and_department_name = db.query("get_professors_by_university_and_department_name", {"university_name": "X", "department_name": "X"})
# print(professors_by_university_and_department_name)

# ## 5.“I like doing research in Large Language Models, can you recommend me some professors doing this in X University?”
# professors_by_research_area_and_university_name = db.query("get_professors_by_research_area_and_university_name", {"research_area_name": "Large Language Models", "university_name": "X"})
# print(professors_by_research_area_and_university_name)
