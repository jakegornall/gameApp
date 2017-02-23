function Player(username, pos, rotation, health, xp) {
    var player = this;

    player.username = username;
    player.health = health || 100;
    player.score = 0;
    player.xp = xp || 0;
    player.pos = pos || {x: 0, y: 0};
    player.rotation = rotation || 0;
}


angular.module('gameApplication', []).controller('gameplayController', function() {
        var gameApp = this;

        gameApp.testing = 256;
        
        gameApp.user = new Player(
            username = $.cookie("username").split()[0],
            xp = $.cookie("xp").split()[0]
        );

        gameApp.printData = function() {
            console.log("hi");
        };
});