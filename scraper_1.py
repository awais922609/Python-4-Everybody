import urllib.request, urllib.parse , urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/authors.txt')
counts= dict()
for line in fhand:
    word= line.decode().split()
    for word in words:
        counts[word]= counts.get(word,0)+1

print(counts)
