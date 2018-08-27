#Question1
'''
import re
email1="zuck26@facebook.com"
email2="page33@google.com"
email3="jeff42@amazon.com"
out=re.split(r'[@.]',email1)
out2=re.split(r'[@.]',email2)
out3=re.split(r'[@.]',email3)
print(out,out2,out3)
'''
#Question2
'''
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
text1=re.findall("[bB]\w",text)
print(text1)
'''
#Question3
'''
import re
sentence="A,very very;irregular_sentence"
text = re.sub(r'\W'," ", sentence)
text1 = re.sub(r'\_'," ", text)
print(text1)

'''
#Optional_Question
'''
>>> tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
>>> ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
'Good advice RT What I would do differently if I was learning to code today cc rstats'
'''
