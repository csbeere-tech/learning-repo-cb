#Implement a function that splits a string by spaces
def split_string_by_spaces(s):
    return s.split(' ')

#Test the functiontest_string = "Hello World! This is a test."
test_string = "Hello World! This is a test."
result = split_string_by_spaces(test_string)

print(result)
#Output: ['Hello', 'World!', 'This', 'is', 'a', 'test.']