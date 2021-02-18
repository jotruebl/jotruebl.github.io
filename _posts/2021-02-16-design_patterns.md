---
title: Using Design Patterns to Improve Your Research Code
tags: 
- Design Patterns
- Research
- Factory Method
- Refactoring
---
Research scientists will be the first to admit: we tend to write code with the intent of getting the immediate task at hand done rather than having clean, reusable packages that adhere to best practices. There's a variety of reasons, or excuses, for this. The most common is that the goals and dataset of each individual project are rarely constant. There's also a tendency to believe, whether true or not, that the only person that will be using the code in the future is you. This often leads to us cursing our past-selves for writing such unintelligible code. But the fact is, when revisions are due tomorrow, the priority rests on just getting it to work.

## Design Patterns
I've recently made an effort to be more vigilant about taking opportunities to write re-usable code. To this end, I've been reviewing various design patterns in programming. Design patterns are basically a set of solutions to common programming problems, which became popular after the so-called Gang of Four's book 'Design Patterns: Elements of Reusable Object-Oriented Software.' 

If you're someone that writes exclusively in Python, you're probably not very familiar with many design patterns. That's because they were developed back when programming languages were less dynamic. Python is extremely flexible in the way it can be used, meaning most design patterns aren't even necessary, and in certain cases are actually 'anti-patterns.' That being said, there are definitely instances where design patterns are extremely useful in Python.

One such design pattern is the factory method, which helps simplify the process of object creation. It does so by using various methods to handle the logic of which concrete implementation of a common interface to create. There's a bit of jargon in that description, so let me restate it more plainly. The factory method separates the creation of an object from the code that depends on the interface of the object. We use it when we know what we want to build, but we don't want to do it directly. Rather than manually calling a specific class, we can use a factory that does it for us. This means that it's easier for new users as they're all pointed to a single method or class, and its also easier to modularize the code for future cases. 

In this post, I'll share an example where I refactored my research code to improve its modularity. The approach I take is inspired by the factory method design pattern. Note that the approach I'll be describing here is *inspired* by the factory method, but isn't necesarily strictly the factory method, as the dynamic nature of Python lets us take some shortcuts. The code I'll describe is part of a package I wrote to analyze ice nucleating particle data, called [Pyce Tools](https://github.com/jotruebl/Pyce_Tools). (Note, to illustrate my original point, I have not yet implemented all of these improvements into the current version of Pyce Tools.)


## The Dataset

I recently took part in a research voyage into the Southern Ocean where my goal was to study the properties of ice nucleating particles (INP). I'll skip the details, but put simply: INP are tiny particles that help water freeze into ice. Some INP are better at this job than others, and my goal was to study the properties of different INP to identify what determines their effectiveness. 

To do achieve my goal, I collected and analyzed INP found in the seawater and in the atmosphere, where they float around as tiny particles called aerosols. So this means we have two types of INP:


- **seawater**
- **aerosol**

The ship had different ways of collecting samples of INP that were located in different locations that I termed the following:

- **underway:** seawater collected from a pump beneath the ship.
- **bubbler:** artificial aerosols that were created onboard the ship using a special instrument.
- **ambient:** natural aerosols collected on a filter.
- **coriolis:** a different instrument for collecting natural aerosols. 

Since each sample was collected from a different location, the resulting raw data needed to be processed differently before it was ready for analysis. Let's build up from the beginning what the code for handling this data might look like. 

## The Quick and Dirty Approach
The first pass through the code would probably be a script with a bunch of if/else statements. You simply load your dataset, and depending on its metadata properties, you pass it along a different logical pathway.

```python
metadata = {
    'type_':  ... # Either seawater or aerosol
    'location': ... # underway, bubbler, ambient, coriolis,
    ... # Any other metadata
}

raw_data = ... # Path to raw data file or the object itself

if metadata['type_'] == 'seawater':
    # Code to process the data
elif metadata['type_'] == 'aerosol':
    if metadata['location'] == 'ambient':
        # Code to process the data
    elif metadata['location'] == 'coriolis':
        # Code to process the data
    elif metadata['location'] == 'bubbler':
        # Code to process the data
```

The drawbacks of this are obvious, so we'll move right away to an improved scenario in which we have a class called RawData that each of the types of data inherit from. They all have a similar interface, meaning they all need to do similar things, just in different ways. In the case of RawData objects, our interface is to take raw data and associated metadata, preprocess it and then output it to a cleaned file for analysis. The actual concrete implementation of this interface is different depending on the type of experimental dataset we're working with. This means we'd need a different piece of code for each combination of INP type and location (e.g., seawater from the underway, aerosols from the bubbler, etc.).

## Adding a RawData Class
The RawData would look like this, and would include a clean_raw_data function:

```python
class RawData:
    def init(self, metadata_dict):
        # Assign properties to the object based on metadata passed
        self.type_ = metadata_dict['type_']
        self.location = metadata_dict['location']

    # A bunch of if/else statements that determine which chunk of code to enact
    def clean_raw_data(self, raw_data):
        if self.type_ == 'seawater':
            # Code to process the data
        elif self.type_ == 'aerosol':
            if self.location == 'ambient':
                # Code to process the data
            elif self.location == 'coriolis':
                # Code to process the data
            elif self.location == 'bubbler':
                # Code to process the data
```
Then we'd run the code like this:

```python
>>> d = RawData(metadata_dict)
>>> d.calculate_raw(raw_data)
```

Depending on the type and location of data passed into the function, we will have a different logical pathway. While this looks simple enough, the use of if/else statement to guide the flow of our logic is still mixed in with the actual implementation. This will eventually present problems as the project scales up. What happens when we have INP data of a new type? We have to go in and add a new branch of if/else statements without messing up the existing code. What happens if someone else wants to use this code? It's not very readable. We'll have these if/else statements floating around inside our clean_raw_data function. Finally, what if the different types of RawData objects have different parameters? We need to ensure our class can handle the different collections of metadata that each type provides.

## Factory Method-Inspired Refactoring
This is where the factory method helps. We basically abstract out the if/elif/else conditional statements into a separate 'factory' classs. The application then delegates the decision of which concrete implementation of an interface to apply to a separate component. Our first step is to look for a common interface.

**Important point**
    The first step when you see complex conditional code in an application is to identify the common goal of each of the execution paths (or logical paths).

In the case of INP objects, our common goal is to take raw data, metadata, and save a cleaned file.

Then, we'll create a concrete implementation for each RawData type and a separate application that delegates which of these components to use when creating the object. This is the essence of the factory method.

It turns out, unsurprisingly, there's a bunch of ways to go about this. I'll give two examples.  The first way is to put each concrete implementation in the RawData class and create a class method that decides which of these to call. Another way is to build a separate class for each INP location/type combination and create an application that decides which of these to use when creating an RawData object.

### Approach 1
Let's look at the first approach. We will define class RawData with a calculate_raw method, which takes in some metadata. We'll also use **kwargs to simplify the parameter passing step. 

```python
class RawData:
    def __init__(self, type_, location, **kwargs):
        # Assign properties to the object based on metadata passed
        self.type_ = type_
        self.location = location
        self.__dict__.update(kwargs)
    
    # Define the client method
    def calculate_raw(self, raw_data):
        # Note: leading underscores denote methods which should not be directly called by the user.
        calculator = self._get_calculator()
        return calculator(raw_data)
    
    # Define the creator method. 
    def _get_calculator(self):
        if self.type_ == 'seawater':
            return self._calculate_underway
        elif self.type_ == 'aerosol':
            if self.location == 'bubbler':
                return self._calculate_bubbler
            elif self.location == 'coriolis':
                return self._calculate_coriolis
            elif self.location == 'ambient':
                return self._calculate_ambient
        # If the type/location combo doesn't exist, notify the user.
        else:
            raise ValueError(self.type_, self.location)

    # Define concrete products
    def _calculate_underway(self, raw_data):
        # Code to process the data
        pass
    def _calculate_bubbler(self, raw_data):
        # Code to process the data
        pass
    def _calculate_coriolis(self, raw_data):
        # Code to process the data
        pass
    def _calculate_ambient(self, raw_data):
        # Code to process the data
        pass
```

Basically we've just abstracted the if statements into a new function. This simple change goes a long way to improving the reability of the code. Now we would run this by doing the following:

```python
>>> d = RawData(type_='aerosol', location='bubbler', metadata_dict)
>>> d.calculate_raw(raw_data)
```

What happens here is the **client method** (calculate_raw) calls a separate **creator method** (_get_calculator) which has the responsibility of deciding which **concrete implementation** of our interface to use (_calculate_underway, _calculate_bubbler, _calculate_coriolis, or _calculate_ambient). Note that the method does not actually call the implementation, but rather simply returns the function object itself. This is possible thanks to first order methods/classes of Python.

This approach can be used in every situation where an application (client) depends on an interface (product) to perform a task and where there are multiple concrete implementations of that interface. You simply need to provide a parameter that can identify the concrete implementation and use it in the creator to decide the concrete implementation.

### Extending the Class for New RawData Types
We can see why this method is superior by considering an example where we have a new RawData type/location combination. Let's say we now can collect seawater INP from the very top layer of the water column instead of the deeper water collected from the boat's underway. To account for this, we can simply add an elif statement to our creator method and create a new concrete product method for its implementation: 

```python
class RawData:
    def __init__(self, type_, location, **kwargs):
        # Assign properties to the object based on metadata passed
        self.type_ = type_
        self.location = location
        self.__dict__.update(kwargs)
    
    # Define the client method
    def calculate_raw(self, raw_data):
        # Note: leading underscores denote methods which should not be directly called by the user.
        calculator = self._get_calculator()
        return calculator(raw_data)
    
    # Define the creator method. 
    def _get_calculator(self):
        if self.type_ == 'seawater':
            if self.location == 'underway':
                return self._calculate_underway
            elif self.location == 'microlayer':
                return self._calculate_microlayer
        elif self.type_ == 'aerosol':
            if self.location == 'bubbler':
                return self._calculate_bubbler
            elif self.location == 'coriolis':
                return self._calculate_coriolis
            elif self.location == 'ambient':
                return self._calculate_ambient
        # If the type/location combo doesn't exist, notify the user.
        else:
            raise ValueError(self.type_, self.location)
    
    # Define concrete products
    def _calculate_underway(self, raw_data):
        # Code to process the data
        pass
    def _calculate_microlayer(self, raw_data):
        # Code to process the data
        pass
    def _calculate_bubbler(self, raw_data):
        # Code to process the data
        pass
    def _calculate_coriolis(self, raw_data):
        # Code to process the data
        pass
    def _calculate_ambient(self, raw_data):
        # Code to process the data
        pass
```

Note how we don't have to worry about messing up any of the code in our other concrete products. 


### Approach 2


The second approach is to define a separate class for each INP type/location combination. Each of these classes will inherit from a base RawINP class. We'll Python's [abstract base class module](https://docs.python.org/3/library/abc.html) to force sub-classes of RawData to include a calculate_raw method. Then we'll use a separate method for delegating which class to instantiate based on the parameters.

```python
# Define a RawData parent class using abstractbaseclass (ABC) to force all subsequent subclasses to have a'calculate_raw' method.
class RawData(ABC):
    @abstractmethod
    def calculate_raw(self):
        pass
```

Then we can define each of the subclasses. Since each class is separate, we can explicitly define the metadata required for instantiation. Note also that each class has different necessary metadata.

```python
class Bubbler(RawData):
    def __init__(self, metadata_dict):
        # Explicitly define the necessary attributes for each type so that if they're not passed in the dictionary, it will give an error upon instantiation.
        self.flow_rate = metadata_dict['flow_rate']
        self.filter_size = metadata_dict['filter_size']
    
    def calculate_raw(self, raw_data):
        # Code to process the data
        pass


class Coriolis(RawData):
    def __init__(self, metadata_dict):
        self.flow_rate = metadata_dict['flow_rate']
        self.sample_volume = metadata_dict['sample_volume']
    
    def calculate_raw(self, raw_data):
        # Code to process the data
        pass


class Underway(RawData):
    def __init__(self, metadata_dict):
        self.sample_volume = metadata_dict['sample_volume']
    
    def calculate_raw(self, raw_data):
        # Code to process the data
        pass
```

Finally, we create a function that accepts raw data and metadata and automatically returns the correct class for us by calling the RawDataFactory class.

```python
class RawDataFactory:
    def create_raw(self, metadata_dict):
        if metadata_dictionary['type_'] == 'aerosol':
            if metadata_dictionary['location'] == 'coriolis':
                return Coriolis(metadata_dict)
            elif metadata_dictionary['location'] == 'Bubbler':
                return Bubbler(metadata_dict)
        elif metadata_dictionary['type_'] == 'seawater':
            return Underway(metadata_dict)
            

def raw_data_creator(metadata_dict):
    data_factory = RawDataFactory()
    data_object = data_factory.create_raw(metadata_dict)
    return data_object
```

In this way, we simply pass in our metadata dictionary to the raw_data_creator function, which uses the RawDataFactory class to automatically decide which class we need to instantiate. We then simply call the calculate_raw() method on our returned object, and voila. 

```python
>>> inp = raw_data_creator(metadata_dict)
>>> inp.calculate_raw(raw_data)
...Raw data calculated!
```

The benefit to this approach is that each type of INP data has its own class. If we have a new type of INP data, we don't have to even touch our other classes, reducing the risk of making errors.

In the end, the approach you take is up to you. But hopefully it's clear why spending an extra 5-10 minutes to think about your code will save you time in the long run.

**More reading:**

[Python Design Patterns](https://python-patterns.guide/) - Brandon Rhodes

[Creational Design Patterns in Python](https://stackabuse.com/creational-design-patterns-in-python/) - Darinka Zobenica

[The Factory Method Pattern and Its Implementation in Python](https://realpython.com/factory-method-python/) -  Isaac Rodriguez

[Python Design Patterns: -03- The Factory](https://medium.com/@mrfksiv/python-design-patterns-03-the-factory-86cb351c68b0) - morf