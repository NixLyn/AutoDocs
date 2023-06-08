

<style>
    body {
    	height: 100vh;
	    --sz: 7px; /*** size ***/
    	--c0: #020202;
    	--c1: #171b1f;
        --c2: #333333;
        --c3: #00ff0095;
        --ts: 50%/ calc(var(--sz) * 16.8) calc(var(--sz) * 22);
        background:
		/*bottom*/
        conic-gradient(from 120deg at 50% 86.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from 120deg at 50% 86.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
		/*bottom dark*/
		conic-gradient(from 120deg at 50% 74%, var(--c0) 0 120deg, #fff0 0 360deg) var(--ts),
		/*right*/
		conic-gradient(from 60deg at 60% 50%, var(--c1) 0 60deg, var(--c2) 0 120deg, #fff0 0 360deg) var(--ts),
		/*left*/
		conic-gradient(from 180deg at 40% 50%, var(--c3) 0 60deg, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
		/*top dark*/
        conic-gradient(from 0deg at 90% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from -90deg at 10% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from 0deg at 90% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from -90deg at 10% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
	    	/*top*/
        conic-gradient(from -60deg at 50% 13.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from -60deg at 50% 13.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
		conic-gradient(from -60deg at 50% 41%, var(--c2) 0 60deg, var(--c3) 0 120deg, #fff0 0 360deg) var(--ts),
		var(--c0) ;
    }


    p {
        font-size: medium;
    }



    .da-head {
        margin-top: -15px;
        margin-left: -40%;
        margin-right: -5%;
        width: 100wv;
        height: fit-content;
        padding-left: 20%; 
        padding-right: 15%;
        padding-top: 1px;
        padding-bottom: 10px;
        border-radius: 20px;
        background-color: #111111F5;
        color: white;
        box-shadow: 10px 8px 10px 5px #00ff00;

    }

    .midspan  {
        margin-top: 10px;
        margin-left: -40%;
        margin-right: -5%;
        width: 90wv;
        height: 90wv;
        padding-left: 25%; 
        padding-right: 10%;
        padding-top: 5px;
        padding-bottom: 5px;
        border-radius: 20px;
        background-color: #111111F7;
        color: white;
        box-shadow: 10px 8px 10px 5px #00ff00;

    }
    .midspan *{
        margin-left: 35px;
    }
    .code_it {
        font-size: small;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 15px; 
        width: 80wv;
        right: 5vw; 
        height: fit-content;
        padding: 5px 80wv; 
        background-color: black; /* linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab); ; */
        color: white;
        border-radius: 20px;
    }
    .code_it *{
        font-size: 13px;
        margin-right: 15px;
    }

    .segment {
        display: box;
        width: 80wv;
        right: 5vw; 
        height: fit-content;
        padding: 5px 80wv; 
        background-color: black; 
        color: #00ff00F2;
        border-radius: 5px;
        padding-left: 2px; 
        padding-top: 0;
        padding-bottom: 1px;
        font-size: small;


    }

    .tb_sh_0 {

        width: 60vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 15px;
        padding-top: 5px;
        padding-bottom: 5px;
        border-top-left-radius: 8em;
        overflow-y: hidden;
        overflow-x: hidden;
    }


    .tb_box {
        margin-left: 1%;
        margin-right: 1%;
        padding-top: 1%;
        padding-bottom: 1%;

        width: 98%;
        height: calc(fit-content + 5px);
        background-color: black;
        border-radius: 14px;
        display: block;
        border-top-left-radius: 20em;
    }
    .tb_box *{
        font-size: small;
    }

    .tb_sh_c {

        width: 60vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 15px;
        padding-top: 5px;
        padding-bottom: 5px;
        border-bottom-left-radius: 8em;
        overflow-y: hidden;
        overflow-x: hidden;
    }


    .tb_box_c {
        margin-left: 1%;
        margin-right: 1%;
        padding-top: 1%;
        padding-bottom: 1%;

        width: 98%;
        height: calc(fit-content + 5px);
        background-color: black;
        border-radius: 14px;
        display: block;
        border-bottom-left-radius: 20em;
    }
    .tb_box_c *{
        font-size: small;
    }


    .tb_box_1 {
        margin-left: 1%;
        margin-right: 1%;
        padding-top: 1%;
        padding-bottom: 2%;

        width: 98%;
        height: calc(fit-content + 5px);
        background-color: black;
        border-radius: 14px;
        display: block;

    }
    .tb_box_1 *{
        font-size: small;
    }

    .tb_sh_1 {
        margin-left: 25px;
        width: 80vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 10px;
        padding-top: 2px;
        padding-bottom: 2px;
    }

    .snippet{
        padding-left: 0%;
        margin-right: 2px;
        margin-left: 1px;
        padding-top: 1px;
        margin-top: 1px;
        width: 100%;
        height: fit-content;
        background-color: black;
        border-radius: 12px;

    }
    .snippet img {
        border-radius: 12px;
    }


    li {
        margin-left: -15px;
        font-size: small;
        list-style-type: none; 
        color: #00ff00;

        }

    .tb_sh_2 {
        margin-left: -21px;
        width: 80vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 10px;
        padding-top: 1px;
        padding-bottom: 1px;
    }


</style>


<body>

<div class="da-head">
<h2 style="margin-left: 55px;"> 
Viewing From a Web <span style="background-color: #00ff00; border-radius: 15px;">🕸️</span>
</h2>
</div>
<br>
<div class="midspan">
<h3> Async-IO </h3>
<h4> Some UDP for our Viewing <u style="margin-left: 0px">hier</u> ... </h4>
<p>
Now that we have everything in order and can <u style="margin-left: 0px">control</u> our packet sniffer with a <span  style="color: #00ff00; margin-left: 0px;">main.py</span>.
 <br>
Why not <span  style="color: orange; margin-left: 0px;">plug-in</span> to it 'remotely'..?
</p>

<h4> The Node </h4>
<p>
Since we have already covered TCP in the series, why not make it more interesting and use UDP.. not only is it a great oppertunity to learn but also it will enable us to do some cooler stuff later <span  style="color: #ff00ff; margin-left: 0px;"> ;) </span>
</p>

<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> snrokly_node.py</u>
<!-- The Inner Block -->
<div class="code_it" style="margin-left: 0px;">
<span  style="color: purple; margin-left: 0px;">import</span> asyncio<br>
<span  style="color: purple; margin-left: 0px;">import</span> websockets<br>
<br>
</div></div>
<br>
<p>
🔺 We'll need this where we're going next 🔺
</p>

<br>
</div>
<br>

<br>
<br>
<br>
<br>
<br>
<br>
<div class="midspan">

<h3> await a'sync 🕥 </h3>

<p>
If you've been coding python for a while, you may have found that there are a few acrobatic moves some pros can flaunt from time to time.. Like using a @decorator (First time I saw that, it was pretty cool..).<br>
This however is not really one of them...<br>
<span  style="color: #ff00ff; margin-left: 0px;">async</span> and <span  style="color: #ff00ff; margin-left: 0px;">await</span> are used the way they are due to the original method at which they are call.. (a muc lower level than what we're covering in this series..).
</p>


<br>
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> snrokly_node.py</u>
<!-- The Inner Block -->
<div class="code_it" style="margin-left: 0px;">

<span  style="color: #00ffff; margin-left: 0px;">async def</span> start_server(self):<br>
&nbsp; &nbsp; &nbsp; &nbsp; #Start Endless Server Loop<br>
&nbsp; &nbsp; &nbsp; &nbsp; print("[WEB_SERVER_STARTED]")<br>
&nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #00ffff; margin-left: 0px;">await</span>websockets.serve(<span  style="color: #00a0ff; margin-left: 0px;margin-right: 0px;">self</span>.new_client_conn, 'localhost', 12345)

</div>
</div>
<br>
<h4> The 'Loop' ♾️ </h4>

<p>
Like any server side connection, there requirs an endless loop to be running for the required duration. Async is no exeption.<br>
The main thing to note here is the <span  style="color: #00ffff; margin-left: 0px;">await</span> way of doing things..
</p>

<br>
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<div class="midspan">

<h3> New Connection 🔼 </h3>
<p> 
Like most servers, we will seperate the functions for new connections and handling those data streams as client.. <br>
As is the best practice..
</p>

<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> from File_man import File_Man</u>
<!-- The Inner Block -->
<div class="code_it" style=" margin-left: 0px; margin-right: 0px;">
<!-- Lines of code.. -->
<span  style="color: #00ffff; margin-left: 0px;">async def</span>
 new_client_conn(self, client_socket, path):<br>
&nbsp; &nbsp; &nbsp; &nbsp; #Identify New Client Connection
<br>
&nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #00a0ff; margin-left: 0px;margin-right: 0px;">self</span>.clients.append(client_socket)
<br>
&nbsp; &nbsp; &nbsp; &nbsp; cl_id = len(self.clients)
<br>
&nbsp; &nbsp; &nbsp; &nbsp; print(f"[+]:[NEW CLIENT CONNECTED]:[>{str(path)}<]")
<br>
&nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #f1a0ff; margin-left: 0px;margin-right: 0px;">while</span> True:
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; msg_ = await client_socket.recv()
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: yellow; margin-left: 0px;margin-right: 0px;">print</span>(f"[FROM_CLIENT]:[{str(msg_)}]")
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #ff00ff; margin-left: 0px;margin-right: 0px;"> if </span> "[CONN_REQ]" in str(msg_):
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: yellow; margin-left: 0px;margin-right: 0px;">print</span>("[@]:[CONNECTION_REQUEST]")
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #00ffff; margin-left: 0px;margin-right: 0px;">await</span> SN.send_msg(client_socket, "Hello Client")
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #ff00ff; margin-left: 0px;margin-right: 0px;"> else</span>:
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #00ffff; margin-left: 0px;margin-right: 0px;">await </span>SN.handle_client(client_socket, cl_id, msg_, path)

</div>
</div>

<h3> But, what if there's more targets..? </h3>
<p>
That being the case in most situations, we should invest in creating a way to write a 'rules' file, which will be the 'listener' will take as guide-lines.
</p>
<br>

</div>


<br>
<br>

<br><br><br><br><br><br>


<br>
<br>
<br>
<div class="midspan">
<h3> Handling the Client.. </h3>
<p>
Now that our new client can connect, let's structure the process to handling the INs and OUTs..
</p>
<h4> Wait for the knock, lol.. </h4>
<p>
To keep the 'flow' of the three-way handshake, it is now the client's turn to message the server... 
</p>
<br>
<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> Getting the Message</u>
<!-- The Inner Block -->
<div class="code_it" style=" margin-left: 0px; margin-right: 0px;"><!-- Lines of code.. -->


<span  style="color: #00ffff; margin-left: 0px;margin-right: 0px;">async def</span> handle_client(self, websocket, cl_id, msg_, path):<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: yellow; margin-left: 0px;margin-right: 0px;">print</span>(f"[FromClient]:{str(msg_)}")<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span  style="color: #ff00ff; margin-left: 0px;margin-right: 0px;"> if</span> "node" in str(msg_):<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span  style="color: #00a0ff; margin-left: 0px;margin-right: 0px;"> self</span>.Li.start_snrokl(rules_, flags_)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ret_msg = "Starting-SnrokL"<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #00ffff; margin-left: 0px;margin-right: 0px;">await</span> <span  style="color: #00a0ff; margin-left: 0px;margin-right: 0px;"> self</span>.send_msg(websocket, ret_msg)<br>
        
</div>
</div>
<h3>So how do we <u style=" margin-left: 0px;">Respond</u> ?</h3>
<p style=none>
Well making the assumption that we have no reason to believe the client would have sent us anything bad for our system, and are only connected with permission...
</p>
<br>
</div>
<br>
<br>
<br>
<br>
<br>

<br><br><br><br><br><br>






<br>
<br>
<br>
<div class="midspan">
<h3> The Response Method  ☎️ </h3>
<p>
A simple funtion, which takes the client connection and the message, and sends it off. 💌<br>
Later we will call this function to 'stream' the data traffic of intrest, and as time goes, we will be able to use it to send 'notifications' of red flagged data.
</p>
<br>
<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> Getting the Message</u>
<!-- The Inner Block -->
<div class="code_it" style=" margin-left: 0px; margin-right: 0px;"><!-- Lines of code.. -->


<span  style="color: #00ffff; margin-left: 0px;margin-right: 0px;">async def</span> handle_client(self, websocket, cl_id, msg_, path):<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: yellow; margin-left: 0px;margin-right: 0px;">print</span>(f"[FromClient]:{str(msg_)}")<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span  style="color: #ff00ff; margin-left: 0px;margin-right: 0px;"> if</span> "node" in str(msg_):<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span  style="color: #00a0ff; margin-left: 0px;margin-right: 0px;"> self</span>.Li.start_snrokl(rules_, flags_)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ret_msg = "Starting-SnrokL"<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span  style="color: #00ffff; margin-left: 0px;margin-right: 0px;">await</span> <span  style="color: #00a0ff; margin-left: 0px;margin-right: 0px;"> self</span>.send_msg(websocket, ret_msg)<br>
        
</div>
</div>
<h3>When to <u style=" margin-left: 0px;">Respond</u> ?</h3>
<p style=none>
Well making the assumption that we have no reason to believe the client would have sent us anything bad for our system, and are only connected with permission. However, in the next part of the series we will be sending bad packets on purpose to get a closer look into how to detect it and what to do about it.
</p>
<br>
</div>
<br>
<br>
<br>
<br>
<br>





<br><br><br><br><br><br>

<div class="midspan">
<h3> The Starting Line 🏁 </h3>
<p>
To get all the above mentioned functions and loops to run, we have to use this complicated function-call sequence.
</p>
<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<h4 style="background-color: #111111F7; color: #00ff00; margin-left: 10px;"> if __name__=="__main__":</h4>
<div class="code_it" style=" margin-left: 0px; margin-right: 0px;">
&nbsp; &nbsp;  &nbsp; &nbsp; SN = SnrokL_Node() <br>
&nbsp; &nbsp;  &nbsp; &nbsp; SN.event_loop = asyncio.get_event_loop() <br>
&nbsp; &nbsp;  &nbsp; &nbsp; SN.event_loop.run_until_complete(SN.start_server()) <br>
&nbsp; &nbsp;  &nbsp; &nbsp; SN.event_loop.run_forever() <br>

</div>
</div>
<br>
<h4> SUDO REQUIRED  ⚡</h4>
<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<h4 style="background-color: #000000; color: #00ff00; margin-left: 10px;"> $ sudo python3 snorkly_node.py <br> [WEB_SERVER_STARTED]<br>
</h4>
<h4 style="color: white;"> Now click to open the test_.html file..<br> & the first things you will see in the terminal: 
<h4 style="background-color: #000000; color: #00ff00; margin-left: 10px;"> [+]:[NEW CLIENT CONNECTED]:[>/<] <br>
[FROM_CLIENT]:[[CONN_REQ]] <br>
[@]:[CONNECTION_REQUEST] <br><br>
-[SENDING]:["Hello Client!"] <br>
-[TO]:[websockets.legacy.server.WebSocketServerProtocol object at 0x7fe8dbcf10d0] <br>
</h4>
</div>
<br>

</div>
<br>
<br>
<br>
</div>
</div>

</div>
<br>
<br>

<br><br><br><br><br><br>

<br><br><br><br><br><br>

<br>
<div class="midspan">
<h3> Web Viewed - 01 </h3>
<p> 
That's right, we can connect to the python UDP server using javascript sockets. <br><br>
Because this script is so long, I had to try to break it into different slides.. 

</p>


<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #000000; margin-left: 15px;">test_.html</u>
<!-- The Inner Block -->
<div class="code_it" style=" margin-left: 0px; margin-right: 0px;">
<!-- Lines of code.. -->
<pre style="width: 100%;  margin-left: -5px; padding-right: 20px;" >
<code src="./test_.js"  style="top: -50px; font-size: 10px; ">
document.addEventListener('DOMContentLoaded', function () {
    const conn_status = document.querySelector('[name=connection-status]');
    const current_cmd = document.querySelector('[name=current-cmd]');
    const data_return = document.querySelector('[name=data-returned]');
    const cmd_to_send = document.querySelector('[name=cmd-to-send]');
    const send_button = document.querySelector('[name=send-button]');
    const back_logmsg = document.querySelector('#back-log');
    console.log('[EventListener]:[Running]');

</code>
</pre>

</div></div>
<br>
<p> Here are the const variables you will be needing to achive the next bit..
</p>
<br>
</div>

<br><br><br><br><br><br>











<br><br><br><br><br><br>

<div class="midspan">
<h3>Web Viewed - 02 </h3>
<div class="code_it" style=" margin-left: 0px; margin-right: 0px;">
<pre style="width: 100%;  margin-left: -5px; padding-right: 20px;" ><code src="./test_.js"  style="top: -50px; font-size: 10px; ">
const websocketClient = new WebSocket("ws://localhost:12345");
    websocketClient.onopen = function () {
        websocketClient.send('[CONN_REQ]');
        console.log('[CONNECTION ESTABLISHED]');
        conn_status.value = "CONNECTED!";
        conn_status.style.backgroundColor = 'rgb(0, 255, 0)';
        var input = document.getElementById("text-input");
        input.addEventListener("keyup", function(event){
            if (event.keyCode === 13){
                event.preventDefault();
                document.getElementById("snd-btn").click();
                console.log('[Sending..]');
                websocketClient.send(cmd_to_send.value);
                back_logmsg.scrollTop = back_logmsg.scrollTop + back_logmsg.scrollHeight;
                console.log(back_logmsg.scrollTop);
            }
        });
    };
    websocketClient.onmessage = function (msg) {
        console.log('[RETURNED]:', msg);
        data_return.value = msg.data;
        const new_log = document.createElement('div');
        new_log.innerHTML = msg.data+"br";
        back_logmsg.appendChild(new_log);
    };
    websocketClient.send('[DIS_CONN]');
    }, 
    false
    );
</code>
</pre>

</div>
<br>
</div>
<br>
<br>
</div>
<br><br><br><br><br><br>




<br><br><br><br><br><br>

<br>
<div class="midspan">

<h3> Web Terminal 🔢 </h3>




<!-- Some Colorful Stuff -->
<div class="tb_sh_1">
<!-- The BlackBoard -->
<div class="tb_box_1">
<!-- The content -->
<img src="./WebTerminal.png" alt="It's _meh_" style="
margin-left: 0px;
border-radius: 20px;
width: 80vw;">
</div>
</div>
<br>

<br>
</div>
<br>
<br>




<br><br><br><br><br><br>



<br><br><br><br><br><br>
<div class="da-head">
<h2 style="margin-left: 55px;"> 
Conclusion
</h2>
</div>
<br>
<div class="midspan">

<h3> Intention </h3>
<p> 
We can now remotely use a terminal which is running as sudo, in any browser from a simple html/css/js file. This same Structure can now also be applied to using the SnrokL project/package, to update rules, get list of saved data, stream traffic live, and sssooo much more.. Which we will get into in the next part of this series :P

</p>

<h4> Thanks to the Readers </h4>
<p>
If it wasn't for the feed-back I got from the readers, I wouldn't have gone this far in documention of my work. I'm truly thankfull to those who have inspired me to take on this venture and those who have suggested areas where I can improve. 
<br>
I truly hope this helps put some lights on for someone out there.. As I believe knowledge is to be shared and code is no exception. By working together, we can always achieve far greater than by grudging alone in the dark. 🕯️

</p>
<br>
</div>

<h6 style="margin-left: 350px; color: #00ff00">Dillon Breytenbach</h6>

<br>









<br>
<br>

<br>
<br>

<br>
<br>
<br>
<br>

<br>
<br>





<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>






















<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>














<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> first_tcp_client.py</u>
<!-- The Inner Block -->
<div class="code_it">
<!-- Lines of code.. -->
import socket<br>
import threading as thr<br>
from thr import Thread as Thr<br>
</div>
</div>
<br>



<!-- Some Colorful Stuff -->
<div class="tb_sh_0">
<!-- The BlackBoard -->
<div class="tb_box">
<!-- The content -->
::::TESTING_VH:::::
</div>
</div>
<br>
</div>
<br>
<br>



<!-- No LineBreak Edit'n -->
<span style="color: blue; font-size: small;">
 OUT_BOUND.txt
 </span>

<!-- If you are crafty, you can make subliminal messages, lol -->
<p style="font-size: 9px">Make sure to check spelling of file & class names</p>







<br>
<br>
<br>
<br>
<br>

<div class="midspan" style="width: 95vw; height: 90vh;">
<br>


<div class="tb_sh_0">
<div class="tb_box">
<div style="margin-left: 25px">
<h2>SnrokL : Part 1</h2>
<h4>Complete Coding Walkthrough </h4>
</div>
</div>
</div>
<br>
<div class="tb_sh_c">
<div class="tb_box_c">
<div style="margin-left: 25px">
<h3>Author : Dillon Breytenbach</h3>
</div>
</div>
</div>
<br>
<br>
<div class="tb_sh_0">
<div style="position: relative; overflow-y: hidden; margin-top: -1px; margin-left: -20px;">
<p>
1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 <br>
1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 <br>
0 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 <br>
1 0 1 0 1 1 1 0 1 1 1 0 1 0 0 1 0 0 1 <br>
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 <br>
1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 <br>
1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 <br>
0 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 <br>
1 0 1 0 1 1 1 0 1 1 1 0 1 0 0 1 0 0 1 <br>
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 <br>
</p>
</div>
<div class="tb_box" 
style="
    position: absolute;  
    height: 240px;
    margin-top: -15.25em; 
    z-index: 2; 
    width: 58%;
    margin-left: 1.9%;">

<div style="
    position: absolute;  
    margin-top: 8px; 
    margin-left: 30px;
    height: 240px;
    font-size: 10px; 
    position: relative;">



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⢀⡀⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⣧⣄⢀⡀⣠⣼⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿⣄⢀⡀⣠⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏
⠀⠀⠀⠀⠀⠀⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⠏
</div>

<br>


</div>
</div>
<br>
</div>
<br>
</div>

<br>
<br>

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⢀⡀⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⣧⣄⢀⡀⣠⣼⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⣿⠀⠀⣿⣄⢀⡀⣠⣿⠀⠀⣿
⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏
⠀⠀⠀⠀⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⠏








⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠋⣠⣶⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⣰⡟⢁⠼⠛⢁⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⢠⡟⠀⣠⣴⠾⠟⠛⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡈⠀⠞⠀⠚⠉⢀⣤⡆⢰⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠻⣿⣶⣄⠐⠾⠀⣾⡿⠀⠈⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣷⣄⠙⢿⣷⠆⠀⠠⠤⠶⣤⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠸⣿⣿⣿⣿⣿⣿⡆⠁⠀⠀⠀⠀⠀⠀⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠰⢿⣷⣄⠙⢿⣿⣿⠏⠀⠀⠀⠀⠀⢀⣠⣴⠟⠁
⠀⢀⡀⠀⣾⡿⠀⡶⠄⠙⠿⣿⣦⠉⠁⠀⢀⣤⡴⠖⠛⠉⠉⠀⠀⠀
⠀⣾⠇⠸⠛⠁⣀⡤⠀⡴⠀⡈⠃⠀⠀⢰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣴⡶⠟⠋⠀⣼⠃⣸⡇⠀⠀⠀⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⢁⣤⡖⢁⣼⠏⢰⣿⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠿⠋⣠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀



</body>










