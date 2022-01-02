let slider=document.getElementById("slider");
let indicators=document.getElementById("indicators");
//let btn1=document.getElementById("btn1");
//let btn2=document.getElementById("btn2");

let l=slider.childElementCount;
slider.style.width=(l*100)+"%";

for (let i=0;i<indicators.childElementCount;i++){
    indicators.children[i].addEventListener("click", function(e){
        console.log("btn1 clicked");
        let shift=(i/l)*100;
        slider.style.transform="translateX(-"+shift+"%)";
    });
}