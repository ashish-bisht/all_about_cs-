# all_about_cs!

## Table of Contents
  - [Data Structures](#data-structures)


  ## Data Structures

  - ### Arrays
    - Arrays is collection of same type of items stored in contiguous memory.
    - Generally zero-based-indexing is used in arrays, i.e to fetch first element in an aray we will use something like this A[0], given A is our array.
    - __Access ::__ To access a particular index from an array we require __O(1)__ time.
      - As arrays are contiguous and our computer  knows the start address, type of element, it requires constant time to get to the index.
    - __Insert ::__ To Insert an element to an array it requires __O(n)__ time.
      - For insertion first all the elemnts will be copied and then again new array will be created with the required size.
    - __Search ::__  To Search an element in an array it requires __O(n)__ time.
      - It will look for every elemnt one by one, till we get thje desired one.

    - __Delete ::__ To Delete an element from an array it requires __O(n)__ time.
      - For deleting again it same as inserting new element after deleting the particular one.
    
    - Important Questions