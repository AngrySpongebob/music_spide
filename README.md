# music_spider
This is a script to crawl music.
> 本项目所有的代码均使用Python3.6.5进行开发
##### 网易云音乐爬虫需要用到的库
- 系统自带的库:csv sys time
- 第三方库: selenium
##### 酷我音乐爬虫需要用到的库
- 系统自带的库:csv re sys time
- 第三方库:requests
<p>
&nbsp;&nbsp;&nbsp;&nbsp;files 文件夹用于存放获取到的歌曲名以及对应的播放链接
music_file 用于存放下载到的歌曲,目前只有酷我音乐实现了这个功能
</p>
> 注意:网易云音乐需要用到headless浏览器,代码中所用到的是GoogleDriver,请自行下载,路径请根据个人情况进行修改