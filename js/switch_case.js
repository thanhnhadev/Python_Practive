// cho bien role
// ADMIN -> co the xem va sua thong tin cua user
// USER -> co the xem thong tin cua user
// GUEST -> co the xem thong tin cua user

// In ra:
// ADMIN → "Toàn quyền"
// USER → "Hạn chế"
// GUEST → "Chỉ xem"
let role ;
switch (role) {
    case admin:
        console.log("Toàn quyền");
        break;
    case user:
        console.log("Hạn chế");
        break;
    case guest:
        console.log("Chỉ xem");
        break;
    default:
        break;
}

// Cho biến statusCode:

// 200 → "OK"

// 201 → "Created"

// 400 → "Bad Request"

// 401 → "Unauthorized"

// 403 → "Forbidden"

// 404 → "Not Found"

// Khác → "Server Error"
let statusCode;
switch (statusCode) {
    case 200:
        console.log("statusCode: OK");
        break;
    case 201:
        console.log("statusCode: Created");
        break;
    case 400:
        console.log("statusCode: Bad Request");
        break;
    case 401:
        console.log("statusCode: Unauthorized");
        break;
    case 403:
        console.log("statusCode: Forbidden");
        break;
    case 404:
        console.log("statusCode: Not Found");
        break;
    default:
         console.log("statusCode: Server Error");
        break;
}

// String
// Summary
// template string ${}
// độ dài chuỗi : length
// in hoa : toUpperCase
// in thường: toLowerCase
// includes : kiểm tra chuỗi con có trong chuỗi mẹ
// indexOf : kiếm tra vị trí xuất hiện, nếu ko có trả về -1
// slice: cắt chuỗi tại ví trí (start, end)
// replace : thay thế
// trim : loải bỏ khoảng trắng
// split : cắt  chuỗi thành mảng

// const str = "Hello JavaScript";
// BT1: in ra độ dài của chuỗi
// BT2: viết hoa chuỗi
// BT3: viết thường chuỗi

// const str = "frontend developer";
// BT4: kiếm tra chuỗi có chứa developer hay không


// const str = "I love JS";
// BT5: Thay thế js bằng javascripts


// const str = "   Hello World   ";
// BT6: xoá khoảng trắng đầu cuối

const str = "Hello JavaScript";
console.log(str.length);
console.log(str.toUpperCase());
console.log(str.toLowerCase());

const str_1 = "frontend developer";
console.log(str_1.includes("developer"));

const str_2 = "I love JS";
console.log(str_2.replace("JS","javascripts"));

const str_3 = "   Hello World   ";
console.log(str_3.trim());
//---------------------------------
const str_4 = "hello"
console.log(str_4.charAt(0).toUpperCase()+str_4.slice(1));
let str_5="thanhnhadev@gmail.com"
console.log(`username:${str_5.split("@")[0]}`);
// isURL("https://google.com"/) → true, Bắt đầu bằng http:// hoặc https://
let isURL ="https://google.com"
console.log();

let url = "http";
let isUrl="https";
let domain = "google.com";

if (url) {
    console.log(`${url}://${domain}`);
    if (!url) {
      console.log(`${isUrl}://${domain}`);
    }
}else {
    console.log("false");
}







