# vsm - Virtual Service Manager

**一个简单的命令行工具，用于在您的服务器上轻松管理多个静态文件 Web 服务。**

---

`vsm` 是一个围绕 `pm2` 和 `http-server` 的简单封装，旨在简化通过 `http-server` 托管的多个静态网站的管理。您可以使用简单的命令来注册、启动、停止、重启和查看您的服务状态。

## ✨ 功能

- **一键初始化**: 快速在 Ubuntu 服务器上安装所需依赖。
- **服务管理**: 轻松注册、启动、停止和重启静态 Web 服务。
- **进程守护**: 基于 `pm2`，确保您的服务稳定运行。
- **状态监控**: 快速查看所有服务的运行状态。
- **命令补全**: 为服务名称提供自动补全支持，提升效率。

## 🚀 安装

您可以通过 `pip` 从 GitHub 或 Gitee 安装最新版本：

```shell
# 从 GitHub
pip3 install git+https://github.com/Rhythmicc/vsm.git -U

# 或者从 Gitee
pip3 install git+https://gitee.com/RhythmLian/vsm.git -U
```

安装后，`vsm` 命令将变为可用。

## 🔧 使用方法

以下是 `vsm` 的常用命令：

### 1. 初始化环境

如果您使用的是 **Ubuntu** 系统，并且是首次使用，可以运行此命令来安装 `nodejs`, `npm`, `pm2` 和 `http-server`。

```shell
vsm init
```

如果您的当前用户没有 `apt` 的权限，请使用 `--with-sudo` 标志：

```shell
vsm init --with-sudo
```

### 2. 注册服务

在启动服务之前，您需要先注册它。注册时需要提供一个服务名称、服务的根目录路径以及要监听的端口。

```shell
vsm register <服务名> <路径> <端口>
```

**示例:**

```shell
# 注册一个名为 "my-blog" 的服务，它指向 /var/www/my-blog 目录，并在 8080 端口上运行
vsm register my-blog /var/www/my-blog 8080
```

### 3. 启动服务

使用服务名来启动一个已注册的服务。

```shell
vsm start <服务名>
```

**示例:**

```shell
vsm start my-blog
```

### 4. 停止服务

使用服务名来停止一个正在运行的服务。

```shell
vsm stop <服务名>
```

**示例:**

```shell
vsm stop my-blog
```

### 5. 重启服务

使用服务名来重启一个服务。

```shell
vsm restart <服务名>
```

**示例:**

```shell
vsm restart my-blog
```

### 6. 查看服务状态

查看由 `pm2` 管理的所有服务的当前状态。

```shell
vsm status
```

### 7. 获取帮助

查看所有可用的命令和选项。

```shell
vsm --help
```
