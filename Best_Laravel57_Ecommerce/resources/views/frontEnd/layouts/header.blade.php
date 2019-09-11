<header id="header"><!--header-->
    <div class="header_top"><!--header_top-->
        <div class="container">
            <div class="row">
                <div class="col-sm-6">
                    <div class="contactinfo">
                        <ul class="nav nav-pills">
                            <li><a href="#"><i class="fa fa-phone"></i> 01517078796</a></li>
                            <li><a href="#"><i class="fa fa-envelope"></i> nazmulhasnsakib@gmail.com</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="social-icons pull-right">
                        <ul class="nav navbar-nav">
                            <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                            <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                            <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                            <li><a href="#"><i class="fa fa-dribbble"></i></a></li>
                            <li><a href="#"><i class="fa fa-google-plus"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div><!--/header_top-->

    <div class="header-middle"><!--header-middle-->
        <div class="container">
            <div class="row">
                <div class="col-sm-8">
                    <div class="logo pull-right"> 
                        <a href="{{url('/')}}"><img src="{{asset('frontEnd/images/home/bestlogo.png')}}" alt="" /></a>
                    </div>
                </div>
                <div class="col-sm-10">
                    <div class="shop-menu pull-right">
                        <ul class="nav navbar-nav">
                            <li><a href="{{url('/viewcart')}}"><i class="fa fa-shopping-cart"></i> Cart</a></li>
                            @if(Auth::check())
                                <li><a href="{{url('/myaccount')}}"><i class="fa fa-user"></i> My Account</a></li>
                                <li><a href="{{ url('/logout') }}"><i class="fa fa-lock"></i> Logout </a>
                                </li>
                            @else
                                <li><a href="{{url('/login_page')}}"><i class="fa fa-lock"></i> Login</a></li>
                            @endif
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div><!--/header-middle-->

    <div class="header-bottom"><!--header-bottom-->
        <div class="container">
            <div class="row">
                <div class="col-sm-6">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                    </div>
                    <div class="mainmenu pull-left">
                        <ul class="nav navbar-nav collapse navbar-collapse">
                            <li><a href="{{url('/')}}" class="hyper"><span>Home</span></a></li>
                            <li class="dropdown"><a href="#"class="dropdown-toggle hyper" data-toggle="dropdown"><span>Shop<b class="caret"></b></span></a>
                                <ul role="menu" class="sub-menu">
                                    <li><a href="{{url('/list-products')}}">Products</a></li>
                                    <li><a href="{{url('/myaccount')}}">Account</a></li>
                                    <li><a href="{{url('/viewcart')}}">Cart</a></li>
                                </ul>
                            </li>     
                            <li>
                                <a href="{{url('/viewavailableshops')}}" class="hyper"> <span>Rent a Shop</span></a>
                            </li>
                            <li><a href="{{url('/contact')}}" class="hyper" target="_blank"><span>Contact Us</span></a></li>
                        </ul>
                    </div>
                    <div class="search-form" align="right">
                    <form action="{{url('/search')}}" method="post">
                    <input type="hidden" name="_token" value="{{csrf_token()}}">
                        <input type="text" placeholder="Search..." name="Search" id="Search">
                        <input type="submit" value="Search">
                    </form>
                </div>
                </div>
            </div>
        </div>
    </div><!--/header-bottom-->
</header><!--/header-->