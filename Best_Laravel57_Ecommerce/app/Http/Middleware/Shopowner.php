<?php

namespace App\Http\Middleware;

use Closure;

class Shopowner
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        if(Auth::check() && Auth::user()->isShopowner()){
            return $next($request);
        }
        return redirect('shopowner_home');
    }
}
