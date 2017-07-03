text = "X-DSPAM-Confidence:    0.8475"

def find_num(input):
    loc = text.find('0.8475')
    print(float(text[loc:]))

find_num(text)
