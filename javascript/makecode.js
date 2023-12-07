function generatePassword(length) {
var characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
    var password = "";

    for (var i = 0; i < length; i++) { var randomIndex=Math.floor(Math.random() * characters.length); password
        +=characters.charAt(randomIndex); } return password; } // 使用方法：调用函数并传入你想要的密码长度 var
        myPassword=generatePassword(12); // 生成一个长度为 12 的密码 console.log(myPassword);
        console.log(myPassword);