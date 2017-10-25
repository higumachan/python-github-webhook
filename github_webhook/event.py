from enum import Enum


class Event(Enum):
    """
    Event enum type
    """
    Commit_comment = 'commit_comment'
    Create = 'create'
    Delete = 'delete'
    Deployment = 'deployment'
    Deployment_status = 'deployment_status'
    Fork = 'fork'
    Gollum = 'gollum'
    Issue_comment = 'issue_comment'
    Issues = 'issues'
    Member = 'member'
    Membership = 'membership'
    Page_build = 'page_build'
    Ping = 'ping'
    Public = 'public'
    Pull_request = 'pull_request'
    Pull_request_review = 'pull_request_review'
    Pull_request_review_comment = 'pull_request_review_comment'
    Push = 'push'
    Release = 'release'
    Repository = 'repository'
    Status = 'status'
    Team_add = 'team_add'
    Watch = 'watch'
