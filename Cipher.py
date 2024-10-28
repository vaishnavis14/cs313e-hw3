#  File: Cipher.py

#  Description: Strings are given to the program to be encrypted and decrypted. To encrypt, the string is rotated 90 degrees clockwise. To decrypt, the string was rotated 90 degrees counterclockwise.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 09/09/2022

#  Date Last Modified: 09/10/2022

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
import sys
import math
def encrypt ( strng ):
  # The string is converted to a list with all the letters.
  lst_letters = list(strng)
  # The number of rows and columns is determined by taking a square root of the length of the string and rounding up.
  num_row_col = math.ceil(math.sqrt(len(lst_letters)))
  # For the empty spots in the square, they are filled in with astericks
  for i in range(pow(num_row_col, 2) - len(lst_letters)):
    lst_letters.append("*")
  # The string is filled into the 2D array
  table = []
  index = 0
  for i in range(num_row_col):
    row = []
    for j in range(num_row_col):
      row.append(lst_letters[index])
      index += 1
    table.append(row)
  # An empty table is filled with 0s for the transformed table.
  transformed_table = []
  for i in range(num_row_col):
    row = []
    for j in range(num_row_col):
      row.append(0)
    transformed_table.append(row)
  # The table is rotated clockwise 90 degrees
  y = num_row_col - 1
  for i in range(num_row_col):
    x = 0
    for j in range(num_row_col):
      transformed_table[x][y] = table[i][j]
      x += 1
    y -= 1
  return_string = ""
  for i in range(num_row_col):
    for j in range(num_row_col):
      if transformed_table[i][j] != "*":
        return_string += transformed_table[i][j]
  return return_string

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def decrypt ( strng ):
  # The string is converted to a list with all the letters.
  lst_letters = list(strng)
  # The number of rows and columns is determined by taking a square root of the length of the string and rounding up.
  num_row_col = math.ceil(math.sqrt(len(lst_letters)))
  # For the empty spots in the square, they are filled in with astericks
  for i in range(pow(num_row_col, 2) - len(lst_letters)):
    lst_letters.append("*")
  # The string is filled into the 2D array
  table = []
  index = 0
  for i in range(num_row_col):
    row = []
    for j in range(num_row_col):
      row.append(lst_letters[index])
      index += 1
    table.append(row)
  transformed_table = []
  # An empty table is filled with 0s for the transformed table.
  for i in range(num_row_col):
    row = []
    for j in range(num_row_col):
      row.append(0)
    transformed_table.append(row)
  y = 0
  # The table is rotated counter clockwise 90 degrees
  for i in range(num_row_col):
    x = num_row_col - 1
    for j in range(num_row_col):
      transformed_table[x][y] = table[i][j]
      x -= 1
    y += 1
  return_string = ""
  for i in range(num_row_col):
    for j in range(num_row_col):
      if transformed_table[i][j] != "*":
        return_string += transformed_table[i][j]
  return return_string


def main():
  # read the two strings P and Q from standard imput
  string_P = sys.stdin.readline().strip()
  string_Q = sys.stdin.readline().strip()
  # encrypt the string P
  print(encrypt(string_P))
  # decrypt the string Q
  print(decrypt(string_Q))
  # print the encrypted string of P and the
  # decrypted string of Q to standard out

if __name__ == "__main__":
  main()
