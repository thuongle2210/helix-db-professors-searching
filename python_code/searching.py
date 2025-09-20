import helix
from sentence_transformers import SentenceTransformer
import json


model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
db = helix.Client(local=True, port=6973, verbose=True)

## num1:
query = "Find me a professor who familiar with big datasets for security purpose"
embedded_query_vector = model.encode(query).astype(float).tolist()
    
results = db.query("search_similar_professors_by_research_area_and_description", 
{"query_vector": embedded_query_vector, "k": 5})

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
