# Object-Oriented Design Principles - OOD

The principles mentioned in your question—"Program to an Interface, not to an Implementation," "Hollywood Principle," and "Favor Composition over Inheritance"—are object-oriented design principles that guide developers in creating flexible, maintainable, and reusable software systems. They are complementary to the GRASP principles described in the readme.md file. Here's how they relate:

## 1. Program to an Interface, not to an Implementation

This principle encourages designing systems where classes depend on abstractions (interfaces) rather than concrete implementations.
Purpose: It promotes flexibility and reduces coupling, making it easier to swap out implementations without affecting the rest of the system.
Relation to GRASP: This aligns with Low Coupling and Protected Variations in GRASP, as it reduces dependencies and protects against changes in specific implementations.

## 2. Hollywood Principle ("Don't call us, we'll call you")

This principle suggests that higher-level components dictate the flow of control, and lower-level components should only respond when called upon.
Purpose: It promotes inversion of control (IoC) and ensures that components are loosely coupled.
Relation to GRASP: This is closely related to Controller and Indirection in GRASP, as it emphasizes delegating responsibilities to intermediary or higher-level components.

## 3. Favor Composition over Inheritance

This principle advocates using composition (i.e., combining objects with specific responsibilities) instead of inheritance to achieve code reuse and flexibility.
Purpose: It avoids the pitfalls of rigid inheritance hierarchies and promotes modularity and reusability.
Relation to GRASP: This aligns with High Cohesion and Pure Fabrication, as it encourages creating focused, reusable components rather than tightly coupled inheritance chains.

## Summary

While GRASP principles focus on assigning responsibilities to classes and objects in a way that promotes maintainability and robustness, the principles you mentioned are broader object-oriented design guidelines that help achieve similar goals of flexibility, reusability, and low coupling. Together, they form a strong foundation for designing high-quality software systems.
