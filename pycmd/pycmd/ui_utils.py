INTRO = 'Welcome to PyCMD! Enter the command "HELP" to get started.'

# Static error messages -----

NO_INPUT_ERROR = "Error: no input detected."
INVALID_COMMAND_ERROR = "Error: invalid command."
INVALID_DIR_ERROR = "Error: invalid directory change."
PLAYER_DNE_ERROR = "Error: player does not exist."


# Dynamic error messages -----
def raise_unaccounted_error(e):
    print(f"Program has crashed due to unaccounted error: {e}")


def raise_syntax_error(command):
    print(f"Error: incorrect command syntax. Format {command.call_name['form']}")
