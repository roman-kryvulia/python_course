import xml.etree.ElementTree as ET
filename = 'mondial-3.0.xml'
path  = 'mondial-3.0.xml'
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


government_all = []
raw_data = parse_and_remove('mondial-3.0.xml', 'country')
for g in raw_data:
    gov = g.attrib['government']
    government_all.append(gov)

government_unique = set(government_all)

print(government_unique)




