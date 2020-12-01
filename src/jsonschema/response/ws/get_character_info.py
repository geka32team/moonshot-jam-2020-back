GetCharacterInfoSchema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'type': 'object',
    'properties': {
        'lvl': {'type': 'integer'},
        'hp': {'type': 'integer'},
        'exp': {'type': 'integer'},
        'strn': {'type': 'integer'},
        'vit': {'type': 'integer'},
        'dex': {'type': 'integer'},
        'acc': {'type': 'integer'},
        'dmg': {'type': 'integer'},
        'stats': {'type': 'integer'},
        'bosses_defeated': {'type': 'integer'},
    },

    'required': ['lvl', 'hp', 'exp', 'strn', 'vit', 'dex',
                 'acc', 'dmg', 'stats', 'bosses_defeated'],

    'additionalProperties': False
}
