from enum import Enum


class Event(Enum):
    """
    Event enum type
    """
    COMMIT_COMMENT = 'commit_comment'
    CREATE = 'create'
    DELETE = 'delete'
    DEPLOYMENT = 'deployment'
    DEPLOYMENT_STATUS = 'deployment_status'
    FORK = 'fork'
    GOLLUM = 'gollum'
    ISSUE_COMMENT = 'issue_comment'
    ISSUES = 'issues'
    MEMBER = 'member'
    MEMBERSHIP = 'membership'
    PAGE_BUILD = 'page_build'
    PING = 'ping'
    PUBLIC = 'public'
    PULL_REQUEST = 'pull_request'
    PULL_REQUEST_REVIEW = 'pull_request_review'
    PULL_REQUEST_REVIEW_COMMENT = 'pull_request_review_comment'
    PUSH = 'push'
    RELEASE = 'release'
    REPOSITORY = 'repository'
    STATUS = 'status'
    TEAM_ADD = 'team_add'
    WATCH = 'watch'
