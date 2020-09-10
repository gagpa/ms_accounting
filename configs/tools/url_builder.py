class UrlBuilder:
    temmplates = \
        {
            'with_auth': '{protocol}://{username}:{password}@{host}:{port}/{name}',
            'without_auth': '{protocol}://{host}:{port}/{name}',
        }

    def build(self, protocol, host, port, name=None, username=None, password=None):
        if username and password:
            url = self.temmplates['with_auth'].format(protocol=protocol,
                                                      username=username,
                                                      password=password,
                                                      host=host,
                                                      port=port, name=name)
        else:
            url = self.temmplates['without_auth'].format(protocol=protocol,
                                                         host=host,
                                                         port=port,
                                                         name=name)
        return url


url_builder = UrlBuilder()
