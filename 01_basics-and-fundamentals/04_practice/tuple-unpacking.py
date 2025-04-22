import os

mock_env_vars = {
    "GITHUB_TOKEN": "mock_token",
    "GITHUB_REPOSITORY": "mock_user/mock_repo",
    "GITHUB_RUN_ID": "123456789",
    "PROJECT_ID": "123",
    "GITHUB_RUN_NUMBER": "1",
}


def set_env_vars():
    for key, value in mock_env_vars.items():
        os.environ[key] = value


set_env_vars()

req_vars = {
    "GITHUB_TOKEN": (str, "default_token"),
    "GITHUB_REPOSITORY": (str, "default_repo"),
    "GITHUB_RUN_ID": (str, "default_run_id"),
    "PROJECT_ID": (int, 0),
    "GITHUB_RUN_NUMBER": (int, 0),
}

provider_vars = {}

for var_name, var_type in req_vars.items():
    if isinstance(var_type, tuple):
        type_class, default = var_type
        value = os.getenv(var_name)
        if value is None:
            provider_vars[var_name] = default
        else:
            try:
                provider_vars[var_name] = type_class(value)
            except ValueError as exc:
                raise ValueError(
                    f"Environment variable {var_name} must be of type {type_class.__name__}"
                ) from exc
    else:
        if var_name not in os.environ:
            raise ValueError(f"Environment variable {var_name} is required")
        try:
            type_class, _ = var_type
            provider_vars[var_name] = type_class(os.environ[var_name])
        except ValueError as exc:
            raise ValueError(
                f"Environment variable {var_name} must be of type {type_class.__name__}"
            ) from exc


print(provider_vars)
