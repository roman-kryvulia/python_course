import xml.etree.ElementTree as ET
filename = 'mondial-3.0.xml'
path  = 'C:/Users/roman/PycharmProjects/My_project'
def parse_and_remove(filename, path):
   path_parts = path.split('/')
   doc = ET.iterparse(filename, ('start', 'end'))
   # Skip root element
   next(doc)
   tag_stack = []
   elem_stack = []
   for event, elem in doc:
    if event == 'start':
      tag_stack.append(elem.tag)
      elem_stack.append(elem)
    elif event == 'end':
                if tag_stack == path_parts:
                    yield elem
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass


country_gov = {}

raw_data = parse_and_remove('mondial-3.0.xml', 'country')
for c_ in raw_data:
    cn = c_.attrib['name']
    gn = c_.attrib['government']
    country_gov[cn] = gn

country_2_words = {}
for country, gov in country_gov.items():
    if len(country.split(" ")) >= 2:
        country_2_words[country] = gov

gov_unique = set(country_2_words.values())
print(gov_unique)




