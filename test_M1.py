print("hello")

# to install -> pip install newspaper3k

try:
    import newspaper
   
    print("Module imported")
except ImportError:
    print("Module not imported")

