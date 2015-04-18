var app = angular.module('zop', []);

app.controller("search", ["$scope", "$http",function($scope, $http){
	$scope.locality="";
	$scope.state="";
	$scope.district = "";
	$scope.pincode = "";
	$scope.output_list = [];
	$scope.fetchRecords = function(){
		$scope.output_list = [];
		var locality_in = $scope.locality;
		var state_in = $scope.state;
		var district_in = $scope.district;
		var pincode_in = $scope.pincode;
		var urlToPost = '/api/search';
		var postData = { 'locality': locality_in, 'state': state_in, 'district': district_in, 'pincode': pincode_in };
		var reqObject = { url: urlToPost, method: "POST", data: postData, headers: { 'Content-Type': 'application/json' }, };
        var res = $http(reqObject);
        res.success(function(data, status, headers, config) {
           // alert( "Success message: " + JSON.stringify({data: data.response}));
           	if (data.result.length){
           		$scope.output_list = data.result;
           	}
           	else{
           		alert("No record found!");
           	}

        });
        res.error(function(data, status, headers, config, statusText) {
            // alert( "Error message: " + JSON.stringify({data: data.response}));
        });
		$scope.locality="";
		$scope.state="";
		$scope.district = "";
		$scope.pincode = "";
	};

}]);