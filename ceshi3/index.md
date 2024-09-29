# [「源阅读」](https://legado.aoaostar.com)


 一些「源阅读」书源、订阅源、主题、说明

源阅读 APP [官方下载地址](https://github.com/gedoor/legado/releases)

## 工具

|  网站 | 说明  |
| ------------ | ------------ |
|[源阅读书源转换工具](https://rc.real9.cn/ ) |来源[CSDN](https://blog.csdn.net/wangrui1573/article/details/131898637)，用于将源阅读的书源转换为IOS源阅读APP的书源  |
|[美化发现工具](https://yuedu.juhua.fun/tool ) |关耳大神美化发现工具  |

## 网站

[猫公子源](https://yuedu.miaogongzi.net/gx.html )
[源仓库](https://www.yckceo.com/yuedu/shuyuan/index.html )
[一程书源](https://www.gitlink.org.cn/yi-c/yd)

##说明

### 将源阅读的书源转换为IOS源阅读APP的书源的说明

以`list:"`开头将`id`转为`#`；将`class`转为`.`；将`a.1@text`转为`a:nth-child(2)@text`；将`a.-1@text`转为`a:nth-last-child(1)@text`；将`a.!1@text`转为`a::not(:nth-of-type(2))@text`；
从**2024.08.16**开始，需要将 `  "lastUpdateTime": "1727576680671"`删除才可识别书源
````json
function replaceContent(text) {
                for (let i = 0; i < 5; i++) {
                    text = text
                        .replace(/(List": ")id\./g, '$1#')
                        .replace(/(List": ")class\./g, '$1.')
                        .replace(/(List": ".*?)@/g, '$1 ')
                        .replace(/(List": ".*?)\.0/g, '$1:nth-child(1)')
                        .replace(/(List": ".*?)\.1/g, '$1:nth-child(2)')
                        .replace(/(List": ".*?)\.2/g, '$1:nth-child(3)')
                        .replace(/(List": ".*?)!0/g, '$1:not(:nth-of-type(1))')
                        .replace(/(List": ".*?)!1/g, '$1:not(:nth-of-type(2))');
                }
                return text;
            }
````
Thanks for stopping by! 😁
