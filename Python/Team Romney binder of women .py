#Lists in Python
team_r = "Go Team Romney!"

print team_Romney
print "Print the list of women in Mitt Romney's binder!"
women = ["Jasmine", "Samantha", "Jenny", "Alice", "Sofia"]
print women

#count of women
count_of_women = len(women)
print "Romney has %d binders of women in his binder!" % (count_of_women)
print ' ' #space

#slicing in Python
print "Slice list of women to show the first two!"
print women[0:2]
print ' '

#Assing using indexing
print "Now Assign new women into Mitt's binder with indexing!"
women[0] = "Brittney"
print women[0]
print "Mitt chooses you Brittney to replace Jasmine!"
print "Romney added " + women[0] + " into his binder!" 
print ' '

print "Good Work! " + team_r
print "Now, Append a new woman into Mitt's binder!"
women.append("Laura")
print "Here is the new list"
print women

#assign women[-1:] then change to a str variable
women_neg1 = str(women[-1:])
print women_neg1
print "We added " + women_neg1 + " to our list using the -1 indexing"

print' '

#I dont like the way ['Laura'] is outputted so I will fix it by slcing the string
women_neg1_str = women_neg1[2:-2]
print "or rather, Mitt added " + women_neg1_str + " to his binder!"
print ' '

#Using insert
print "Now Insert Ariela into Jenny's position!"
women_index = women.index("Jenny")
women.insert(women_index, "Ariela")

print women

print ''

print "Excellent! Mitt's binder of white women is complete!" 
print team_r