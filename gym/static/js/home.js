
$(()=>{
    $("#login").click(()=>{
        $.post("/login",{username:$("#username").val(),password:$("#password").val()},(json)=>{
                if (json.status==1)
                    window.location.href="/success?username="+$("#username").val();
                else if (json.status==0)
                    alert("doesn't exist user");
                else if (json.status==2)
                    alert("username or password should not empty!");
        })
    });

    $("#register").click(()=>{
           window.location.href="/register_form"
    });

})