# Find-the-longest-substring
Python program to find the longest substring, of a numeric string, containing numbers with a difference of a given number. This is a solution for a Hackerrank problem to obtain a certificate.

# Example
For the numeric string '11123', with a difference of '1', the longest substring is '1112'.
![image](https://github.com/Unusual-Waffles-Situation/Find-the-longest-substring/assets/62034860/3822b540-53af-42d4-87af-991055ee609d)

Starting from the index 0, being a '1':

**Index 1**: Is another '1', so is valid as it's the same number as the index.

**Index 2**: Same as index 1.

**Index 3**: Is a number '2', and the difference between the index is '1'; meaning is valid.

**Index 4**: Is a number '3', and the difference between the index is '2'; meaning is invalid.

The longest substring is **1112**.

# How it works?
The program recieves 2 inputs from the user: *A numeric string*, and a number between 1 and 10 for the for the *difference*.
