#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy
nlp = spacy.load("en_core_web_lg")


# In[1]:


import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'


# In[2]:


get_ipython().system('pip install -U pip setuptools wheel')
get_ipython().system('pip install -U spacy')

get_ipython().system('python -m spacy download en_core_web_sm')


# In[3]:


import spacy
nlp = spacy.load("en_core_web_lg")


# In[4]:


import pandas as pd


# In[6]:


df=pd.read_csv('all_the_news.csv')


# In[7]:


df


# In[8]:


sources = df["publication"].unique()
print(sources)


# In[9]:


condition = df["publication"].isin(["New York Times"])

content_df = df.loc[condition, :]["content"][:100]

content_df.shape


# In[10]:


content_df.head()


# In[11]:



text = "He would not tell the police what he had learned"

doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop  )


# In[17]:


text = "He would not tell the police what he had learned"

doc = nlp(text)

for token in doc:
    print(token.tag_)


# In[19]:


for ent in doc.ents:
    entity_text = ent.text
    entity_type = str(ent.label_) # e.g. 'GPE'
    


# In[35]:


entity_tex
for item in content_df[:1]:
    doc=nlp(item)
    for ent in doc.ents:
        


# In[36]:


spacy.explain('NORP')


# In[34]:


for i in content_df[:1]:
    print(i)


# In[42]:


d={"a":2,"b":3}


# In[48]:


if "a" in d.keys():
    print(d.get("a"))


# In[46]:


d.get("a")


# In[47]:


q


# In[63]:


named_entities


# In[67]:


current={}


# In[72]:


named={'GPE': {'WASHINGTON': 18,
  'Obama': 2,
  'the District of Columbia Circuit': 1,
  'Manhattan': 30,
  'New York City': 13,
  'Bronx': 26,
  'Upper Manhattan': 2,
  'Lower Manhattan': 2},'PERSON': {'Obama': 114,
  'Donald J. Trump’s': 4,
  'Phillip J. Blando': 1,
  'Rosemary M. Collyer': 1,
  'Collyer': 2,
  'Trump': 255,
  'John A. Boehner': 2,
  'Gola White': 1,
  'James Fernandez': 2,
  'Fernandez': 23,
  'Maria Fernandez': 1,
  'Sgt': 2}}


# In[73]:


named.keys()


# In[74]:


if 'GPE' in named.keys():
    current=named.get('GPE')


# In[75]:


current


# In[83]:


current['WASHINGTON'] = current_ents.get(entity_text, 0) + 1


# In[84]:


current


# In[106]:


named_entities


# In[ ]:





# In[105]:


content_df[:100]


# In[104]:


named_entities


# In[90]:


named_entities


# In[86]:


named_entities


# In[78]:


len(entity_type)


# In[81]:


doc.ents


# In[122]:


data_frame


# In[143]:


def return_entities_and_processed_docs(data_frame):
    named_entities = {}
    processed_docs = []
    
    for item in data_frame:
        doc = nlp(item)
        processed_docs.append(doc)
        
        for ent in doc.ents:
            entity_text = ent.text # e.g. WASHINGTON
            entity_type = str(ent.label_) # e.g. 'GPE'
            current_ents = {}
            
            #If the Type, say 'GPE' already exists in named_entities then get it      
            if entity_type in named_entities.keys():
                current_ents = named_entities.get(entity_type)
                
            # and then increase the counter number of the actual entity_text e.g. 'Manhattan'
            # this will just add 1 to the inner dict
            current_ents[entity_text] = current_ents.get(entity_text, 0) + 1
            
            # then make this updated inner dict to be the new inner dict for
            # the final named_entities
            named_entities[entity_type] = current_ents
    return named_entities, processed_docs


named_entities, processed_docs = return_entities_and_processed_docs(content_df)
                


# In[144]:


named_entities


# In[183]:


named_entities.keys()


# In[ ]:


#https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/


# In[202]:


for key in named_entities.keys():        
    entities = named_entities.get(key)
    print(key)
    

    # Sort the entries by their frequency in descending 
    # order and print out the most frequent n ones
    sorted_keys = sorted(entities, key=entities.get, reverse=True )
    print('this is sorted',sorted_keys)
    for item in sorted_keys[:10]:
        if entities.get(item)>1:
            print(" " + item + ":",entities.get(item) )


# In[205]:


def print_top_10(named_entities):
    for key in named_entities.keys():
        entities=named_entities.get(key)
        print(key)
        sorted_keys=sorted(entities,key=entities.get,reverse=True)
        for item in sorted_keys[:10]:
            if entities.get(item)>1:
                print(" " + item + ":",entities.get(item) )
print_top_10(named_entities)                


# In[ ]:


#We need to figure out what is the subject and what is the object. From the given entities we'll get entity list
# as The new York times and Apple. We need to create a dependancy tree where we'll find out that the word
# wrote(verb) has two children(times and about). We need to pick the entire multiword expression The New york times


# In[237]:


a="The New York Times wrote about Apple"
req='The New York Times'
doc=nlp(a)
index=[]
for ent in doc.ents:
    print(ent)
    if ent.text==req:
        for i in range(len(req.split())):
            index.append(i)
index


# In[ ]:


#Que how do we get the entire expression ' The New York Times' as the subject? Check rohan paul sir's github code


# In[388]:


def calculate_entity_span(document,entity):
    indexes=[]
    for ent in document.ents:
        if ent.text==entity:
            for i in range(int(ent.start),int(ent.end)): #question about ent.start,ent.end. Also could do range(ent.text)
                indexes.append(i)
    return indexes            
    


# In[389]:


entity = "The New York Times"

sentences = "The New York Times wrote about Apple"
doc=nlp(sentences)
calculate_entity_span(doc,entity)


# In[390]:


sentences = ["The New York Times wrote about Apple"]

for sentence in sentences:
    print(sentence)
    doc = nlp(sentence)
    for token in doc:
        print(token)


# In[391]:


sentences = ["The New York Times wrote about Apple"]

for sentence in sentences:
    print(sentence)
    doc = nlp(sentence)
    for token in doc:
        print(token,token.dep_,token.pos_)


# In[ ]:





# In[266]:


displacy.render(doc, style='dep')


# In[ ]:


#https://www.analyticsvidhya.com/blog/2021/12/dependency-parsing-in-natural-language-processing-with-examples/
#https://spacy.io/usage/linguistic-features/#navigating
#https://medium.com/data-science-in-your-pocket/dependency-parsing-associated-algorithms-in-nlp-96d65dd95d3e#:~:text=Dependency%20parsing%20helps%20us%20build,handsome%20boy%27)%20get%20changed.


# In[ ]:


#https://www.analyticsvidhya.com/blog/2021/12/dependency-parsing-in-natural-language-processing-with-examples/
#https://spacy.io/usage/linguistic-features/#navigating
#https://medium.com/data-science-in-your-pocket/dependency-parsing-associated-algorithms-in-nlp-96d65dd95d3e#:~:text=Dependency%20parsing%20helps%20us%20build,handsome%20boy%27)%20get%20changed.


# In[280]:


doc


# In[293]:


spacy.explain('ADP')


# In[283]:


displacy.render(doc, style='dep')


# In[ ]:





# In[355]:


entity = "The New York Times"

sentences = "The New York Times wrote about Apple"

doc = nlp(sentences)

calculate_entity_span(doc, entity)


# In[392]:


#Firs#Second Main
actions = []
action = ''
participant1 = ''
participant2 = ''

for token in doc:
    print('this is token',token)
    # Next, you identify the main verb expressing the main action in the sentence
    # To extract the relation, we have to find the ROOT of the sentence (which is also the verb of the sentence)
    if token.pos_ == "VERB" and token.dep_ == 'ROOT':
        # Initialize the indexes for the subject and the object related to the main verb
        subj_ind = -1
        obj_ind = -1
        # Store the main verb itself (token.text) in the action variable
        action = token.text
        print('this is action',action)
        children = [child for child in token.children ]
        print('this is children:',children)
        for child1 in children:
            print('this is child1',child1)
            # Find the subject via the nsubj relation and store it as participant1 
            # and its index as subj_ind
            if child1.dep_ == 'nsubj':
                participant1 = child1.text
                print('for {} this is participant1 {}'.format(child1,participant1))
                subj_ind = int(child1.i)
                print('for {} this is index {}'.format(child1,subj_ind))
            # If there is a preposition attached to the verb (e.g., “write about”), then
            # you need to search for the indirect object as the second participant. 
            if child1.dep_ == 'prep':
                print('child1 which is prep:',child1)
                participant2 = ''
                child1_children = [child for child in child1.children]
                print('child1_children',child1_children)
                
                for child2 in child1_children:
                    # If such an object is a noun or a proper noun, 
                    # you store it as participant2 and its index as obj_ind
                    if child2.pos_ == 'NOUN' or child2.pos_ == 'PROPN':
                        participant2 = child2.text
                        print('for {} this is participant2 {}'.format(child2,participant2))
                        obj_ind = int(child2.i)
                        print('for {} this is index {}'.format(child2,obj_ind))
                        # If at this point both participants of the main action have been identified and
                    # their indexes are included in the indexes of the words covered by the entity, 
                    # you add the action with two participants to the list of actions.
                if not participant2=="":
                    if subj_ind in indexes:
                        actions.append(entity + " " + action + " " + child1.text + " " + participant2)
                        print('Actions',actions)
                    elif obj_ind in indexes:
                        actions.append(participant1 + " " + action + " " + child1.text + " " + entity)
                        print('this is action of object when it is prep',actions)
                        print('actions',actions)

            # Otherwise, if there is no preposition attached to the verb,
            # participant2 is a direct object of the main verb, 
            # which can be identified via the dobj relation
            if child1.dep_ == 'dobj' and (child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN' ):
                participant2 = child1.text
                print('this is participant 2 when not prep',participant2)
                obj_ind = int(child1.i)
                print('this is obj_index 2 when not prep',obj_ind)
                # In this case, you apply the same strategy as above, 
                # adding the action with two participants to the list of actions. 
                if subj_ind in indexes:
                    actions.append(entity + " " + action + " " + participant2) 
                    print('this is action of subject when not prep',actions)
                elif obj_ind in indexes:
                    actions.append(participant1 + " " + action + " " + entity)
                    print('this is action of obj when not prep',actions)
# Finally if the final list of actions is not empty, 
# Finally if the final list of actions is not empty, 
# Print out the sentence and all actions together with the participants.
if not len(actions) == 0:
    print(f"\nSentence = {document}")
    for item in actions:
        print(item)      


# In[393]:


for sentence in sentences:
    doc = nlp(sentence)
    indexes = calculate_entity_span(doc, entity)
    calc_entity_subject_object(doc, entity, indexes)


# In[394]:


entity = "Kshitiz Khandelwal"

sentences = "Kshitiz Khandelwal plays basketball"

docu = nlp(sentences)

indexes=calculate_entity_span(docu, entity)


# In[406]:


#Second Main
actions = []
action = ''
participant1 = ''
participant2 = ''

for token in docu:
    print('this is token',token)
    # Next, you identify the main verb expressing the main action in the sentence
    # To extract the relation, we have to find the ROOT of the sentence (which is also the verb of the sentence)
    if token.pos_ == "VERB" and token.dep_ == 'ROOT':
        # Initialize the indexes for the subject and the object related to the main verb
        subj_ind = -1
        obj_ind = -1
        # Store the main verb itself (token.text) in the action variable
        action = token.text
        print('this is action',action)
        children = [child for child in token.children ]
        print('this is children:',children)
        for child1 in children:
            print('this is child1',child1)
            # Find the subject via the nsubj relation and store it as participant1 
            # and its index as subj_ind
            if child1.dep_ == 'nsubj':
                participant1 = child1.text
                print('for {} this is participant1 {}'.format(child1,participant1))
                subj_ind = int(child1.i)
                print('for {} this is index {}'.format(child1,subj_ind))
            # If there is a preposition attached to the verb (e.g., “write about”), then
            # you need to search for the indirect object as the second participant. 
            if child1.dep_ == 'prep':
                print('child1 which is prep:',child1)
                participant2 = ''
                child1_children = [child for child in child1.children]
                print('child1_children',child1_children)
                
                for child2 in child1_children:
                    # If such an object is a noun or a proper noun, 
                    # you store it as participant2 and its index as obj_ind
                    if child2.pos_ == 'NOUN' or child2.pos_ == 'PROPN':
                        participant2 = child2.text
                        print('for {} this is participant2 {}'.format(child2,participant2))
                        obj_ind = int(child2.i)
                        print('for {} this is index {}'.format(child2,obj_ind))
                        # If at this point both participants of the main action have been identified and
                    # their indexes are included in the indexes of the words covered by the entity, 
                    # you add the action with two participants to the list of actions.
                if not participant2=="":
                    if subj_ind in indexes:
                        actions.append(entity + " " + action + " " + child1.text + " " + participant2)
                        print(actions)
                    elif obj_ind in indexes:
                        actions.append(participant1 + " " + action + " " + child1.text + " " + entity)

            # Otherwise, if there is no preposition attached to the verb,
            # participant2 is a direct object of the main verb, 
            # which can be identified via the dobj relation
            if child1.dep_ == 'dobj' and (child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN' ):
                participant2 = child1.text
                print('this is participant 2 when not prep',participant2)
                obj_ind = int(child1.i)
                print('this is obj_index 2 when not prep',obj_ind)
                # In this case, you apply the same strategy as above, 
                # adding the action with two participants to the list of actions. 
                if subj_ind in indexes:
                    actions.append(entity + " " + action + " " + participant2) 
                    print('this is action of subject when not prep',actions)
                elif obj_ind in indexes:
                    actions.append(participant1 + " " + action + " " + entity)
                    print('this is action of obj when not prep',actions)
# Finally if the final list of actions is not empty, 
# Print out the sentence and all actions together with the participants.
            


# In[408]:


docu


# In[409]:


doc


# In[407]:


actions


# In[365]:


entity = "The New York Times"

sentences = "The New York Times wrote about Apple"

doc = nlp(sentences)

calculate_entity_span(doc, entity)


# In[338]:


indexes


# In[327]:


displacy.render(docu, style='dep')


# In[373]:


def calc_entity_subject_object(document, entity, indexes):
    actions = []
    action = ''
    participant1 = ''
    participant2 = ''
    
    for token in document:
        # Next, you identify the main verb expressing the main action in the sentence
        # To extract the relation, we have to find the ROOT of the sentence (which is also the verb of the sentence)
        if token.pos_ == "VERB" and token.dep_ == 'ROOT':
            # Initialize the indexes for the subject and the object related to the main verb
            subj_ind = -1
            obj_ind = -1
            # Store the main verb itself (token.text) in the action variable
            action = token.text
            children = [child for child in token.children ]
            for child1 in children:
                # Find the subject via the nsubj relation and store it as participant1 
                # and its index as subj_ind
                if child1.dep_ == 'nsubj':
                    participant1 = child1.text
                    subj_ind = int(child1.i)
                # If there is a preposition attached to the verb (e.g., “write about”), then
                # you need to search for the indirect object as the second participant. 
                if child1.dep_ == 'prep':
                    participant2 = ''
                    child1_children = [child for child in child1.children]
                    for child2 in child1_children:
                        # If such an object is a noun or a proper noun, 
                        # you store it as participant2 and its index as obj_ind
                        if child2.pos_ == 'NOUN' or child2.pos_ == 'PROPN':
                            participant2 = child2.text
                            obj_ind = int(child2.i)
                    
                    # If at this point both participants of the main action have been identified and
                    # their indexes are included in the indexes of the words covered by the entity, 
                    # you add the action with two participants to the list of actions.
                    if not participant2=="":
                        if subj_ind in indexes:
                            actions.append(entity + " " + action + " " + child1.text + " " + participant2)
                        elif obj_ind in indexes:
                            actions.append(participant1 + " " + action + " " + child1.text + " " + entity)
                            
                # Otherwise, if there is no preposition attached to the verb,
                # participant2 is a direct object of the main verb, 
                # which can be identified via the dobj relation
                if child1.dep_ == 'dobj' and (child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN' ):
                    participant2 = child1.text
                    obj_ind = int(child1.i)
                    # In this case, you apply the same strategy as above, 
                    # adding the action with two participants to the list of actions. 
                    if subj_ind in indexes:
                         actions.append(entity + " " + action + " " + participant2)
                    elif obj_ind in indexes:
                        actions.append(participant1 + " " + action + " " + entity)
    # Finally if the final list of actions is not empty, 
    # Print out the sentence and all actions together with the participants.
    if not len(actions) == 0:
        print(f"\nSentence = {document}")
        for item in actions:
            print(item)            


# In[374]:


for sentence in sentences:
    doc = nlp(sentence)
    indexes = calculate_entity_span(doc, entity)
    calc_entity_subject_object(doc, entity, indexes)


# In[384]:


actions = []
action = ''
participant1 = ''
participant2 = ''

for token in doc:
    # Next, you identify the main verb expressing the main action in the sentence
    # To extract the relation, we have to find the ROOT of the sentence (which is also the verb of the sentence)
    if token.pos_ == "VERB" and token.dep_ == 'ROOT':
        # Initialize the indexes for the subject and the object related to the main verb
        subj_ind = -1
        obj_ind = -1
        # Store the main verb itself (token.text) in the action variable
        action = token.text
        children = [child for child in token.children ]
        for child1 in children:
            # Find the subject via the nsubj relation and store it as participant1 
            # and its index as subj_ind
            if child1.dep_ == 'nsubj':
                participant1 = child1.text
                subj_ind = int(child1.i)
            # If there is a preposition attached to the verb (e.g., “write about”), then
            # you need to search for the indirect object as the second participant. 
            if child1.dep_ == 'prep':
                participant2 = ''
                child1_children = [child for child in child1.children]
                for child2 in child1_children:
                    # If such an object is a noun or a proper noun, 
                    # you store it as participant2 and its index as obj_ind
                    if child2.pos_ == 'NOUN' or child2.pos_ == 'PROPN':
                        participant2 = child2.text
                        obj_ind = int(child2.i)

                # If at this point both participants of the main action have been identified and
                # their indexes are included in the indexes of the words covered by the entity, 
                # you add the action with two participants to the list of actions.
                if not participant2=="":
                    if subj_ind in indexes:
                        actions.append(entity + " " + action + " " + child1.text + " " + participant2)
                    elif obj_ind in indexes:
                        actions.append(participant1 + " " + action + " " + child1.text + " " + entity)

            # Otherwise, if there is no preposition attached to the verb,
            # participant2 is a direct object of the main verb, 
            # which can be identified via the dobj relation
            if child1.dep_ == 'dobj' and (child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN' ):
                participant2 = child1.text
                obj_ind = int(child1.i)
                # In this case, you apply the same strategy as above, 
                # adding the action with two participants to the list of actions. 
                if subj_ind in indexes:
                     actions.append(entity + " " + action + " " + participant2)
                elif obj_ind in indexes:
                    actions.append(participant1 + " " + action + " " + entity)
# Finally if the final list of actions is not empty, 
# Print out the sentence and all actions together with the participants.
if not len(actions) == 0:
    print(f"\nSentence = {document}")
    for item in actions:
        print(item)            


# In[385]:


actions


# In[386]:


Sentence = "The New York Times wrote about Apple"
for sentence in sentences:
    doc = nlp(sentence)
    indexes = calculate_entity_span(doc, entity)
    calc_entity_subject_object(doc, entity, indexes)


# In[218]:


a="The New York Times wrote about Apple"
req='Apple'
doc=nlp(a)
index=[]
for ent in doc.ents:
    print(ent)
    for i in range(int(ent.start),int(ent.end)): #doubt about ent.start,ent.end
        print(ent.start,ent.end)
        index.append(i)


# In[410]:


def calculate_entity_span(document, entity):
    indexes = []
    for ent in document.ents:
        if ent.text == entity:
            for i in range(int(ent.start), int(ent.end)):
                indexes.append(i)
    return indexes


# In[411]:


entity = "The New York Times"

sentences = "The New York Times wrote about Apple"

doc = nlp(sentences)

calculate_entity_span(doc, entity)


# In[412]:


sentences = ["The New York Times wrote about Apple"]

for sentence in sentences:
    doc = nlp(sentence)
    for token in doc:
        print(token.dep_)


# In[421]:


def calc_entity_subject_object(document, entity, indexes): #Definition main
    actions = []
    action = ''
    participant1 = ''
    participant2 = ''
    
    for token in document:
        # Next, you identify the main verb expressing the main action in the sentence
        # To extract the relation, we have to find the ROOT of the sentence (which is also the verb of the sentence)
        if token.pos_ == "VERB" and token.dep_ == 'ROOT':
            # Initialize the indexes for the subject and the object related to the main verb
            subj_ind = -1
            obj_ind = -1
            # Store the main verb itself (token.text) in the action variable
            action = token.text
            children = [child for child in token.children ]
            for child1 in children:
                # Find the subject via the nsubj relation and store it as participant1 
                # and its index as subj_ind
                if child1.dep_ == 'nsubj':
                    participant1 = child1.text
                    subj_ind = int(child1.i)
                # If there is a preposition attached to the verb (e.g., “write about”), then
                # you need to search for the indirect object as the second participant. 
                if child1.dep_ == 'prep':
                    participant2 = ''
                    child1_children = [child for child in child1.children]
                    for child2 in child1_children:
                        # If such an object is a noun or a proper noun, 
                        # you store it as participant2 and its index as obj_ind
                        if child2.pos_ == 'NOUN' or child2.pos_ == 'PROPN':
                            participant2 = child2.text
                            obj_ind = int(child2.i)
                    
                    # If at this point both participants of the main action have been identified and
                    # their indexes are included in the indexes of the words covered by the entity, 
                    # you add the action with two participants to the list of actions.
                    if not participant2=="":
                        if subj_ind in indexes:
                            actions.append(entity + " " + action + " " + child1.text + " " + participant2)
                        elif obj_ind in indexes:
                            actions.append(participant1 + " " + action + " " + child1.text + " " + entity)
                            
                # Otherwise, if there is no preposition attached to the verb,
                # participant2 is a direct object of the main verb, 
                # which can be identified via the dobj relation
                if child1.dep_ == 'dobj' and (child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN' ):
                    participant2 = child1.text
                    obj_ind = int(child1.i)
                    # In this case, you apply the same strategy as above, 
                    # adding the action with two participants to the list of actions. 
                    if subj_ind in indexes:
                         actions.append(entity + " " + action + " " + participant2)
                    elif obj_ind in indexes:
                        actions.append(participant1 + " " + action + " " + entity)
    # Finally if the final list of actions is not empty, 
    # Print out the sentence and all actions together with the participants.
    if not len(actions) == 0:
        print(f"\nSentence = {document}")
        for item in actions:
            print('items in actions: ',item)            


# In[422]:


for sentence in sentences:
    doc = nlp(sentence)
    indexes = calculate_entity_span(doc, entity)
    calc_entity_subject_object(doc, entity, indexes)


# In[436]:


processed_docs[0]


# In[ ]:


#Printing all sentences where we want the required entity


# In[452]:


entity='Apple'
ent_type='ORG'
output_sentences=[]
for doc in processed_docs:
    for sentence in doc.sents:
        print('this is sentence',sentence)
        # Only consider sentences that contain the input entity 
        # of the specified type among its named entities
        if entity in [ent.text for ent in sentence.ents if ent.label_ == ent_type ]:
            output_sentences.append(sentence)


# In[447]:


output_sentences


# In[461]:


def return_docs_of_given_ent_type(processed_docs, entity, ent_type):
    output_sentences = []
    for doc in processed_docs:
        for sentence in doc.sents:
            # Only consider sentences that contain the input entity 
            # of the specified type among its named entities
            if entity in [ent.text for ent in sentence.ents if ent.label_ == ent_type ]:
                output_sentences.append(sentence)
    return output_sentences

entity = "Apple"

ent_sentences = return_docs_of_given_ent_type(processed_docs, entity, 'ORG' )
print(ent_sentences)        
        


# In[517]:


for sentence in ent_sentences: #We have 25 Sentences in list but get o/p for only 3 because The rest 22 don't follow calc_entity_span
    indexes = calculate_entity_span(sentence, entity)
    calc_entity_subject_object(sentence, entity, indexes)#Not having verbs in them . Same is depicted below


# In[515]:


calc_entity_subject_object(d,e,i)


# In[514]:


e = "Apple"

s = "American tech giants like Google, Apple and Facebook are on a collision course with European regulators over issues including privacy and taxes."

d = nlp(s)

i=calculate_entity_span(d, e)


# In[516]:


actions = [] #Why the rest 22 are not working
action = ''
participant1 = ''
participant2 = ''

for token in d:
    print('this is token',token)
    # Next, you identify the main verb expressing the main action in the sentence
    # To extract the relation, we have to find the ROOT of the sentence (which is also the verb of the sentence)
    if token.pos_ == "VERB" and token.dep_ == 'ROOT':
        # Initialize the indexes for the subject and the object related to the main verb
        subj_ind = -1
        obj_ind = -1
        # Store the main verb itself (token.text) in the action variable
        action = token.text
        print('this is action',action)
        children = [child for child in token.children ]
        print('this is children:',children)
        for child1 in children:
            print('this is child1',child1)
            # Find the subject via the nsubj relation and store it as participant1 
            # and its index as subj_ind
            if child1.dep_ == 'nsubj':
                participant1 = child1.text
                print('for {} this is participant1 {}'.format(child1,participant1))
                subj_ind = int(child1.i)
                print('for {} this is index {}'.format(child1,subj_ind))
            # If there is a preposition attached to the verb (e.g., “write about”), then
            # you need to search for the indirect object as the second participant. 
            if child1.dep_ == 'prep':
                print('child1 which is prep:',child1)
                participant2 = ''
                child1_children = [child for child in child1.children]
                print('child1_children',child1_children)
                
                for child2 in child1_children:
                    # If such an object is a noun or a proper noun, 
                    # you store it as participant2 and its index as obj_ind
                    if child2.pos_ == 'NOUN' or child2.pos_ == 'PROPN':
                        participant2 = child2.text
                        print('for {} this is participant2 {}'.format(child2,participant2))
                        obj_ind = int(child2.i)
                        print('for {} this is index {}'.format(child2,obj_ind))
                        # If at this point both participants of the main action have been identified and
                    # their indexes are included in the indexes of the words covered by the entity, 
                    # you add the action with two participants to the list of actions.
                if not participant2=="":
                    if subj_ind in i:
                        actions.append(entity + " " + action + " " + child1.text + " " + participant2)
                        print(actions)
                    elif obj_ind in i:
                        actions.append(participant1 + " " + action + " " + child1.text + " " + entity)

            # Otherwise, if there is no preposition attached to the verb,
            # participant2 is a direct object of the main verb, 
            # which can be identified via the dobj relation
            if child1.dep_ == 'dobj' and (child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN' ):
                participant2 = child1.text
                print('this is participant 2 when not prep',participant2)
                obj_ind = int(child1.i)
                print('this is obj_index 2 when not prep',obj_ind)
                # In this case, you apply the same strategy as above, 
                # adding the action with two participants to the list of actions. 
                if subj_ind in i:
                    actions.append(entity + " " + action + " " + participant2) 
                    print('this is action of subject when not prep',actions)
                elif obj_ind in i:
                    actions.append(participant1 + " " + action + " " + entity)
                    print('this is action of obj when not prep',actions)


# In[ ]:


entity = "The New York Times"

ent_sentences = return_docs_of_given_ent_type(processed_docs, entity, "ORG")
print(len(ent_sentences))

for sentence in ent_sentences:
    indexes = calculate_entity_span(sentence, entity)
    calc_entity_subject_object(sentence, entity, indexes)


# In[518]:


entity = "The New York Times"
ent_sentences=return_docs_of_given_ent_type(processed_docs,entity,'ORG')
print('len is :',len(ent_sentences))
for sentence in ent_sentences:
    indexes=calculate_entity_span(sentence,entity)
    calc_entity_subject_object(sentence,entity,indexes)


# # VISUALIZATION

# In[519]:


from spacy import displacy

text = "Last week, Democratic lawmakers from both parties said they had the Senate votes needed to pass legislation that would prevent tech platforms, including Apple, GM and Facebook, from favoring their own businesses."

doc = nlp(text)

displacy.render(doc, style="ent")


# In[ ]:


def visualize_given_ent_type(processed_docs, entity, ent_type):
    for doc in processed_docs:
        for sentence in doc.sents:
            if entity in [ent.text for ent in sentence.ents if ent.label_ == ent_type ]:
                displacy.render(sentence, style='ent' )

visualize_given_ent_type(processed_docs, 'Apple', 'ORG' )


# In[520]:


def visualize_given_ent_type(processed_docs, entity, ent_type): #returning visualized format of all sentences in 
    for doc in processed_docs:#processed docs where entity is apple label is ORG
        for sentence in doc.sents:
            if entity in [ent.text for ent in sentence.ents if ent.label_==ent_type]:
                displacy.render(sentence,style='ent')
visualize_given_ent_type(processed_docs, 'Apple', 'ORG' )                


# In[521]:


def return_count_of_ent_type(sentence, ent_type):
    return len([ent.text for ent in sentence.ents if ent.label_ == ent_type ])

txt = "Last week, Democratic lawmakers from both parties said they had the Senate votes needed to pass legislation that would prevent tech platforms, including Apple, GM and Facebook, from favoring their own businesses."

doc = nlp(txt)

return_count_of_ent_type(doc, 'ORG')


# In[522]:


def return_docs_of_given_ent_type_custom(processed_docs, entity, ent_type):
    output_sentences = []
    for doc in processed_docs:
        for sentence in doc.sents:
            if entity in [ent.text for ent in sentence.ents if ent.label_ == ent_type and
                          return_count_of_ent_type(sentence, ent_type) > 1 ]:
                output_sentences.append(sentence)
    return output_sentences

output_sentences = return_docs_of_given_ent_type_custom(processed_docs, "Apple", "ORG")

print(len(output_sentences))
                
                
                


# In[ ]:


def visualize_conditional_sentences(sentences):
    colors = {"ORG": "linear-gradient(90deg, #64B5F6, #E0F7FA)"}
    options = {"ents": ["ORG"], "colors": colors}
    
    for sentence in sentences:
        displacy.render(sentence, style="ent", options=options)
        


visualize_conditional_sentences(output_sentences )
    


# In[523]:


def visualize_conditional_sentences(sentences):
    colors = {"ORG": "linear-gradient(90deg, #64B5F6, #E0F7FA)"}
    options = {"ents": ["ORG"], "colors": colors}
    for sentence in sentences:
        displacy.render(sentence, style="ent", options=options)

visualize_conditional_sentences(output_sentences )        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




