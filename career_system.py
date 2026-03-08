
def recommend_career(skills):
    mapping={
        "Java":["Software Engineer","Backend Developer"],
        "SQL":["Data Analyst","Database Administrator"],
        "Python":["Data Scientist","ML Engineer"]
    }
    result=set()
    for s in skills:
        if s in mapping:
            result.update(mapping[s])
    print("Recommended careers:")
    for r in result:
        print("-",r)

recommend_career(["Java","SQL"])
