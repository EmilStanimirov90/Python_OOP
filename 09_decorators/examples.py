# def hello_function():
#     def say_hi():
#         return "Hi"
#
#     return say_hi
#
#
# hello = hello_function()
# print(hello())
#
#
# def print_message(message):
#     def message_sender():
#        # "Nested Function"
#         print(message)
#     message_sender()
#
# print_message("Some random message")
#


def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


@uppercase
def say_hi():
    return 'hello there'



print(say_hi())