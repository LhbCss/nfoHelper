# nfoHelper
# nfoHelper

##### 基于PythonOS库实现的小工具！

##### 本工具已经使用 pyinstaller 进行打包，打包为单 .exe 文件，下载即用！



## 主要功能为：

**批量修改文件夹名**

**通过 KMP 算法批量匹配旧文件夹字符串并将匹配成功的字符串修改为新字符串**

**批量修改 .nfo 描述文件中的艺人名；扫描当前目录下所有文件夹内的 .nfo 描述文件并修改描述信息内的艺人名**

**扫描当前目录下所有文件夹内的 .nfo 描述文件并修改艺人名称的同时修改文件夹名**



## 主要使用的库：

```python
import re
import os
```



## 主界面运行效果：

![image-20230518151959656](https://s2.xptou.com/2023/05/18/6465d3c18f62c.png)



## .nfo 影片描述文件简介：

​		**.nfo 是一种类似于 .xml 文件的影片（你懂的）信息描述文件，其格式如下：**

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<movie>
  <plot</plot>
  <title></title>
  <originaltitle></originaltitle>
  <director></director>
  <year></year>
  <mpaa></mpaa>
  <customrating></customrating>
  <countrycode></countrycode>
  <premiered></premiered>
  <release></release>
  <runtime></runtime>
  <country></country>
  <studio></studio>
  <id></id>
  <num></num>
  <set></set>
  <genre>系列:</genre>
  <genre>片商:</genre>
  <tag>系列:</tag>
  <tag>片商:</tag>
  <actor>
    <name></name>
    <type>Actor</type>
  </actor>
</movie>
```

**本工具实现了对 \<actor> 标签下的字标签 \<name> 定位并修改标签值，能够批量修改多个 .nfo 文件的该标签值，方便影片信息的管理**



## 工具运行效果：

![微信截图_20230518152821](https://s2.xptou.com/2023/05/18/6465d3bf2502f.png)
