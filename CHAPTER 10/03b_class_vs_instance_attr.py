# Python objects are flexible. You don’t need to predefine attributes in the class; you can add them dynamically to an instance.  is this same for JAVA
# ChatGPT said:
# ChatGPT
# No, this is not the case in Java.

# In Python, objects are highly flexible because you can dynamically add attributes to an instance at runtime. This is part of Python's dynamic nature, where classes and instances can be modified during execution. For example, you can create an object and then add a new attribute to it like this:

# python
# Copy code
class MyClass:
    pass

obj = MyClass()
obj.new_attr = "I am new!"
print(obj.new_attr)  # Output: I am new!






# In Java, on the other hand, objects are not as flexible in this regard. Java is a statically-typed language, meaning that all attributes (fields) must be predefined in the class definition. You cannot dynamically add new fields to an instance at runtime like you can in Python. All attributes must be declared in the class beforehand. For example:

# java
# Copy code
# class MyClass {
#     String existingAttr;

#     MyClass(String existingAttr) {
#         this.existingAttr = existingAttr;
#     }
# }

# public class Main {
#     public static void main(String[] args) {
#         MyClass obj = new MyClass("Hello");
#         // obj.newAttr = "I am new!"; // This will cause a compile-time error
#         System.out.println(obj.existingAttr);  // Output: Hello
#     }
# }
# In Java, to achieve dynamic behavior like adding attributes, you would typically use a Map or some other data structure to hold additional properties. Alternatively, you could use reflection (which allows inspecting and modifying object properties at runtime), but it still doesn’t allow adding completely new attributes directly to an object instance in the way Python does.

# In summary:

# Python allows dynamic addition of attributes to objects.
# Java does not allow adding attributes dynamically and requires all fields to be predefined in the class.







class Employee:
    lang= "Py"
    first_salary= "1400000 LPA"


vivekObj = Employee()
vivekObj.name="Vivek"
print(vivekObj.lang, vivekObj.first_salary, vivekObj.name)

avinashObj = Employee()
avinashObj.age=23
print(avinashObj.first_salary, avinashObj.lang,avinashObj.age)
