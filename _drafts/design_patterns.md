Design patterns became popular after GoF's book 'Design Patterns: Elements of Reusable Object-Oriented Software'

Creational design patterns are on category of patterns, and are related to the creation of objects.

Factory method is one design pattern which creates objects with a shared interface.

It creates concrete implementations of a common interface.

It separates the creation of an object from code that depends on the interface of the object. (??)

INstead of using if/elif/else conditional statements to determine concrete implementation o fobjects, factory method allows for a separate comoonent to handle it.

reasons for why if elif and else conditional statements are bad

The first step when you see complex conditional code in an application is to identify the common goal of each of the execution paths (or logical paths).

Code that uses if/elif/else usually has a common goal that is implemented in different ways in each logical path. .

In the case of INP, we take raw data, metadata, and save a cleaned file.

Create an implementation for each logical path.

So one for seawater, bubbler, coriolis, etc.

Then provide another component that decides which of those concrete implementations to use based on the format.

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