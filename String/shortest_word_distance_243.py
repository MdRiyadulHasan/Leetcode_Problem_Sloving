# Easy
# Given a list of words and two words word1_and_word2, return the shortest distance between these two words in the list.
# Example:
# Assume that words =["practice", "makes", "perfect", "coding", "makes"].
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and _word1 _and _word2 _are both in the list.
def find_ans(words, word1,word2):
    i1=-1
    i2=-1
    shortest=len(words)
    for i in range(len(words)):
        if words[i]==word1:
            i1=i
        elif words[i]==word2:
            i2=i
        if i1!=-1 and i2!=-1:
            result=min(shortest,abs(i1-i2))
    return result


if __name__ =='__main__':
    words=list(input().strip().split())
    word1=input()
    word2=input()
    ans=find_ans(words,word1,word2)
    print(ans)