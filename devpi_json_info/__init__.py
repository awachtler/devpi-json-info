__version__ = "0.1.3"


def includeme(config):
    config.add_route("json_info", "/{user}/{index}/{project}/json")
    config.scan()
