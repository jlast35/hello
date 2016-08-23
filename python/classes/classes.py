class MyClass: #define a simple test class

    greeting = "Hello World" #this is a class variable.. by default you can probably assign to it as though public
    #it seems that whenever you call a function defined in a class,
    #it always silently / automatically passes a reference to the class as its first parameter,
    #even though no parameter is specified in the call
    #so, by convention, every function defined as part of a class starts its parameter list with a variable called "self"
    #the variable "self" plays a similar role in Python to using the keyword "this" in other languages like Java

    def say_hello(self): 
        print self.greeting #reference an internal class variable - useful for keeping state info
        self.internal_function() #call a class function from another function inside the class
        #note: even though internal_function is not defined yet, we can still call it
        #because it will be defined before say_hello() actually gets called

    def internal_function(self):
        print "Internal function called"

       
myObject = MyClass() #variable names are case sensitive
print hasattr(myObject,'greeting')
myObject.greeting = "Something else" #class variables are not private in Python; you can assign to them directly
print hasattr(myObject,'greeting')
myObject.say_hello()  #this function call actually passes one parameter even though it looks blank - implicitly, it passes a reference to the object it is being called from (myObject)
print MyClass.greeting 