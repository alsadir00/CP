# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

 

# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:

# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:

# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"

class Solution:
    def interpret(self, command: str) -> str:
        string_len = len(command)
        new_string = ""
        point = 0
        while point <= string_len -1:
            if command[point] == "G":
                new_string += "G"
                point += 1
            else: 
                if command[point + 1] == ")":
                    new_string += "o"
                    point += 2
                else:
                    new_string += "al"
                    point += 4
        return new_string

