{% include navbar.html %}


# Create Task

 * Describes the overall purpose of the program

The purpose of the program is to have an interactive 8-stage timer where the user can configure the timer. It’s intended use is to provide a scheduler for use in the Pomodoro studying technique. 

 * Describes what functionality of the program is demonstrated in
the video

The video demonstrates the timer’s default settings, which can run without the user setting any special settings, and then the mode where the user can configure the timer by setting each time 

 * Describes the input and output of the program demonstrated in
the video

The input of the program consists of the user defining a list of the lengths of the timers. There is a start button which starts the timer sequence. The output consists of a display on the page which represents the time left on the timer in milliseconds, seconds, minutes, hours, and days. 
Additional inputs include a debug mode, where the multiplier (default is set to 60, for regular speed) can be changed and the ID and intended length of each timer is displayed below the time remaining. 



 * The first program code segment must show how data have been
stored in the list.
```java
const timerLengths = [25,5,25,5,25,5,25,30]
function setTimerLengths(){

   for (let i = 0; i < timerLengths.length; i++) {
       timerLengths[i] = document.getElementById('timerlength'+ String(i+1)).value
   }
       console.log(timerLengths)
}
```

 * The second program code segment must show the data in the
same list being used, such as creating new data from the existing
data or accessing multiple elements in the list, as part of fulfilling
the program’s purpose.
```java
// Code below is based off timer tutorial code from W3Schools: https://www.w3schools.com/howto/howto_js_countdown.asp
let DEEZnuts = 0;
function timer(time) {
   document.getElementById('2').setAttribute("hidden","")
   console.log("function started")

   let SISTERS = 0;

   let rn = new Date().getTime();

   // Set the date we're counting down to !!MAKE SURE TO ADD BACK THE 60*!! it is only gone for testing purposes
   // let timerCoefficient = document.getElementById('timerconfig').value
   let countDownDate = new Date(rn + document.getElementById('timerconfig').value*1000*time).getTime();

   // Update the count down every 1 second
   let x = setInterval(function () {

       console.log("async function loop started with Timer ID (DEEZnuts): " +
       DEEZnuts + " // Timer countdown time (SISTERS): " + SISTERS)
       // Get today's date and time
       let now = new Date().getTime();

       // Find the distance between now and the count down date
       let distance = countDownDate - now;

       // Time calculations for days, hours, minutes and seconds

       let days = Math.floor(distance / (1000 * 60 * 60 * 24));
       let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
       let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
       let seconds = Math.floor((distance % (1000 * 60)) / 1000);
       let yourMOM = Math.floor(distance % 1000)

       // Display the result in the element with id="demo"
       document.getElementById("demo").innerHTML = days + "d " + hours + "h "
           + minutes + "m " + seconds + "." + yourMOM + " s   " ;


       SISTERS = timerLengths[DEEZnuts]

       // If the count down is finished, write some text
       if (distance <= 0) {
           if(DEEZnuts==1 || DEEZnuts==3 || DEEZnuts==5 || DEEZnuts==7 ){
               document.getElementById('display').innerText = "ITS TIME FOR A BREAK SISTERS!!"
               document.getElementById('1').removeAttribute("hidden")
           }
           if(DEEZnuts==0 || DEEZnuts==2 || DEEZnuts==4 || DEEZnuts==6 || DEEZnuts==8){
               document.getElementById('display').innerText= "GET TO WORRKKKK"
               document.getElementById('1').setAttribute("hidden", "")
           }
           DEEZnuts = DEEZnuts + 1;
           document.getElementById("debuginfo").innerHTML = "Timer ID (DEEZnuts): " +
               DEEZnuts + " // Timer countdown time (SISTERS): " + SISTERS;
           if (DEEZnuts==8){
               DEEZnuts = 0;
           }
           clearInterval(x);
           timer(SISTERS);
       }
   }, 1);
}
```

 * Identifies the name of the list being used in this response

timerLengths 

 * Describes what the data contained in the list represent in your
Program

The data contained in the list represents the length of time of each segment of the 8-segment timer cycle, in minutes. The first element in the list represents the length of the first timer, the second element the second timer, and so on. However, the length of time represented is not always in minutes and can be changed with Debug Mode.

 * Explains how the selected list manages complexity in your program
code by explaining why your program code could not be written, or
how it would be written differently, if you did not use the list

Without the list, it would be difficult and cumbersome to store 8 different variables and use them all separately. 

### Capture and paste two program code segments you developed during
the administration of this task that contain a student-developed
procedure that implements an algorithm used in your program and a
call to that procedure. Approx. 200 words (for all subparts of 3c combined, exclusive of
program code) 
 * The first program code segment must be a student-developed
procedure that:
 *  * Defines the procedure’s name and return type (if necessary)
 *  * Contains and uses one or more parameters that have an effect
on the functionality of the procedure
 *  * Implements an algorithm that includes sequencing, selection,
and iteration
```java
const timerLengths = [25,5,25,5,25,5,25,30]
function setTimerLengths(){

   for (let i = 0; i < timerLengths.length; i++) {
       timerLengths[i] = document.getElementById('timerlength'+ String(i+1)).value
   }
       console.log(timerLengths)
}
// Code below is based off timer tutorial code from W3Schools: https://www.w3schools.com/howto/howto_js_countdown.asp
let DEEZnuts = 0;
function timer(time) {
   document.getElementById('2').setAttribute("hidden","")
   console.log("function started")

   let SISTERS = 0;

   let rn = new Date().getTime();

   // Set the date we're counting down to !!MAKE SURE TO ADD BACK THE 60*!! it is only gone for testing purposes
   // let timerCoefficient = document.getElementById('timerconfig').value
   let countDownDate = new Date(rn + document.getElementById('timerconfig').value*1000*time).getTime();

   // Update the count down every 1 second
   let x = setInterval(function () {

       console.log("async function loop started with Timer ID (DEEZnuts): " +
       DEEZnuts + " // Timer countdown time (SISTERS): " + SISTERS)
       // Get today's date and time
       let now = new Date().getTime();

       // Find the distance between now and the count down date
       let distance = countDownDate - now;

       // Time calculations for days, hours, minutes and seconds

       let days = Math.floor(distance / (1000 * 60 * 60 * 24));
       let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
       let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
       let seconds = Math.floor((distance % (1000 * 60)) / 1000);
       let yourMOM = Math.floor(distance % 1000)

       // Display the result in the element with id="demo"
       document.getElementById("demo").innerHTML = days + "d " + hours + "h "
           + minutes + "m " + seconds + "." + yourMOM + " s   " ;


       SISTERS = timerLengths[DEEZnuts]

       // If the count down is finished, write some text
       if (distance <= 0) {
           if(DEEZnuts==1 || DEEZnuts==3 || DEEZnuts==5 || DEEZnuts==7 ){
               document.getElementById('display').innerText = "ITS TIME FOR A BREAK SISTERS!!"
               document.getElementById('1').removeAttribute("hidden")
           }
           if(DEEZnuts==0 || DEEZnuts==2 || DEEZnuts==4 || DEEZnuts==6 || DEEZnuts==8){
               document.getElementById('display').innerText= "GET TO WORRKKKK"
               document.getElementById('1').setAttribute("hidden", "")
           }
           DEEZnuts = DEEZnuts + 1;
           document.getElementById("debuginfo").innerHTML = "Timer ID (DEEZnuts): " +
               DEEZnuts + " // Timer countdown time (SISTERS): " + SISTERS;
           if (DEEZnuts==8){
               DEEZnuts = 0;
           }
           clearInterval(x);
           timer(SISTERS);
       }
   }, 1);
}
```
 * The second program code segment must show where your student-developed procedure is being called in your program.
```
<a class="center"  id="2" onclick="timer(0)">
   <img class="center" style="width: 200px; height: auto" src="/static/assets/POMODORO.png">
</a>

<button onclick="setTimerLengths()">Set Lengths</button>
```

### Then, provide a written response that does both of the following:
 * Describes in general what the identified procedure does and how it
contributes to the overall functionality of the program

The setTimer procedure sets how long the 8 timers are, according to what numbers the user entered into the 8 fields. The timer procedure runs the backend of the timer and 

 * Explains in detailed steps how the algorithm implemented in the
identified procedure works. Your explanation must be detailed
enough for someone else to recreate it.

The setTimerLengths procedure sets the list timerLengths with the values the user entered, and it is called when the user clicks the Set Lengths button. Next, the user must click a button that starts the timer procedure. The timer() function starts off with getting the current time, then adding the length of time equal to the length of the timer. It then enters a loop that repeats every millisecond where it gets the remaining time and displays it in days, hours, minutes, and seconds by using the modulo operation. This means that the timer display updates every millisecond. When the time reaches zero (which is checked every millisecond), a code segment of nested conditionals tells the timer which timer out of the 8 is next, and how long the next timer will last.

### Provide a written response that does all three of the following:
Approx. 200 words (for all subparts of 3d combined)
 * Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.
First call:
Clicking the start button without inputting values for custom timer lengths
Second call:
Filling out the input boxes, clicking Set Lengths, then clicking the start button. 

 * Describes what condition(s) is being tested by each call to the
procedure
Condition(s) tested by the first call: 
When the input boxes are left empty and the timer lengths are not specified by the user. In this instance, the function setTimerLengths() is not being ran.
Condition(s) tested by the second call: 
The inputs are used to set the timers’ lengths; setTimerLengths() is run before the timer() function itself.

 * Identifies the result of each call
Result of the first call:
The timers use the default settings of 25 minutes, 5 minutes, 25 minutes, 5 minutes, 25 minutes, 5 minutes, 25 minutes, and 30 minutes.
Result of the second call: The timers use the custom settings of whatever the user inputs. 
