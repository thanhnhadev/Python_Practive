// ôn js
const strLen = "hello"
// check độ dài
console.log(strLen.length);

//viết in hoa
console.log(strLen.toUpperCase());

//viết thường
console.log(strLen.toLowerCase());

//bao gồm
console.log(strLen.includes("ello"));

//tìm vị trí đầu tiên trong chuỗi, nếu không có trả về -1
console.log(strLen.indexOf("lloe"));

//cắt chuỗi slice(start,end), không dùng cho mãng
console.log(strLen.slice(1,4));

//replace thay thế chuỗi đầu tiên tièm dc
const testreplace="hello java"
console.log(testreplace.replace("java","js"));

//split chuyển chuỗi thành mãng
const splitTest ="hello word,java"
console.log(splitTest.split(","));

//startWith  bắt đầu từ đầu
const startWithTest="hello"
console.log(startWithTest.startsWith("hel"));

//endWith bắt đầu từ cuối
console.log(startWithTest.endsWith("llo"));