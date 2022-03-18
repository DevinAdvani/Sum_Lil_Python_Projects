#Basically want to make a randomly evolving piece of code

#Code Input
code = ("""
love = 'what is love'
print(love)
""")

#Turning Multi-line code into list



#Basic Writing Thing - Use quotations for input. but need to make multiline
def write_file(text):
    with open(f'Py_Ev.py', 'w') as f:
        f.write(text)

#Test
write_file("""
print("Hello World")
"""
)

#Running program
import Py_Ev.py
