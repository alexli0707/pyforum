#开发说明
写在所有的之前,这个项目并无任何野心,初衷是为了磨练服务端的编程水平,将来能发展到什么程度犹未可知.但是我们可以将很多了解过想实现或者练手的技术以及设计在这个项目中得以实现.So,have fun!

##后端
###环境搭建(目前先采用传统方式,docker的开发方式正在评估)
* 采用Python3.5版本开发,基于Flask框架,使用virtualenv做lib管理,建议路径为项目的venv/文件夹中.
* 如果当前os包含2.7以及3两种版本,可以运行
		
		virtualenv -p python3 venv
* 配置好virtualenv并active之后可以运行
		
		pip install  -r requirement.txt  
  以安装工具库
  


### HTTP返回码


        200  成功
        其他 失败

### HTTP 接口返回值结构

        {
            "meta":
            {
                "code": "业务码",
                "message": "状态信息"
            },
            "pagination": ...
            "data": ...
        }
    
        说明:
        pagination有两种
        1 普通分页
            {
                "rows_found": "找到的总记录数",
                "offset": "起始游标",
                "limit": "条数"
            }