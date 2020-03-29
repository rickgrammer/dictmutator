'''
:usage:
    specimen = {
        "name": "Ranadebilla",
        "speaks": {
            'phrases': ['kavali', 'hello']
        },
        "favourite-phrase": 'hello'
    }

    hello_to_hi = lambda greet: 'hello' if greet=='hi' else greet

    mutate(specimen, hello_to_hi)

    specimen mutated to -> {
                        "name": "Ranadebilla",
                        "speaks": {
                            'phrases': ['kavali', 'hi']
                        },
                        "favourite-phrase": 'hi'
                    }
'''
import typing


def _mutate(specimen, mutating_function):
    for key in specimen:
        # Call recursively if the specimen is a dict
        if isinstance(specimen[key], dict):
            _mutate(specimen[key], mutating_function)
        # Recurse iteratively if its an iterable, ignore str type
        elif isinstance(specimen[key], typing.Iterable) and not isinstance(
                specimen[key], str):
            for index, entry in enumerate(specimen[key]):
                if isinstance(entry, dict):
                    _mutate(entry, mutating_function)
                else:
                    specimen[key][index] = mutating_function(entry)
        else:
            specimen[key] = mutating_function(specimen[key])


def mutate(specimen, mutating_function):
    '''
    Mutates the values of a dictionary using the provided mutating_function
    Ideal for mutating the JSON values.

    :params:
    specimen:
        type: dict
        description: The dictionary whose values get mutated.
    mutating_function:
        type: function
        description: Use this function to mutate each value in a specimen.

    :warnings:
    mutating_function: function must return a value unless you want None as the
    mutated value.

    '''
    if not isinstance(specimen, dict):
        raise TypeError('specimen must be of type dict.')
    _mutate(specimen, mutating_function)


if __name__ == '__main__':

    def hi_to_hello(greet):
        return 'hello' if greet == 'hi' else greet

    d = {
        'greet':
        'hi',
        'list_of_greetings': [
            'hello',
            'good morning',
            'hi',
        ],
        'container_of_greetings': [('hi', {
                'greet':
                'hi',
                'tuple_of_greetings': ('hi', 'good evening')
            }, ('greet', 'hi')
        ), {'hi', 'hello', 'namaste', }, ({'greet': 'hi'},)
        ]
    }
    mutate(d, hi_to_hello)
    print(d)
