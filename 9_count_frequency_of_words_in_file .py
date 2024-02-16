from collections import Counter
def total_words():
    with open("sample3.txt","r") as f:
        return Counter (f.read().split())
print("number of words in the files ",total_words())


