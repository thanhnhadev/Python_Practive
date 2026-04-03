// 1. Đếm số ký tự trong chuỗi
// Input: "hello"
// Output: 5
// const input="hello"
// console.log(input.length);

// -----------------------
// 2. In từng ký tự của chuỗi
// Input: "abc"
// Output:
// a
// b
// c
// let str="abc"
// for(let i =0; i<str.length;i++){
//     console.log(str[i]);
// }

// -----------------------
// 3. Đếm số nguyên âm trong chuỗi
// a, e, i, o, u
// Input: "abc"
// Output: 1
// function checkNguyenAm(str) {
//     for (let index = 0; index < array.length; index++) {
//         if (condition) {
//             const element = array[index];
//             const str = "aeiou"
//             console.log(str.includes("a"));
//         }
//     }
// }

// -----------------------
// 4. Đếm số chữ cái in hoa
// Dùng Character.isUpperCase().
// Input: "HeLLo"
// Output: 3
// Character.isUpperCase()

// let str = "HeLLo"
// let count = 0;
// for(let i = 0; i<str.length;i++){
//     if(str[i]===str[i].toUpperCase()){
//         console.log(i);
//         count++;
//     }
// }
// console.log("so chu in hoa:",count);

// -----------------------
// 5. Đảo ngược chuỗi
// Input: "hello"
// Output: "olleh"
let str = "hello"
let reversed = "";
for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
}
console.log(reversed);