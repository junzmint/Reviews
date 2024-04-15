// Khai báo một mảng để lưu trữ các URL của các liên kết có thuộc tính data-sqe
var linksList = [];

// Lấy danh sách tất cả các thẻ <a> có thuộc tính data-sqe
var linksWithDataSqe = document.querySelectorAll("a[data-sqe]");

// Lặp qua từng thẻ <a> và thêm URL của chúng vào mảng linksList
linksWithDataSqe.forEach(function (link) {
  linksList.push(link.href);
});

// Chuyển đổi mảng linksList thành chuỗi JSON và in ra console
console.log(JSON.stringify(linksList, null, 2));

// This code is used on browser only
