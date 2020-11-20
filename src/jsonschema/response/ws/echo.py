EchoSchema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'type': 'object',
    'properties': {
        'msg': {
            'type': 'object',
            'properties': {
                'msg': {
                    'type': 'string',
                    'minLength': 4,
                    'maxLength': 15,
                },
            },

            'required': ['msg'],
            'additionalProperties': False
        },
    },

    'required': ['msg'],
    'additionalProperties': False
}
