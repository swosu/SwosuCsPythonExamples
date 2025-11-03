def get_inputs_for_mad_lib():
    mad_lib_inputs = []
    print('a noun is a person, place, or thing')
    mad_lib_inputs.append(input("Enter a noun: "))
    print('a verb is an action word')
    mad_lib_inputs.append(input("Enter a verb: "))
    print('an adjective is a word that describes a noun')
    mad_lib_inputs.append(input("Enter an adjective: "))
    print('an adverb is a word that describes a verb')
    mad_lib_inputs.append(input("Enter an adverb: "))
    return mad_lib_inputs

def get_mad_lib():
    inputs = get_inputs_for_mad_lib()
    mad_lib = f'Be kind to your {inputs[0]}-footed {inputs[1]} or a duck may be somebody\'s {inputs[2]}, be kind to your {inputs[2]} in {inputs[3]} weather for a duck may be somebody\'s {inputs[0]}'
    return mad_lib
if __name__ == '__main__':
    print(get_mad_lib())
