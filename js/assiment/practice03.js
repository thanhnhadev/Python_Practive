// BT5: isValidEmail("abc@gmail.com") → true , Có ký tự @, có dấu . , @ đứng trước ., Không chứa khoảng trắng

// BT6: isEmpty("") → true
// findLongestWord("I love programming") // "programming"
function findLongestWord(str){
    let words = str.split(" ");
    let longest = "";
    for(let word of words){
        if(word.length> longest.length){
            longest= word
        }
    }
    return longest
}
console.log(findLongestWord("I love Programing"));
//removeDuplicateChars("aabbccdde") // "abcde"
function removeDuplicates(str) {
    let result = "";
    for (let char of str) {
        if (!result.includes(char)) {
            result += char;
        }
    }
    return result;
}
console.log(removeDuplicates("aabbccdde"));
//decompressString("a3b2c1") // "aaabbc"
function decompress(inputString) {
    // Tạo biến lưu kết quả
    let result = "";
    // Duyệt từng cặp: chữ + số
    for (let index = 0; index < inputString.length; index = index + 2) {
        // Lấy ký tự (ví dụ: "a")
        let character = inputString[index];
        // Lấy số phía sau (ví dụ: "3") và chuyển thành số
        let count = Number(inputString[index + 1]);
        // Lặp lại ký tự theo số lần và cộng vào kết quả
        let repeatedText = character.repeat(count);
        result = result + repeatedText;
    }
    // Trả về kết quả cuối cùng
    return result;
}
// Test thử
let output = decompress("a3b2c1");
console.log(output); // aaabbc
// aaabbc
function decompressString(strs){
    let result = ""
   for (let i = 0; i< strs.length; i+=2){
        const char = strs[i] // a
        const count = Number(strs[i+1])//3
        result+=char.repeat(count)
   }
   console.log(113113, result);
}
decompressString("a3b2c1")