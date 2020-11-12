SigninSchema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'type': 'object',
    'properties': {
        'username': {
            'type': 'string',
            'minLength': 4,
            'maxLength': 15
        },
        'password': {
            'type': 'string',
            'minLength': 8,
            'maxLength': 32
        }
    },

    'required': ['username', 'password'],
    'additionalProperties': False
}
