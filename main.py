#dictionary program
import requests
#get word from user
word=input("What word please ? ")
diction="https://api.dictionaryapi.dev/api/v2/entries/en/"+word
response=requests.get(diction)
#check if there was an error or not
if response.status_code==200:
  #convert json to python understandable format
  answer=response.json()
  try:
    meaning=answer[0]["meanings"][0]
    definition=meaning["definitions"][0]["definition"]
    #checks if theres syn and anton ,if none it leaves them empty
    synonyms=meaning["definitions"][0].get("synonyms",[])
    antonyms=meaning["definitions"][0].get("antonyms",[])
    
    sentence=f"{word.capitalize()} means {definition} . "
    #checks if synonyms and antonyms are there to add to sentence
    if synonyms:
      sentence += f" Synonym: {synonyms[0]}."
    if antonyms:
      sentence += f" Antonym: {antonyms[0]}."

    print(sentence)
    #if there was error it prints the following
  except Exception:
    print("Sorry there was an issue")
else:
  print("Could not get info !")
  