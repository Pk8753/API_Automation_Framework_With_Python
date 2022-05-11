create_gist_response_schema = {
    "$schema": "http://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "url",
        "forks_url",
        "commits_url",
        "id",
        "node_id",
        "git_pull_url",
        "git_push_url",
        "html_url",
        "files",
        "created_at",
        "updated_at",
        "description",
        "comments",
        "comments_url",
        "owner",
        "forks",
        "history"
    ],
    "properties": {
        "url": {
            "type": "string",
            "default": "",
            "title": "The url Schema",
            "examples": [
                "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8"
            ]
        },
        "forks_url": {
            "type": "string",
            "default": "",
            "title": "The forks_url Schema",
            "examples": [
                "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/forks"
            ]
        },
        "commits_url": {
            "type": "string",
            "default": "",
            "title": "The commits_url Schema",
            "examples": [
                "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/commits"
            ]
        },
        "id": {
            "type": "string",
            "default": "",
            "title": "The id Schema",
            "examples": [
                "8980b6f77ec7439b5b1e2abac800f1c8"
            ]
        },
        "node_id": {
            "type": "string",
            "default": "",
            "title": "The node_id Schema",
            "examples": [
                "G_kwDOAlm7H9oAIDg5ODBiNmY3N2VjNzQzOWI1YjFlMmFiYWM4MDBmMWM4"
            ]
        },
        "git_pull_url": {
            "type": "string",
            "default": "",
            "title": "The git_pull_url Schema",
            "examples": [
                "https://gist.github.com/8980b6f77ec7439b5b1e2abac800f1c8.git"
            ]
        },
        "git_push_url": {
            "type": "string",
            "default": "",
            "title": "The git_push_url Schema",
            "examples": [
                "https://gist.github.com/8980b6f77ec7439b5b1e2abac800f1c8.git"
            ]
        },
        "html_url": {
            "type": "string",
            "default": "",
            "title": "The html_url Schema",
            "examples": [
                "https://gist.github.com/8980b6f77ec7439b5b1e2abac800f1c8"
            ]
        },
        "files": {
            "type": "object",
            "default": {},
            "title": "The files Schema",
            "required": [
                "python request module"
            ],
            "properties": {
                "python request module": {
                    "type": "object",
                    "default": {},
                    "title": "The python request module Schema",
                    "required": [
                        "filename",
                        "type",
                        "raw_url",
                        "size",
                        "content"
                    ],
                    "properties": {
                        "filename": {
                            "type": "string",
                            "default": "",
                            "title": "The filename Schema",
                            "examples": [
                                "python request module"
                            ]
                        },
                        "type": {
                            "type": "string",
                            "default": "",
                            "title": "The type Schema",
                            "examples": [
                                "text/plain"
                            ]
                        },
                        "raw_url": {
                            "type": "string",
                            "default": "",
                            "title": "The raw_url Schema",
                            "examples": [
                                "https://gist.githubusercontent.com/Pk8753/8980b6f77ec7439b5b1e2abac800f1c8/raw/e2cfd01ed51afe4cbb46a9de7335fc91f813b6bd/python%20request%20module"
                            ]
                        },
                        "size": {
                            "type": "integer",
                            "default": 0,
                            "title": "The size Schema",
                            "examples": [
                                93
                            ]
                        },
                        "content": {
                            "type": "string",
                            "default": "",
                            "title": "The content Schema",
                            "examples": [
                                "Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                            ]
                        }
                    },
                    "examples": [{
                        "filename": "python request module",
                        "type": "text/plain",
                        "raw_url": "https://gist.githubusercontent.com/Pk8753/8980b6f77ec7439b5b1e2abac800f1c8/raw/e2cfd01ed51afe4cbb46a9de7335fc91f813b6bd/python%20request%20module",
                        "size": 93,
                        "content": "Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                    }]
                }
            },
            "examples": [{
                "python request module": {
                    "filename": "python request module",
                    "type": "text/plain",
                    "raw_url": "https://gist.githubusercontent.com/Pk8753/8980b6f77ec7439b5b1e2abac800f1c8/raw/e2cfd01ed51afe4cbb46a9de7335fc91f813b6bd/python%20request%20module",
                    "size": 93,
                    "content": "Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                }
            }]
        },
        "created_at": {
            "type": "string",
            "default": "",
            "title": "The created_at Schema",
            "examples": [
                "2022-05-02T12:39:51Z"
            ]
        },
        "updated_at": {
            "type": "string",
            "default": "",
            "title": "The updated_at Schema",
            "examples": [
                "2022-05-02T12:39:51Z"
            ]
        },
        "description": {
            "type": "string",
            "default": "",
            "title": "The description Schema",
            "examples": [
                "GIST created by python code"
            ]
        },
        "comments": {
            "type": "integer",
            "default": 0,
            "title": "The comments Schema",
            "examples": [
                0
            ]
        },
        "comments_url": {
            "type": "string",
            "default": "",
            "title": "The comments_url Schema",
            "examples": [
                "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/comments"
            ]
        },
        "owner": {
            "type": "object",
            "default": {},
            "title": "The owner Schema",
            "required": [
                "login",
                "id",
                "node_id",
                "avatar_url",
                "gravatar_id",
                "url",
                "html_url",
                "followers_url",
                "following_url",
                "gists_url",
                "starred_url",
                "subscriptions_url",
                "organizations_url",
                "repos_url",
                "events_url",
                "received_events_url",
                "type"
            ],
            "properties": {
                "login": {
                    "type": "string",
                    "default": "",
                    "title": "The login Schema",
                    "examples": [
                        "Pk8753"
                    ]
                },
                "id": {
                    "type": "integer",
                    "default": 0,
                    "title": "The id Schema",
                    "examples": [
                        39435039
                    ]
                },
                "node_id": {
                    "type": "string",
                    "default": "",
                    "title": "The node_id Schema",
                    "examples": [
                        "MDQ6VXNlcjM5NDM1MDM5"
                    ]
                },
                "avatar_url": {
                    "type": "string",
                    "default": "",
                    "title": "The avatar_url Schema",
                    "examples": [
                        "https://avatars.githubusercontent.com/u/39435039?v=4"
                    ]
                },
                "gravatar_id": {
                    "type": "string",
                    "default": "",
                    "title": "The gravatar_id Schema",
                    "examples": [
                        ""
                    ]
                },
                "url": {
                    "type": "string",
                    "default": "",
                    "title": "The url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753"
                    ]
                },
                "html_url": {
                    "type": "string",
                    "default": "",
                    "title": "The html_url Schema",
                    "examples": [
                        "https://github.com/Pk8753"
                    ]
                },
                "followers_url": {
                    "type": "string",
                    "default": "",
                    "title": "The followers_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/followers"
                    ]
                },
                "following_url": {
                    "type": "string",
                    "default": "",
                    "title": "The following_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/following{/other_user}"
                    ]
                },
                "gists_url": {
                    "type": "string",
                    "default": "",
                    "title": "The gists_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/gists{/gist_id}"
                    ]
                },
                "starred_url": {
                    "type": "string",
                    "default": "",
                    "title": "The starred_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/starred{/owner}{/repo}"
                    ]
                },
                "subscriptions_url": {
                    "type": "string",
                    "default": "",
                    "title": "The subscriptions_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/subscriptions"
                    ]
                },
                "organizations_url": {
                    "type": "string",
                    "default": "",
                    "title": "The organizations_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/orgs"
                    ]
                },
                "repos_url": {
                    "type": "string",
                    "default": "",
                    "title": "The repos_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/repos"
                    ]
                },
                "events_url": {
                    "type": "string",
                    "default": "",
                    "title": "The events_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/events{/privacy}"
                    ]
                },
                "received_events_url": {
                    "type": "string",
                    "default": "",
                    "title": "The received_events_url Schema",
                    "examples": [
                        "https://api.github.com/users/Pk8753/received_events"
                    ]
                },
                "type": {
                    "type": "string",
                    "default": "",
                    "title": "The type Schema",
                    "examples": [
                        "User"
                    ]
                }
            },
            "examples": [{
                "login": "Pk8753",
                "id": 39435039,
                "node_id": "MDQ6VXNlcjM5NDM1MDM5",
                "avatar_url": "https://avatars.githubusercontent.com/u/39435039?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Pk8753",
                "html_url": "https://github.com/Pk8753",
                "followers_url": "https://api.github.com/users/Pk8753/followers",
                "following_url": "https://api.github.com/users/Pk8753/following{/other_user}",
                "gists_url": "https://api.github.com/users/Pk8753/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/Pk8753/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/Pk8753/subscriptions",
                "organizations_url": "https://api.github.com/users/Pk8753/orgs",
                "repos_url": "https://api.github.com/users/Pk8753/repos",
                "events_url": "https://api.github.com/users/Pk8753/events{/privacy}",
                "received_events_url": "https://api.github.com/users/Pk8753/received_events",
                "type": "User"
            }]
        },
        "forks": {
            "type": "array",
            "default": [],
            "title": "The forks Schema",
            "items": {},
            "examples": [
                []
            ]
        },
        "history": {
            "type": "array",
            "default": [],
            "title": "The history Schema",
            "items": {
                "type": "object",
                "default": {},
                "title": "A Schema",
                "required": [
                    "user",
                    "version",
                    "committed_at",
                    "change_status",
                    "url"
                ],
                "properties": {
                    "user": {
                        "type": "object",
                        "default": {},
                        "title": "The user Schema",
                        "required": [
                            "login",
                            "id",
                            "node_id",
                            "avatar_url",
                            "gravatar_id",
                            "url",
                            "html_url",
                            "followers_url",
                            "following_url",
                            "gists_url",
                            "starred_url",
                            "subscriptions_url",
                            "organizations_url",
                            "repos_url",
                            "events_url",
                            "received_events_url",
                            "type"
                        ],
                        "properties": {
                            "login": {
                                "type": "string",
                                "default": "",
                                "title": "The login Schema",
                                "examples": [
                                    "Pk8753"
                                ]
                            },
                            "id": {
                                "type": "integer",
                                "default": 0,
                                "title": "The id Schema",
                                "examples": [
                                    39435039
                                ]
                            },
                            "node_id": {
                                "type": "string",
                                "default": "",
                                "title": "The node_id Schema",
                                "examples": [
                                    "MDQ6VXNlcjM5NDM1MDM5"
                                ]
                            },
                            "avatar_url": {
                                "type": "string",
                                "default": "",
                                "title": "The avatar_url Schema",
                                "examples": [
                                    "https://avatars.githubusercontent.com/u/39435039?v=4"
                                ]
                            },
                            "gravatar_id": {
                                "type": "string",
                                "default": "",
                                "title": "The gravatar_id Schema",
                                "examples": [
                                    ""
                                ]
                            },
                            "url": {
                                "type": "string",
                                "default": "",
                                "title": "The url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753"
                                ]
                            },
                            "html_url": {
                                "type": "string",
                                "default": "",
                                "title": "The html_url Schema",
                                "examples": [
                                    "https://github.com/Pk8753"
                                ]
                            },
                            "followers_url": {
                                "type": "string",
                                "default": "",
                                "title": "The followers_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/followers"
                                ]
                            },
                            "following_url": {
                                "type": "string",
                                "default": "",
                                "title": "The following_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/following{/other_user}"
                                ]
                            },
                            "gists_url": {
                                "type": "string",
                                "default": "",
                                "title": "The gists_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/gists{/gist_id}"
                                ]
                            },
                            "starred_url": {
                                "type": "string",
                                "default": "",
                                "title": "The starred_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/starred{/owner}{/repo}"
                                ]
                            },
                            "subscriptions_url": {
                                "type": "string",
                                "default": "",
                                "title": "The subscriptions_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/subscriptions"
                                ]
                            },
                            "organizations_url": {
                                "type": "string",
                                "default": "",
                                "title": "The organizations_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/orgs"
                                ]
                            },
                            "repos_url": {
                                "type": "string",
                                "default": "",
                                "title": "The repos_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/repos"
                                ]
                            },
                            "events_url": {
                                "type": "string",
                                "default": "",
                                "title": "The events_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/events{/privacy}"
                                ]
                            },
                            "received_events_url": {
                                "type": "string",
                                "default": "",
                                "title": "The received_events_url Schema",
                                "examples": [
                                    "https://api.github.com/users/Pk8753/received_events"
                                ]
                            },
                            "type": {
                                "type": "string",
                                "default": "",
                                "title": "The type Schema",
                                "examples": [
                                    "User"
                                ]
                            }
                        },
                        "examples": [{
                            "login": "Pk8753",
                            "id": 39435039,
                            "node_id": "MDQ6VXNlcjM5NDM1MDM5",
                            "avatar_url": "https://avatars.githubusercontent.com/u/39435039?v=4",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/Pk8753",
                            "html_url": "https://github.com/Pk8753",
                            "followers_url": "https://api.github.com/users/Pk8753/followers",
                            "following_url": "https://api.github.com/users/Pk8753/following{/other_user}",
                            "gists_url": "https://api.github.com/users/Pk8753/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/Pk8753/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/Pk8753/subscriptions",
                            "organizations_url": "https://api.github.com/users/Pk8753/orgs",
                            "repos_url": "https://api.github.com/users/Pk8753/repos",
                            "events_url": "https://api.github.com/users/Pk8753/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/Pk8753/received_events",
                            "type": "User"
                        }]
                    },
                    "version": {
                        "type": "string",
                        "default": "",
                        "title": "The version Schema",
                        "examples": [
                            "daafd1e84e587000aff0729ddfb1576ad83f9873"
                        ]
                    },
                    "committed_at": {
                        "type": "string",
                        "default": "",
                        "title": "The committed_at Schema",
                        "examples": [
                            "2022-05-02T12:39:51Z"
                        ]
                    },
                    "change_status": {
                        "type": "object",
                        "default": {},
                        "title": "The change_status Schema",
                        "required": [
                            "total",
                            "additions",
                            "deletions"
                        ],
                        "properties": {
                            "total": {
                                "type": "integer",
                                "default": 0,
                                "title": "The total Schema",
                                "examples": [
                                    4
                                ]
                            },
                            "additions": {
                                "type": "integer",
                                "default": 0,
                                "title": "The additions Schema",
                                "examples": [
                                    4
                                ]
                            },
                            "deletions": {
                                "type": "integer",
                                "default": 0,
                                "title": "The deletions Schema",
                                "examples": [
                                    0
                                ]
                            }
                        },
                        "examples": [{
                            "total": 4,
                            "additions": 4,
                            "deletions": 0
                        }]
                    },
                    "url": {
                        "type": "string",
                        "default": "",
                        "title": "The url Schema",
                        "examples": [
                            "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/daafd1e84e587000aff0729ddfb1576ad83f9873"
                        ]
                    }
                },
                "examples": [{
                    "user": {
                        "login": "Pk8753",
                        "id": 39435039,
                        "node_id": "MDQ6VXNlcjM5NDM1MDM5",
                        "avatar_url": "https://avatars.githubusercontent.com/u/39435039?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/Pk8753",
                        "html_url": "https://github.com/Pk8753",
                        "followers_url": "https://api.github.com/users/Pk8753/followers",
                        "following_url": "https://api.github.com/users/Pk8753/following{/other_user}",
                        "gists_url": "https://api.github.com/users/Pk8753/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/Pk8753/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/Pk8753/subscriptions",
                        "organizations_url": "https://api.github.com/users/Pk8753/orgs",
                        "repos_url": "https://api.github.com/users/Pk8753/repos",
                        "events_url": "https://api.github.com/users/Pk8753/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/Pk8753/received_events",
                        "type": "User"
                    },
                    "version": "daafd1e84e587000aff0729ddfb1576ad83f9873",
                    "committed_at": "2022-05-02T12:39:51Z",
                    "change_status": {
                        "total": 4,
                        "additions": 4,
                        "deletions": 0
                    },
                    "url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/daafd1e84e587000aff0729ddfb1576ad83f9873"
                }]
            },
            "examples": [
                [{
                    "user": {
                        "login": "Pk8753",
                        "id": 39435039,
                        "node_id": "MDQ6VXNlcjM5NDM1MDM5",
                        "avatar_url": "https://avatars.githubusercontent.com/u/39435039?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/Pk8753",
                        "html_url": "https://github.com/Pk8753",
                        "followers_url": "https://api.github.com/users/Pk8753/followers",
                        "following_url": "https://api.github.com/users/Pk8753/following{/other_user}",
                        "gists_url": "https://api.github.com/users/Pk8753/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/Pk8753/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/Pk8753/subscriptions",
                        "organizations_url": "https://api.github.com/users/Pk8753/orgs",
                        "repos_url": "https://api.github.com/users/Pk8753/repos",
                        "events_url": "https://api.github.com/users/Pk8753/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/Pk8753/received_events",
                        "type": "User"
                    },
                    "version": "daafd1e84e587000aff0729ddfb1576ad83f9873",
                    "committed_at": "2022-05-02T12:39:51Z",
                    "change_status": {
                        "total": 4,
                        "additions": 4,
                        "deletions": 0
                    },
                    "url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/daafd1e84e587000aff0729ddfb1576ad83f9873"
                }]
            ]
        }
    },
    "examples": [{
        "url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8",
        "forks_url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/forks",
        "commits_url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/commits",
        "id": "8980b6f77ec7439b5b1e2abac800f1c8",
        "node_id": "G_kwDOAlm7H9oAIDg5ODBiNmY3N2VjNzQzOWI1YjFlMmFiYWM4MDBmMWM4",
        "git_pull_url": "https://gist.github.com/8980b6f77ec7439b5b1e2abac800f1c8.git",
        "git_push_url": "https://gist.github.com/8980b6f77ec7439b5b1e2abac800f1c8.git",
        "html_url": "https://gist.github.com/8980b6f77ec7439b5b1e2abac800f1c8",
        "files": {
            "python request module": {
                "filename": "python request module",
                "type": "text/plain",
                "raw_url": "https://gist.githubusercontent.com/Pk8753/8980b6f77ec7439b5b1e2abac800f1c8/raw/e2cfd01ed51afe4cbb46a9de7335fc91f813b6bd/python%20request%20module",
                "size": 93,
                "content": "Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
            }
        },
        "created_at": "2022-05-02T12:39:51Z",
        "updated_at": "2022-05-02T12:39:51Z",
        "description": "GIST created by python code",
        "comments": 0,
        "comments_url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/comments",
        "owner": {
            "login": "Pk8753",
            "id": 39435039,
            "node_id": "MDQ6VXNlcjM5NDM1MDM5",
            "avatar_url": "https://avatars.githubusercontent.com/u/39435039?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Pk8753",
            "html_url": "https://github.com/Pk8753",
            "followers_url": "https://api.github.com/users/Pk8753/followers",
            "following_url": "https://api.github.com/users/Pk8753/following{/other_user}",
            "gists_url": "https://api.github.com/users/Pk8753/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Pk8753/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Pk8753/subscriptions",
            "organizations_url": "https://api.github.com/users/Pk8753/orgs",
            "repos_url": "https://api.github.com/users/Pk8753/repos",
            "events_url": "https://api.github.com/users/Pk8753/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Pk8753/received_events",
            "type": "User"
        },
        "forks": [],
        "history": [{
            "user": {
                "login": "Pk8753",
                "id": 39435039,
                "node_id": "MDQ6VXNlcjM5NDM1MDM5",
                "avatar_url": "https://avatars.githubusercontent.com/u/39435039?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Pk8753",
                "html_url": "https://github.com/Pk8753",
                "followers_url": "https://api.github.com/users/Pk8753/followers",
                "following_url": "https://api.github.com/users/Pk8753/following{/other_user}",
                "gists_url": "https://api.github.com/users/Pk8753/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/Pk8753/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/Pk8753/subscriptions",
                "organizations_url": "https://api.github.com/users/Pk8753/orgs",
                "repos_url": "https://api.github.com/users/Pk8753/repos",
                "events_url": "https://api.github.com/users/Pk8753/events{/privacy}",
                "received_events_url": "https://api.github.com/users/Pk8753/received_events",
                "type": "User"
            },
            "version": "daafd1e84e587000aff0729ddfb1576ad83f9873",
            "committed_at": "2022-05-02T12:39:51Z",
            "change_status": {
                "total": 4,
                "additions": 4,
                "deletions": 0
            },
            "url": "https://api.github.com/gists/8980b6f77ec7439b5b1e2abac800f1c8/daafd1e84e587000aff0729ddfb1576ad83f9873"
        }]
    }]
}