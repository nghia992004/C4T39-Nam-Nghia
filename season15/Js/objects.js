var movie ={
    title:"Batman",
    ratting:8.3,
};

console.log(movie.ratting);
// Có thể dùng console.log(movie["ratting"]) như trên python.Khi dùng [] nó sẽ biểu diễn file cụ thể hơn khi là "." như cách trên
//Chỉ dùng "." khi biết chắc thông tin đó là gì.

movie["ratting"] = 9;

console.log(movie.ratting);

//movie : object
//title : property
//"Batman" : value


var prop = "ratting";

console.log(movie[prop]);
