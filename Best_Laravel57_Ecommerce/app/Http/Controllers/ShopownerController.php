<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ShopownerController extends Controller
{
    public function index(){
        $menu_active=1;
        return view('backEnd.index',compact('menu_active'));
    }
}
