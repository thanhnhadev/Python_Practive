// 4. Đếm số chữ cái in hoa
// Dùng Character.isUpperCase().
// Input: "HeLLo"
// Output: 3
const input = "HeLLo"
let count =0;
for(let char of input){
    if(char>='A' && char<='Z'){
        count++;
    }
}
console.log("ouput:",count);
// 5. Đảo ngược chuỗi
// Input: "hello"
// Output: "olleh"
const name="hello"
let result = "";
for (let i = input.length - 1; i >= 0; i--) {
    result += input[i];
}
console.log(result);
//  6. Kiểm tra chuỗi đối xứng
// Input: "madam"
// Output: true
const inputname="madam";
let isCheck=true;
for(let i=0;i< input.length/2;i++){
    if(inputname[i]!==inputname[inputname.length-1-i]){
        isCheck=false;
        break;
    }
}
console.log(isCheck);
// 7. Đếm số lần xuất hiện của một ký tự
// Input: s = "banana", target = 'a'
// Output: 3
const s = "banana";
const target = 'a';
const counts = s.split(target).length - 1;
console.log(counts);
// 10. Nối hai chuỗi
// Input: "hello", "world"
// Output: "helloworld"
const s1 = "hello";
const s2 = "world";
const results = `${s1} ${s2}`; 
console.log(results);