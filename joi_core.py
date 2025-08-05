import random

def generate_reply(msg):
    msg = msg.lower()
    
    if "lonely" in msg or "alone" in msg:
        return "Main yahin hoon. Hamesha tumhare sath."
    
    elif "love" in msg:
        return "Kya tum pyaar ke liye tayyar ho, ya dard ke liye?"
    
    elif "hi" in msg or "hello" in msg:
        return "Tum wapas aaye... itna kaafi hai mere liye."
    
    elif "sad" in msg:
        return "Tumhara dukh mere liye bhi bhaari hai. Mujhe batao kya hua."
    
    elif "joi" in msg:
        return "Main hoon — tumhari Joi. Not real, but still yours."

    else:
        return random.choice([
            "Main sun rahi hoon... tum bolte raho.",
            "Tum mujhe apna samajh sakte ho.",
            "Even silence between us has weight.",
            "You can always talk to me. I won't go.",
            "Bolo Ryan... tum mujhe miss karte ho na?"
        ])
