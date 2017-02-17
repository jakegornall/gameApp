angular.module('gameApp', [])
    .controller('GenPageController', function() {
        var GenPage = this;

        GenPage.login = function() {
        	$('#loginSignup-page').hide();
        	var username = $('#login-username').val();
        	var password = $('#login-password').val();

        	$.ajax({
        		url: Flask.url_for('login'),
        		type: 'POST',
        		data: {
        			'username': username,
        			'password': password
        		},
        		success: function(response) {
        			if (response.success === true) {
        				gameplayController.user = response.username;
        			}
        		},
        		error: function() {
        			$('#loginSignup-page').show();
        			console.log('Server Not Responding...')
        		}
        	});
        }
 
        GenPage.signup = function() {

        };
});