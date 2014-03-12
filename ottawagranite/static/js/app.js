// General purpose spinner.
var spin_opts = {
  lines: 13, // The number of lines to draw
  length: 7, // The length of each line
  width: 4, // The line thickness
  radius: 10, // The radius of the inner circle
  rotate: 0, // The rotation offset
  color: '#00f', // #rgb or #rrggbb
  speed: 1, // Rounds per second
  trail: 60, // Afterglow percentage
  shadow: true, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: 0, // Top position relative to parent in px
  //left: 400 // Left position relative to parent in px
  left: $(window).width() / 2 - 2
};
var spinner = null;

function get_csrf_token() {
    var widgets = $('form input');
    for (var i = 0; i < widgets.length; i++) {
        if (widgets[i].name === "csrfmiddlewaretoken") {
            return widgets[i].value;
        }
    }
    return null;
}

// FIXME: make this generic
function start_spinner() {
    var target = $('#progress_row')[0];
    if (spinner === null) {
        spinner = new Spinner(spin_opts).spin(target);
    }
    else {
        spinner.spin(target);
    }
}

function stop_spinner() {
    if (spinner !== null) {
        spinner.stop();
    }
}

// Angularjs app code.
var app = angular.module("ottawagranite", []);

// Change the template tags to avoid conflicts with Django.
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// Add the CSRF token to all requests.
app.run(function($http) {
    $http.defaults.headers.common["X-CSRFToken"] = get_csrf_token();
});

app.controller('LoginController',
    function($scope, $http) {
        console.log("in LoginController");

        $scope.init = function() {
            console.log("In init");
        }

        $scope.performLogout = function(url) {
            $http.post(url)
                .success(function(data, status, headers, config) {
                    document.location.reload();
                })
                .error(function(data, status, headers, config) {
                    alert("Error on logout - Report this to the site administrator");
                });
        }

        $scope.performLogin = function(url) {
            var data = {};
            data.userid = $scope.userid;
            data.password = $scope.password;
            $http.post(url, data)
                .success(function(data, status, headers, config) {
                    document.location.reload();
                })
                .error(function(data, status, headers, config) {
                    alert("Bad username or password");
                });
        };
    }
);
