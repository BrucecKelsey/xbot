import random

based_comments = [
    "Based Coded",
    "$based",
    "$based moon",
    "Based af",
    "Make america based again",
    "Stay based",
    "$Based af",
    "All in $based",
    "$based next 1000x",   
    "Based 🗿"
]

def get_random_based_comment():
    based_comments = [
    "Based Coded",
    "$based",
    "$based moon",
    "Based af",
    "Make america based again",
    "Stay based",
    "$Based af",
    "All in $based",
    "$based next 1000x",   
    "Based 🗿"]
    return random.choice(based_comments)

if __name__ == "__main__":
    print(get_random_based_comment())