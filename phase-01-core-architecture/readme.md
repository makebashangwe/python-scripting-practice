
# Week 1 Summary: Foundational Data Structures

Week 1 focused on understanding how Python stores and retrieves data using **lists** and **dictionaries**, with an emphasis on choosing the right structure based on lookup efficiency.

The core lesson was that lists are useful for ordered collections and sequential processing, while dictionaries are better for fast key-based lookups. In infrastructure terms, a list is like manually checking every rack until you find a device, while a dictionary is like querying an inventory system by asset tag and instantly finding the right record.

During this week, I practiced creating dictionaries, adding and deleting entries, updating values safely, using `.get()` to avoid crashes, and counting duplicate asset tags from a raw list.

The larger architectural lesson was that writing better software is not only about knowing the syntax. The real gap was learning how to separate responsibilities inside a program. Instead of mixing user input, printing, validation, storage, and business logic in one loop, I practiced breaking programs into clear layers:

- **Model:** represents one entity and its data
- **Manager:** controls the collection and business logic
- **Driver:** handles user interaction, prompts, and output

The main takeaway from Week 1 was:

> Do not let storage logic talk directly to the user.

This week established the foundation for moving from flat procedural scripts toward cleaner object-oriented systems with better separation of concerns, encapsulation, and reusable logic.

Detailed Notes Here: https://docs.google.com/document/d/12Ur3GSHMmGtQdNm_qTqbDb-O6iQFlEYdhMtqWSZnBrY/edit?usp=sharing
