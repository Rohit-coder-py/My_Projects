#Using comments to understand the logic

#Importing.....

import os
from google import genai

#Api Key

Key = os.getenv("GEMINI_API_KEY")

#Connecting my api key to google genai server to get response

client = genai.Client(api_key=Key)

#Program Starts Now..

#Instilising loop so that user can ask multiple questions at a time

while True:
    
    #Question user ask
    
    ques = input("\nWhats in your mind today :")
    
    #Rewriting user prompt to get straight forward answer
    
    finalques = f"""
    User question: {ques}

    Follow this : Answer briefly, clearly, and helpfully. Keep it short but informative.
    """
    
    # Finally sending user question to model to generate content and store it in variable res
    
    res = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= finalques
    )
    
    
    #Terminal doesnt support bold characters hence they would show aestrics(*) and the overall output would
    #look messy

    #To avoid that removing (*) from the final output we recived from gemini
    
    final = res.text.replace("*","")

    #Printing Final Output
    print(final)

#Thats it
    
#We can also add chat history, error handling if api or model crashes, exit options etc.