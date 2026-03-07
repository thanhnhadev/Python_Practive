// BT3: isURL("https://google.com"/) → true, Bắt đầu bằng http:// hoặc https://
const isUrl ="https://google.com"
console.log(isUrl.startsWith("https://")||isUrl.startsWith("http://"));
// BT4 : countWords("Hello world") → 2, Các từ cách nhau bởi 1 hoặc nhiều khoảng trắng
var s = "Hello world"
function countWords(string) {
   const a= string.split(" ")
   console.log(a);
   console.log(a.length);
}
countWords(s)

const email = "abc@gmail.com"
function isValidEmail(){
    if( email.includes("@") && email.includes(".") && !email.includes("") && email.indexOf("@") < email.indexOf("."))
        return true
    return false
}
console.log(isValidEmail(email));

