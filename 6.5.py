text = "X-DSPAM-Confidence:    0.8475"
string = 'X-DSPAM-Confidence:    0.8475'
a = string.find('0')
print(a)
b = string[a:]
value = float(b)
print(value)