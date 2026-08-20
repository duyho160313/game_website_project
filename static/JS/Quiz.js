
let answer;
let score=0;
let total=0;
let time=30;
let timer;

function startGame(){

clearInterval(timer);

score=0;
total=0;
time=30;

document.getElementById("start").style.display="none";
document.getElementById("game").style.display="block";
document.getElementById("result").innerHTML="";
document.getElementById("message").innerHTML="";
document.getElementById("timer").innerHTML="Time:30";

newQuestion();

timer=setInterval(countDown,1000);

}

function countDown(){

time--;

document.getElementById("timer").innerHTML="Time:"+time;

if(time<=0){

clearInterval(timer);

document.getElementById("game").style.display="none";

let accuracy=0;

if(total>0){
accuracy=Math.round(score/total*100);
}

document.getElementById("result").innerHTML=
"Time's Up!<br><br>"+
"Correct:"+score+
"<br>Total:"+total+
"<br>Accuracy:"+accuracy+"%";

document.getElementById("start").style.display="block";

}

}

function newQuestion(){

let a=Math.floor(Math.random()*20);
let b=Math.floor(Math.random()*20);

answer=a+b;

document.getElementById("question").innerHTML=a+" + "+b;
document.getElementById("message").innerHTML="";

let answers=[answer];

while(answers.length<5){

let wrong=Math.floor(Math.random()*40);

if(!answers.includes(wrong)){
answers.push(wrong);
}

}

for(let i=answers.length-1;i>0;i--){

let j=Math.floor(Math.random()*(i+1));

let temp=answers[i];
answers[i]=answers[j];
answers[j]=temp;

}

document.getElementById("b1").innerHTML=answers[0];
document.getElementById("b2").innerHTML=answers[1];
document.getElementById("b3").innerHTML=answers[2];
document.getElementById("b4").innerHTML=answers[3];
document.getElementById("b5").innerHTML=answers[4];

for(let i=1;i<=5;i++){
document.getElementById("b"+i).disabled=false;
document.getElementById("b"+i).style.backgroundColor="white";
}

}

function check(button){

document.getElementById("b1").disabled=true;
document.getElementById("b2").disabled=true;
document.getElementById("b3").disabled=true;
document.getElementById("b4").disabled=true;
document.getElementById("b5").disabled=true;

total++;

if(Number(button.innerHTML)==answer){

score++;
button.style.backgroundColor="lightgreen";
document.getElementById("message").innerHTML="Correct!";

}
else{

button.style.backgroundColor="pink";
document.getElementById("message").innerHTML="Wrong!";

}

setTimeout(function(){

if(time>0){
newQuestion();
}

},1000);

}
