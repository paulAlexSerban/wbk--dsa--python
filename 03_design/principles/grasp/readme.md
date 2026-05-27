# General Responsibility Assignment Software Principles - GRASP
> published by Craig Larman

GRASP (General Responsibility Assignment Software Principles) is a set of guidelines introduced by Craig Larman to help developers assign responsibilities to classes and objects in object-oriented design. These principles aim to create maintainable, reusable, and robust software systems. Here’s a brief explanation of each principle:

## 1. Information Expert
Assign responsibility to the class that has the necessary information to fulfill it. This minimizes the need for external data and ensures cohesion.

## 2. Creator
Assign the responsibility of creating an object to the class that has the information needed to initialize it or closely uses the created object.

## 3. Controller
Assign the responsibility of handling system events to a controller class. This class acts as an intermediary between the UI and the domain logic.

## 4. Low Coupling
Design classes with minimal dependencies on other classes. This reduces the impact of changes and increases reusability.

## 5. High Cohesion
Ensure that a class has a focused set of responsibilities. This makes the class easier to understand, maintain, and reuse.

## 6. Polymorphism
Use polymorphism to handle variations in behavior. Assign responsibility to the class that implements the behavior, allowing for flexibility and extensibility.

## 7. Pure Fabrication
Create a class that does not represent a concept in the problem domain but is introduced to achieve low coupling, high cohesion, or reuse.

## 8. Indirection
Assign responsibility to an intermediate class to mediate between other classes, reducing direct coupling and promoting flexibility.

## 9. Protected Variations
Protect elements from changes in other elements by encapsulating the volatile parts behind stable interfaces or abstractions.

These principles are not strict rules but guidelines to help you make better design decisions in object-oriented programming.