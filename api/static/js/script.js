(function() {
  var app;

  app = angular.module('api.app.appointment', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.appointment = [];
      return $http.get('/api/appointments/1').success(function(data) {
        return $scope.appointment = data;
      });
    }
  ]);
}).call(this);

(function() {
  var app;

  app = angular.module('api.app.appointments', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.appointments = [];
      return $http.get('/api/appointments').then(function(result) {
        return angular.forEach(result.data, function(item) {
          return $scope.appointments.push(item);
        });
      });
    }
  ]);
}).call(this);

//(function() {
  //var app;

  //app = angular.module('api.resources', ['ngResource']);

  //app.factory('Appointment', [
    //'$resource', function($resource) {
      //return $resource('/api/appointment/:id', {
        //id: '@id'
      //});
    //}
  //]);

//}).call(this);

