def anagram_word(text1, tex2):
     textl= "ford"
     text2="dorf"
     
     if sorted(text1) == sorted(text2):
         return True
         
     else:
         return False
         
print(anagram_word('ford', 'dorf'))
     
  