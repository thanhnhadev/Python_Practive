// let username = "admin";
// let password = "123456";

// let inputUserName
// let inputPassword

// // login success
// // neu sai user name => sai user name
// // sai password => sai password
// if(inputUserName===username && inputPassword===password){
//     console.log("login successs");
// }else {
//     console.log("login fail");
//     if (inputUserName!==username) {
//         console.log("username sai");
//     }else if(inputPassword !== password){
//         console.log("password sai");
//     }
// }
// let year=2024;
// if(year%4===0 && year%100!==0){
//     console.log("la nam nhuan");
// }else{
//     console.log("khong phai la nam nhuan");
// }
let age = 25;
let hasJob = true;
let salary = 15000000; // VNĐ
let hasBadDebt = false;
if(age<18 && hasJob==false && salary<10000000 &&  hasBadDebt <10000000){
    console.log("Từ chối");
}else if(age>18 && hasJob==true && salary>=10000000 && hasBadDebt >10000000)
{
    console.log("Duyệt vay mức trung bình");
}
else(age>18 && hasJob==true && salary>=20000000 && hasBadDebt >20000000)
{
    console.log("Duyệt vay mức cao");
}
// Luật xét duyệt
// 1️⃣ Tuổi
// < 18 → ❌ "Từ chối: Chưa đủ tuổi"
// 2️⃣ Việc làm
// Không có việc → ❌ "Từ chối: Không có việc làm"
// 3️⃣ Lịch sử nợ
// Có nợ xấu → ❌ "Từ chối: Có nợ xấu"
// 4️⃣ Thu nhập
// ≥ 20 triệu → ✅ "Duyệt vay mức cao"
// ≥ 10 triệu → ✅ "Duyệt vay mức trung bình"
// < 10 triệu → ❌ "Từ chối: Thu nhập không đủ"