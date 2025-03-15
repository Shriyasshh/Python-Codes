import re

pattern = "was"
p=r"[A-Z]+ales"

text='''Cyfeilliog (died c. 927) was a bishop in south-east Wales. The location and extent of his diocese is uncertain, but lands granted to him are mainly close to Caerwent, suggesting that his diocese covered Gwent, possibly extending into Ergyng (now south-west Herefordshire). He is recorded in charters dating from the mid-880s to the early tenth century. In 914 he was captured by the Vikings and ransomed by Edward the Elder, King of the Anglo-Saxons, for 40 pounds of silver. Edward's assistance is regarded by historians as evidence that he inherited the overlordship of his father, Alfred the Great, over the south-east Welsh kingdoms. Cyfeilliog is probably the author of a cryptogram (encrypted text) which was added as a marginal note to the ninth-century collection of poetry known as the Juvencus Manuscript. '''


#word 'search' - search for  1st a pattern

# match=re.search(pattern,text)
match=re.search(p,text)  
print(match)



#word finditer - search for all  patterns in the text

# matches=re.finditer(p,text)
matches=re.finditer(pattern,text)
for i in matches:
    # print(i)
    print(i.span())
    print(text[i.span()[0]:i.span()[1]])


#Documentation
# https://docs.python.org/3/library/re.html
# https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
# regex website