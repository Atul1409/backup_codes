fun main(args: Array<String>) {

    var hours = readLine()!!.toInt()

    var total: Double = 0.0

    

    

    if(hours in 1..5) {

        total += hours  

        hours = 0 

    }

    

    if(hours in 6..23) {



total += 5 + (hours - 5)*0.5

        hours = 0  

    }

    

    

    while(hours > 0) {

        

        if(hours >= 24) {

            total += 15

            hours -= 24

        }

        if(hours in 1..23) {

            total += hours  * 0.5

            hours -= hours 



        }

    

    }

    

    print(total)

}

