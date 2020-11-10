ResponseSchema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'type': 'object',
    'properties': {
        'status': {
            'type': 'integer',
            'minimum': 100,
            'maximum': 699
        }
    },

    'required': ['status']
}
