## GitHub常见用法

 <img src="http://pic1.win4000.com/mobile/2019-09-19/5d83307505cc9.jpg" height=50% width=50% title="AhriLove"><br>
 
#### 1.超链接使用：
	[vue.js 1.x 文档](https://v1-cn.vuejs.org/)：格式[文本内容](链接的URL)
	显示为：带有超链接的文本内容，隐藏链接的URL
	
#### 2.github的markdown写法：[MakeDown写法一](https://blog.csdn.net/BlueAmerTJ/article/details/51556308) &nbsp;&nbsp; [Makedown写法二](https://www.jianshu.com/p/40ba812dd973) &nbsp;&nbsp;&nbsp;[makedown写法三](https://www.jianshu.com/p/191d1e21f7ed)
   &nbsp;&nbsp;-2.1 换行：\<br> <br>
   &nbsp;&nbsp;-2.2 空格：\&nbsp;(分号一定要有)
   
#### 3.vscode 用git 拉取代码，提示：在签出前，请清理存储库工作树
	问题主要是git仓库上的代码和本地代码存在冲突。
	解决办法：
  >1.新建一个文件夹重新从git拉取最新的代码，使用beyond compare对比合并自己修改的代码到新拉的代码里，提交<br>
  >2.放弃本地修改，直接覆盖
  
	git reset --hard
	git pull
	


	
