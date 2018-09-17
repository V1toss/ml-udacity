#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

print min([len(v) for v in enron_data.itervalues()])

print sum([v['poi'] for v in enron_data.itervalues()])

print sum(1 for line in open("../final_project/poi_names.txt", "r") if line.startswith("("))

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

mykeys = ['SKILLING JEFFREY K', 'LAY KENNETH L', 'FASTOW ANDREW S']
print [(k, v['total_payments']) for k, v in enron_data.iteritems() if k in mykeys]

print sum([v['salary'] != 'NaN' for v in enron_data.itervalues()])
print sum([v['email_address'] != 'NaN' for v in enron_data.itervalues()])

print (sum([v['total_payments'] == 'NaN' and v['poi'] for v in enron_data.itervalues()]) / float(len(enron_data)))

print (sum([v['total_payments'] == 'NaN' for v in enron_data.itervalues()])) + 10

print sum([v['poi'] for v in enron_data.itervalues()]) + 10

print (sum([v['total_payments'] == 'NaN' and v['poi'] for v in enron_data.itervalues()])) + 10