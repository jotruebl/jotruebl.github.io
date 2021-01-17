Research scientists will be the first to admit: we usually write code with the intent of getting the immediate task at hand done rather than having clean, reusable packages that adhere to best practices. There's a variety of reasons, or excuses, for this. The most common is that each project and it's asociated goals and data are rarely constant from one day to the next. That being said, there are plenty of instances in which taking the extra day or two to write good code can save you plenty of time in the long run. I've recently become more aware of opportunities to write re-usable code. In this post, I'll share an example of a design pattern called the factory method, which can be used to improve the reusability of your code.

Design patterns became popular after GoF's book 'Design Patterns: Elements of Reusable Object-Oriented Software. They're basically a set of solutions to common programming problems. Creational design patterns are on category of patterns, and are related to the creation of objects. If you're a research scientists that writes exclusively in Python, you probably don't have much familiarity with these terms. That's because design patterns were developed back when less dynamic languages like C was the most popular language. Python is extremely flexible in the way it can be used, meaning most design patterns aren't even necessary, and may even be 'anti-patterns.' That being said, there are definitely instances where design patterns are extremely useful in Python code. 

The factory method is one design pattern which creates objects with a shared interface. It creates concrete implementations of a common interface. It separates the creation of an object from code that depends on the interface of the object. Factory method is used when we know what we want to build, but we don't want to do it directly. We want to abstract it out so that rather than manually calling the specific class, we can use a factory that does it for us. This means that it's easier for new users as they're all pointed to a single method or class, and its also easier to modularize the code for future cases. See here for an explanation: https://www.giacomodebidda.com/factory-method-and-abstract-factory-in-python/

'In Factory Method the client knows what she wants, but for some reason she can’t create the object directly. The reasons vary case-by-case: maybe she wants to use a common interface instead of manually instantiating the class she requires, or maybe she would need to pass a huge set of parameters to the constructor. Most of the time the client wants a single object, and this pattern relieves her of the responsability of creating this object directly.'

I'll describe a recent project in which the factory method proved useful for me. I recently took part in a research voyage into the Southern Ocean. My goal was to study the properties of ice nucleating particles (INP). INP are tiny particles that help water freeze into ice. Some INP are better at this job than others, and my goal was to study the various properties of INP. To do this, I had to collect samples from a number of locations. Since each sample was collected from a different location, the resulting raw data needed to be processed differently before it was ready for analysis. Here's an example of the various types of INP data:

seawater
bubbler
ambient
coriolis

We can think of a class called INP which is defined by the following interface: it takes in raw data and metadata, and then processes that data and outputs a cleaned data file ready for analysis. As mentioned above, each data type requires different analysis process. 

We can imagine buuilding the function like this:

```python
class raw_data:
    def init(raw_data, params):
        # assign properties to the object based on params passed
        pass
    def clean_raw_data:
        # a bunch of if/else statements that determine which chunk of code to enact
        pass
```

Depending on the type of data passed into the function, we will have a different logical pathway. The problem with this approach shoudl be clear. We're using a bunch of if/else statements to guide the flow of our logic. What happens when we have INP data of a new type? We have to go in and add a new branch of if/else statements, without messing up the existing code. What happens if someone else wants to use this code? It's not very readable.

This is where the factory method helps. Instead of using if/elif/else conditional statements to determine concrete implementation of objects, factory method allows for a separate component to handle it. The application delegates the decision of which concrete implementation of an interface to apply to a separate component.

The first step when you see complex conditional code in an application is to identify the common goal of each of the execution paths (or logical paths).

Code that uses if/elif/else usually has a common goal that is implemented in different ways in each logical path.

In the case of INP objects, we take raw data, metadata, and save a cleaned file. This is the interface. But the actual concrete implementation is different depending on the type of experimental dataset we're working with. So one for seawater, bubbler, coriolis, etc.

Therefore, we'll create a concrete implementation for each type, and an application that delegates which of these components to use when creating the object.

At first glance, we could just create a method that takes parameters and uses if/else statements to decide how to handle this data. But that leads to the following code: *show calculate_raw() function in pyce tools*

The problem with this is obvious. It's difficult to update and not very friendly to new coders. So we could take it a step further...So imagine we have a class INP that consists of some metadata and raw data.
We also have a class that takes the INP obbject and, depending on the specifics of that object, will 'calculate raw' as guided by a bunch of if/else statements.

See the following section for why this code is still sub-optimal:
https://realpython.com/factory-method-python/#the-problems-with-complex-conditional-code

So now we use factory method. The goal is to provide a separate component which automatically decides which concrete implementation to use. 

There's actually a few ways to go about this. One of them is to put each concrete implementation in the class and create a factory method which decides which implementation within the class to call. This can lead to an unwieldy chunk of code in the RawData2 class. This approach comes from realpython's blog post.

Another way is to use composition. We will build a class consisting of the necessary components using a factory method design pattern.

This means we create a class for each type of data, which si then returned depending on the logic of tthe factory. This is the approach as described [here](https://stackabuse.com/the-factory-method-design-pattern-in-python/)

A ncie overview of other pagtterns: https://stackabuse.com/creational-design-patterns-in-python/


Basic Implementation of Factory Method
A separate component has the responsibility of deciding which conrete implementation shoudl be used. Note that the method does not CALL the implementatino, but rather simply returns the function object itself. This is possible thanks to first order methods/classes of Python. (I think).

So now the class will
1) serialize() method, which takes in a song and a format and define a serializer by calling the get_serializer method. This is called the client portion. The serializer is returned by get_serializer as an uncalled method, which is not called until the final return.
2) get_serializer method takes in a format and determines the correct concrete implementation and returns it as an object (not called!). This is the creator component.
3) concrete serialize method, these are called the concrete products. The product is the interface, which is not explicitly defined in Python.


The mechanics of Factory Method are always the same. A client (SongSerializer.serialize()) depends on a concrete implementation of an interface. It requests the implementation from a creator component (get_serializer()) using some sort of identifier (format).

The creator returns the concrete implementation according to the value of the parameter to the client, and the client uses the provided object to complete its task.

Factory Method should be used in every situation where an application (client) depends on an interface (product) to perform a task and there are multiple concrete implementations of that interface. You need to provide a parameter that can identify the concrete implementation and use it in the creator to decide the concrete implementation.

Replacing complex logical code: Complex logical structures in the format if/elif/else are hard to maintain because new logical paths are needed as requirements change.

Factory Method is a good replacement because you can put the body of each logical path into separate functions or classes with a common interface, and the creator can provide the concrete implementation.

The parameter evaluated in the conditions becomes the parameter to identify the concrete implementation. The example above represents this situation.

Constructing related objects from external data: Imagine an application that needs to retrieve employee information from a database or other external source.

The records represent employees with different roles or types: managers, office clerks, sales associates, and so on. The application may store an identifier representing the type of employee in the record and then use Factory Method to create each concrete Employee object from the rest of the information on the record.

Supporting multiple implementations of the same feature: An image processing application needs to transform a satellite image from one coordinate system to another, but there are multiple algorithms with different levels of accuracy to perform the transformation.

The application can allow the user to select an option that identifies the concrete algorithm. Factory Method can provide the concrete implementation of the algorithm based on this option.

Combining similar features under a common interface: Following the image processing example, an application needs to apply a filter to an image. The specific filter to use can be identified by some user input, and Factory Method can provide the concrete filter implementation.

Integrating related external services: A music player application wants to integrate with multiple external services and allow users to select where their music comes from. The application can define a common interface for a music service and use Factory Method to create the correct integration based on a user preference.

Ideally, we want to make it so each concrete product is its own class. This makes it easier to make changes in the future. Here we define a new interface called 'Calculator' that has multiple implementations depending on the format of the data.

Our interface, again, is not explicitly defined, but rather implicitly defined by duck typing. 
Rather than keeping these implementations in the original class, we will create a generic class called 'DataCalculator.' This is now the client. Not sure why we'd want to do this though.

Our RawData class should be abstract interface that has methods for defining raw metadata and then calculating. Each type of INP data should have its own concrete implementation depending on the type and location.

Recall above that the creator was a function called 'get_serializer'. Here, we use the client to retrieve the calculator from the object factory. So we need an ObjectFactory. An ObjectFactory is just a class of a creator.

https://realpython.com/factory-method-python/#a-general-purpose-object-factory