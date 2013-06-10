import json
import csv

# load file - provide file path 
path = '../LiteratureReviewEV_V2.json'

# create a csv file for writing
#csv_file = csv.writer(open("../test.csv", "wb+"))
csv_file = open("../test.csv", "wb+")
csv_writer = csv.writer(csv_file, delimiter=";")

author_file = open("../authors.csv", "wb+")
author_writer = csv.writer(author_file, delimiter=";")

# open the file and parse
json_data=open(path)

data = json.load(json_data)

header_set = set()

# walk through array row by row
# for each publication get headers
for publication in data:
    # we now have a dictionary of publication attributes
    for k, v in publication.items():
    	if k == 'issued' or k == 'accessed' or k == 'id':
    		pass
    	elif k == 'author':
    		# do stuff
    		pass
        else:
        	header_set.add(k)

# write headers
header_list = list(header_set)
header_list.insert(0, unicode('id'))

csv_writer.writerow(header_list)
author_writer.writerow(['publication_id', 'author_given', 'author_family'])

# now our csv
for publication in data:
    # we now have a dictionary of publication attributes
    row_list = [''] * len(header_list)
    for k, v in publication.items():

        pub_id = publication.get('id')
          
    	if k != 'author' and k != 'issued' and k != 'accessed':
            position = header_list.index(k)
            row_list[position] = v

        elif k == 'author':
            for author in v:
                author_list = [publication['id'], author.get('family'), author.get('given')]
                author_writer.writerow(
                    [unicode(s).encode("utf-8") for s in author_list]
                )

            
    # write row
    csv_writer.writerow([unicode(s).encode("utf-8") for s in row_list])

    # TODO: traget author key, or any field which is multidimensional

# output to csv

# close file

#if __name__ == '__main__':
#	pass
