# JavaScript knowledge and skill

### Prettier and VS Code

Prettier

1. 在扩展中搜索prettier并安装

2. 在设置中搜索default form,选Prettier

3. 勾选format on save

4. 在父文件夹中创建.prettierrc

5. ```json
   {
     "singleQuote": true,
     "arrowParens": "avoid"
   }
   
   ```

Snippets

1. 齿轮 => User Snippets

2. ```json
   "Print to console": {
   		"scope": "javascript,typescript",
   		"prefix": "cl",
   		"body": [
   			"console.log($1);"
   		],
   		"description": "Log output to console"
   	}
   ```

### Node.js

保存文件自动加载网页

- VS Code扩展 => Live Server
-  使用Node.js
  1. 官网安装Node.js
  2. `npm install live-server -g`
  3. 在当前文件夹中运行`live-server`

