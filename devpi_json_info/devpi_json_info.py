from devpi_common.url import URL
from devpi_server.readonly import get_mutable_deepcopy
from pluggy import HookimplMarker
from pyramid.view import view_config

__version__ = "0.1.0"
devpiserver_hookimpl = HookimplMarker("devpiserver")


@devpiserver_hookimpl
def devpiserver_pyramid_configure(config, pyramid_config):
    # by using include, the package name doesn't need to be set explicitly
    # for registrations of static views etc
    pyramid_config.include("devpi_json_info")


def includeme(config):
    config.add_route("json_info", "/{user}/{index}/{project}/json")
    config.scan()


@view_config(
    route_name="json_info",
    accept="application/json",
    request_method="GET",
    renderer="json",
)
def json_info_view(context, request):
    baseurl = URL(request.application_url).asdir()
    version = context.stage.get_latest_version(context.project, stable=True)
    info = get_mutable_deepcopy(context.stage.get_versiondata(context.project, version))
    info.pop("+elinks", None)
    result = dict(info=info, releases={})
    for release in context.stage.get_releaselinks(context.project):
        result["releases"].setdefault(release.version, []).append(
            dict(url=baseurl.joinpath(release.relpath).url)
        )
    return result
