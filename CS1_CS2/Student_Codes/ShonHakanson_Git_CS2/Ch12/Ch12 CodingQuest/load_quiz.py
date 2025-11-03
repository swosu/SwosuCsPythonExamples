def load_quiz_from_file(file_name):
    """Reads a quiz text file (question line followed by answer line)
       and returns a dictionary {question: answer}."""

    quiz_dictionary = {}

    # Open the file safely
    with open(file_name, 'r', encoding='utf-8') as quiz_file:
        # Read all non-empty lines, removing spaces and newlines
        all_lines = [line.strip() for line in quiz_file if line.strip()]

        # Go through the list two lines at a time (question, then answer)
        for line_index in range(0, len(all_lines), 2):
            current_question = all_lines[line_index]
            current_answer = all_lines[line_index + 1]
            quiz_dictionary[current_question] = current_answer

    return quiz_dictionary

