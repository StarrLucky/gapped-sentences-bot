from github import Github
import config

class GitRepo:
    g = Github(config.GITHUB_REPO_ACCESS_TOKEN)
    repo = g.get_repo(config.GITHUB_REPO_NAME)
    def init(self):
        return self.repo
