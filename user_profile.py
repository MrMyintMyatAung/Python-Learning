def bulid_profile(first,last,**user_info):
    """ Build a dictionary of a user profile contiaing first and last name and any additional user info """

    user_info ['first_name'] = first
    user_info ['last_name'] = last
    return user_info

user_profile = bulid_profile('albert', 'einstein',location='princeton',field='physics')

print(user_profile)