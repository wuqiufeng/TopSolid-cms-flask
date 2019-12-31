# TopSolid-cms-flask
启动步骤

1.  安装依赖包
    > pip install -r requirements.txt

2.  启动服务
    >运行根目录下run.py脚本

3. UI页面地址
    * 注意每次重建UI以后发现页面没变化最好浏览器清一次缓存，因为静态页面引用缓存经常出问题
    > http://127.0.0.1:8555/static/swagger-ui/index.html
	> http://127.0.0.1:8555/static/swagger-ui-v3/index.html

开发步骤

1.  编辑描述文件v2.yaml以后，根据描述文件重建UI以及项目目录
    >swagger_py_codegen --swagger-doc ./app/v2.yaml app -p . --ui --spec
	编辑描述文件v3.yaml以后，根据描述文件重建UI以及项目目录
    >swagger_py_codegen --swagger-doc ./app/v3.yaml app -p . --ui --spec

2.  实现业务逻辑
    >/onecity_v2/api/

3.  测试命令
    * 注意应该在根目录（./occapi）执行
    > python -m unittest tests.test_api

命令备忘

1.  根据SQL结构自动生成SQLAlchemy模型
    > sqlacodegen mysql+pymysql://occ:occ@192.168.50.224:3306/occo --outfile my_model.py


error status:
        
        http code == 200 # HTTP请求成功，且业务成功
        status:
        200：成功        
        
        http code == 400 # 表示HTTP请求收到，但是业务上未能完成
        status:
        1001：用户未找到
        1002：用户已存在
        1003: 角色未找到
        1004: 同名角色已存在
        1005: 角色已使用，不能删除
        1010：Mac不合法
        1011：设备未找到
        1012：设备已绑定
        1013：设备类型不支持
        1014：该设备类型需要额外信息才能绑定
        1021：场所未找到
        1022：重复的场所
        1023：该场所下已存在监管绑定的设备
        1031：监管人已绑定
        1032：监管人绑定失败
        1040：基站已存在
        1050：运营商云片错误
        1051：短信发送过于频繁
        1061：分销商未找到
        1062：重复的分销商
        1063: 分销商下已存在人员信息
        1070：不支持的系统角色
        2001: 该告警所属设备已解绑，不能再派工单了
        2011: 未找到该告警的工单
        2012: 无效的告警工单状态
        2013: 该告警已经由其他人派过工单了

        http code == 401 # 权限验证失败
        status:
        401：权限验证失败
        
        http code == 422 # 参数异常
        status:
        422：参数类型或者长度不符合要求
        
        http code == 429 # 表示HTTP请求收到，但是短时间请求次数过多，与业务无关
        status:
        429：请求次数过多``