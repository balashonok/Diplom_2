class UserErrors:
   already_exists = "User already exists"
   field_missed = "Email, password and name are required fields"
   field_is_incorrect = 'email or password are incorrect'
   not_authorised = 'You should be authorised'

class OrderErrors:
   no_ingredients = 'Ingredient ids must be provided'
   wrong_ingredient = 'One or more ids provided are incorrect'