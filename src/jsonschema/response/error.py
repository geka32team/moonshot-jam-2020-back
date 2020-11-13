ErrorSchema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'type': 'object',
    'properties': {
        'status': {
            'type': 'integer',
            'minimum': 400,
            'maximum': 699
        },
        'message': {
            'type': 'string'
        }
    },

    'required': ['status'],
    'additionalProperties': False
}
