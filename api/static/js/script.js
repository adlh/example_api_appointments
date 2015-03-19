function change_ng_brackets(app) {
    // Change the brackets in angularJS to prevent mix ups with django templates
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });
    return app;
};

function add_csrf_token(app, csrf_token) {
    // Not including a list of dependent modules (2nd parameter to `module`)
    //"re-opens" the module for additional configuration
    app.config(function($httpProvider) {
        //console.log('add_csrf_token: ', csrf_token);
        $httpProvider.defaults.headers.common['X-CSRFToken'] = csrf_token;
    });
    return app;
};


(function() {
    var app = angular.module('api.app_list', []);
    app = change_ng_brackets(app);

    ////
    // A very simple list of appointments
    ////
    app.controller('api.list_ctrl', ['$scope', '$http', 
        function($scope, $http) {
            console.log('in list_ctrl');
            $scope.appointments = [];
            return $http.get('/api/appointments').then(function(result) {
                console.log('getting appointments...');
                return angular.forEach(result.data, function(item) {
                    return $scope.appointments.push(item);
                });
            });
        }
    ]);
}).call(this);


(function() {
    var app = angular.module('api.appointments', ['ngRoute']);
    //var app = angular.module('api.appointments', []);
    app = change_ng_brackets(app);
    
    app.config(['$routeProvider', '$locationProvider',
        function($routeProvider, $locationProvider) {
            console.log('in config');
            $routeProvider.
                when('/view/:id', {
                    controller: 'api.view_ctrl'
                });
            //routing DOESN'T work without html5Mode
            $locationProvider.html5Mode(true);
            console.log('in config: $routeProvider:', $routeProvider);
        }]);


    /////
    // A view for the participants to update the options for the appointment
    // and to show an overview of the current stand (best option so far, and
    // an overview of all options fo this appointment.
    ////
    app.controller('api.view_ctrl', ['$scope', '$location', '$route', '$http',
        function($scope, $location, $route, $http) {
            // get $route.current after $routeChangeSuccess because it is an
            // asynchronous event...
            $scope.$on('$routeChangeSuccess', function(next, current) { 
                var $id = current.params.id;
                $scope.appointment = [];
                return $http.get('/api/appointments/' + $id).success(
                    function(data) { 
                        // init scope.selection now
                        $scope.selection= [];
                        return $scope.appointment = data; 
                    });
            });

            // When the user clicks on an option, it is added/removed from
            // the selection list
            $scope.toggleSelection = function toggleSelection(id) {
                var idx = $scope.selection.indexOf(id);

                // is currently selected
                if (idx > -1) {
                    $scope.selection.splice(idx, 1);
                }

                // is newly selected
                else {
                    $scope.selection.push(id);
                }
            };

            $scope.participantChanged = function participantChanged() {
                // get the selection for this participant
                if (typeof($scope.attendant) == 'undefined' ||
                        $scope.attendant.id == '' ||
                        typeof($scope.attendant.id) == 'undefined') {
                    $scope.selection = [];
                    return;
                }
                $scope.selection = [];
                $http.get('/api/accepted/' + $scope.appointment.id 
                        + '/' + $scope.attendant.id).success(
                    function(obj) {
                        // build a list of the option-ids
                        lst = [];
                        for (k in obj) { 
                            lst.push(obj[k].option); 
                        }
                        $scope.selection = lst;
                    });
            };

            $scope.save_options = function() {
                console.log('Saving options...');
                if (typeof($scope.attendant) == 'undefined' ||
                        $scope.attendant.id == '' ||
                        typeof($scope.attendant.id) == 'undefined') {
                    return;
                }
                var up_data = JSON.stringify({
                    appointment: $scope.appointment.id,
                    participant: $scope.attendant.id,
                    options: $scope.selection
                });
                console.log(up_data);
                // PUSH the results to the server
                $http.post('/api/accepted/' + $scope.appointment.id + '/' 
                        + $scope.attendant.id + '/' + 'update', up_data).then(
                    function(resp) {
                        // now update the appointment
                        return $http.get('/api/appointments/' + 
                                $scope.appointment.id).success(
                            function(data) { 
                                $scope.selection= [];
                                return $scope.appointment = data; 
                            });
                    },
                    function(resp) {
                        window.alert('uppps! Something went wrong!');
                    }
                );
                return false;
            };
        }]);
}).call(this);

