
function backtotop(){
    window.scrollTo({top:0,behavior:'smooth'});
}
document.getElementById("backtoup").addEventListener('click',backtotop,false);

function dropdown()
{
    document.getElementById("content").style.display = "block";
}
function dropout()
{
    document.getElementById("content").style.display = "none";
}


function opennav()
{
    document.getElementById("slidenav2").style.display="block";
}

function closenav()
{
    document.getElementById("slidenav2").style.display="none";
}


function openpincode()
{
    document.getElementById("setpincode").style.display="block";
    document.getElementsByTagName("body").style.opacity=0.2;
}
function closepincode()
{
    document.getElementById("setpincode").style.display="none";
}

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:false,
    dots:false,
    autoplay:true,
    autoplayTime:1000,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
})
