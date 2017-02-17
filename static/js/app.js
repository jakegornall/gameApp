function Player(username, pos, rotation, health, xp) {
    var player = this;

    player.username = username;
    player.health = health || 100;
    player.score = 0;
    player.xp = xp || 0;
    player.pos = pos || {x: 0, y: 0};
    player.rotation = rotation || 0;
}





angular.module('gameApp', [])
    .controller('gameplayController', function() {
        var gameApp = this;

        gameApp.username = null;
        gameApp.score = null;
        gameApp.enemy = null;
        gameApp.enemyScore = null;

 
        gameApp.MainLoop = function() {
            
        };
});