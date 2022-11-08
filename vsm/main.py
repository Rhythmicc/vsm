from QuickProject.Commander import Commander
from . import _ask
from . import *

app = Commander(name)


@app.command()
def init(with_sudo: bool = False):
    """
    初始化VSM运行环境 (Ubuntu)
    """
    command_ls = [
        "apt update",
        "apt install -y nodejs",
        "apt install -y npm",
        "npm install -g pm2",
        "npm install -g http-server",
    ]
    with QproDefaultConsole.status(
        "[bold green]Installing dependencies..."
        if user_lang != "zh"
        else "[bold green]正在安装依赖..."
    ):
        for item in command_ls:
            if with_sudo:
                item = "sudo " + item
            st, ct = external_exec(item)
            if st != 0:
                QproDefaultConsole.print(QproErrorString, ct)
                return
    QproDefaultConsole.print(
        QproInfoString, "init success" if user_lang != "zh" else "初始化成功"
    )


def service_check(service: str):
    if not config.valid_service(service):
        QproDefaultConsole.print(
            QproErrorString, "service not found" if user_lang != "zh" else "未找到服务"
        )
        return False
    return True


@app.custom_complete("service")
def start():
    return [{"name": i, "icon": "🚀"} for i in config.config if i != "sudo"]


@app.custom_complete("service")
def stop():
    return [{"name": i, "icon": "🛑"} for i in config.config if i != "sudo"]


@app.custom_complete("service")
def restart():
    return [{"name": i, "icon": "🔄"} for i in config.config if i != "sudo"]


@app.command()
def start(service: str):
    """
    启动服务

    :param service: 服务名
    """
    item = config.select(service)
    with QproDefaultConsole.status(
        f"[bold green]Starting {service}..."
        if user_lang != "zh"
        else f"[bold green]正在启动 {service}..."
    ):
        st, ct = external_exec(
            f'pm2 start http-server --name {service} -- {item["path"]} -p {item["port"]}',
            without_output=True,
        )
    if st != 0:
        QproDefaultConsole.print(QproErrorString, ct)
        return
    else:
        QproDefaultConsole.print(
            QproInfoString,
            f"Start {service} success" if user_lang != "zh" else f"启动 {service} 成功",
        )


@app.command()
def stop(service: str):
    """
    停止服务

    :param service: 服务名
    """
    with QproDefaultConsole.status(
        f"[bold green]Stopping {service}..."
        if user_lang != "zh"
        else f"[bold green]正在停止 {service}..."
    ):
        st, ct = external_exec(f"pm2 stop {service}", without_output=True)
    if st != 0:
        QproDefaultConsole.print(QproErrorString, ct)
        return
    else:
        QproDefaultConsole.print(
            QproInfoString,
            f"Stop {service} success" if user_lang != "zh" else f"停止 {service} 成功",
        )


@app.command()
def status():
    """
    查看服务状态
    """
    os.system("pm2 status")


@app.command()
def restart(service: str):
    """
    重启服务

    :param service: 服务名
    """
    app.real_call("stop", service)
    app.real_call("start", service)


@app.command()
def register(service: str, path: str, port: int):
    """
    注册服务

    :param service: 服务名
    :param path: 服务路径
    :param port: 服务端口
    """
    if service in ["sudo"]:
        QproDefaultConsole.print(
            QproErrorString,
            'service name cannot be "sudo"' if user_lang != "zh" else '服务名不能为 "sudo"',
        )
        return
    if not config.valid_port(port):
        QproDefaultConsole.print(
            QproErrorString, "port has been used" if user_lang != "zh" else "端口已被占用"
        )
        return
    if config.valid_service(service) and not _ask(
        {
            "type": "confirm",
            "message": "Service has been registered, do you want to overwrite it?"
            if user_lang != "zh"
            else "服务已被注册, 是否覆盖?",
            "default": False,
        }
    ):
        return
    config.update(service, {"path": os.path.abspath(path), "port": port})
    QproDefaultConsole.print(
        QproInfoString,
        f"Register {service} success" if user_lang != "zh" else f"注册 {service} 成功",
    )


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app.bind_pre_call("start", service_check)
    app.bind_pre_call("stop", service_check)
    app.bind_pre_call("restart", service_check)
    app()


if __name__ == "__main__":
    main()
