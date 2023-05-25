[English](readme.md) | **中文**

<h1 align="center">MCDReforged PluginCatalogue</h1>
<h3 align="center"><i> (使用 <a href="http://fastgit.org/">FastGit UK</a>)</i></h3>

<p align="center">
  一个用于列出 <a href="https://github.com/Fallen-Breath/MCDReforged">MCDReforged</a> 插件的仓库。
  <br>
  <i><a href="https://github.com/Lazy-Bing-Server/PluginCatalogue-FG/tree/meta">meta</a> 分支中的 URL 已被替换为指向 FastGit 用以加速自动化插件管理</i>
  <br>
  <br>
  <a href="https://github.com/Lazy-Bing-Server/PluginCatalogue-FG/blob/catalogue/readme-zh_cn.md"><strong>主插件目录</strong></a>
  ·
  <a href="https://github.com/MCDReforged/PluginCatalogue/blob/legacy/readme_cn.md">旧插件目录</a>
  <br>
  <i>当前仓库未对原插件仓库中的旧插件目录实施镜像，因此上方的旧插件目录链接仍指向原插件仓库的旧插件分支</i>
  <br>
  <br>
  <a href="https://hub.fgit.ml/Lazy-Bing-Server/PluginCatalogue-FG">通过 FastGit UK 访问该仓库</a>
  <br>
  <i>若当前已经是通过 FastGit 访问，则点击以上链接将回到此处，无事发生</i>
  <br>
</p>
<br>

> ⚠️ **注意：在使用任何插件之前，请先阅读其仓库中的 README。**

<br>

**主插件目录** 仅包含支持 MCDReforged >=2.x 的插件

**旧插件目录** 收录早期版本 MCDR 的插件。这些过时的插件可能无法兼容当前版本的 MCDR，请谨慎使用

如果你想添加你的插件到插件仓库中，不妨交个 PR。**请注意这些 PR 应该被提交至[原插件仓库](https://github.com/MCDReforged/PluginCatalogue)**。查看 [文档](https://mcdreforged.readthedocs.io/zh_CN/latest/plugin_dev/plugin_catalogue.html) 以了解更多信息

你可以在 [这里](https://github.com/MCDReforged/PluginCatalogue/tree/meta) 了解到插件仓库提供的插件数据


## 插件源配置

当 GitHub 连接不稳定时，变更插件管理器的插件源配置指向该仓库可加速下载，以下介绍插件管理器中配置插件源的方式，如配置方式与该插件管理器文档存在出入，请首先参考它自己文档的描述

> ⚠️ **注意：FastGit 的服务并非绝对稳定，当无法访问如下配置的插件源时，请还原插件源配置**

### [MCDReforged Plugin Manager](https://github.com/Ivan-1F/MCDReforgedPluginManager) *(由 [Ivan1F](https://github.com/Ivan-1F) 开发)*


在其配置文件 `config/mcdreforged_plugin_manager/config.yml` 中调整如下配置: 

```commandline
source: https://hub.fgit.gq/Lazy-Bing-Server/PluginCatalogue-FG/archive/refs/heads/meta.zip
```

或者是

```commandline
source: https://hub.fgit.ml/Lazy-Bing-Server/PluginCatalogue-FG/archive/refs/heads/meta.zip
```

