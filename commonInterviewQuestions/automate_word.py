'''
*   Typehead (autocomplete) feature. We already given list of dictionary
(Hello -> world, man)
(Hello-> world)
(Nice -> Job) etc.
Input: Hello Output: world (since world appear more frequently)
Given first word, we have to find another word in O(1). (Only get operation)
[
{"Hello": ["world", "man"]},
{"Hello": ["world"]},
{"Nice": ["Job"]}
]


'''
def frequency_count(lst):
    freq={}
    output = []
    for word in lst:
        if word not in freq:
            freq[word]=1
        else:
            freq[word] += 1
    max_value =max([value for key,value in freq.items()])
    for key, value in freq.items():
        if value == max_value:
            output.append(key) 
    return output

def autocomplete(lst,input):
    input_map = {}
    for dict in lst:
        for key,value in dict.items():
            if key in input_map:
                input_map[key] += value 
            else:
                input_map[key]=value
    return frequency_count(input_map.update(input))[0]

input =[
{"Hello": ["world", "man"]},
{"Hello": ["world"]},
{"Nice": ["Job"]}
]
print(autocomplete(input,'Hello'))
            