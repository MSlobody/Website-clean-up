import glob
import codecs
import re
from bs4 import BeautifulSoup

i = 0
total_html = []
total_crosslinks = []

for filepath in glob.iglob('**/*.html', recursive=True):
    filename = re.findall("\\\\(\d+\.html)", filepath)
    i += 1
    if len(filename) != 1:
        continue
    #print(filename,i)
    total_html.append(filename[0])
#print(total_html)

# search for anchor tags in filename
    read_file = codecs.open(filepath, 'r', 'utf-8').read()
    soup = BeautifulSoup(read_file, 'html.parser')
    tags = soup('a')

    for tag in tags:
        tags_href = tag.get('href')
        if tags_href is not None:
            i+= 1
            #print(tags_href, i, type(tags_href))
            num_href = tags_href[0:-5]
            if num_href.isnumeric():
               # print(num_href)
                total_crosslinks.append(tags_href)
j = 0
for entry in total_html:
    if entry not in total_crosslinks:
        j += 1
        print(entry)
print(j)
# Found the orphaned files. Need to find broken links, which are hrefs that go nowhere.