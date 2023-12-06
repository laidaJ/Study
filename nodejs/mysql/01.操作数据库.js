// 1.导入mysql模块
const { connect } = require('http2');
const mysql = require('mysql');
// 2.建立与mysql的连接关系
const db = mysql.createPool({
    host: '127.0.0.1',
    user: 'lesen',
    password: '123',
    database: 'test'
})
// 3.测试是否正常工作
db.query('select 1', (err, results) => {
    if (err) return console.log(err.message);
    console.log(results);
})

// 4.查询users表中所有的数据
const sqlStr = 'select * from user';
db.query(sqlStr, (err, results) => {
    if (err) return console.log(err.message);
    console.log(results);
})

// 要插入到user的数据对象
const user = { name: 'guanzhon', age: 34 }
// 执行sql语句,其中?表示占位符
const sqlInsert = 'INSERT INTO user (name,age) VALUES (?, ?)';
// 使用数组的形式,依次为?指定具体的值
db.query(sqlInsert, [user.name, user.age], (err, results) => {
    if (err) return console.log(err.message)
    if (results.affectedRows === 1) { console.log('success') }
})