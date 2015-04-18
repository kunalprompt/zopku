var app = angular.module("zopCrud", []);

app.controller("crudUpdate", ["$scope", "$http",function($scope, $http){
	$scope.oid="";
	$scope.officeName="";
	$scope.pincode="";
	$scope.officeType="";
	$scope.deliveryStatus="";
	$scope.divisionName="";
	$scope.regionName="";
	$scope.circleName="";
	$scope.taluk="";
	$scope.districtName="";
	$scope.stateName="";
	$scope.updateRecord = function(){
		var oid = $scope.oid;
		var off_name = $scope.officeName;
		var	pin_code = $scope.pincode;
		var	off_type = $scope.officeType;
		var	del_status = $scope.deliveryStatus;
		var	dev_name = $scope.divisionName;
		var	reg_name = $scope.regionName;
		var	cir_name = $scope.circleName;
		var	taluk = $scope.taluk;
		var	dis_name = $scope.districtName;
		var	st_name = $scope.stateName;

		var urlToPost = '/api/create';
		var postData = {
			"id": oid,
			"officeName": off_name,
			"pincode": pin_code,
			"officeType": off_type,
			"deliveryStatus": del_status,
			"divisionName": dev_name,
			"regionName": reg_name,
			"circleName": cir_name,
			"taluk": taluk,
			"districtName": dis_name,
			"stateName": st_name,
		};
		var reqObject = { url: urlToPost, method: "PUT", data: postData, };
        var res = $http(reqObject);
        res.success(function(data, status, headers, config) {
        	if (data.response==200) {alert("Record updated successfully.");}
           	else if (data.response==400) {alert("Can't update record.");}
        });
        res.error(function(data, status, headers, config, statusText) {
           	if (data.response==400) {alert("Can't update record.");}
        });
		$scope.oid="";
		$scope.officeName="";
		$scope.pincode="";
		$scope.officeType="";
		$scope.deliveryStatus="";
		$scope.divisionName="";
		$scope.regionName="";
		$scope.circleName="";
		$scope.taluk="";
		$scope.districtName="";
		$scope.stateName="";
	};
}]);