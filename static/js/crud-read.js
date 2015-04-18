var app = angular.module("zopCrud", []);

app.controller("crudReadDelete", ["$scope", "$http",function($scope, $http){
	$scope.oid = "";
	$scope.readRecord = function(){
		var object_id = $scope.oid;
		if(object_id.length){
			var urlToGet = '/api/record/' + object_id;
			var postData = { };
			var reqObject = { url: urlToGet, method: "GET", data: postData, headers: { 'Content-Type': 'application/json' }, };
	        var res = $http(reqObject);
	        res.success(function(data, status, headers, config) {
	           	$("#readResponse").text(JSON.stringify(data.result));
	        });
	        res.error(function(data, status, headers, config, statusText) {
	           	$("#readResponse").text(JSON.stringify(data.result));
	        });
    	};
    	$scope.oid="";
	};
	$scope.deleteRecord = function(){
		var object_id = $scope.oid;
		if(object_id.length){
			var urlToGet = '/api/record/' + object_id;
			var postData = { };
			var reqObject = { url: urlToGet, method: "DELETE", data: postData, headers: { 'Content-Type': 'application/json' }, };
	        var res = $http(reqObject);
	        res.success(function(data, status, headers, config) {
	        	if (data.response==200){
	           		$("#readResponse").text("Record deleted successfully.");	
	        	}
	        	if (data.response==400){
	           		$("#readResponse").text("Couldn't delete record.");	
	        	}
	        });
	        res.error(function(data, status, headers, config, statusText) {
	        	if (data.response==400){
	           		$("#readResponse").text("Couldn't delete record.");	
	        	}
	        });
    	};
    	$scope.oid="";
	};
}]);