def proprietary_legal_documents_path(instance, filename):
    '''file will be uploaded to MEDIA_ROOT/images/legal/proprietary_<id>/<filename>'''

    return f'images/legal/proprietary_{instance.proprietary.id}/{filename}'