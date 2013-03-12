define(["my/sayHello"], function(sayHello){
	sayHello = function(str){
		console.log(str);
	};
	return sayHello;
});