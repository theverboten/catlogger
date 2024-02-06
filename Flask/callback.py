from get_response import get_advice
from get_audio import get_response


def main_process(callback, input):
    data = get_advice(input)
    callback(data)  # Call the callback function with the result
    print("Main process finished.")


def my_callback_function(input):
    get_response(input)
    print(f"Inside the callback: {input}")


def catcall(input):
    main_process(my_callback_function, input)
    print("Finished")
