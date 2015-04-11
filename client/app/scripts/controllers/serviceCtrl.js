define(["./controllers"], function(controllers) {
	"use strict";
	controllers.controller("serviceCtrl", [
		"$scope",
		function($scope){
			$scope.services = [];
			$scope.loading = false;
			$scope.saving = false;

			$scope.mask = "";
			$scope.maskTitle = "";
			$scope.maskDir = "";

			$scope.getApis = function(){
				$scope.loading = true;
				apis.getApis(false);
			};

			$scope.$on("apisLoaded", function(e, data){
				$scope.services = data;
				$scope.loading = false;
			});

			$scope.toggleExpand = function(id){
				for(var i in $scope.services){
					var service = $scope.services[i];
					if(service.id == id){
						service.expand = !service.expand;
					}
				}
			};

			$scope.service = {
				name: "",
				desc: ""
			};
			$scope.editService = function(e, s){
				$scope.deleteServiceConfirm = false;
				if(e){
					e.preventDefault();
					e.stopPropagation();
				}

				var title = "添加系统";

				$scope.service = {
					name: "",
					desc: ""
				};

				if(s){
					$scope.service = angular.copy(s);
					title = "编辑系统"
				}

				$scope.showMask("service", title);
			};

			$scope.serviceStatu = {
				name: ""
			};
			$scope.saveService = function(){
				$scope.serviceStatu = {
					name: ""
				};

				var method = "POST",
					url = OPS3_API
						+ "/useful/service",
					msg = "系统创建成功。";

				if($scope.service.id){ // edit
					method = "PUT";
					url = OPS3_API
						+ "/useful/service/"
						+ $scope.service.id;
					msg = "系统修改成功。";
				}

				if(!$scope.service.name){
					$scope.serviceStatu.name = "error";
				}else{
					$scope.saving = true;

					request.send(method,
						url,
						$scope.service,
						function(data, status){
							if(data.id){
								if($scope.service.id){ // edit
									for(var i in $scope.services){
										var s = $scope.services[i];
										if(s.id == data.id){
											s.name = data.name;
											s.desc = data.desc;
										}
									}
								}else{
									if(!$scope.services || !$scope.services.length){
										$scope.services = [];
									}
									$scope.services.push(data);
								}

								notice.showMsg({
									msg: msg,
									type: "info",
									close: true,
									duration: 3
								});

								$scope.hideMask();
								$scope.saving = false;
							}
						},
						function(data, status){
							var errorMsg = "系统保存数据";
							if(data && data.detail){
								errorMsg += "："
									+ data.detail;
							}
							
							notice.showMsg({
								msg: errorMsg,
								type: "error",
								close: true
							});
							$scope.saving = false;
						}
					);
				}
			};

			$scope.deleteServiceConfirm = false;
			$scope.deleteService = function(){
				$scope.deleteServiceConfirm = true;
			};
			$scope.deleteServiceOk = function(){
				$scope.saving = true;

				request.send("DELETE",
					OPS3_API
						+ "/useful/service/"
						+ $scope.service.id,
					{},
					function(data, status){
						for(var i in $scope.services){
							var s = $scope.services[i];
							if(s.id == $scope.service.id){
								$scope.services.splice(i, 1);
							}
						}

						notice.showMsg({
							msg: "系统已删除。",
							type: "info",
							close: true,
							duration: 3
						});

						$scope.hideMask();
						$scope.saving = false;
						$scope.deleteServiceConfirm = false;
					},
					function(data, status){
						var errorMsg = "系统删除失败";
						if(data && data.detail){
							errorMsg += "："
								+ data.detail;
						}
						
						notice.showMsg({
							msg: errorMsg,
							type: "error",
							close: true
						});
						$scope.saving = false;
					}
				);
			};
			$scope.deleteServiceCancel = function(){
				$scope.deleteServiceConfirm = false;
			};

			$scope.api = {
				handler: "",
				desc: "",
				service_id: null
			};
			$scope.editApi = function(s, e, a){
				$scope.deleteApiConfirm = false;

				if(e){
					e.preventDefault();
					e.stopPropagation();
				}

				$scope.service = s;

				var title = "添加 API";

				$scope.api = {
					handler: "",
					desc: ""
				};

				if(a){
					$scope.api = {
						id: a.id,
						handler: a.handler,
						desc: a.desc
					};
					title = "编辑 API"
				}

				$scope.api.service_id = s.id;

				$scope.showMask("api", title);
			};
			$scope.apiStatu = {
				handler: ""
			};
			$scope.saveApi = function(){
				$scope.apiStatu = {
					handler: ""
				};

				var method = "POST",
					url = OPS3_API
						+ "/useful/api",
					msg = "API 创建成功。";

				if($scope.api.id){
					method = "PUT";
					url = OPS3_API
						+ "/useful/api/"
						+ $scope.api.id;
					msg = "API 修改成功。";
				}

				if(!$scope.api.handler){
					$scope.apiStatu.handler = "error";
				}else{
					$scope.saving = true;

					request.send(method,
						url,
						$scope.api,
						function(data, status){
							if($scope.api.id){ // edit
								for(var i in $scope.service.apis){
									var a = $scope.service.apis[i];
									if(a.id == $scope.api.id){
										a = data;
									}
								}
							}else{ // new
								if(!$scope.service.apis){
									$scope.service.apis = [];
								}
								$scope.service.apis.push(data);
							}

							notice.showMsg({
								msg: msg,
								type: "info",
								close: true,
								duration: 3
							});

							$scope.hideMask();
							$scope.saving = false;
						},
						function(data, status){
							var errorMsg = "API 保存失败";
							if(data && data.detail){
								errorMsg += "："
									+ data.detail;
							}
							
							notice.showMsg({
								msg: errorMsg,
								type: "error",
								close: true
							});
							$scope.saving = false;
						}
					);
				}
			};

			$scope.deleteApiConfirm = false;
			$scope.deleteApi = function(){
				$scope.deleteApiConfirm = true;
			};
			$scope.deleteApiOk = function(){
				$scope.saving = true;

				request.send("DELETE",
					OPS3_API
						+ "/useful/api/"
						+ $scope.api.id,
					{},
					function(data, status){
						for(var i in $scope.service.apis){
							var s = $scope.service.apis[i];
							if(s.id == $scope.api.id){
								$scope.service.apis.splice(i, 1);
							}
						}

						notice.showMsg({
							msg: "API 已删除。",
							type: "info",
							close: true,
							duration: 3
						});

						$scope.hideMask();
						$scope.saving = false;
					},
					function(data, status){
						var errorMsg = "API 删除失败";
						if(data && data.detail){
							errorMsg += "："
								+ data.detail;
						}
						
						notice.showMsg({
							msg: errorMsg,
							type: "error",
							close: true
						});
						$scope.saving = false;
					}
				);
			};
			$scope.deleteApiCancel = function(){
				$scope.deleteApiConfirm = false;
			};

			$scope.cancelEdit = function(){
				$scope.hideMask();
				$scope.deleteServiceConfirm = false;
				$scope.deleteApiConfirm = false;
			};

			$scope.showMask = function(m, t){
				$scope.mask = m;
				$scope.maskTitle = t;
			};
			$scope.$watch("mask", function(){
				$scope.maskDir = "./views/mask/"
					+ $scope.mask
					+ ".html";
			});
			$scope.hideMask = function(){
				$scope.mask = "";
			};

			$scope.getApis();
		}
	]);
});