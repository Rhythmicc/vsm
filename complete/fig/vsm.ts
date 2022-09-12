const completionSpec: Fig.Spec = {
    "name": "vsm",
    "description": "vsm",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助"
        },
        {
            "name": "init",
            "description": "init",
            "args": [
                {
                    "name": "--with_sudo",
                    "description": "<with_sudo>",
                    "isOptional": true,
                    "args": {
                        "name": "with_sudo",
                        "description": "<with_sudo>"
                    }
                }
            ],
            "options": []
        },
        {
            "name": "start",
            "description": "start",
            "args": [
                {
                    "name": "service",
                    "description": "<service>"
                }
            ],
            "options": []
        },
        {
            "name": "stop",
            "description": "stop",
            "args": [
                {
                    "name": "service",
                    "description": "<service>"
                }
            ],
            "options": []
        },
        {
            "name": "restart",
            "description": "restart",
            "args": [
                {
                    "name": "service",
                    "description": "<service>"
                }
            ],
            "options": []
        },
        {
            "name": "register",
            "description": "register",
            "args": [
                {
                    "name": "service",
                    "description": "<service>"
                },
                {
                    "name": "path",
                    "description": "<path>",
                    "template": [
                        "filepaths",
                        "folders"
                    ]
                },
                {
                    "name": "port",
                    "description": "<port>"
                }
            ],
            "options": []
        }
    ]
};
export default completionSpec;
