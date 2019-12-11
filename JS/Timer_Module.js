//Timer module that exports a timer function

//Timer function waits a set amount of time, then repeats a function for
//a specified duration at set intervals, and then stops repeating function
//All times in ms (1000ms=1s)
function timer(start, duration, repeat_Interval, repeat_Func) {
    function start_Interval(len, rep_time, rep_func) {
        //start given function at the interval given
        let intervalID = (setInterval(rep_func, rep_time))

        //setup function to clear the interval set above
        //after the len of time (in ms) has passed
        setTimeout(()=>clearInterval(intervalID), len)

        return intervalID
    }
    let root = this;
    let cancelID;
    root.intID = new Promise(function(resolve){
    return cancelID = setTimeout(()=>{
        result = start_Interval(duration, repeat_Interval, repeat_Func);
        resolve(result)
    }, start)
    })
    //output consists of the first element of the array to be the ID used to
    //cancel the inital setTimeout (before it starts), and the second element
    //of the array to be a Promise that returns the result
    return [cancelID, root.intID]
}

//Note - this version of the timer does not have a way of stopping the
//function repeating on the interval until it has completed, but you can
//stop the function before it starts by cancelling the timeout ID returned
exports.time_func = timer
