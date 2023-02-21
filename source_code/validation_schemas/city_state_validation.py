from marshmallow import Schema, fields, ValidationError, validates


class ValidateCityStateSchema(Schema):
    city = fields.String(required=True)
    state = fields.String(required=True)

    @validates('city')
    def validate_city(self, city):
        if (len(str(city)) < 1) or (all([x.isalpha() or x.isspace() for x in city]) is False):
            raise ValidationError('The city should only contain alphabets')

    @validates('state')
    def validate_last_name(self, state):
        if (len(str(state)) < 1) or (all([x.isalpha() or x.isspace() for x in state]) is False):
            raise ValidationError('The state should only contain alphabets')


'''

The code above is defining a Marshmallow schema called ValidateCityStateSchema that is used for validating city and state values.

The schema has two required fields, city and state, both of which are defined as string fields.

In addition to the required fields, the schema has two validation methods defined using the @validates decorator. 
The @validates decorator is used to specify a field that should be validated and to define the validation function that should be used.

The validate_city function is used to validate the city field. It checks if the length of the city is greater
 than 1 and if all characters in the city are either alphabets or spaces. If the city value is not valid, it raises a ValidationError with an error message.

The validate_last_name function is used to validate the state field. It checks if the length of the state is 
greater than 1 and if all characters in the state are either alphabets or spaces. If the state value is not valid, it raises a ValidationError with an error message.

The ValidationError class is used to raise an error when a validation error occurs. The error message passed 
to the constructor of the ValidationError class will be used to describe the validation error.
'''