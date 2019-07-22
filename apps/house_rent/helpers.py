def modify_input_for_multiple_files(property_id, image):
    dict = {}
    dict['property_id'] = property_id
    dict['image'] = image
    
    return dict

def user_house_directory_path(instance, filename):
    '''file will be uploaded to MEDIA_ROOT/images/user_<id>/<filename>'''

    return f'images/houses/user_{instance.property_place.id}/{filename}'