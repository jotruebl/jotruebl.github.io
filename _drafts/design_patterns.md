A nice overview of other pagtterns: https://stackabuse.com/creational-design-patterns-in-python/

READ: https://medium.com/@mrfksiv/python-design-patterns-03-the-factory-86cb351c68b0

Research scientists will be the first to admit: we tend to write code with the intent of getting the immediate task at hand done rather than having clean, reusable packages that adhere to best practices. There's a variety of reasons, or excuses, for this. The most common is that the goals and dataset of each individual project are rarely constant. Furthermore there's a tendency to believe, whether true or not, that the only person that will be using the code in the future is you. This often leads to us cursing our past-selves for wtriting such unintelligible code. But the fact is, when revisions are due tomorrow, the priority rests on just getting it to work.

I've recently made an effort to be more vigilant about taking opportunities to write re-usable code. This meant reviewing the various design patterns in programming. Design patterns are basically a set of solutions to common programming problems, and became popular after the so-called Gang of Four's book 'Design Patterns: Elements of Reusable Object-Oriented Software' which came out in the '90s. Creational design patterns are a specific category of design patterns related to the creation of objects. 

If you're someone that writes exclusively in Python, you probably don't have much familiarity with these terms. That's because design patterns were developed back when less dynamic languages were more popular. Python is extremely flexible in the way it can be used, meaning most design patterns aren't even necessary, and may even be 'anti-patterns.' That being said, there are definitely instances where design patterns are extremely useful in Python code. In this post, I'll share an example of a design pattern called the factory method, which can be used to improve the reusability of your code.

The factory method helps simplify the process of object creation. It does so by using various methods to handle the logic of which concrete implementation of a common interface to create. 

 Someone else explains it well in their post:

'In Factory Method the client knows what she wants, but for some reason she can’t create the object directly. The reasons vary case-by-case: maybe she wants to use a common interface instead of manually instantiating the class she requires, or maybe she would need to pass a huge set of parameters to the constructor. Most of the time the client wants a single object, and this pattern relieves her of the responsability of creating this object directly.'

It separates the creation of an object from code that depends on the interface of the object. Factory method is used when we know what we want to build, but we don't want to do it directly. We want to abstract it out so that rather than manually calling the specific class, we can use a factory that does it for us. This means that it's easier for new users as they're all pointed to a single method or class, and its also easier to modularize the code for future cases. See here for an explanation: https://www.giacomodebidda.com/factory-method-and-abstract-factory-in-python/

################
################
Let's look at an example. I'll describe a recent project in which the factory method proved useful for me. I recently took part in a research voyage into the Southern Ocean where my goal was to study the properties of ice nucleating particles (INP). I'll skip the details, but put simply: INP are tiny particles that help water freeze into ice. Some INP are better at this job than others, and my goal was to study the various properties of INP. To do this, I had to collect samples from a number of different locations on the ship, which I've named as follows:

- seawater
- bubbler
- ambient
- coriolis

Since each sample was collected from a different location, the resulting raw data needed to be processed differently before it was ready for analysis. 

Let's build up from the beginning what some code might look like. We can imagine a class called raw_data that each of these types of data inherit from. They all have a similar interface, meaning they all need to do similar things, but in different ways. In the case of INP raw data objects, we take raw data, metadata, preprocess it and then output a cleaned file. But the actual concrete implementation is different depending on the type of experimental dataset we're working with. So one for seawater, bubbler, coriolis, etc.


We can imagine buuilding the class raw_data like this, with a clean_raw_data function:

```python
class RawData:
    
    # assign properties to the object based on params passed
    def init(raw_data, params):
        pass

    # a bunch of if/else statements that determine which chunk of code to enact
    def clean_raw_data(self):
        if self.type_ == seawater:
            if self.location == surface_water:
                pass
            elif self.location == subsurface_water
                pass
        elif self.type_ == aerosol:
            if self.location == ambient:
                pass
            elif self.location == coriolis:
                pass
            elif self.location == bubbler:
                pass
```

Depending on the type of data passed into the function, we will have a different logical pathway. The problem with this approach shoudl be clear. We're using a bunch of if/else statements to guide the flow of our logic. What happens when we have INP data of a new type? We have to go in and add a new branch of if/else statements without messing up the existing code. What happens if someone else wants to use this code? It's not very readable. We'll have these if/else statements all floating around our complex pre-processing code. 

And what if the different types of raw data objects have differnt parameters? We'd need to handle all of this in one single class. 

When a new INP type is ontroduced, well have to add a bunch of new if/else statements. When the parameters and metadata for that new type changes, we have to add this to the class.

This is where the factory method helps. We basically abstract out the if/elif/else conditional statements into a separate 'factory' classs. The application delegates the decision of which concrete implementation of an interface to apply to a separate component. Our first step in building a factory method is to look for a common interface.

**Important point:**
    The first step when you see complex conditional code in an application is to identify the common goal of each of the execution paths (or logical paths).

In the case of INP objects, our common goal is to take raw data, metadata, and save a cleaned file.

Then, we'll create a concrete implementation for each type and an application that delegates which of these components to use when creating the object. This is the essence of the factory method.

It turns out, unsurprisingly, there's a bunch of ways to go about this. I'll give two examples.  The first way is to put each concrete implementation in the raw_data class and create a factory method which decides which implementation within the class to call. This can lead to an unwieldy chunk of code in the RawData2 class, as we'll see. Another way is to build a class consisting of the necessary components using a factory method design pattern.

Let's look at the first approach. We will define class RawData with a calculate_raw method, which takes in some metadata. We'll also use **kwargs to simplify the parameter passing step. 

```python
class RawData:
    def __init__(self, type_, location, **kwargs)
        self.type_ = type_
        self.location = location
        self.__dict__.update(kwargs)
    
    # Define the client method
    def calculate_raw(self):
        calculator = self._get_calculator()
        return calculator()
    
    # Define creator method. Leading underscores denote these methods should not be directly called by the user.
    def _get_calculator(self):
        if self.type_ == 'seawater':
            return self._calculate_seawater
        elif self.type_ == 'aerosol':
            if self.location == 'bubbler':
                return self._calculate_bubbler
        else:
            raise ValueError(self.type_, self.location)
    
    # Define concrete products
    def _calculate_seawater(self):
        pass
    def _calculate_bubbler(self):
        pass
```

Now we would run this by doing the following:

```python
>>> d = RawData('aerosol', 'bubbler', other parameters..)
>>> d.calculate_raw()
```

What happens here is A separate component has the responsibility of deciding which conrete implementation shoudl be used. Note that the method does not CALL the implementatino, but rather simply returns the function object itself. This is possible thanks to first order methods/classes of Python. (I think).

So now the class will
1) calculate_raw() method, which define a calculator by calling the _get_calculator method. This is called the client portion. The calculator is returned by _get_calculator as an uncalled method. Note that the calculator which is returned is not actually called until the final return.
2) _get_calculator method takes in a format and determines the correct concrete implementation and returns it as an object (not called!). This is the creator component.
3) concrete calculator method, these are called the concrete products. The product is the interface, which is not explicitly defined in Python.


The mechanics of Factory Method are always the same. A client (RawData.calculate_raw()) depends on a concrete implementation of an interface. It requests the implementation from a creator component (_get_calculator()) using some sort of identifier, which in this case are the properties of the object.

The creator returns the concrete implementation according to the value of the parameter to the client, and the client uses the provided object to complete its task.

Factory Method should be used in every situation where an application (client) depends on an interface (product) to perform a task and there are multiple concrete implementations of that interface. You need to provide a parameter that can identify the concrete implementation and use it in the creator to decide the concrete implementation.

Replacing complex logical code: Complex logical structures in the format if/elif/else are hard to maintain because new logical paths are needed as requirements change.

Factory Method is a good replacement because you can put the body of each logical path into separate functions or classes with a common interface, and the creator can provide the concrete implementation.

Now if we have a new raw data type, we can simply add an elif statement to our creator method, and create a new concrete product method for its implementation: 

```python
class RawData:
    def __init__(self, type_, location, **kwargs)
        self.type_ = type_
        self.location = location
        self.__dict__.update(kwargs)
    
    # Define the client method
    def calculate_raw(self):
        calculator = self._get_calculator()
        return calculator()
    
    # Define creator method. Leading underscores denote these methods should not be directly called by the user.
    def _get_calculator(self):
        if self.type_ == 'seawater':
            return self._calculate_seawater
        elif self.type_ == 'aerosol':
            if self.location == 'bubbler':
                return self._calculate_bubbler
            if self.location == 'coriolis':
                return self._calculate_coriolis
        else:
            raise ValueError(self.type_, self.location)
    
    # Define concrete products
    def _calculate_seawater(self):
        pass
    def _calculate_bubbler(self):
        pass
    def _coriolis(self):
        pass
```

The second approach to this is to use composition (https://stackabuse.com/the-factory-method-design-pattern-in-python/). So here we make a separate class for each data type. First we create a superclass that defines the interface for all subclasses.

```python
# we can define a parent class of rawINP which forces all subsequent subclasses to have a'calculate raw' method
class RawINP(ABC):
    @abstractmethod
    def calculate_raw(self):
        pass
```

Then we can define each of the subclasses:

```python
# create a different class for each data type/location
# we can make an INP class that this inherits from, then all processes can be done with one object
# see the inp class in pyce_tools.py file
class Bubbler:
    def __init__(self, metadata_dictionary):
        # actually should do this explicitly so that if the attr is not passed in the dictionary, it will give an explicit error upon instantiation
        self.__dict__.update(metadata_dictionary)
    
    # this will be_calculate_seawater() from below
    def calculate_raw(self):
        pass

class Seawater:
    def __init__(self, params):
        # explicitly update attributes
    def calculate_raw(self):
        pass

class Coriolis:
    def __init__(self, params):
        # explicitly update attributes
    def calculate_raw(self):
        pass
```

Finally, we create a function that accepts raw data and returns the correct class for us by calling the datafactory.

```python
class DataFactory:
    def create_raw(self, metadata_dictionary):
        if metadata_dictionary[type_] == 'bubbler':
            return Bubbler(metadata_dictionary)
        elif...
            pass

def raw_data_creator(metadata_dictionary):
    data_factory = DataFactory()
    data_object = data_factory.create_raw(metadata_dictionary)
    return data_object
```

In this way, we simply pass in our metadata dictionary to the raw_data_creator function, which uses the factory method to automatically create the correct class. We then simply call the calculate_raw() method on our returned object.

```python
>>> inp = raw_data_creator(params)
>>> inp.calculate_raw()
Raw data calculated!
```


This is a more modular approach, and may prove to be simpler for future users.





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
