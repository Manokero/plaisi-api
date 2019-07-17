def propietary_legal_documents_path(instance, filename):
    '''file will be uploaded to MEDIA_ROOT/images/user_<id>/<filename>'''

    return f'images/legal/propietary_{instance.propietary.id}/{filename}'