**English** | [中文](readme_cn.md)

<h1 align="center"> MCDReforged PluginCatalogue</h1>
<h3 align="center"><i> (with <a href="https://mirror.ghproxy.com//">GitHub Proxy</a>)</i></h3>
<p align="center"> 
  A repository for listing <a href="https://github.com/Fallen-Breath/MCDReforged">MCDReforged</a> plugins.
  <br><i>
  Replaced all the download URLs to GitHub in <a href="https://github.com/Lazy-Bing-Server/PluginCatalogue-GP/tree/meta">meta</a> branch to accelerate automatic plugin management
  </i><br>
  <br>
  <a href="https://github.com/Lazy-Bing-Server/PluginCatalogue-GP/blob/catalogue/readme.md"><strong>Main Plugins Catalogue</strong></a>
  ·
  <a href="https://github.com/MCDReforged/PluginCatalogue/blob/legacy/readme.md">Legacy Plugins Catalogue</a> 
  <br>
  <i>Current repository didn't copy the data of original repository and therefore the legacy catalogue link above still directs to the legacy branch of original repository</i>
  <br>
  <i>If you are accessing this repo with GitHub Proxy, clicking this link will only bring you back here and nothing will happen</i>
</p>
<br>


> ⚠️ **Warning: Before using any plugin, please read the README file in its repository.**

<br>

**Main Plugins Catalogue** contains plugins that support MCDReforged >= 2.x

**Legacy Plugins Catalogue** contains plugins for earlier versions of MCDR. They may not be compatible with current version of MCDR. Use them with caution

If you would like to add your plugin to the plugin repository, you may wish to submit a PR. **Note that these PR should be submitted to [the original repository](https://github.com/MCDReforged/PluginCatalogue).** Check out the [documentation](https://mcdreforged.readthedocs.io/en/latest/plugin_dev/plugin_catalogue.html) for more information

You can learn about the plugin data provided by the plugin repository [here](https://github.com/Lazy-Bing-Server/PluginCatalogue-GP/tree/meta)

## Plugin Source Configuration

When connection to GitHub is unstable, change the plugin source configuration to this repo for plugin managers to accelerate download. The following are the ways to configure plugin source for plugin managers, if there's any different in configuration to the document of the mentioned plugin manager, please make the description in its own document your primary reference

> ⚠️ <strong>Warning: GitHub Proxy service is not absolutely stable. when access to the plugin source configured as following is denied, please restore plugin source config. </strong>

### [MCDReforged](https://mcdreforged.com) official plugin management

MCDReforged introduced plugin installation feature in version 2.13

Configure the specified field here in MCDR config file `config.yml` to:

```commandline
catalogue_meta_url: https://mirror.ghproxy.com/https://raw.githubusercontent.com/Lazy-Bing-Server/PluginCatalogue-GP/meta/everything.json.xz
```

### [MCDReforged Plugin Manager](https://github.com/Ivan-1F/MCDReforgedPluginManager) *(by [Ivan1F](https://github.com/Ivan-1F))*

Configure the following field in its configuration file `config/mcdreforged_plugin_manager/config.yml` to：

```commandline
source: https://mirror.ghproxy.com/https://github.com/Lazy-Bing-Server/PluginCatalogue-GP/archive/refs/heads/meta.zip
```
