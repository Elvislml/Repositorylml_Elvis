<?php

/** @var \Laravel\Lumen\Routing\Router $router */


$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router->group(['prefix' => 'cliente'], function($router){
    $router->get('all', 'ClienteController@allSinRestricciones');
    $router->get('allJson', 'ClienteController@allJson');
    $router->get('get/{cedula}', 'ClienteController@getCliente');
    $router->post('new', 'ClienteController@create');
});
