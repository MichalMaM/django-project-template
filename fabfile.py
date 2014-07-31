# example:
# fab {{ project_name }}_on_test:update --hosts="user@server"

from deployment.projects import Project as BaseProject
from deployment.machines import VPSMachine
from deployment.base import Deployment as BaseDeployment


class Project(BaseProject):

    project_name = '{{ project_name }}'

    repo_sources = {
        'pypi': '%(repo_name)s',
        'git': 'repo url...',
        'local_tar_gz': '%(repo_name)s',
    }

    supervisor_name = '%(supervisor_name)s'

    git_clone_url = 'ssh://git@bitbucket.org/michalmam/%(repo_name)s.git'


class Deployment(BaseDeployment, VPSMachine, Project):
    pass


{{ project_name }}_on_production = Deployment()
