#Fake News Haedlines Genrator Project
#PROJECT 1/25

import random
import time

#Categories Subjects to use

tech = [
"AI Researchers","Software Engineers","Developers","Tech CEOs","Robotics Experts",
"Cybersecurity Experts","Data Scientists","Startup Founders","Engineers","IT Teams"
]

politics = [
"Government","World Leaders","Ministers","Officials","Parliament Members",
"Policy Makers","Diplomats","Senators","Judges","Political Leaders"
]

sports = [
"Football Players","Cricket Teams","Athletes","Coaches","Olympic Players",
"Captains","Teams","Strikers","Bowlers","Defenders"
]

entertainment = [
"Actors","Bollywood Stars","Singers","Influencers","Directors",
"Producers","YouTubers","Content Creators","Models","Artists"
]


# Middle part of the headline(wghat they done)

tech_actions = [
"develop","build","launch","upgrade","automate","design","create","test","deploy","improve"
]

politics_actions = [
"announce","approve","reject","introduce","debate","sign","enforce","discuss","review","propose"
]

sports_actions = [
"win","lose","defeat","dominate","prepare","train","compete","lead","challenge","perform"
]

entertainment_actions = [
"release","create","announce","perform","promote","produce","direct","launch","record","stream"
]

#From what they do 

tech_work = [
"AI system","robot model","software platform","automation tool","data system",
"mobile app","cybersecurity system","cloud platform","AI model","tech product"
]

politics_work = [
"new law","policy reform","economic plan","bill","agreement",
"security policy","tax reform","development plan","government scheme","budget plan"
]

sports_work = [
"match","tournament","championship","league match","final game",
"training session","series","competition","sports event","season"
]

entertainment_work = [
"new movie","music album","song","web series","video",
"film project","live show","concert","social media content","ad campaign"
]

#Where wok done

places = [
"in a major city","in a stadium","in parliament","on social media",
"in a research center","in a secret lab","in a corporate office",
"in a university","in a film studio","in a training camp"
]

tones = [
"BREAKING","NORMAL","FUNNY","SHOCKING","DRAMATIC"
]


history = [] 


def type_print(text):
    words = text.split()
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(0.2)
    print()


def headline(category, tone):

    # Categories
    if category == "1":
        sub = random.choice(tech)
        act = random.choice(tech_actions)
        obj = random.choice(tech_work)

    elif category == "2":
        sub = random.choice(politics)
        act = random.choice(politics_actions)
        obj = random.choice(politics_work)

    elif category == "3":
        sub = random.choice(sports)
        act = random.choice(sports_actions)
        obj = random.choice(sports_work)

    elif category == "4":
        sub = random.choice(entertainment)
        act = random.choice(entertainment_actions)
        obj = random.choice(entertainment_work)

    else:  
        all_sub = tech + politics + sports + entertainment
        all_act = tech_actions + politics_actions + sports_actions + entertainment_actions
        all_obj = tech_work + politics_work + sports_work + entertainment_work

        sub = random.choice(all_sub)
        act = random.choice(all_act)
        obj = random.choice(all_obj)

    place = random.choice(places)

    #Tones logic 

    if tone == "1":  
        return f"{sub} {act} {obj} {place}"

    elif tone == "2":  
        template = [
            f"{sub} {act} {obj} {place}",
            f"{sub} {act} {obj} during recent developments {place}",
            f"{sub} {act} {obj} in latest update {place}"
        ]
        return random.choice(template)

    elif tone == "3":  
        template = [
            f"{sub} accidentally {act} {obj} {place}",
            f"{sub} tries to {act} {obj} but things go wrong {place}",
            f"{sub} {act} {obj} after watching tutorials online {place}"
        ]
        return random.choice(template)

    elif tone == "4":  
        return f"{sub} secretly {act} {obj} {place}"

    elif tone == "5":
        return f"{sub} finally {act} {obj} {place}"

    elif tone == "6":  
        randomtone = str(random.randint(1,5))
        return headline(category, randomtone)


while True:

    print("\n=== Fake News Headlines Generator ===")
    print("1. Generate Headlines")
    print("2. Exit")

    try:
        choice = input("\nEnter choice: ")

        if choice == "1":

            print("\nSelect Category Below:")
            print("       ")
            print("1. Tech")
            print("2. Politics")
            print("3. Sports")
            print("4. Entertainment")
            print("5. Random")
            print("       ")

            cat = input("Enter category: ")

            print("\nSelect Tone:")
            print("       ")
            print("1. Breaking")
            print("2. Normal")
            print("3. Funny")
            print("4. Shocking")
            print("5. Dramatic")
            print("6. Mixed")
            print("       ")

            tone = input("Enter tone: ")

            print("\n Generating Headlines... \n")
            time.sleep(1)

            for i in range(1,6):
                
                line = headline(cat, tone)
                history.append(line)
                
                print(f"{i}. ", end="")
                
                type_print(line)

            print("\n----------------------")

        elif choice == "2":

            if len(history) > 1:
                save = input("Do you want to save generated headlines (yes/no): ")

                if save.lower() == "yes":
                    filename = input("Enter file name: ")

                    with open(filename + ".txt", "w") as file:
                        for line in history:
                            file.write(line + "\n")  

                    print(f"File saved as : {filename}.txt ✔️")

            print("Goodbye ")
            break

        else:
            print("Invalid input enterred")

    except (TypeError,ValueError):
        print("Enter Enter Only Numbers")
        print("Select From The Options")