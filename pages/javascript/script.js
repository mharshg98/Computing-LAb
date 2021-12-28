let slider=document.getElementById("slider");
let btn1=document.getElementById("btn1");
let btn2=document.getElementById("btn2");

btn1.addEventListener("click", function(e){
    console.log("btn1 clicked");
    slider.style.transform="translateX(0px)";
})

btn2.addEventListener("click", function(e){
    console.log("btn2 clicked");
    slider.style.transform="translateX(-100%)";
})