# 💻 WechatImgDatDecodeQt

**WechatImgDatDecodeQt** 基于 `Pyqt6`，用于解析微信图片 `.dat`，转换为其原始格式（png、jpg 或 gif)。


> 注：
>  最新版本不再支持旧版微信，如需解析旧版微信文件结构，请使用 `Release/v1.0.4` 之前的版本。
>  支持 Linux 微信，实测在 archlinux 和 ubuntu 系统下运行正常。

## 使用方法

选择下面两种方式任意一种，运行软件后，选择要处理的微信图片路径 `..\WeChat Files\xxx\FileStorage\MsgAttach`，并选择要保存解析后的图片的路径，确认无误后点击转换，会自动识别处理路径中的 `Image` 文件夹下的 `.dat` 文件，并按照 `yyyy-mm` 格式保存到输出文件夹。

### 下载安装

前往 [releases](https://github.com/nixgnauhcuy/WechatImgDatDecodeQt/releases) 发布页，下载最新版本的程序，解压后运行 `.exe` 即可。

### 编译运行

``` bash
git clone https://github.com/nixgnauhcuy/WechatImgDatDecodeQt.git
cd WechatImgDatDecodeQt
pip install -r requirements.txt
cd src
python main.py
```

## 效果预览

| Name             | Preview                 |
| ---------------- | ----------------------- |
| win              | ![](/assert/win.gif)    |
| linux            | ![](/assert/linux.gif)  |



