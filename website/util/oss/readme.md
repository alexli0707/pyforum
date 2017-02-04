##Oss工具包说明

###OssHelper为oss基类.任何对接的oss帮助类必须继承OssHelper并实现抽象方法.

###oss_manager作为对使用者开发的入口,通过oss_by_bucket_name(bucket_name)方法获取对应的bucket实例.


###使用:
    当前使用的是阿里云提供的oss,需要安装pip install oss2阿里云提供的oss帮助工具
    目前的bucket 
                "nb-imgs":图片bucket,
                "oss-newgamer-com": 各种包以及各类资源的bucket 
                
###注意:
    有新的项目无论是否是短期项目,都需要和运维人员沟通并创建对应的bucket,便于将来资金对应结算以及bucket与项目同生命周期的管理
    
    
###新的存储资源名称构建说明(旧的存储资源就保持原名迁移到各自业务的bucket上)

* 图片bucket :图片资源采用图片md5+ '.'+图片后缀的命名格式,例如0bedc67feb0ef8260c5834af87aedf88.jpeg
* 包bucket : 采用{统一资源id}.{包的版本号}+'/'+ 文件名的命名方式,例如  3.1430/newgame-release-v1.4.3for_update_test.apk