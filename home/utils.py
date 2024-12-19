def get_listings_directory(instance, filename):
    return 'user_{0}/listings/{1}'.format(instance.dealer.user.id, filename)


