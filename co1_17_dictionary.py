d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("orginal dictionary : ',d)
sorted_d = sorted(d.items())
print('Dictionary in asending order by value : ',sorted_d)
sorted_d + sorted(d.items(),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)
